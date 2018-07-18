# 从www.xkcd.com网站获取图片链接自动下载图片
import os,requests,bs4
url='http://www.xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    #download page
    print('start download page %s'%url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text)
#find url comic image
    comicElem=soup.select('#comic img')
    if comicElem==[]:
        print('not find')
    else:
        comicUrl='http:'+comicElem[0].get('src')
        print('downloading img %s'%comicUrl)
        res=requests.get(comicUrl)
        res.raise_for_status()
        imgFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for item in res.iter_content(100000):
            imgFile.write(item)
        imgFile.close()
        # open pre page
        prevLink=soup.select('a[rel="prev"]')[0]
        url='http://xkcd.com'+prevLink.get('href')
print('done....')
system('pause')


