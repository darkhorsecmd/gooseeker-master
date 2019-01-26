#-*_coding:utf-8-*-
# 使用GsExtractor类的示例程序
# 访问集搜客论坛，以xslt为模板提取论坛内容
# xslt保存在xslt_bbs.xml中
from urllib import request
from lxml import etree
from gooseeker import GsExtractor
# 访问并读取网页内容
url = "http://cs.njust.edu.cn/1735/list1.htm"
conn = request.urlopen(url)
doc = etree.HTML(conn.read())

bbsExtra = GsExtractor()    # 生成xsltExtractor对象
bbsExtra.setXsltFromAPI("e346796c93c6ba7441636666e401e5cc", "hehai_test")
xs=bbsExtra.getXslt()
print(str(xs))
pass
result = bbsExtra.extract(doc)    # 调用extract方法提取所需内容
# out file
file_name = 'E:/parse_detail_'+'.xml'
open(file_name, "wb").write(result)
print(str(result))
