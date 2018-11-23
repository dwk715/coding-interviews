#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/23 6:46 PM
# @Author  : Dlala
# @File    : findNumber.py

'''
找出数组中重复的数字

在一个长度为n的数组里的所有数字都在0～n-1的范围内。数组中某些数字是重复的，
但不知道有几个数字重复了，也不知道每个数字重复了几次。

请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3},
那么对应的输出是重复的数字2活着3
'''


def find(array):
    # 判断数组非空
    if not array:
        return None
    # 判断数组是否存在不在0～n-1中的数字
    for i in array:
        if i < 0 or i > (len(array) - 1):
            return None
    for i in range(len(array)):
        while array[i] != i:
            if array[i] == array[array[i]]:
                return array[i]
            temp = array[i]
            array[i] = array[temp]
            array[temp] = temp
    return None


def main():
    print(find([2, 3, 1, 0, 2, 5, 3]))
    print(find([2, 1, 3, 1, 4]))
    print(find([]))
    print(find([5, 4, 1, 3, 2, 0]))


if __name__ == '__main__':
    main()
