# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from member import Member
from application import Application


class AddNewMember(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_new_member(self):
        self.app.login(username="admin", password="secret")
        self.app.add_new_member(Member(first_name="nfirst",
                                       middle_name="nmiddle",
                                       last_name="nlast",
                                       nickname="nnick",
                                       title="ntitle",
                                       company="ncompany",
                                       address="new address",
                                       home_number="123444",
                                       mobile_number="548",
                                       work_number="5654",
                                       fax_number="848",
                                       email="email@gg.ru",
                                       email2="email2@gg.ru",
                                       email3="email3@gg.ru",
                                       homepage="http://homepage",
                                       birthday="30",
                                       birthmonth="March",
                                       birthyear="2000",
                                       annyversary_day="21",
                                       annyversary_month="August",
                                       annyversary_year="2020",
                                       second_address="second address",
                                       phone2_number="12 bld",
                                       notes="new notes"))
        self.app.logout()

    def is_element_present(self, how, what):
        try: self.app.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: alert = self.app.wd.switch_to.alert
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.app.destroy()


if __name__ == "__main__":
    unittest.main()
