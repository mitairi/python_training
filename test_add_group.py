# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group
from application import Application


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="newGroup", header="grHeader", footer="grFooter"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(username="admin", password="secret")
        self.app.create_group(Group(name="", header="", footer=""))
        self.app.logout()

    def is_element_present(self, how, what):
        try: self.app.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        #try: self.wd.switch_to_alert()
        try: alert = self.app.wd.switch_to.alert
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
