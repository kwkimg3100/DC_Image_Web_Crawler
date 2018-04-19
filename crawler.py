import requests
from bs4 import BeautifulSoup
import time
import urllib
import os

def request(url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'gall.dcinside.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }
    url_get=requests.get(url, headers=header)

    return url_get

def parser(url_dc,url_html):
    parser=BeautifulSoup(url_html, "html.parser")
    for data in parser.find_all('a', class_="icon_pic_n"):
        parameters=data.get('href')
        posts=url_dc+parameters
        try:
            time.sleep(3)
            in_ret=request(posts)
        except:
            try:
                print("internal_request_error")
                time.sleep(15)
                in_ret=request(posts)
            except:
                print("internal_request_error_twice")
                time.sleep(30)
                in_ret = request(posts)
                
        in_html=in_ret.text

        internal=BeautifulSoup(in_html, "html.parser")
        for link in internal.find_all('li',class_="icon_pic"):
            for href in link.find_all('a'):
                url=href.get('href')
                title=href.text
                down_link="http://image.dcinside.com/download.php"
                change="http://image.dcinside.com/viewimage.php"
                url=str(url).replace(down_link,change)
                print(title)
                save_file(url,title)

        """for link in internal.find_all('img',style="cursor:pointer;"):
            href=str(link)
            url=href.split("'")[1]
            for link in internal.find_all('li',class_="icon_pic"):
                for download in link.findAll('a'):
                    title=download.text
                    #print(url)
                    save_file(url,title)"""

def save_file(url,title):
    var = 0
    while 1: #file save after overlap check
        res = os.path.exists("C:\\Users\\kwkim_000\\PycharmProjects\\croller\\result\\%s"%title)
        if res == False:
            try:
                f = open("C:\\Users\\kwkim_000\\PycharmProjects\\croller\\result\\%s"%title, 'wb')
                img = urllib.request.Request(url)
                f.write(urllib.request.urlopen(img).read())
                f.close()
                break
            except:
                pass
                break
        elif res == True:
            var += 1
            title=str(var)+title

def main():
    url_dc="http://gall.dcinside.com"
    url_gallery="/board/lists/?id=baseball_new6"
    url_page="&page="
    pageN=0
    while(1):
        #pageN += 1
        pageN=1
        url = url_dc + url_gallery + url_page + str(pageN)
        ret=request(url)
        url_ret=ret.text
        parser(url_dc,url_ret)
        print("8 minutes later...")
        time.sleep(480)
        #print("%d page crawling finished. %d page start..."%(pageN, pageN+1))

if __name__ == "__main__":
    main()