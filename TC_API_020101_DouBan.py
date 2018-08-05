# coding = utf-8

'''
created on 2018/7/14
@author: yajun.hu
project: xxxx

'''

import unittest, os, requests

class Test(unittest.TestCase):
    url_1 = "https://movie.douban.com/subject/1304102/"
    url_2 = "https://movie.douban.com/subject/1292052"

    def setUp(self):
        print("===setUp start===")
        response = requests.get(self.url_1)
        print(response.text)

	
    def test_purchase(self):
        print("===test start===")
  
        

    def tearDown(self):
        print("===tearDown start===")


if __name__=="__main__":
    unittest.main()




