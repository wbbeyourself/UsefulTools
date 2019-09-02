# UsefulTools
自己编写的一些工具，主要用来解决日常编程中遇到的一些棘手或是琐碎、重复的事情。

## DependencyScanner
由于我的系统是win10 64位的，virtualenv 不能正常工作，所以无法为特定项目创建隔离的虚拟环境。
也就是说，无论是Flask Web开发，还是跑深度学习的代码，都只能在同一个python环境里。
这也直接导致pip freeze > requirements.txt会非常庞大，而我的需求是将该Project里用到library导出到requirements.txt中。
所以DependencyScanner就是扫描给定目录的Python代码中的import语句(自动忽略项目里的module和Python自带的库)，并且与pip list列表自动进行比对，
输出已匹配的成功的Library和未匹配成功的(交由人工处理)，达到精准定位每一个依赖库的目的。

## tools.py
常用的文件操作方法，字符判断方法，还有日期、时间相关工具。


## multi-bleu.perl
计算BLEU值的脚本
用法：`perl multi-bleu.perl < src.txt dst.txt`

## build_vocab.py
在shell里直接执行，免去了在IDE中仿佛修改文件名的繁琐操作。这个文件是用来 构建词汇表的。
用法：`python build_vocab.py vocab_size < train_file > vocab_file`


## 扫描文件进行操作.sh
一些以后可能会经常用到的一些简单shell脚本用法，遍历文件，进行操作
