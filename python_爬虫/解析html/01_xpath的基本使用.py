"""
xpath的两种运用：（1）解析本地文件
                tree = etree.xpath()
                （2）解析服务器响应文件    response.read().decode('utf8')
                tree = etree.http()
基本语法：
        1.路径查询
            //：查询所有子孙节点，不考虑层级关系
            /：直接查询子节点
        2.谓词查询
            //div[@id]：查询有id属性的div结点
            //div[@id = "xxx"]：查询id='xxx'的div结点
        3.属性查询
            //@class
        4.模糊查询
            //div[contains(@id,"xx")]：查询id中包含xx字段的div结点
            //div[start-with(@id,"xx")]：查询id中开头为xx字段的div结点
        5.内容查询
            //div/text()：查询div结点中的内容
        6.逻辑查询
            //div[@id="xx" and @class="yy"]：查询id为xx并且class为yy的div结点
            //title | price：结点之间使用，属性之间不可用


"""

from lxml import etree

etree.HTML()