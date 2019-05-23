import re
import urllib.request
import pandas as pd

def getNovelContent():
	html = urllib.request.urlopen("http://hd.book.qq.com/6477675/vivo.html").read()
	html = html.decode("utf-8") 
	#解析并提取数据源超链接地址
	reg = r'<script type="text/javascript" src="(https{1}://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"></script>'  
	reg = re.compile(reg)     
	urls = re.findall(reg,html) 
	print(urls)

	for url in urls:
		print(url)
		chapter_html = urllib.request.urlopen(url).read() 

		#当前要解析的原始数据
		chapter_html = chapter_html.decode("utf-8")

		worldlist=re.split("men:",chapter_html)

		book1=str(worldlist[1])
		nanshu=re.split(",girls:",book1)
		#print(nanshu[1])

		bookgirl=str(nanshu[1]).split("booklist1:")[1]

		#女书列表
		bookgirl=str(bookgirl).split("},mounted")[0]
		bookgirl=str(bookgirl).split(",booklist2:")
		bookgirl=str(bookgirl).split(",desc1")[0]
		bookgirls=str(bookgirl).split(",")
		#print(bookgirl)
        
        #男书列表
		bookmen=str(nanshu[0]).split("booklist1:")[1]
		bookmen=str(bookmen).split(",booklist2:")
		bookmen=str(bookmen).split(",desc1")[0]
		bookmen=str(bookmen).split(",")
		#bookmen1=str(bookmen)
		print(bookmen)


		# print(len(bookmen))

		df=pd.DataFrame(bookmen,columns=['内容'])
		df.to_excel("wenxuemen.xlsx",index=False)

		df=pd.DataFrame(bookgirls,columns=['内容'])
		df.to_excel("wenxuemgirl.xlsx",index=False)





		#if 'yuewendata' not 


		#print(chapter_html)


if __name__ == "__main__": 
	getNovelContent()