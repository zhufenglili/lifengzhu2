import pytest

from com import Computer1


class Testcom(Computer1):
    def setup_class(self):
        self.com = Computer1()


    def testadd(self, com_add):
        result = self.com.aa_add(com_add[0], com_add[1])
        assert result == com_add[2]
