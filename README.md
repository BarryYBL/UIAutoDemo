# UIautoDemo
UI自动化测试框架模板

#### 项目架构

```
-  PoiumAutoTest/
-  |── test_case/
-          |──models/
-                    |── url.py
-          |──page_object/
-                    |── loginPage.py
-                    |── invoiceOpenPage.py
-          |── test_login.py
-          |── test_invoiceOpen.py
- |── driver/
-          |── chromedriver
- |── reports/
-          |—— 年_月_日_时_分_秒_result.html
- └── run.py
```

#### 依赖库

1.  Python3.7.4+
2.  poium0.6.3+(pip install poium)
3.  seldom1.5.6+(pip install seldom)
