# -*- coding:utf-8 -*-  
# author:Jaydan

try:
    import cpickle as pickle
except ImportError:
    import pickle
'''
    cPickle 用C语言重写的python库文件，速度快
    Function：

        dump(object,file)
        dumps(object) -> string
        load(file) -> object
        loads(string) -> object

'''

# 保存数据
hfile1 = open('pickle','w')
dict1 = {'a':1,'b':2}
pickle.dump(dict1,hfile1)
hfile1.close()

# 读取数据
# hfile1 = open('pickle')
# dict2 = pickle.load(hfile1)
# print type(dict2)
# hfile1.close()