# 处理excel

## 解决了什么问题？

- 解放劳动力，同时操作多个Excel文件

## 有哪些场景？

- （批量）合并文件
- （批量）拆分文件
- 如果是加密的excel怎么处理

```text
这里用到的是win32com接口，调用office的VBA脚本，所以只能支持windows。通过官方文档 https://docs.microsoft.com/zh-CN/office/vba/api/Excel.Workbooks.Open
参考可以得知，打开文件，有个参数是Password

因此可以采用下面方式打开
from win32com.client import Dispatch  
excel = Dispatch('Excel.Application')
excel.Workbooks.Open(filename, UpdateLinks=False, ReadOnly=False, Format=None, Password=password, WriteResPassword=password)
```

## 相关包库

- xlrd
- [xlwt](https://xlwt.readthedocs.io/en/latest/)
- -pandas
- [xlsxwriter](https://xlsxwriter.readthedocs.io/)
- openpyxl

## code

- [读取豆瓣250](../code/excel/01-read-xlsx.py)
- [拆分工资单](../code/excel/02-split-salary.py)
- [拆分工资单函数式封装](../code/excel/03-split-salary-func.py)
- [读取目录下的excel文件](../code/excel/05-read-xlsx-in-directory.py)
- [使用openpyxl合并调查结果](../code/excel/04-merge-survey-openpyxl.py)
- [合并调查结果](../code/excel/06-merge-survery.py)

## 注意事项

- 2.01版本的xlrd不支持xlsx文件，只支持xls文件 ,亲测装旧版本的可用`pip install xlrd==1.2.0`
- 