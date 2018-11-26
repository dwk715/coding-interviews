#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 20:27
# @Author  : Dlala
# @File    : FindInPartiallySortedMatrix.py

'''
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''


def find(array, target):
    if not array or len(array) == 0:
        return False
    rows = len(array[0]) - 1
    row = 0
    cols = len(array) - 1
    col = cols
    while row <= rows and col >= 0:
        if array[row][col] == target:
            return True
        elif array[row][col] < target:
            row += 1
        else:
            col -= 1
    return False


def main():
    # 最大值测试
    print(find([[1, 2, 8, 9], [2, 3, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 5))
    # 最小值测试
    print(find([[1, 2, 8, 9], [2, 3, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 15))
    # 找不到的测试
    print(find([[1, 2, 8, 9], [2, 3, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 1))
    # 空指针测试
    print(find([], 54))


if __name__ == '__main__':
    main()
