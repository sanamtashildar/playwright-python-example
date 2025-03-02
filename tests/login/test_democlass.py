from src.automation_playwright.pages.dataPOM import DataPOM
from src.automation_playwright.pages.datademo import MyDataClass

import pytest
report_data = MyDataClass()
def test_demo_data():
    v1 = report_data.my_dict.get("key1")
    print(v1)
    # DataPOM().my_function()

