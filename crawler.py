from urllib.request import Request,urlopen
from bs4 import BeautifulSoup

def main():
    main="http://gall.dcinside.com"
    gallery="/board/lists/?id=baseball_new6"
    url=main+gallery
    request(url)

def request(url):
    ret=Request(url)
    ret.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',)
    ret.add_header('Accept-Encoding', 'gzip,deflate')
    ret.add_header('Accept-Language', 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
    ret.add_header('Cache-Control', 'max-age=0')
    ret.add_header('Connection', 'keep-alive')
    ret.add_header('Host', 'gall.dcinside.com')
    ret.add_header('Upgrade-Insecure-Requests', '1')
    ret.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36')

    result=urlopen(ret)
    html=BeautifulSoup(result.read(),'html.parser')

if __name__ == "__main__":
    main()