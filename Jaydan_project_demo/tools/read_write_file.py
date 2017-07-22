# -*- coding:utf-8 -*-  
# author:Jaydan

def read_file():
    hfile = open('data_write.txt','r')
    for i in hfile.readlines():
        print i.strip().decode('utf-8')
    hfile.close()

def write_file():
    name_list = [u'Jaydan',u'jun',u'蛋蛋']
    hfile = open('data_write.doc','w')
    for i in name_list:
        hfile.write(i.encode('utf-8')+'\n')
    hfile.close()


if __name__ == '__main__':
    # read_file()
    write_file()
