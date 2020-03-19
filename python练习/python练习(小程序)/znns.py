import requests
import re
import _thread
import os


def getHTMLText(url):
    try:
        kv = {
            'user-agent':
            "mozilla/5.0 (Windows nt 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
        }
        r = requests.get(url, headers=kv, timeout=100)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text

    except:
        print("遇到错误")
        return ""


def parsePage(ilt, html):
    try:
        zongshu = re.findall(
            r'<span style=\'color: #DB0909\'>[0-9]*张照片</span>', html)
        temp = zongshu[0]
        temp = temp[:-10]
        temp = temp[29:]
        plt = re.findall(r'<img src=\'.{50,60}\.jpg\' alt=', html)
        url11 = plt[1]
        url11 = url11[10:]
        url11 = url11[:-12]
        ilt.append(url11 + '.jpg')

        for i in range(1, int(temp)):
            if i < 10:
                url2 = url11 + '0' + str(i) + '.jpg'
                ilt.append(url2)
        else:
            url2 = url11 + str(i) + '.jpg'
            ilt.append(url2)
    except:
        print("遇到错误2")


def parsePage1(ilt, html):
    try:
        url1 = re.findall(r'<a class=\'galleryli_link\' href=\'.{9}\' ><img',
                          html)
        if len(url1) == 0:
            return ''
        for i in range(len(url1)):
            url = url1[i]
            url = url[:-7]
            url = url[32:]
            url11 = 'https://www.nvshens.net' + url
            ilt.append(url11)
    except:
        print("遇到错误1")


def xiewenjian(lit):
    print("123")
    count = 0
    path = 'E:\\mv\\'
    for url in lit:
        path1 = path + str(count) + '.jpg'
        print(path1)
        try:
            count = count + 1
            r = requests.get(url)
            with open(path1, 'wb') as f:
                f.write(r.content)
            f.close()
        except:
            print("连接失败")
            continue


if __name__ == '__main__':
    url = "https://www.nvshens.net"
    # url1 = ["/gallery/meiguo/"]
    url1 = ["/gallery/neidi/"]
    houzhui = ".html"
    zonglist = []
    lit = []
    for i in url1:
        for j in range(1, 20):
            if j == 1:
                zurl = url + i
            else:
                zurl = url + i + str(j) + houzhui
            try:
                html = getHTMLText(zurl)
                parsePage1(zonglist, html)
            except:
                print("遇到错误4")
    for i in zonglist:
        try:
            html = getHTMLText(i)
            parsePage(lit, html)
        except:
            print("遇到错误3")
            continue

    print(len(lit))
    xiewenjian(lit)
