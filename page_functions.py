from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time


class PageFunctions(object):
    """
    Helper functions used for page functionality
    """
    def __init__(self, driver):
        """
        Initialize the driver, and other data we will use throughout functions.
        """
        self.driver = driver

    def wait_until_element_exist(self, time, element_id):
        """
        Waits for an element to exist in the given time frame
        :param time: time in seconds for the element to exist
        :param element_id: id of element
        """
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((By.ID, element_id)))

    def login(self, username=None, password=None):
        """
        Login to Hudl
        :param username: str
        :param password: str
        """
        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_id('logIn').click()

    def logout(self):
        """
        Logout of Huld
        """
        self.driver.find_element_by_id('inline-nickname').click()
        self.driver.find_element(By.LINK_TEXT, 'Log Out').click()

    def nav_to_manage_roster(self):
        """
        Navigate to the manage roster page
        """
        self.driver.find_element_by_id('nav_team').click()
        self.driver.find_element(By.LINK_TEXT, 'Roster').click()
        WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.ID, "add_player_link")))

    def get_roster_size(self):
        """
        Returns the size of the roster height
        (Used to verify roster additions or deletions)
        :return: (int)
        """
        return self.driver.find_element_by_id('roster_w').size['height']

    def add_player(self, firstname=None, lastname=None, **kwargs):
        """
        Adds a player to the roster with the given arguments
        :param firstname: First name of player
        :param lastname: Last name of player
        @param opts:    *jeresy_number: Player Jersey Number
                        *grad_year: Year of the player is graduating
                        *positions: Player positions
                        *email_address: Player's email address
        """
        self.driver.find_element_by_id('first_name').send_keys(firstname)
        self.driver.find_element_by_id('last_name').send_keys(lastname)
        jersey_number = kwargs.get('jersey_number')
        grad_year = kwargs.get('grad_year')
        positions = kwargs.get('positions')
        email_address = kwargs.get('email_address')

        if jersey_number:
            self.driver.find_element_by_id('jersey').send_keys(jersey_number)

        if email_address:
            self.driver.find_element_by_id('email').send_keys(email_address)

        if grad_year:
            class_picker = Select(self.driver.find_element_by_id('class'))
            class_picker.select_by_visible_text(grad_year)

        if positions:
            self.driver.find_element_by_id('position').click()
            self.wait_until_element_exist(10, 'newPosMenu')
            for pos in positions:
                self.driver.find_element_by_id('new_pos_' + pos).click()

        self.driver.find_element_by_id('add_player_link').click()
        time.sleep(3)

    def select_player(self, email_address):
        """
        Selects a player to click on with the given email address
        (email addresses differentiate players)
        :param email_address: Player's email address
        """
        xpath = "//p[contains(., '%s')]" % email_address
        self.driver.find_element_by_xpath(xpath).click()

    def delete_player_from_roster(self, email_address):
        """
        Deletes the selected player from teh roster
        :param email_address: The email address of the player to be deleted
        """

        self.select_player(email_address)
        self.driver.find_element_by_class_name(
            'delete_from_roster_link').click()
        self.wait_until_element_exist(5, 'ban_dialog')
        self.driver.find_element_by_id('delete_from_team').click()
        time.sleep(2)

    def clear_roster(self):
        """
        Used to clean roster of players
        """
        players_to_delete = []
        roster = self.driver.find_elements_by_class_name('email')
        for player in roster:
            players_to_delete.append(player.text)

        players_to_delete = filter(lambda player: player.strip(),
                                   players_to_delete)

        for player in players_to_delete:
            self.delete_player_from_roster(player)

    def upload_roster_file(self, file_path):
        """
        Uploads a roster from a xlsx or csv file stored locally
        :param file_path: Absolute path of file to be uploaded
        """
        self.driver.find_element_by_id('upload_new_roster').click()
        self.wait_until_element_exist(10, 'RosterFileUpload')
        self.driver.find_element_by_id('RosterFileUpload').send_keys(file_path)
        time.sleep(3)
        self.wait_until_element_exist(10, 'upload_dialog')
        self.driver.find_element_by_id('uploadNext').click()
        time.sleep(5)

    def disable_enable_player(self, email_address):
        """
        Disable or enable player from the roster
        :param email_address: The email address of the player to disable
        """
        self.select_player(email_address)
        self.driver.find_element_by_class_name('toggle_disabled_link').click()

    def is_element_displayed(self, element):
        """
        Return true or false if the element is displayed
        :param element: Element to check
        :return: bool
        """

        return self.driver.find_element_by_id(element).is_enabled()







