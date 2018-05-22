from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()
    def test_can_start_a_list_retrieve_it_later(self):

        #伊迪听说有个很不错的应用,她去看了这个应用首页
        self.browser.get('http://localhost:8000')

        #她注意到网面的标题和头部都包含了"To-Do"这个词
        self.assertIn('To-Do',self.browser.title,'testTDD')
        self.fail('Finish the test!')

        #应用邀请她输入一个待办事项

if __name__ == '__main__':
    #warnings='ignore' 作用禁止抛出resourceWarning异常
    unittest.main(warnings='ignore')
