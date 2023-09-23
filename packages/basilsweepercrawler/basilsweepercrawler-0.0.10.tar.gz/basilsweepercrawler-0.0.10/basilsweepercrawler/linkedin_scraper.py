import os
import shutil
import json
import time
import re
from hashlib import md5
from glob import glob
from typing import Optional, Tuple, Dict, List
from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.window import WindowTypes
from selenium.common.exceptions import NoSuchElementException, NoSuchAttributeException

# Change this to whatever folder you want the results to be saved in
BASE_FOLDER = os.getcwd()

# Profile from where to start the search if links.txt is absent
SEED_PROFILE = 'https://www.linkedin.com/in/andrea-manenti-00098625b/'

# Implicit wait between operations in seconds
IMPLICIT_WAIT = 0.5


class LinkedInDriver:
    """
    Represents a selenium WebDriver which crawls LinkedIn for profiles.
    """

    URL_TEMPLATE = r'https://www.linkedin.com/search/results/people/?keywords={keywords}&page={page}'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.linkedin.com/home')
        self.implicit_wait = IMPLICIT_WAIT
        self.driver.implicitly_wait(IMPLICIT_WAIT)
        self.signed_in = False

    def wait_for_captcha(self):
        """
        Waits for a captcha to be solved
        """
        print('waiting for CAPTCHA to be solved', end='')
        while re.search(r'checkpoint/challenges', self.driver.current_url):
            print('.', end='')
            time.sleep(2 * self.implicit_wait)

        print('\nthanks for solving the CAPTCHA, human!')

    def signin(self):
        """
        Attempts a sign-in with the username and password given as environment variables
        """

        # TODO Make an account for the scraper

        self.driver.get('https://www.linkedin.com/uas/login')
        time.sleep(self.implicit_wait)

        if re.search(r'uas/login', self.driver.current_url):
            print('trying to sign-in...')

            try:
                username_field = self.driver.find_element(By.ID, 'username')
                password_field = self.driver.find_element(By.ID, 'password')
            except NoSuchElementException as e:
                print(f'could not find the username or password field: {e}')
                return

            try:
                username = os.environ['LINKEDIN_USERNAME']
                password = os.environ['LINKEDIN_PASSWORD']
            except KeyError:
                print('you must provide environment variables LINKEDIN_USERNAME and LINKEDIN_PASSWORD')
                raise

            username_field.clear()
            password_field.clear()
            username_field.send_keys(username)
            password_field.send_keys(password)

            try:
                signin = self.driver.find_element(By.CLASS_NAME, 'btn__primary--large')
            except NoSuchElementException:
                print(f'could not find the sign-in button somehow')
                return

            signin.click()
            time.sleep(self.implicit_wait)

            print('I managed to sign in')
            self.signed_in = True

        else:
            print('Something went wrong')

    def explore_profile(self, url: str) -> Tuple[dict, Dict[str, list]]:
        """
        Explores a single profile.

        Parameters
        ----------
        url : str
            The url of the profile's page

        Returns
        -------
        tuple
            A tuple with candidate's profile and a dict of various links of potential new profiles
        """
        if self.signed_in:
            return self._explore_profile_signed_in(url)
        else:
            return self._explore_profile_signed_out(url)

    def _explore_profile_signed_in(self, url: str) -> Tuple[dict, Dict[str, list]]:
        """
        Explores a single profile while signed out.
        """
        # TODO
        pass

    def _explore_profile_signed_out(self, url: str) -> Tuple[dict, Dict[str, list]]:
        """
        Explores a single profile while signed out
        """

        print(f'Accessing {url}')
        self.driver.get(url)

        time.sleep(self.implicit_wait)

        if re.search(r'checkpoint/challenges', self.driver.current_url):
            self.wait_for_captcha()

        button = self.driver.find_elements(By.CLASS_NAME, 'modal__dismiss')
        for b in button:
            try:
                b.click()
            except:
                continue

        # Name
        try:
            name = self.driver.find_element(By.CLASS_NAME, 'top-card-layout__title').text
        except NoSuchElementException:
            # When this happens typically the profile was completely empty
            # m = md5()
            # m.update(url.encode('utf8'))
            # name = f'unknown-{m.hexdigest()}'
            return {}, {'People also viewed': []}

        # All core sections
        elts = self.driver.find_elements(By.CLASS_NAME, value='core-section-container')

        # Bio
        try:
            bio = elts[0]
            biography = bio.find_element(By.TAG_NAME, value='div').text
        except IndexError:
            biography = 'Not found'

        # Experiences or education or any sort of thing
        experiences = {}
        for e in elts[1:]:
            try:
                exp_type = e.find_element(By.CLASS_NAME, value='core-section-container__title').text
                experiences[exp_type] = []
                itere = e.find_elements(By.CLASS_NAME, value='profile-section-card')
                for x in itere:
                    experiences[exp_type].append(e.text)
            except NoSuchElementException:
                pass

        # All side elements
        elts2 = self.driver.find_elements(By.CLASS_NAME, value='aside-section-container')

        extra_links = {}
        for e in elts2:
            key = e.find_element(By.TAG_NAME, value='h2').text
            extra_links[key] = []
            links = e.find_elements(By.CLASS_NAME, value='base-aside-card--link')
            for link in links:
                extra_links[key].append(link.get_property('href'))

        return {
            'name': name,
            'url': url,
            'biography': biography,
            'experiences': experiences,
        }, extra_links

    @classmethod
    def to_disk_and_queue(
            cls,
            profile: dict,
            extra_links: Dict[str, list],
            queue: List[str],
            base_folder: str
    ) -> Tuple[bool, List[str]]:
        """
        Saves a profile to disk and updates the queue.

        Parameters
        ----------
        profile : dict
            A dict containing the user's profile
        extra_links : dict
            The links found in the above profile's page
        queue : str
            The current queue
        base_folder : str
            The base folder where to save results

        Returns
        -------
        tuple[bool, list[str]]
            A bool representing the success or failure of the method and the updated queue
        """

        try:
            lnks = extra_links['People also viewed']
        except KeyError:
            lnks = []

        lnks = [ln for ln in lnks if ln not in queue]

        new_queue = lnks + queue
        with open(f'{base_folder}/links.txt', 'a+') as g:
            for q in lnks:
                g.write(q + '\n')
        print(f'Added {len(lnks)} links, queue length={len(new_queue)}')

        if cls.to_disk(profile, base_folder):
            return True, new_queue
        else:
            return False, queue

    @staticmethod
    def to_disk(profile: dict, base_folder: str) -> bool:
        """
        Saves a profile to disk.

        Parameters
        ----------
        profile : dict
            A dict containing the user's profile
        base_folder : str
            The base folder where to save results

        Returns
        -------
        bool
            A bool representing the success or failure of the method and the updated queue
        """

        try:

            name = profile['name']
            url = profile['url']

            m = md5()
            m.update(url.encode('utf8'))
            path = f'{base_folder}/{name}-{m.hexdigest()}.json'

            if os.path.isfile(path):
                path_noext, ext = os.path.splitext(path)
                tentative = f'{path_noext}_old.{ext}'
                n = 0
                while os.path.isfile(tentative):
                    n += 1
                    tentative = f'{path_noext}_old{n}.{ext}'

                print(f'moved existing profile from {path} to {tentative}')
                shutil.move(path, tentative)

            with open(path, 'w') as f:
                json.dump(profile, f)

            print(f'Candidate {name} saved to {path}')
            return True

        except KeyError as k:
            print(f'key not found: {k}')
            return False

    def explore_search_results(self, query: str, max_results: int) -> List[str]:
        """
        Performs a search and explores the results

        Arguments
        ---------
        query : str
            The query to search for
        max_results : int
            Maximum number of results to retrieve

        Returns
        -------
        list[str]
            A list of potential links to user profiles
        """
        max_page = 100  # what is the max page number??
        found = []
        self.signin()

        for page in range(1, max_page + 1):
            self.driver.get(self.URL_TEMPLATE.format(keywords=quote(query), page=page))

            try:
                all_results = self.driver.find_elements(By.CLASS_NAME, value='entity-result__item')
            except NoSuchElementException:
                print(f'search results container not found in page {page}')
                continue

            # Create a new tab for later
            search_tab = self.driver.current_window_handle
            self.driver.switch_to.new_window(WindowTypes.TAB)
            profile_tab = self.driver.current_window_handle
            self.driver.switch_to.window(search_tab)

            for result in all_results:
                try:
                    lnk_tag = result.find_element(By.CLASS_NAME, value='app-aware-link')
                    lnk = lnk_tag.get_attribute('href')

                    # We actually have to follow the link otherwise this won't be accessible from logged-out
                    self.driver.switch_to.window(profile_tab)
                    self.driver.get(lnk)
                    time.sleep(self.implicit_wait)
                    lnk = self.driver.current_url
                    found.append(lnk)
                    self.driver.switch_to.window(search_tab)
                    if len(found) >= max_results:
                        return found
                except (NoSuchElementException, NoSuchAttributeException) as e:
                    print(f'link not found in page {page}: {e}')
                    continue

        return found


def run_linkedin_scraper(
        max_users: int,
        seed_profile: Optional[str] = SEED_PROFILE,
        base_folder: Optional[str] = BASE_FOLDER
):
    """
    Main function to run the LinkedIn scraper.

    Parameters
    ----------
    max_users : int
        Maximum number of users to fetch and save.
    seed_profile : Optional[str]
        The initial profile from where to start branching out.
    base_folder : Optional[str]
        The folder where to save profiles.
    """
    driver = LinkedInDriver()
    n_profiles = 0

    try:
        with open(f'{base_folder}/links.txt', 'r') as f:
            queue = list(f.readlines())
    except FileNotFoundError:
        queue = [seed_profile]

    driver.driver.get(queue[0])
    driver.wait_for_captcha()

    while queue and n_profiles < max_users:
        url = queue.pop()
        cand, lnks = driver.explore_profile(url)
        success, queue = driver.to_disk_and_queue(cand, lnks, queue, base_folder)
        if success:
            n_profiles += 1
        time.sleep(driver.implicit_wait)


def update_profiles(base_folder: str, backup_folder: Optional[str] = None):
    """
    Updates existing profiles (optionally making a backup)

    Parameters:
    ----------
    base_folder : str
        The folder with the profiles
    backup_folder : str | None
        The folder where to make the backup
    """
    scraped = list(glob(f'{base_folder}/*.json'))

    if backup_folder and os.path.isdir(backup_folder):
        for a in scraped:
            shutil.copy(a, os.path.join(backup_folder, os.path.basename(a)))

    driver = LinkedInDriver(seed_profile=SEED_PROFILE, base_folder=base_folder)
    driver.wait_for_captcha()

    for i, a in enumerate(scraped):
        try:
            with open(a, 'r') as f:
                print(f'[{i}/{len(scraped)}] done ...')
                x = json.load(f)
                cand, lnks = driver.explore_profile(x['url'])
                driver.to_disk_and_queue(cand, lnks)
        except FileNotFoundError:
            print(f'file {a} was removed')
            continue


def merge_profiles(base_folder: str, merge_folder: str):
    """
    Merge profiles from a folder to another keeping the largest file between the two.

    Parameters
    ----------
    base_folder : str
        The folder to merge into
    merge_folder : str
        The folder to merge from (could be the backup copy you did above)
    """
    to_merge = list(glob(f'{merge_folder}/*.json'))

    for m in to_merge:
        f_name = os.path.basename(m)
        target = os.path.join(base_folder, f_name)
        if os.path.isfile(target):
            size_target = os.stat(target).st_size
            size_merge = os.stat(m).st_size
            print(f'found match {f_name}, target: {size_target}B, merge: {size_merge}B.', end=' ')
            if size_merge > size_target:
                print('merge -> target')
                shutil.copy(m, target)
            else:
                print('do nothing')
        else:
            print(f'{f_name} not found in target, copying')
            shutil.copy(m, target)


def run_linkedin_search(query: str, max_users: int) -> Tuple[List[str], List[dict]]:
    """
    Runs a LinkedIn search with the given query and returns at most n_max results

    Arguments
    ---------
    query : str
        The keywords of the search
    max_users : int
        Max number of results to retrieve

    Returns
    -------
    tuple[list[str], list[dict]]
        The list of links and the respective retrieved user profiles
    """

    results = []
    driver = LinkedInDriver()
    links = driver.explore_search_results(query, max_users)

    if len(links) == 0:
        print('no links retrieved')
        return [], []

    print('retrieved the following links:')
    for ln in links:
        print(ln)

    # We need to make another driver because now we don't want to be logged in
    other_driver = LinkedInDriver()
    other_driver.driver.get(links[0])
    other_driver.wait_for_captcha()

    for ln in links:
        profile, _ = other_driver.explore_profile(ln)
        results.append(profile)

    return links, results
