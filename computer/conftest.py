import pytest
import yaml

from computer.computer_1 import computer


@pytest.fixture()
def get_co():
    print('开始测试')
    yield
    print('测试结束')


# 所有数据
with open('dle_1.yaml') as f:  # 打开数据文件
    # 减法数据
    co = yaml.safe_load(f)  # 把数据存储在co
    co_del = co['sub']['dates']  # 获取数据中的字典和字典中的列表 ，存储co_del中
    myid = co['sub']['myid']  # 获取数据中的字典sub 和字典中的key值 myid列表 存储 mid中

    # 乘法数据
    mul = co['mul']['dates']  # 乘法列表数据
    mids_1 = co['mul']['myid']  # 乘法别名


# 减法参数传递
@pytest.fixture(params=co_del, ids=myid)  # 参数化 优先执行   parms 传递参数  使用request ids别名
def dome_add(request):  # 使用request传递参数
    deta = request.param  # request.param储存参数
    print(f'测试数据是{deta}')
    yield deta  # 返回数据


# 乘法数据传递
@pytest.fixture(params=mul, ids=mids_1)
def mull(request):
    mul = request.param
    yield mul
