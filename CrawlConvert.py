"""
Created on Jul 29 2020

@author: ricky
"""
import requests
from bs4 import BeautifulSoup
import re


one_compare_wordlist = list()

class tranferword(object):
      def __init__(self,ch_name,sim_ch_nam):
          self.ch_name = ch_name
          self.sim_ch_nam = sim_ch_nam

class crawlcontent(object):
    def __init__(self,title,price):
        self.title = title
        self.price = price

def get_word_list():
     response = requests.get("https://phabricator.wikimedia.org/source/mediawiki/browse/master/languages/data/ZhConversion.php?view=raw")
     itemlist =(item for item in response.text.split(',') if '=>' in item)
     for item in itemlist:
        wordlist = item.split("=>")
        if len(wordlist) ==2:
           ch_name = re.findall(r"\'(.+?)\'",wordlist[0])[0]
           sim_ch_name = re.findall(r"\'(.+?)\'",wordlist[1])[0]
           if len(ch_name) == 1:
               one_compare_wordlist.append(tranferword(ch_name,sim_ch_name))

def get_crawl_list():
    headers = {
        'User-Agent': 'Googlebot',
        'From': 'm94221006@gmail.com'
    }
    url ="https://shopee.tw/%E7%8E%A9%E5%85%B7-cat.75.2185?brands=5005&locations=-1&page=0&ratingFilter=4"
    r = requests.get(url,headers=headers,allow_redirects=True)

    soup = BeautifulSoup(r.text, "html.parser")
    contents = soup.find_all("div", class_="_1NoI8_ _16BAGk")
    prices = soup.find_all("span", class_="_341bF0")
    crawl_list = list()
    for content,price in zip(contents, prices):
        crawl_list.append(crawlcontent(content.contents[0],price.contents[0]))
    return crawl_list

def set_tranferword(o_pattern):
    t_pattern = ''
    for word in o_pattern:
        result = [oneword for oneword in one_compare_wordlist if oneword.ch_name ==word]             
        if len(result)>0:
            t_pattern +=result[0].sim_ch_nam
        else:
             t_pattern +=word
    return t_pattern

def crawl_convert():
    get_word_list()
    if len(one_compare_wordlist)>0:
        crawl_list = get_crawl_list()
        if len(crawl_list)>0:
            for crawlitem in crawl_list:
                tanfer_pattern = set_tranferword(crawlitem.title)
                print("{}:{}".format(tanfer_pattern,crawlitem.price))



if __name__ == "__main__":

    crawl_convert()