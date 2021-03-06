#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2018/11/27 22:17
# @Author  : Dlala
# @File    : constructBinarayTree.py

'''
重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def re_construct_binary_tree(self, pre, tin):
        if not pre or not tin:
            return None
        if len(pre) == 0 or len(tin) == 0:
            return None
        if len(pre) == len(tin) == 1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            # 利用递归思想， 将左右树通过.index()出入
            root.left = self.re_construct_binary_tree(pre[1:tin.index(pre[0]) + 1], tin[:tin.index(pre[0])])
            root.right = self.re_construct_binary_tree(pre[tin.index(pre[0]) + 1:], tin[tin.index(pre[0]) + 1:])


