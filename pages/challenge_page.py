from pages.base_page import BasePage
from config import BASE_URL, TIMEOUT

class ChallengePage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.download_excel_btn = page.get_by_text("Download Excel")
        self.start_btn = page.get_by_role("button", name="Start")
        self.submit_btn = page.get_by_role("button", name="Submit")

        self.first_name = page.locator("[ng-reflect-name='labelFirstName']")
        self.last_name = page.locator("[ng-reflect-name='labelLastName']")
        self.company = page.locator("[ng-reflect-name='labelCompanyName']")
        self.role = page.locator("[ng-reflect-name='labelRole']")
        self.address = page.locator("[ng-reflect-name='labelAddress']")
        self.email = page.locator("[ng-reflect-name='labelEmail']")
        self.phone = page.locator("[ng-reflect-name='labelPhone']")

    def open(self):
        self.page.goto(BASE_URL, wait_until="load", timeout=TIMEOUT)

    def download_excel(self, save_path):
        with self.page.expect_download() as download_info:
            self.download_excel_btn.click()

        download = download_info.value
        download.save_as(save_path)

    def start(self):
        self.start_btn.click()
        self.first_name.wait_for()

    def fill_form(self, row):
        self.first_name.fill(str(row["First Name"]))
        self.last_name.fill(str(row["Last Name"]))
        self.company.fill(str(row["Company Name"]))
        self.role.fill(str(row["Role in Company"]))
        self.address.fill(str(row["Address"]))
        self.email.fill(str(row["Email"]))
        self.phone.fill(str(row["Phone Number"]))

    def submit(self):
        self.submit_btn.click()

    def complete_record(self, row):
        self.fill_form(row)
        self.submit()