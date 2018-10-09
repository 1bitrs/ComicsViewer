# -*- coding: utf-8 -*-
# python 3.7.0

import os
import time
import shelve

BASE_PATH = os.getcwd()
CONTENTS_PATH = BASE_PATH + "/contents"

DATA_PATH = "data/data"
INDEX_HTML = "/index.html"
CONTENT_HTML = "/29f459a44fee58c7.html"

TEMPLETE_HTML = "/h/templete.html"
INDEX_TEMPLETE_HTML = "/h/index_templete.html"

IMG_SUFFIX = [".jpg", ".png", ".jpeg", ".gif"]


def createComicItems(title, content_path, first_img, count):
	templete = r'<li><a href="{url}" target="_blank" title="{title}"><h2>{title}</h2><div class="image"><img class="lazy" src="{first_img}"><table class="data"><tr><th scope="row">枚数</th><td>{count}枚</td></tr><tr><td class="tag" colspan="2"><span>{title}</span></td></tr></table></div><p class="date">{date}</p></a></li><!--{comic_contents}-->'
	templete = templete.replace(r"{url}", content_path + CONTENT_HTML)
	templete = templete.replace(r"{title}", title)
	templete = templete.replace(r"{count}", str(count))
	templete = templete.replace(r"{first_img}", content_path+"/"+first_img)
	date = time.localtime(os.stat(content_path).st_ctime)
	templete = templete.replace(r"{date}", ("%d-%d-%d" % (date.tm_year,date.tm_mon,date.tm_mday)))
	return templete

def getTempleteHtml(templeteURL):
	templete = open(BASE_PATH + templeteURL, "r", encoding="UTF-8")
	htmlStr = templete.read()
	templete.close()
	return htmlStr

def output2Html(htmlContent, file):
	output = open(file, "w", encoding="UTF-8")
	output.write(htmlContent)
	output.flush()
	output.close()

def createOptions(imgData):
	options = ""
	_i = 0
	for _img in imgData:
		options += ('<option value="%d" file="%s">第%d页</option>' % (_i, _img, _i+1))
		_i += 1
	return options

def createImgList(content_path):
	imgs = []
	for _dir in os.listdir(content_path):
		if os.path.splitext(_dir)[1].lower() in IMG_SUFFIX:
			imgs.append(_dir)
	try:
		imgs.sort(key=lambda x:int(x[:-4]))
	except:
		pass
	return imgs

def createContentHtml(contentPath):
	imgData = createImgList(contentPath)
	if len(imgData) == 0 or imgData == None:	return
	count = len(imgData)
	options = createOptions(imgData)
	htmlStr = getTempleteHtml(TEMPLETE_HTML)
	title = contentPath.replace(CONTENTS_PATH+"/", "")
	htmlStr = htmlStr.replace(r"{imgData}", "var imgData="+str(imgData))
	htmlStr = htmlStr.replace(r"{title}", title).replace(r"{options}", options)
	htmlStr = htmlStr.replace(r"{count}", str(count)).replace(r"{first_img}", imgData[0])
	try:
		htmlStr = htmlStr.replace(r"{next_img}", imgData[1])
	except IndexError:
		htmlStr = htmlStr.replace(r"{next_img}", imgData[0])
	output2Html(htmlStr, contentPath + CONTENT_HTML)
	return [title, contentPath, imgData[0], count]

def pushData(data):
	with shelve.open(DATA_PATH) as write:
		write[data[0]] = data

def checkData():
	with shelve.open(DATA_PATH) as read:
		keys = list(read.keys())
		for key in keys:
			if not checkFileExist(read[key][1]+CONTENT_HTML):
				print("移除： ", read[key])
				del(read[key])

def getData():
	data = []
	with shelve.open(DATA_PATH) as read:
		keys = list(read.keys())
		for key in keys:
			data.append(read[key])
	return data

def createIndexHtml():
	checkData()
	datas = getData()
	indexStr = getTempleteHtml(INDEX_TEMPLETE_HTML)
	for data in datas:
		_s = createComicItems(data[0], data[1], data[2], data[3])
		indexStr = indexStr.replace(r"<!--{comic_contents}-->", _s)	
	output2Html(indexStr, BASE_PATH + INDEX_HTML)


def checkFileExist(fileURI):
	if os.path.isfile(fileURI):
		return True
	return False

def getContentPaths(path):
	contentPaths = []	
	for _path in os.listdir(path):
		_dir = path + "/" + _path
		if os.path.isdir(_dir):
			contentPaths.append(_dir)
	return contentPaths

if __name__ == '__main__':
	contentPaths = getContentPaths(CONTENTS_PATH)
	for contentPath in contentPaths:
		if checkFileExist(contentPath + CONTENT_HTML):	continue
		data = createContentHtml(contentPath)
		if data is not None:
			print("新增： ", data)
			pushData(data)
	createIndexHtml()