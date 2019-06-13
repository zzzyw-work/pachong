import xlrd
from xlwt import *



def read_excel(fileName):
    bk=xlrd.open_workbook(fileName)
    shxrange=range(bk.nsheets)
    try:
        sh=bk.sheet_by_name("Sheet1")#根据sheet1名字确定表格内容
    except:
        print ("代码出错")
    nrows=sh.nrows #获取行数
    li=[]
#定义一个空列表，以存储第二列的数据（哪一列都行，只要它具有唯一性）
    for i in range(1,nrows):
#对表格用行数进行遍历，存储到刚刚定义的li列表中，并返回它
        row_data=sh.row_values(i)
        value=sh.cell_value(i,1)
        li.append(value)
        return li



list1=list2=list3=list4=[]       
list1=read_excel('before.xlsx')
list2=read_excel('now.xlsx')
for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
 
for b in (list1 + list2):
    if b not in list3:
        list4.append(b) 
print(list3)

