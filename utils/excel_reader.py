import pandas as pd


class ExcelReader:

    @staticmethod
    def read_excel(file_path):
        data = pd.read_excel(file_path)
        data.columns = data.columns.str.strip()
        return data