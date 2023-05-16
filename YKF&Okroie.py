# *_* coding: UTF-8 *_*
# Team: BigData Two
# Time: 2022/4/1 21:34
# Name: 偶颗
# Program: YKF&Okroie.PY
# Format: PyCharm


# ls = [1, 2, 3]
# s = 2, 4, 6, 'tt'
# d = 5; 7; 8; 0
# print(ls)
# print(s)
# print(d)


# l = ['袁科峰', '赵帅', '123']
# with open('c.csv', 'w') as f:
#     f.write(','.join(l) + '\n')


# with open('c.csv', 'r') as f:
#     s = f.read().strip().split(',')
#     print(s)


# ls = [['1', '2', '3'], ['4', '5', '6']]
# with open('d.csv', 'w') as f:
#     for i in ls:
#         f.write(','.join(i) + '\n')

# with open('d.csv', 'r') as f:
#     l = []
#     for i in f:
#         l.append(i.strip('\n').split(','))
#     print(l)


# ls = [['1', '2', '3'], ['4', '5', '6']]
# for i in ls:
#     for j in i:
#         print(j)

# for i in ls:
#     line = ''
#     for j in i:
#         line = line + '{:1}\t'.format(j)
#     print(line)


# for i in range(3):
#     for j in range(3):
#         print('$', end=' ')
#     print()


# for i in range(10):
#     for j in range(10):
#         print('&', end='   ')
#     print()


# s = 0
# for i in range(1, 101):
#     s = s + i
# print(s)


# def a():
#     print(666)
# def b(x):
#     print(x)
# def c(y, z=10):
#     return y ** z
# d = lambda g:g % 2
# # a()
# # b(70)
# # print(c(10, 2))
# # print(d((20)))
# def main():
#     a(), b(70), print(c(10 ,2), d(20))
# if __name__ == '__main__':
#     main()

# print(abs.__name__)
# print(sum.__name__)


# import demo as e
# from bs4 import BeautifulSoup as a


# import turtle as t
# t.circle(100)
# t.done()

# from turtle import *
# circle(100)

# from turtle import circle
# circle(100)


# import time
# from turtle import *
# setup(500, 500, 500, 200)
# time.sleep(10)

# import time
# import turtle as t
# t.write('袁', font=0)
# time.sleep(10)


# import time
# import turtle as t
# t.circle(100, 360)
# t.penup()
# t.goto(200, 200)
# t.dot(50, 'red')
# t.pendown()
# # t.speed()
# time.sleep(30)


# import turtle as t
# t.pensize(3)
# t.pensize()
# t.penup()
# t.goto(-100, -50)
# t.pendown()
# t.begin_fill()
# t.color('blue')
# t.circle(50, steps=6)
# t.end_fill()
# t.hideturtle()
# t.done()


# from random import *
# print(random())
# print(randint(1, 10))
# print(getrandbits(10))
# print(randrange(1, 100, 10))
# print(uniform(1, 10))

# l = [1, 2, 3, 5]
# print(choice(l))
# shuffle(l)
# print(l)
# print(sample(l, 3))


# import time
# # print(time.time())
# # print(time.ctime())
# # print(time.gmtime())
# # print(time.localtime())
# # print(time.mktime(time.localtime()))
# # print(time.ctime(time.mktime(time.gmtime())))
# # print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# # print(time.strptime('1999-05-23 16:33:24', '%Y-%m-%d %H:%M:%S'))
#
# print(1)
# time.sleep(3)
# print(2)

# print('dc%sdc' % 123)
# print('dc{}sdc'.format(123))


# import time
# for i in range(1000):
#     print(i)
#     time.sleep(1)


# import jieba
# jieba.add_word('犯得')
# print(jieba.lcut('犯得上发射点十分士大夫士大夫士大夫'))
# print(jieba.lcut('犯得上发射点十分士大夫士大夫士大夫', cut_all=True))
# print(jieba.lcut_for_search('犯得上发射点十分士大夫士大夫士大夫'))


# import jieba
# from wordcloud import WordCloud
# txt = 'DVD发v地方v地方v的v'
# word = jieba.lcut(txt)
# nw = ''.join(word)
# wdcd = WordCloud(font_path='msyh.ttc').generate(nw)
# wdcd.to_file('词云图.png')