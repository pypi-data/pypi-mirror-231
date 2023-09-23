import json
import requests
import time
import os
from datetime import date

from searchdatamodels import Candidate, WorkExperience, EducationExperience, ContactInfo, DescriptionModel

try:
    from .github_scraper import scrape_github_user
except ImportError:
    from github_scraper import scrape_github_user


def run_external_web_sweeper(query_list: list[str], num_results_per_site: int = 10, allowed_sites: list['str'] = ['github']) -> list[Candidate]:
    '''
    Main function to run the external web sweeper. Uses Google search to find links to relevant candidates based on natural language query and then scrapes the links for candidate data.

    Parameters:
    ----------
    query_list : list[str]
        List of queries to search users by.
    num_results_per_site : int
        Maximum number of results to fetch per site.
    allowed_sites : list[str]
        List of sites to search users on.

    Returns:
    ----------
    list
        List of candidates matching the given query.
    '''
    sites = {
        'linkedin': 'site:linkedin.com/in',
        'github': 'site:github.com -site:github.com/collections -site:github.com/topics -site:github.com/trending -site:github.com/readme -site:github.com/features -site:github.com/orgs',
        'stackoverflow': 'site:stackoverflow.com/users',
        'dribbble': 'site:dribbble.com',
    }

    links = {}
    candidates = []
    for site in sites:
        if site not in allowed_sites:
            continue

        links = []
        for query in query_list:
            links.extend(call_serper_api(
                query + " " + sites[site], num_results=num_results_per_site))

        if site == 'linkedin':
            candidates.extend(scrape_linkedin_profile_links(links))
        elif site == 'github':
            candidates.extend(scrape_github_links(links))
        elif site == 'stackoverflow':
            pass
        elif site == 'dribbble':
            pass

    return candidates


def call_serper_api(query: str, location: str = "us", num_results: int = 10) -> list[str]:
    """
    Calls SERPER API to search Google for links relevant to the query

    Parameters:
    ----------
    query : str
        The search keyword following google search parameters to search users by.
    num_pages : int
        Maximum number of pages to fetch.

    Returns:
    ----------
    list
        List of links matching the given query and site.

    """
    url = "https://google.serper.dev/search"
    links = set()

    payload = json.dumps({
        "q": query,
        "location": location,
        "autocorrect": False,
        "num": num_results,
    })
    headers = {
        'X-API-KEY': os.getenv('SERPER_API_KEY'),
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        data = response.json()
        for result in data["organic"]:
            links.add(result["link"])
    else:
        print("Error: ", response.status_code)

    return list(links)


def scrape_linkedin_profile_links(linkedin_profile_links: list[str]) -> list[Candidate]:
    """
    Getting Linkedin profile data by using Nubela's ProxyCurl API

    Parameters:
    ----------
    linkedin_profile_url : str
        The Linkedin profile url to get the data from.

    Returns:
    ----------
    list
        list of the Linkedin profile data in Candidate model.
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    candidates = []

    for link in linkedin_profile_links:
        response = requests.get(
            api_endpoint,
            params={"url": link, "personal_email": "include"},
            headers={"Authorization": f"Bearer {os.getenv('PROXY_CURL_API')}"}
        )

        if response.status_code == 200:
            data = response.json()

            location = ""
            if data["city"]:
                location += data["city"]
            if data["state"]:
                if location != "":
                    location += ", "
                location += data["state"]
            if data["country_full_name"]:
                if location != "":
                    location += ", "
                location += data["country_full_name"]

            work_experience_list = []
            for experience in data["experiences"]:
                if experience["starts_at"] != None:
                    start_date = date(
                        experience["starts_at"]["year"], experience["starts_at"]["month"], experience["starts_at"]["day"])
                else:
                    start_date = None

                if experience["ends_at"] != None:
                    end_date = date(
                        experience["ends_at"]["year"], experience["ends_at"]["month"], experience["ends_at"]["day"])
                else:
                    end_date = None

                work_experience_list.append(WorkExperience(
                    Start=start_date,
                    End=end_date,
                    Description=DescriptionModel(
                        Text=experience["description"] if experience["description"] != None else ""),
                    Institution=experience["company"],
                    Specialization=experience["title"],
                ))

            education_experience_list = []
            for experience in data["education"]:
                if experience["starts_at"] != None:
                    start_date = date(
                        experience["starts_at"]["year"], experience["starts_at"]["month"], experience["starts_at"]["day"])
                else:
                    start_date = None

                if experience["ends_at"] != None:
                    end_date = date(
                        experience["ends_at"]["year"], experience["ends_at"]["month"], experience["ends_at"]["day"])
                else:
                    end_date = None

                education_experience_list.append(EducationExperience(
                    Start=start_date,
                    End=end_date,
                    Description=DescriptionModel(
                        Text=experience["description"] if experience["description"] != None else ""),
                    Institution=experience["school"],
                    Specialization=experience["field_of_study"] if experience["field_of_study"] != None else "",
                    Degree=experience["degree_name"] if experience["degree_name"] != None else "",
                ))

            contact_info_list = []
            if "personal_emails" in data and data["personal_emails"]:
                contact_info_list.append(ContactInfo(
                    Type="email",
                    Value=data["personal_emails"][0]
                ))
            if "personal_numbers" in data and data["personal_numbers"]:
                contact_info_list.append(ContactInfo(
                    Type="phone",
                    Value=data["personal_numbers"][0]
                ))

            project_list = []
            for project in data["accomplishment_projects"]:
                project_list.append(DescriptionModel(
                    Text=project["description"],
                ))

            skills = data["skills"] if "skills" in data else []
            skills = skills if skills != None else []

            candidates.append(Candidate(
                Name=data["full_name"],
                Location=location,
                Skills=skills,
                WorkExperienceList=work_experience_list,
                EducationExperienceList=education_experience_list,
                ContactInfoList=contact_info_list,
                Tags=[],
                Sources=[link],
                ExternalSummaryStr=data["summary"] if data["summary"] != None else "",
                ProjectList=project_list
            ))
        else:
            print("Error: ", response.status_code)

    return candidates


def scrape_github_links(github_links: list[str], enforce_email: bool = True, enforce_summary: bool = True) -> list[Candidate]:
    """
    Getting GitGub profile data by using GitHub User API

    Parameters:
    ----------
    github_links : list[str]
        The GitHub profile url to get the data from.
    enforce_email : bool
        Whether to enforce email to be present in the candidate's profile.
    enforce_summary : bool
        Whether to enforce summary to be present in the candidate's profile.

    Returns:
    ----------
    list
        List of the Github profile data in Candidate model.
    """
    candidates = []
    for link in github_links:
        username = link.strip().replace(
            "https://", "").replace("http://", "").split("/")[1]

        print(f'Scraping {username} from GitHub...')
        data = scrape_github_user(
            os.getenv('GITHUB_ACCESS_TOKEN'), username)

        if data and data["name"] != None:
            if enforce_email and data["email"] == None:
                continue
            if enforce_summary and data["bio"] == None:
                continue

            sources = ["https://github.com/" + username]
            # if user specifies their blog
            if data["blog"] != "":
                sources.append(data["blog"])
            if "social_accounts" in data:
                for social_account in data["social_accounts"]:
                    sources.append(social_account["url"])

            contact_info_list = []
            if data["email"]:
                contact_info_list.append(ContactInfo(
                    Type="email",
                    Value=data["email"]
                ))

            candidates.append(Candidate(
                Name=data["name"],
                Location=data["location"] if data["location"] != None else "",
                Picture=data["avatar_url"] if data["avatar_url"] != None else "",
                Summary=DescriptionModel(
                    Text=data["bio"] if data["bio"] != None else ""),
                Sources=sources,
                ContactInfoList=contact_info_list,
                ExternalSummaryStr=data["bio"] if data["bio"] != None else "",
            ))

        time.sleep(1)

    return candidates
