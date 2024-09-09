Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
title = 'Python'
title[0]
'P'
title[-1]
'n'
title[2:4]
'th'
title[:]
'Python'
title[-2]
'o'
title[-2:]
'on'


twice = [ 'momo', 'sana' , 'zwi']
#리스트 초기화

type(twice)
<class 'list'>
len(twice)
3
#3명

twice.append('jihyo')
twice
['momo', 'sana', 'zwi', 'jihyo']
len(twice)
4
twice,sort()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    twice,sort()
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
twice.sort()
twice
['jihyo', 'momo', 'sana', 'zwi']
twice[0]
'jihyo'
twice[3]
'zwi'
twice[2]
'sana'
twice[-1]
'zwi'
>>> black_pink = ['jisu', 'jeni', 'rose']
>>> len(black_pink)
3
>>> 
>>> unite = twice + black_pink
>>> len(unite)
7
>>> type(unite)
<class 'list'>
>>> #리스트와 리스트는 더할 수 있다
>>> 
>>> unite.sort()
>>> unite[0]
'jeni'
>>> unite[:3]
['jeni', 'jihyo', 'jisu']
>>> 
>>> best3=unite[:3]
>>> best3
['jeni', 'jihyo', 'jisu']
>>> low3
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    low3
NameError: name 'low3' is not defined
>>> low3 = unite[-3:]
>>> low3
['rose', 'sana', 'zwi']
>>> unite.remove('momo')
>>> unite.insert(0, 'daehyun')
>>> unite
['daehyun', 'jeni', 'jihyo', 'jisu', 'rose', 'sana', 'zwi']
>>> del.unite[-1]
SyntaxError: invalid syntax
>>> del unite[-1]
>>> unite
['daehyun', 'jeni', 'jihyo', 'jisu', 'rose', 'sana']
>>> #파이썬은 리스트 자료구조가 내장되어있다
