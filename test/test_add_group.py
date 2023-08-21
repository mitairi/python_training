# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from model.group import Group

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="newGroup", header="grHeader", footer="grFooter"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

def is_element_present(self, how, what):
    try: self.app.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True


