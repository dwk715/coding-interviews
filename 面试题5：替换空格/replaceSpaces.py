#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2018/11/26 23:18
# @Author  : Dlala
# @File    : replaceSpaces.py


def replace(string):
    if not string or len(string) == 0:
        return

    number_of_space = string.count(" ")

    new_len = len(string) + 2 * number_of_space

    index_of_original = len(string) - 1

    index_of_new = new_len - 1

    string += ["" for i in range(new_len - len(string))]

    while 0 <= index_of_original < index_of_new:
        if string[index_of_original] == ' ':
            index_of_new -= 2
            string[index_of_new: index_of_new+3] = '%20'
        else:
            string[index_of_new] = string[index_of_original]
        index_of_new -= 1
        index_of_original -= 1

    print(''.join(string))


def main():
    replace(list('We are happy'))
    replace(list(' We are happy'))
    replace(list('We are happy '))
    replace(list('Wearehappy'))
    replace(list('W e a r e h a p p y'))
    replace(list(''))
    replace(list())


if __name__ == '__main__':
    main()
