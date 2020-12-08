from bs4 import BeautifulSoup as bs
import urllib.request as req

# 네이버 사전에서 단어와 뜻 가져오기

url = "https://en.dict.naver.com/#/entry/enko/dca3a30f55114aa79876939b06b0f769"
res = req.urlopen(url)
soup = bs(res, "html.parser")

# word_name = soup.select_one("#content > div.section.section_entry._section_entry > div > div.entry_title._guide_lang > strong > span[ data-lang='en']").string
# word_name = soup.select_one("#content > div.section.section_entry._section_entry > div > div.entry_title._guide_lang > strong > span.u_word_dic").string
word_name = soup.select("#content > div.section.section_entry._section_entry > div > div.entry_title._guide_lang > strong > span")
print("출력 >> ", word_name.string)
# for i in word_name:
#     print("출력 >> ", i.string)