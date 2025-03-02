from src.automation_playwright.pages.datademo import MyDataClass
from typing import Type

class DataPOM:
    def my_function(report_data: Type[MyDataClass]):
        print("Received dictionary:", report_data.my_dict)
