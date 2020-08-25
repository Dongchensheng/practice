# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, sys

#定义一个下载器类
class downloader(object):

#初始化，定义主页面和下载目标，以及定义name，url，num为空列表
    def __init__(self):
        self.mainpage = 'https://www.bxwx.io/book/121842/'
        self.target = 'https://www.bxwx.io/book/121842/43825226.html'
        self.names = []
        self.urls = []
        self.nums = []

#获取下载链接方法定义,目的是获取每一章的url
    def get_download_url(self):
        req = requests.get(self.mainpage)  #用request库的get方法获取mainpage的内容并赋值给req
        html = req.content.decode("GBK", "ignore") #content是response类型的一个属性，decode解决乱码问题，解码后赋值给html
        bf = BeautifulSoup(html, 'html.parser') #先把html转为BeautifulSoup类型方便下面抓取内容
        div = bf.find_all('div', class_='zjbox') #使用.find_all来抓取网页文件中的内容，标签div中，类为zjbox的部分
        a_bf = BeautifulSoup(str(div[0]), 'html.parser') #将div列表的第一项转为str类型，并赋值给a_bf,本工具中没体现出来作用
        a = a_bf.find_all('a') #把a_bf中a标签内的内容赋值给a,里面是每章的部分url
        self.nums = len(a) #统计url个数
        # print(div[0])
        # print(texts[0].text.replace('\xa0','\n\n'))
        for each in a: #从a中循环每一个key-value
            self.names.append(each.string)
            self.urls.append(self.mainpage + each.get('href')) #get()从字典中查找键值,和mainpage组合起来成为完全url

#获取每一页中小说的文字
    def get_contents(self, target):
        req = requests.get(target) #从target中获取页面内容赋值给req
        html = req.content.decode("GBK", "ignore") #req的content转码并赋值给html
        bf = BeautifulSoup(html, 'html.parser') #用BeautifulSoap格式化html并赋值给bf
        texts = bf.find_all('div', id = 'content') #用find_all将bf中div标签里 id=content 的所有数据都查找到并赋值给texts
        texts = texts[0].text.replace('\xa0'*8,'\r\n') #把texts里<br>等标签去掉(replace成\r\n
        return texts #返回texts给函数

#将每个get_contents获取的文字写入到一个文件
    def writer(self, name, path, text): #定义writer函数, 参数包括名字, 路径, 文字
        #write_flag = True #没用
        with open(path, 'a', encoding='utf-8') as f: #打开某路径,模式'a',即追加 解释: 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
            f.write(name + '\n') #先写一行, 小说章节标题?
            f.writelines(text) #再写一行，输入内容
            f.write('\n\n')

if __name__ == "__main__":  #程序从这里执行
    dl = downloader()  #实例化downloader类
    dl.get_download_url() #调用downloader类中的get_download_url函数
    print('开始下载：')
    for i in range(dl.nums): #循环多少次 从dl.num里取值
        dl.writer(dl.names[i], '兄弟-余华.txt', dl.get_contents(dl.urls[i])) #调用writer函数,参数(章节名字, 文件名, 内容)重点是这里, 文件名调用get_contents函数,参数用url列表内容
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r') #显示进度
        sys.stdout.flush()
    print('下载完成')

