from web_sweepers import run_external_web_sweeper, call_serper_api, scrape_github_links, scrape_linkedin_profile_links
from unittest.mock import patch, Mock, mock_open, call
from searchdatamodels import Candidate
import unittest
import os
import sys
from dotenv import load_dotenv
sys.path.append(os.getcwd())


class TestWebSweepers(unittest.TestCase):

    def setUp(self):
        self.token = "test_token"
        self.username = "alice"
        load_dotenv()

    @patch('requests.post')
    def test_call_serper_api(self, mock_post):
        mock_response = Mock()
        mock_response.json.return_value = {"organic": [
            {"link": "https://github.com/alice"}, {"link": "https://github.com/bob"}, {"link": "https://linkedin.com/in/carl"}, {"link": "https://linkedin.com/in/dave"}]}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        links = call_serper_api("ML Engineers", num_results=2)
        self.assertEqual(len(links), 4)
        self.assertIn("https://github.com/alice", links)
        self.assertIn("https://github.com/bob", links)
        self.assertIn("https://linkedin.com/in/carl", links)
        self.assertIn("https://linkedin.com/in/dave", links)

    @patch('requests.get')
    def test_scrape_linkedin_profile_links(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "public_identifier": "alice_smith",
            "full_name": "Alice Smith",
            "summary": None,
            "country_full_name": "Sweden",
            "city": "Stockholm",
            "state": None,
            "experiences": [
                {
                    "starts_at": None,
                    "ends_at": None,
                    "company": "Talentium",
                    "company_linkedin_profile_url": None,
                    "title": "Software Engineer",
                    "description": None,
                    "location": None,
                    "logo_url": None
                },
                {
                    "starts_at": {
                        "day": 1,
                        "month": 1,
                        "year": 2020
                    },
                    "ends_at": {
                        "day": 13,
                        "month": 5,
                        "year": 2021
                    },
                    "company": "Google",
                    "company_linkedin_profile_url": None,
                    "title": "Product Manager",
                    "description": "Manages product.",
                    "location": "Jakarta, Indonesia",
                    "logo_url": None
                }
            ],
            "education": [
                {
                    "starts_at": {
                        "day": 1,
                        "month": 1,
                        "year": 2022
                    },
                    "ends_at": None,
                    "field_of_study": "Computer Science",
                    "degree_name": "Bachelor",
                    "school": "University of Wololo",
                    "school_linkedin_profile_url": None,
                    "description": "Studied computer science at University of Wololo. Joined multiple clubs and societies.",
                    "logo_url": None,
                    "grade": None,
                    "activities_and_societies": None
                },
                {
                    "starts_at": {
                        "day": 1,
                        "month": 1,
                        "year": 2018
                    },
                    "ends_at": {
                        "day": 31,
                        "month": 12,
                        "year": 2021
                    },
                    "field_of_study": "Social Sciences",
                    "degree_name": None,
                    "school": "SMA 1 Semarang",
                    "school_linkedin_profile_url": None,
                    "description": None,
                    "logo_url": None,
                    "grade": None,
                    "activities_and_societies": None
                }
            ],
            "accomplishment_projects": [
                {
                    "title": None,
                    "description": "Build a website.",
                }
            ],
            "skills": [
                "Rust", "Python", "C++", "Project Management"
            ],
            "personal_emails": [],
            "personal_numbers": ["(+47) 81237291"]
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        candidate: Candidate = scrape_linkedin_profile_links(
            ["https://linkedin.com/in/alice"])

        self.assertEqual(len(candidate), 1)

        candidate = candidate[0]
        self.assertEqual(candidate.Name, "alice smith")
        self.assertEqual(candidate.Location, "stockholm, sweden")
        self.assertEqual(candidate.Skills, [
                         "rust", "python", "c++", "project management"])

        self.assertEqual(
            candidate.WorkExperienceList[0].Specialization, "software engineer")
        self.assertEqual(
            candidate.WorkExperienceList[0].Institution, "talentium")
        self.assertEqual(
            candidate.WorkExperienceList[1].Specialization, "product manager")
        self.assertEqual(candidate.WorkExperienceList[1].Institution, "google")
        self.assertEqual(
            candidate.WorkExperienceList[1].Description.Text, "Manages product.")

        self.assertEqual(
            candidate.EducationExperienceList[0].Specialization, "computer science")
        self.assertEqual(
            candidate.EducationExperienceList[0].Institution, "university of wololo")
        self.assertEqual(
            candidate.EducationExperienceList[0].Degree, "bachelor")
        self.assertEqual(candidate.EducationExperienceList[0].Description.Text,
                         "Studied computer science at University of Wololo. Joined multiple clubs and societies.")
        self.assertEqual(
            candidate.EducationExperienceList[1].Specialization, "social sciences")
        self.assertEqual(
            candidate.EducationExperienceList[1].Institution, "sma 1 semarang")
        self.assertEqual(candidate.EducationExperienceList[1].Degree, "")
        self.assertEqual(
            candidate.EducationExperienceList[1].Description.Text, "")

        self.assertEqual(candidate.ExternalSummaryStr, "")
        self.assertEqual(candidate.ProjectList[0].Text, "Build a website.")
        self.assertEqual(candidate.ContactInfoList[0].Type, "phone")
        self.assertEqual(candidate.ContactInfoList[0].Value, "(+47) 81237291")
        self.assertIn("https://www.linkedin.com/in/alice_smith",
                      candidate.Sources)

    @patch('requests.get')
    def test_scrape_github_links(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {
            "login": "alice",
            "type": "User",
            "name": "Alice Smith",
            "blog": "https://alice.com",
            "bio": "I am a software engineer.",
            "email": "alice@smi.th",
            "location": "USA",
            "avatar_url": "image.com"
        }
        mock_response.status_code = 200

        mock_response_social_accounts = Mock()
        mock_response_social_accounts.json.return_value = [
            {
                "provider": "twitter",
                "url": "https://twitter.com/alice"
            },
            {
                "provider": "linkedin",
                "url": "https://linkedin.com/in/alice"
            }
        ]
        mock_response_social_accounts.status_code = 200

        mock_get.side_effect = [mock_response, mock_response_social_accounts]

        candidate = scrape_github_links(["https://github.com/alice"])

        self.assertEqual(len(candidate), 1)

        candidate = candidate[0]
        self.assertEqual(candidate.Name, "alice smith")
        self.assertEqual(candidate.Location, "usa")
        self.assertEqual(candidate.Picture, "image.com")
        self.assertEqual(candidate.Summary.Text,
                         "I am a software engineer.")
        self.assertEqual(candidate.ExternalSummaryStr,
                         "I am a software engineer.")
        self.assertEqual(candidate.ContactInfoList[0].Type, "email")
        self.assertEqual(candidate.ContactInfoList[0].Value, "alice@smi.th")
        self.assertIn("https://github.com/alice", candidate.Sources)
        self.assertIn("https://twitter.com/alice", candidate.Sources)
        self.assertIn("https://linkedin.com/in/alice", candidate.Sources)

        self.assertEqual(candidate.Skills, [])
        self.assertEqual(candidate.WorkExperienceList, [])
        self.assertEqual(candidate.EducationExperienceList, [])
        self.assertEqual(candidate.ProjectList, [])

    @patch('requests.post')
    @patch('requests.get')
    def test_run_external_web_sweepers(self, mock_get, mock_post):
        mock_response_serper = Mock()
        mock_response_serper.json.return_value = {"organic": [
            {"link": "https://github.com/alice"}]}
        mock_response_serper.status_code = 200
        mock_post.return_value = mock_response_serper

        mock_response_github = Mock()
        mock_response_github.json.return_value = {
            "login": "alice",
            "type": "User",
            "name": None,
            "blog": "https://alice.com",
            "bio": "I am a software engineer.",
            "email": None,
            "location": "USA",
            "avatar_url": "image.com"
        }
        mock_response_github.status_code = 200

        mock_response_github_social_accounts = Mock()
        mock_response_github_social_accounts.json.return_value = []
        mock_response_github_social_accounts.status_code = 200

        mock_get.side_effect = [mock_response_github,
                                mock_response_github_social_accounts]

        candidates = run_external_web_sweeper(
            ["ML Engineers"], num_results_per_site=1)

        self.assertEqual(len(candidates), 0)


if __name__ == '__main__':
    unittest.main()
