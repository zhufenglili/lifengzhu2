import pytest
import yaml

from computer.computer_1 import computer


# 1、补全计算器（加减乘除）的测试用例
# 2、使用fixture方法，完成加减乘除用例的自动生成，添加别名
# 3、修改测试用例的收集规则，执行所有以 check_开头和test_ 开头的测试用例
# 4、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
# 5、将 Fixture 方法存放在conftest.py ，灵活设置scope的级别


class Test_computer(computer):  # 计算机测试用例类

    @pytest.mark.parametrize('a,b,result', [(1, 2, 3), (3, 4, 7), (5, 6, 11), (7, 8, 15), ],
                             ids=['ins', 'flot', 'str', 'none'])
    def test_add(self, get_co, a, b, result):  # 计算器加法
        result_1 = self.com_add(a, b)  # a,b和 存储变量result
        assert result == result_1  # 断言预期结果result== result_1
        print(result)

    def test_del(self, get_co, dome_add):  # 计算器减法
        result_2 = self.com_del(dome_add[0], dome_add[1])
        assert result_2 == dome_add[2]
        print(result_2)

    def test_mul(self, get_co, mull):  # 计算器乘法
        result_3 = self.test_mul(mull[0],[1])
        assert result_3 == mull[2]

    def test_div(self, get_co):  # 计算器除法
        pass
