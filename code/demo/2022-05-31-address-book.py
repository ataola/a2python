#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys

"""
@description 设计一个具有基本功能的通讯录，查询全部联系人、查询联系人、插入联系人、删除联系人、
"""

# 定义存储联系人的字典
users = {}


# 查询全部联系人
def query_users():
    if len(users.keys()) > 0:
        print('查询全部联系人成功，结果如下：')
        for key, value in users.items():
            print(key, value)
    else:
        print('暂无数据！')


# 查询联系人
def query_user(name):
    is_find = False
    for key in users.keys():
        if key == name:
            is_find = True
            print(name, users[name])
            break
    if not is_find:
        print('查无此人！')


# 插入联系人
def insert_user(name, mobile):
    is_find = False
    for key in users.keys():
        if key == name:
            print('联系人已存在！')
            break
    if not is_find:
        users[name] = mobile
        print('联系人', name, '添加成功！')


# 删除联系人
def delete_user(name):
    del users[name]
    print('联系人', name, '删除成功！')


# main函数
def main():
    print('========欢迎来到，小郑同学的通讯录系统========')
    ipt_word = ''
    while ipt_word != 'quit':
        ipt_word = input('请输入数字提示操作：1.查询全部联系人，2.查询联系人，3.插入联系人，4.删除联系人，输入quit退出\n')
        if ipt_word == '1':
            query_users()
        elif ipt_word == '2':
            name = input('请输入联系人姓名\n')
            query_user(name)
        elif ipt_word == '3':
            name = input('请输入联系人姓名\n')
            mobile = input('请输入联系人手机号\n')
            insert_user(name, mobile)
        elif ipt_word == '4':
            name = input('请输入联系人姓名\n')
            delete_user(name)
        elif ipt_word == 'quit':
            sys.exit(0)
        else:
            print('输入无效，请重新输入')


if __name__ == '__main__':
    main()
