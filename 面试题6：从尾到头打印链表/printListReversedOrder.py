#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 21:45
# @Author  : Dlala
# @File    : printListReversedOrder.py

'''
输入一个链表的头节点，从尾到头反过来打印每个结点的值
python可以利用[::-1]
也可以用栈来实现
'''


def print_list_from_tail_to_head(listNode):
    l = []
    if not listNode or len(listNode) == 0:
        return None
    print(listNode[::-1])


def main():
    print_list_from_tail_to_head([1, 2, 3])
    print_list_from_tail_to_head([1])
    print_list_from_tail_to_head([])


if __name__ == '__main__':
    main()
