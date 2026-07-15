import os

from config import EXCEL_FILE
from pages.challenge_page import ChallengePage
from utils.excel_reader import ExcelReader

def test_rpa_challenge(page):

    challenge = ChallengePage(page)

    challenge.open()

    challenge.download_excel(EXCEL_FILE)

    assert os.path.exists(EXCEL_FILE), "Excel file was not downloaded."

    data = ExcelReader.read_excel(EXCEL_FILE)

    challenge.start()

    for _, row in data.iterrows():
        challenge.complete_record(row)

    page.wait_for_timeout(3000)