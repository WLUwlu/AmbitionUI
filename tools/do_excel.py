#coding=utf-8
from openpyxl import load_workbook

wb=load_workbook('xh.xlsx')
sheet=wb["Python"]

res=sheet.cell(1,1)
#错误演示：只演示到单元格，并未取值，cell是单元格
print(res)
