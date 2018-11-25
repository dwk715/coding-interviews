#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 9:34 PM
# @Author  : Dlala
# @File    : findNumber.py

'''
不修改数组找出重复的数字

在一个长度为n+1的数组里的所有数字都在1~n的范围内，所以数组中至少有一个数字是重复的。
请找出数组中任意一个重复的数字，但是不能修改输入的数组。
例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}, 那么对应的输出是重复的数字2或者3
'''


def get_duplication(array):
    # 检测数组非空
    if not array:
        return None
    start = 1
    end = len(array) - 1
    while end >= start:
        middle = int((end - start) / 2) + start
        count = count_range(array, start, middle)
        if end == start:
            if count > 1:
                return start
            else:
                break
        if count > (middle - start + 1):
            end = middle
        else:
            start = middle + 1
    return None


def count_range(array, start, end):
    if not array:
        return 0
    count = 0
    for i in range(len(array)):
        if start <= array[i] <= end:
            count += 1
    return count


def main():
    print(get_duplication([2, 3, 1, 0, 5, 4, 6]))
    print(get_duplication([2, 3, 1, 0, 2, 5, 3]))
    print(get_duplication([]))


if __name__ == '__main__':
    main()
