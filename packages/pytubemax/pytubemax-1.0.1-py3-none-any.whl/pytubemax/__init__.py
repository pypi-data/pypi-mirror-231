import requests
from bs4 import BeautifulSoup
session = requests.session()

def youtube(url,value=None):
	resp = session.get(f"https://10downloader.com/download?v={url}=ygUganVnb25lcyBkZSBsYSBzZXh0YSBob3kgY29tcGxldG8%3D&lang=en&type=video")
	soup = BeautifulSoup(resp.text,"html.parser")
	title = soup.find("span",attrs={"class":"title"}).text
	duration = str(soup.find("div",attrs={"class":"duration"}).text).replace("Duration","Duración")
	photo_url = soup.find("img")["src"]
	v = soup.find_all("a",attrs={"class":"downloadBtn"})
	t = 0
	urls = []
	for i in v:
		url = i["href"]
		urls.append(url)
		t+=1
		if t==3:
			break
	if value:
		value = int(value)
		urls = [urls[value-1]]
	return {"title":title,"thumb":photo_url,"duration":duration,"urls":urls}