# 项目描述

基于 DFA 算法的敏感词检测器。

# 作者信息

昵称：lcctoor.com

域名：lcctoor.com

邮箱：lcctoor@outlook.com

[主页](https://lcctoor.github.io/arts/) \| [微信](https://lcctoor.github.io/arts/arts/static/static-files/WeChatQRC.jpg) \| [Python交流群](https://lcctoor.github.io/arts/arts/static/static-files/PythonWeChatGroupQRC.jpg) \| [捐赠](https://lcctoor.github.io/arts/arts/static/static-files/DonationQRC-1rmb.jpg)

# Bug提交、功能提议

您可以通过 [Github-Issues](https://github.com/lcctoor/arts/issues)、[微信](https://lcctoor.github.io/arts/arts/static/static-files/WeChatQRC.jpg) 与我联系。

# 安装

```
pip install cooldfa
```

# 教程 ([查看美化版](https://lcctoor.github.io/me/pypi/cooldfa)👈)

#### 导入

```python
from cooldfa import dfa
```

#### 创建dfa模型

```python
敏感词S = ['123', '56', 'end']
example = dfa(敏感词S)
```

#### 查找第1个敏感词

```python
example.find_one('1--2--3--4--5--6--7--8--9--end--')
# >>> '1--2--3'
```

#### 查找所有敏感词

```python
example.find_all('1--2--3--4--5--6--7--8--9--end--')
# >>> ['1--2--3', '5--6', 'end']
```

#### 替换所有敏感词

```python
example.sub('1--2--3--4--5--6--7--8--9--end--', '*')
# >>> '*******--4--****--7--8--9--***--'
```

#### 使用预置的敏感词库

```python
from cooldfa import dfa, preset_words

example = dfa(
    preset_words.politics,  # 政治类
    preset_words.sex,  # 色情类
    preset_words.violence,  # 暴力类
    preset_words.url,  # 网址
    preset_words.others,  # 其它
)
```
