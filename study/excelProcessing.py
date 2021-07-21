from openpyxl import Workbook


def make_excelfile():
    wb = Workbook()
    sheet1=wb.active

    sheet1.title="Device Level"