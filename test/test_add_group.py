# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
import pytest
from model.group import Group
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="newGroup", header="grHeader", footer="grFooter"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

def is_element_present(self, how, what):
    try: self.app.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True


