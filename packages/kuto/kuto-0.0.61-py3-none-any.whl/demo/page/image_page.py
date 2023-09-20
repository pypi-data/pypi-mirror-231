"""
@Author: kang.yang
@Date: 2023/8/21 17:10
"""
import kuto

"""
图像识别可以配合安卓应用或者IOS应用使用
"""


class ImagePage(kuto.Page):
    searchEntry = kuto.AdrElem(rid="com.tencent.mm:id/j5t", desc='搜索框入口')
    searchInput = kuto.AdrElem(rid="com.tencent.mm:id/cd7", desc='搜索框')
    searchResult = kuto.AdrElem(rid="com.tencent.mm:id/kpm", desc="搜索结果")
    schoolEntry = kuto.ImageElem(image="../static/校园场馆.png", desc='校园场馆入口')


