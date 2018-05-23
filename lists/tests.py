from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')
        # 检查解析网站根路径"/"时,是否能找到名为home_page的函数
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        #创建一个HttpRequest对象,用户在浏览器请求网页时,Django看到的就是这对象
        request = HttpRequest()
        #把这个对象传给home_page视图,得到响应对象,响应对象是HttpResponse类的实例,响应对象.content属性(发给用户的html)
        response = home_page(request)
        #希望响应对象以<html>开头
        print (repr(response.content))
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

# class SmokeTest(TestCase):
    # def test_bad_maths(self):
    #     self.assertEqual(1+1,3)