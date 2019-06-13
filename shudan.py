import re
import urllib.request
import pandas as pd
import json 


"""获取原始数据内容，并保存到excel"""
def getNovelContent():
	html = urllib.request.urlopen("http://uat.pages.book.qq.com/book/64714637").read()
	json_str=json.loads(html)
	#html = html.decode("utf-8") 
	# print(json_str)
	# print(type(json_str))
	book_sorted=json_str['data']
	# print(book_sorted)
	# print(len(book_sorted))
	numberx=len(book_sorted) 
	
	list_bookid = []
	list_bookname = []
	list_bookauthor = []
	list_bookprice = []
	list_bookintro = []

	books1=book_sorted.keys()
	booknew = [int(x) for x in books1]
	bubbleSort(booknew)
	booknew = [str(x) for x in booknew]

	for num in booknew:

		#提取书号
		list_bookid.append(book_sorted[num]['bookId'])
		#提取书名
		list_bookname.append(book_sorted[num]['bookName'])
		#提取作者
		list_bookauthor.append(book_sorted[num]['author'])
		#提取书本价格
		list_bookprice.append(book_sorted[num]['price'])
		#提取书本简介信息
		list_bookintro.append(book_sorted[num]['intro'])

	df = pd.DataFrame({'书号':list_bookid,'书名':list_bookname,'作者':list_bookauthor,'现价/元':list_bookprice,'简介':list_bookintro})
	#保存至excel中
	df.to_excel("book_net.xlsx",index=False)

"""引入排序算法"""
def bubbleSort(arr):
    n = len(arr)
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]


if __name__ == "__main__": 
	getNovelContent()