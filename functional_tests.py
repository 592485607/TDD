from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        #self.fail('Finish the test!')

        #应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #她在一个文本框中输入了"buy peacock feathers"
        #伊迪丝的爱好是使用假蝇做鱼饵钓鱼
        inputbox.send_keys('Buy peacock feathers')

        #她按回车键后,页面更新了,待办事项表格中显示了"1:Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        import time
        time.sleep(10)
        table = self.browser.find_element_by_id('id_list_table')

        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows)
        )

        #页面中又显示了一个文本框,可以输入其他的事项
        #她输入了:Use peacock feathers to make a fly"
        #伊迪丝做事很有条理
        self.fail('Finish the test!')
        # 页面再次更新,她的清单中显示了这两个待办事项

if __name__ == '__main__':
    #warnings='ignore' 作用禁止抛出resourceWarning异常
    unittest.main(warnings='ignore')
