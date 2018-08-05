# coding = utf-8

'''
created on 2018/7/14
@author: yajun.hu
project: xxxx

'''


import unittest, os, time, HTMLTestRunner

casepath = os.path.join(os.getcwd(), "case")
path = os.path.join(os.getcwd(), "report")
reportpath = os.path.join(path, "report.html")

	
if __name__=="__main__":
	f = open(reportpath, "wb")
	test = unittest.defaultTestLoader.discover(casepath, pattern="TC*.py", top_level_dir=None)
	HTMLTestRunner.HTMLTestRunner(stream=f, title=u'自动化测试报告', description=u'case执行情况').run(test)
	f.close

