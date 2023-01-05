import os

# os.removedirs('b')#删除空目录
if not os.path.exists('b'):  #如果这个路径下没有B目录，就创建一个B目录
    os.mkdir('b')
if not os.path.exists('b/a.text'): #如果这个路径下没有a.text文件
    f = open('b/a.text', 'w') #就打开这个路径下的文件  并且写
    f.write('lallallalall,lallalla,\n lallallla')
    f.close() #关闭文件

with open('b/a.text') as a: # 打开文件
    while True: #循环文件
        aa=a.readline() #读取一行
        if aa:#如果读取的行有内容就打印内容
            print(aa)
        else:#读取的行没有内容就退出
            break