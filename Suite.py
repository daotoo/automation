from selenium import webdriver
import unittest
import os

from page_functions import PageFunctions

# Grad Years Strings
SENIOR = '2014 - SR'
JUNIOR = '2015 - JR'
SOPHOMORE = '2016 - SR'
FRESHMAN = '2017 - FR'


class Suite(unittest.TestCase):
    def setUp(self):
        self.email = os.environ.get('HUDL_EMAIL')
        self.password = os.environ.get('HUDL_PASS')
        self.import_path = os.environ.get('HUDL_IMPORT_FILE')
        self.chrome_driver_path = os.environ.get('Chrome_driver')
        self.driver = webdriver.Firefox()
        self.pg = PageFunctions(self.driver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.hudl.com/login/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def test_login_and_out(self):
        self.pg.login(self.email, self.password)
        self.pg.wait_until_element_exist(10, 'nav_coaching_tools')
        self.pg.nav_to_manage_roster()
        self.pg.logout()

    def test_add_player_required_only(self):
        self.pg.login(self.email, self.password)
        self.pg.wait_until_element_exist(10, 'nav_coaching_tools')
        self.pg.nav_to_manage_roster()
        orig_roster_size = self.pg.get_roster_size()
        self.pg.add_player(firstname='Derek', lastname='Otoo',
                           email_address='test2@comcast.net')
        new_roster_size = self.pg.get_roster_size()
        self.assertGreater(new_roster_size, orig_roster_size)

    def test_add_player_optional_args(self):
        self.pg.login(self.email, self.password)
        self.pg.wait_until_element_exist(10, 'nav_coaching_tools')
        self.pg.nav_to_manage_roster()
        orig_roster_size = self.pg.get_roster_size()
        self.pg.add_player(firstname='Derek', lastname='Otoo',
                           jersey_number='16', grad_year=SENIOR,
                           email_address='test@iastate.edu',
                           positions=['QB', 'TE', 'RB'])
        new_roster_size = self.pg.get_roster_size()
        self.assertGreater(new_roster_size, orig_roster_size)

    def test_add_player_required_only_already_exist(self):
        self.pg.login(self.email, self.password)
        self.pg.wait_until_element_exist(10, 'nav_coaching_tools')
        self.pg.nav_to_manage_roster()
        orig_roster_size = self.pg.get_roster_size()
        self.pg.add_player(firstname='Derek', lastname='Otoo',
                           email_address='test2@comcast.net')
        new_roster_size = self.pg.get_roster_size()
        self.assertEqual(new_roster_size, orig_roster_size)

    def test_delete_player(self):
        self.pg.login(self.email, self.password)
        self.pg.wait_until_element_exist(10, 'nav_coaching_tools')
        self.pg.nav_to_manage_roster()
        orig_roster_size = self.pg.get_roster_size()
        self.pg.delete_player_from_roster('test2@comcast.net')
        new_roster_size = self.pg.get_roster_size()
        self.assertGreater(orig_roster_size, new_roster_size)

    def test_upload_roster(self):
        self.pg.login(self.email, self.password)
        self.pg.wait_until_element_exist(10, 'nav_coaching_tools')
        self.pg.nav_to_manage_roster()
        orig_roster_size = self.pg.get_roster_size()
        self.pg.upload_roster_file(self.import_path)
        new_roster_size = self.pg.get_roster_size()
        self.assertGreater(new_roster_size, orig_roster_size)

    def test_disabled_enable_player(self):
        self.pg.login(self.email, self.password)
        self.pg.wait_until_element_exist(10, 'nav_coaching_tools')
        self.pg.nav_to_manage_roster()
        self.pg.disable_enable_player('test@iastate.edu')
        self.pg.is_element_displayed('notificationinner')
        self.pg.disable_enable_player('test@iastate.edu')
        self.pg.is_element_displayed('notificationinner')

    def test_ZZZ_cleanup(self):
        self.pg.login(self.email, self.password)
        self.pg.wait_until_element_exist(10, 'nav_coaching_tools')
        self.pg.nav_to_manage_roster()
        self.pg.clear_roster()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()