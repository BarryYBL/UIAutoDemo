# UiAutoDemo
>基于seldom 和 poium库的 UI自动化测试框架模板

#### 简介

<u>UiAutoDemo</u>是一个下载即可用的<u>UI自动化测试框</u>架，专为公司自动化项目免去搭建自动化脚手架，也极其适合刚入门的自动化测试小白。很多入门小白不知道如何去搭建脚本的基本结构，自动化的框架架构；不用担心！这款框架绝对让您满意！

```框架支持邮件发送、HTML测试报告、框架默认含Chrome浏览器驱动```  

#### 特点
+ 已经搭建好的```PageObject```设计模式的脚手架。
+ 提供[seldom](https://github.com/SeldomQA/seldom/blob/master/docs/seldom_api.md) 与 [poium](https://github.com/SeldomQA/poium/wiki) API编写自动化测试。
+ 全局启动浏览器和关闭浏览器，减少浏览器的启动次数。
+ 支持测试用例参数化 [parameterized](https://github.com/SeldomQA/seldom/blob/master/docs/parameterized.md)
+ 支持用例 失败/错误 重新尝试case
+ 支持生成```HTML```测试报告 与 ```XML```测试报告，用例失败/错误自动截图
+ 支持```HTML```测试报告邮件发送
+ 自动根据当前环境，调用Chrome浏览器驱动

#### 必看！

+ ```UiAutoDemo```框架使用的是 ```PageObject```设计模式，简称```PO```；不懂什么是PO设计模式，下面有介绍 ↓；
+ 使用的编译语言 ```Python>=3.5```；
+ 框架使用的是 ```seldom``` 与 ```poium``` 第三方库，往下看有介绍 ↓；
+ 本框架自带```Chromedriver```浏览器驱动，自动检测本地操作环境调用该环境相应的Chrome驱动程序，但需要本地浏览器更新到最近版本
+ 测试类与测试用例的命名请遵从 ```ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z```
+ ```UiAutoDemo```仅兼容```Unittest```框架；请勿使用其他测试框架运行
+ 框架内的```Chromedriver```驱动作者会持续更新，也可自行引入路径

#### 项目架构

 ```
-  UiAutoDemo/
- |── test_case/
-          |── test_login.py
- |──models/
-          |── url.py
-          |── mail.py
-          |── osDriver.py
- |──PageObject/
-          |── loginPage.py
- |── Browser_Driver/
-          |── chromedriver84(Mac64)
-          |── chromedriver84(win32).exe
- |── reports/
-          |—— 年_月_日_时_分_秒_result.html
-          |—— 年_月_日_时_分_秒.xml
- └── run.py
```

+ ```testcase``` 文件夹用于存放页面元素，测试用例，公共元素
    + ```- test_login.py``` 编写局部模块的测试用例并执行
+ ```models``` 文件夹存放公共元素，如url
    + ```- url.py``` 存放测试url路径
    + ```- mail.py``` 用于发送邮件
    + ```- osDriver.py``` 检查本地操作系统环境，根据本地环境自动选择相应的driver驱动运行项目
+ ```PageObject``` 文件夹存放测试过程中需要使用的页面元素
    + ```- loginPage.py``` 存放页面元素定位，封装元素实例化
+ ```Browser_Driver``` 文件夹存放浏览器驱动
    + ```- chromedriver84(Mac64)``` Mac操作系统Chrome驱动
    + ```- chromedriver84(win32).exe``` Windows操作系统Chrome驱动
+ ```reports``` 文件夹存放项目测试后生成的测试报告
    + ```- 年_月_日_时_分_秒_result.html``` HTML测试报告
    + ```- 年_月_日_时_分_秒.xml``` XML测试报告
+ ```run.py``` 执行所有的测试用例并执行

#### 依赖库

+  Python3.7.4 >=
+  poium0.6.3 >= (pip install poium)
+  seldom1.6.0 >= (pip install seldom)

#### PageObject设计模式

>PageObject模式是Selenium中的一种测试设计模式，主要是将每一个页面设计为一个Class，将页面定位和业务操作分开，分离测试对象（元素对象）和测试脚本（用例脚本），提高用例的可维护性。其中包含页面中需要测试的元素（按钮，输入框，标题 等），这样在测试页面中可以通过调用页面类来获取页面元素，这样巧妙的避免了当页面元素id或者其他位置变化时，需要改测试页面代码的情况。 当页面元素id变化时，只需要更改测试页Class中页面的属性即可。



#### UiAutoDemo框架模块
```框架内的每个py文件都有注解；请使用者仔细阅读```

1、此框架仅根据PageObject设计模式搭建的基础框架
2、封装一些便于运行项目的模块
3、Chromedriver驱动调用```from models import osSystem```

4、运行项目
![运行项目](https://s1.ax1x.com/2020/08/27/d4dPq1.png)
![d4I3TK.png](https://s1.ax1x.com/2020/08/27/d4I3TK.png)

5、查看报告
可以到```reports```查看测试报告

![查看报告](https://s1.ax1x.com/2020/08/27/d4dbSe.png)


#### seldom文档
请阅读下面的文档，帮助你快速学习了解Seldom。

* [seldom安装](./docs/install.md)

* [seldom创建项目](./docs/create_project.md)

* [浏览器&驱动](./docs/driver.md)

* [运行测试](./docs/run_test.md)

* [main()方法](./docs/main.md)

* [生成测试报告](./docs/reports.md)

* [seldom 元素定位](./docs/find_element.md)

* [seldom API](./docs/seldom_api.md)

* [keys键盘操作](./docs/keys.md)

* [seldom 断言](./docs/assert.md)

* [用例失败重跑&自动截图](./docs/rerun_screenshot.md)

* [数据驱动最佳实践](./docs/parameterized.md)

* [实现Page Objects设计模式](./docs/poium.md)

* [生成测试数据](./docs/testdata.md)

* [跳过测试用例](./docs/skip.md)

* [发邮件功能](./docs/send_mail.md)

* [test fixture](./docs/setupclass.md)

#### poium文档

* [介绍](https://github.com/SeldomQA/poium/blob/master/README.md)
* [HOME](https://github.com/SeldomQA/poium/wiki)
* [PageSelect](https://github.com/SeldomQA/poium/wiki/PageSelect)
* [PageWait](https://github.com/SeldomQA/poium/wiki/PageWait)

#### 写到最后

1、此项目仅是一个自动化测试项目的脚手架，并不是Python第三方库
2、对selenium有一定的基础底子，能够很快用起来；纯小白也没关系，仔细阅读seldom与poium文档即可
3、后期会不断添加一些新奇功能便于测试项目的工作
