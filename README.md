# UiAutoDemo
UI自动化测试框架模板

#### 简介

<u>UiAutoDemo</u>是一个下载即可用的<u>UI自动化测试框</u>架，专为公司自动化项目免去搭建自动化脚手架，也极其适合刚入门的自动化测试小白。很多入门小白不知道如何去搭建脚本的基本结构，自动化的框架架构；不用担心！这款框架绝对让您满意！
```框架支持邮件发送、HTML测试报告、框架默认含Chrome浏览器驱动```  

#### 必看！

+ ```UiAutoDemo```框架使用的是 ```PageObject```设计模式，简称```PO```；不懂什么是PO设计模式的请至（度娘，谷哥）
+ 使用的编译语言 ```Python```
+ 框架使用的是 ```seldom``` 与 ```poium``` 第三方库，往下看有介绍


#### 项目架构

 ```
-  UiAutoDemo/
- |── test_case/
-          |── test_login.py
- |──models/
-          |── url.py
- |──PageObject/
-          |── loginPage.py
- |── Browser_Driver/
-          |── chromedriver84(Mac64)
-          |── chromedriver84(win32).exe
- |── reports/
-          |—— 年_月_日_时_分_秒_result.html
- └── run.py
```

+ ```testcase``` 文件夹用于存放页面元素，测试用例，公共元素
    + ```test_login.py``` 测试用例部分
+ ```models``` 文件夹存放公共元素，如url
    + ```url.py``` 存放测试url路径
+ ```PageObject``` 文件夹存放测试过程中需要使用的页面元素
    + ```loginPage.py``` 存放页面元素定位，封装元素实例化
+ ```Browser_Driver``` 文件夹存放浏览器驱动
    + ```chromedriver84(Mac64)``` Mac操作系统Chrome驱动
    + ```chromedriver84(win32).exe``` Windows操作系统Chrome驱动
+ ```reports``` 文件夹存放项目测试后生成的测试报告

#### 依赖库

+  Python3.7.4+
+  poium0.6.3+(pip install poium)
+  seldom1.5.6+(pip install seldom)

