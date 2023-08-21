# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from model.member import Member

def test_add_new_member(app):
    app.session.login(username="admin", password="secret")
    app.member.create(Member(first_name="nfirst",
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
    app.session.logout()

def is_element_present(self, how, what):
    try: self.app.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True

