# class Cat():#创建一个猫
#     def __init__(self,name,colour,gender): #初始化属性
#         self.name = name #姓名
#         self.colour = colour#颜色
#         self.geden = gender#性别
#
#     def run(self):# 动作跑
#         print(f'贼能跑{self.name}')
#
#
# Mandeng=Cat('满登','蓝色','女生') #实例化
# Mandeng.run() #实例化调用方法


class TongLao():  # 童姥类
    def __init__(self, xue, wuli):  # 初始化属性  血量 武力值
        self.xue = xue
        self.wuli = wuli

    def see_people(self, name):  # 创建一个方法需要传姓名
        if name == '无崖子':  # 传入无崖子 打印师弟
            print('师弟！！！！！')
        elif name == '李秋水':  # 传入李秋水 打印贱人
            print('呸,贱人')
        elif name == '丁春秋':  # 传入丁春秋  打印叛徒
            print('叛徒')
        else:
            print('不认识')

    def hight_zms(self, hp, power):  # 天山折梅手
        self.xue = self.xue / 2 #调用天山折梅手  血量缩减两倍
        self.wuli = self.wuli * 10 #调用天山折梅手  武力×10
        self.xue = self.xue - power #你自己血量等于  血量减对方武力值
        hp = hp - self.wuli  #对方血量 等于  血量减你的武力值
        if self.xue <= hp: #如果你的血量小于等于 对方的血量   打印【你赢了】
            print('你赢了')
        elif hp <= self.xue:#如果对方血量小于等于对方血量 打印【我赢了】
            print('我赢了')
        else:
            print('继续战斗') #平局打印继续战斗
        print(hp)
        print(self.xue)
#

#
# TongLao = TongLao(2000, 100)#实例化传童姥参数
# TongLao.see_people('hahh')#实力调用第一个方法
# TongLao.hight_zms(2000,100)#调用天山折梅手




