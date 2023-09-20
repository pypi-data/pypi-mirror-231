"""
@Author: kang.yang
@Date: 2023/9/20 10:53
"""
import kuto


class WinPage(kuto.Page):
    num_3 = kuto.MacElem(image='../static/calculator_3_win.png', desc="数字3")
    x = kuto.MacElem(image='../static/calculator_x_win.png', desc="乘以号")
    num_5 = kuto.MacElem(image='../static/calculator_5_win.png', desc="数字5")
    equal = kuto.MacElem(image='../static/calculator_=_win.png', desc="等于")
