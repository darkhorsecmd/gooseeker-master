#-*_coding:utf-8-*-
# 使用GsExtractor类的示例程序
# 访问集搜客论坛，以xslt为模板提取论坛内容
# xslt保存在xslt_bbs.xml中
from urllib import request
from lxml import etree
from gooseeker import GsExtractor
import html
# 访问并读取网页内容
url = "http://im.nju.edu.cn/teachers.do?type=1&mid=4"
conn = request.urlopen(url)
doc = etree.HTML(conn.read())

bbsExtra = GsExtractor()    # 生成xsltExtractor对象
bbsExtra.setXsltFromAPI("e346796c93c6ba7441636666e401e5cc", "im.nju.edu.cn")
xs=bbsExtra.getXslt()
result = html.unescape(str(bbsExtra.extract(doc)))    # 调用extract方法提取所需内容
# result = bbsExtra.extract(doc)
# out file
file_name = 'E:/parse_detail_'+'.xml'
open(file_name, "w").write(result)
# print(str(result))
