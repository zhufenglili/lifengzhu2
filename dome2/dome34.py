from dome2.tonglao import TongLao


class XuZhu(TongLao):

    def read(self):
        print('罪过！')
        super().see_people('无崖子')


XuZhu =XuZhu(200,100)
XuZhu.read()