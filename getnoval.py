import requests, random
import logging
from lxml import etree
from setting import UA
from bs4 import BeautifulSoup
logging.captureWarnings(True)
from _datetime import datetime
def Noval_Html_Code(url):
    headers = {
        'Connection': 'close',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9',
        'upgrade-insecure-requests':'1',
        'user-agent':UA[random.randint(0, len(UA) - 1)],
    }
    weburl = "https://www.37zw.net"
    nextUrl = url
    novalHtml = ''
    indexHtml = ''
    now = datetime.now().strftime('%Y-%m-%d')
    now = datetime.strptime(now, '%Y-%m-%d')
    future = datetime.strptime('2018-12-22', '%Y-%m-%d')
    time = future - now
    titlelist = []
    n = 3
    for i in range(n):
        response = requests.get(nextUrl, headers=headers, cookies=None, proxies=None, timeout=5, verify=False)
        response.encoding = 'gbk'
        if response.status_code == 200 or response.status_code == 302:
            soup = BeautifulSoup(response.text,'html.parser')
            name = soup.select(".con_top a")[1].get_text()
            title = soup.select(".bookname h1")[0].get_text()
            content = soup.select("#content")[0].get_text().replace("    ","<br><br>")
            # indexHtml = indexHtml + "<h2 style='font-style:italic;'><a href = '#chapter"+ str(i) +"'>"+ title +"</a></h2><br><br>"
            novalHtml = novalHtml + "<h3 id = 'chapter" + str(i) +"'>"+ title +"</h3><div>"+ content +"</div><br><br>"
            if "第" not in title:
                n = n + 1
                novalHtml = novalHtml + "<h3>"+ "水了" +"</h3><div>"+ "跳过跳过" +"</div><br><br>"
            else:
                titlelist.append(title)

            Urls = soup.select('.bottem1 a')
            indexUrl = weburl + Urls[2].get('href')
            lastUrl = indexUrl + Urls[1].get('href')
            nextUrl = indexUrl + Urls[3].get('href')
        else:
            novalHtml = novalHtml + "<h3>"+ "卡了" +"</h3><div>"+ "网络不好" +"</div><br><br>"

    novalHtml = "<html><head></head><body>"+ indexHtml + novalHtml +"</body></html>"

    subject = name + "(" + titlelist[0].split("第")[1].split("章")[0] + "->" + titlelist[-1].split("第")[1].split("章")[0]+")" + "  " + str(time)[0:7]

    return novalHtml,nextUrl,subject



    # htmlCode = etree.HTML(response.text)
    # contextText = htmlCode.xpath("//*[@id='content']/text()")
    # print(type(contextText))
    # novaltxt = "<br>"
    # for context in contextText[:-2]:
    #     #novaltxt = novaltxt + context.encode('utf-8') + "<br><br>"
    #     c = context.encode('utf-8')
    #     print(type(c))
    #     print(c)

    # titleText = htmlCode.xpath("/html/head/title/text()")
    # nextUrl = htmlCode.xpath(".//div[@class='page_chapter']/ul/text()")
    # print(titleText[0])

    # print(nextUrl)


