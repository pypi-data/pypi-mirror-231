import os
import shutil
import json
import time
import re
from hashlib import md5
from glob import glob
from typing import Optional, Tuple, Dict, List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Change this to whatever folder you want the results to be saved in
BASE_FOLDER = os.getcwd()

# Profile from where to start the search if links.txt is absent
SEED_PROFILE = 'https://www.linkedin.com/in/andrea-manenti-00098625b/'

# Implicit wait between operations in seconds
IMPLICIT_WAIT = 0.5


class LinkedInDriver:
    """
        Represents a selenium WebDriver which crawls LinkedIn for profiles.

    Parameters:
    ----------
    seed_profile : Optional[str]
        The initial profile from where to start branching out.
    base_folder : Optional[str]
        The folder where to save profiles.
    """
    def __init__(self, seed_profile: Optional[str] = SEED_PROFILE, base_folder: Optional[str] = BASE_FOLDER):
        self.driver = webdriver.Chrome()
        self.driver.get(seed_profile)
        self.base_folder = base_folder
        self.implicit_wait = IMPLICIT_WAIT
        self.driver.implicitly_wait(IMPLICIT_WAIT)

        try:
            with open(f'{base_folder}/links.txt', 'r') as f:
                self.queue = list(f.readlines())
        except FileNotFoundError:
            self.queue = [SEED_PROFILE]

    def wait_for_captcha(self):
        """
            Waits for a captcha to be solved
        """
        print('waiting for CAPTCHA to be solved', end='')
        while re.search(r'checkpoint/challenges', self.driver.current_url):
            print('.', end='')
            time.sleep(2 * self.implicit_wait)

        print('\nthanks for solving the CAPTCHA, human!')

    def explore_profile(self, url: str) -> Tuple[dict, Dict[str, list]]:
        """
            Explores a single profile.

        Parameters:
        ----------
        url : str
            The url of the profile's page

        Returns:
        ----------
        A tuple with candidate's profile and a dict of various links of potential new profiles
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

    def to_disk_and_queue(self, profile: dict, extra_links: Dict[str, list]) -> bool:
        """
        Saves a profile to disk and updates the queue.

        Parameters:
        ----------
        profile : dict
            A dict containing the user's profile
        extra_links : dict
            The links found in the above profile's page

        Returns:
        ----------
        True if successful and False if a key wasn't found
        """

        try:
            try:
                lnks = extra_links['People also viewed']
            except KeyError:
                lnks = []

            self.queue = lnks + self.queue
            with open(f'{self.base_folder}/links.txt', 'a+') as g:
                for q in lnks:
                    g.write(q + '\n')
            print(f'Added {len(lnks)} links, queue length={len(self.queue)}')

            name = profile['name']
            url = profile['url']

            m = md5()
            m.update(url.encode('utf8'))
            path = f'{self.base_folder}/{name}-{m.hexdigest()}.json'

            with open(path, 'w') as f:
                json.dump(profile, f)

            print(f'Candidate {name} saved to {path}')
            return True

        except KeyError as k:
            print(f'key not found: {k}')
            return False


def run_linkedin_scraper(
        max_users: int,
        seed_profile: Optional[str] = SEED_PROFILE,
        base_folder: Optional[str] = BASE_FOLDER
):
    """
    Main function to run the LinkedIn scraper.

    Parameters:
    ----------
    max_users : int
        Maximum number of users to fetch and save.
    seed_profile : Optional[str]
        The initial profile from where to start branching out.
    base_folder : Optional[str]
        The folder where to save profiles.
    """
    driver = LinkedInDriver(seed_profile=seed_profile, base_folder=base_folder)
    n_profiles = 0

    driver.wait_for_captcha()

    while driver.queue and n_profiles < max_users:
        url = driver.queue.pop()
        cand, lnks = driver.explore_profile(url)
        success = driver.to_disk_and_queue(cand, lnks)
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

    Parameters:
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