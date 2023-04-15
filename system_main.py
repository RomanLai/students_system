#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
system_main.py:学生信息管理系统
Module description:
Author:Roman Lai
Current date:2023-04-14 20:52:05
Version:1.0
'''

import system_tools

# 加载学生信息
system_tools.read_student_info()
while True:
    system_tools.show_menu()
    choice_str = input("请选择你要执行的操作：")
    if choice_str == "1":
        system_tools.add_student()
        system_tools.continue_action(system_tools.add_student)
    elif choice_str == "2":
        system_tools.del_student()
        system_tools.continue_action(system_tools.del_student)
    elif choice_str == "3":
        system_tools.find_student()
        system_tools.continue_action(system_tools.find_student)
    elif choice_str == "4":
        system_tools.modify_student()
        system_tools.continue_action(system_tools.modify_student)
    elif choice_str == "5":
        system_tools.show_all()
    elif choice_str == "6":
        # 保存学生信息
        system_tools.write_student_info()
        print("欢迎下次再次使用圣育强学校学生管理系统，谢谢！")
        break
    else:
        print("您的输入有误，请重新输入!")
