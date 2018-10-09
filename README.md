# 欢迎使用 ComicsViewer
ComicsViewer是一个基于HTML的图片阅读器，旨在将本地的漫画图片进行整理生成HMTL文件，以便于在浏览器中阅读，项目使用python 3.7.0进行开发，HTML模板使用hcomic的代码，因此保留了网站的logo和跳转链接。

## 目前版本
ComicsViewer1.0.0-SNAPSHOT

## 目录结构
| 名称        | 说明                |  类型   |
| --------    | :-----             | :----:  |
| contents    | 漫画文件存放目录     |  目录   |
| data        | shelve数据目录      |  目录   |
| h           | HTML模块文件目录     |  目录   |
| README.md   | 项目说明文件         |  文件   |
| run.bat     | 运行python run.py   |  文件   |
| run.py      | 主要代码文件         |  文件   |
| index.html  | 程序运行后生成       |  文件   |

## 使用方法
### Step1
将漫画文件夹放在contents目录下，即```contents/C(94).../xxxx.jpg```
注意，如```contents/favorite/C(94).../xxxx.jpg```等多级目录将不会被解析

### Step2
当前目录运行```python run.py```或是Windows用户双击run.bat

### Step3
点击生成的index.html文件

## 未来可能有的更新 
- [ ] 移除hcomic的代码，增添更好的动画效果
- [ ] 改进图片排序算法
- [ ] 支持多级目录

## 联系以及BUG反馈
[masazumi_@outlook.com]