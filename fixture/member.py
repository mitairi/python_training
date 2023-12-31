from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MemberHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def create(self, member):
        wd = self.app.wd
        self.open_add_new_page()
        # add new member
        # fill in basic info
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(member.first_name)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(member.middle_name)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(member.last_name)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(member.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").clear()
        wd.find_element(By.NAME, "title").send_keys(member.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(member.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(member.address)
        # fill in phone info
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").clear()
        wd.find_element(By.NAME, "home").send_keys(member.home_number)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").clear()
        wd.find_element(By.NAME, "mobile").send_keys(member.mobile_number)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").clear()
        wd.find_element(By.NAME, "work").send_keys(member.work_number)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").clear()
        wd.find_element(By.NAME, "fax").send_keys(member.fax_number)
        # fill in email info
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(member.email)
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").clear()
        wd.find_element(By.NAME, "email2").send_keys(member.email2)
        wd.find_element(By.NAME, "email3").click()
        wd.find_element(By.NAME, "email3").clear()
        wd.find_element(By.NAME, "email3").send_keys(member.email3)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").clear()
        wd.find_element(By.NAME, "homepage").send_keys(member.homepage)
        # fill in birthday info
        wd.find_element(By.NAME, "bday").click()
        Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(member.birthday)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[@name='bday']/option[@value='"+member.birthday+"']").click()
        wd.find_element(By.NAME, "bmonth").click()
        Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(member.birthmonth)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[@name='bmonth']/option[@value='"+member.birthmonth+"']").click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").clear()
        wd.find_element(By.NAME, "byear").send_keys(member.birthyear)
        # fill in anniversary info
        wd.find_element(By.NAME, "aday").click()
        Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(member.annyversary_day)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[@name='aday']/option[@value='"+member.annyversary_day+"']").click()
        wd.find_element(By.NAME, "amonth").click()
        Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(member.annyversary_month)
        wd.find_element(By.XPATH, "//div[@id='content']/form/select[@name='amonth']/option[@value='"+member.annyversary_month+"']").click()
        wd.find_element(By.NAME, "ayear").click()
        wd.find_element(By.NAME, "ayear").clear()
        wd.find_element(By.NAME, "ayear").send_keys(member.annyversary_year)
        # fill in secondary address
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").clear()
        wd.find_element(By.NAME, "address2").send_keys(member.second_address)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").clear()
        wd.find_element(By.NAME, "phone2").send_keys(member.phone2_number)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").clear()
        wd.find_element(By.NAME, "notes").send_keys(member.notes)
        # submit new member creation
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[@name='submit']").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()
