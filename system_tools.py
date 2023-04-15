#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
system_tools.py:搭建学生管理系统时所用到的所有函数工具模块
Module description:
Author:Roman Lai
Current date:2023-04-14 20:53:19
Version:1.0
'''

import pickle
import os

STUDENT_INFO_FILE = "student_info.txt"
gl_students_list = []


def read_student_info():
    """从文件中读取学生信息"""
    if os.path.exists(STUDENT_INFO_FILE):
        with open(STUDENT_INFO_FILE, "rb") as f:
            try:
                gl_students_list = pickle.load(f)
            except EOFError:
                pass


def write_student_info():
    """将学生信息写入文件"""
    with open(STUDENT_INFO_FILE, "wb") as f:
        pickle.dump(gl_students_list, f)


def continue_action(action_func):
    """连续执行某个操作函数，直到用户主动取消 

    Args:
        action_func: 操作的函数
    """
    while True:
        action_str = input("请问还需要继续操作吗？ （y/n） ")
        if action_str.upper() == "Y":
            action_func()
        else:
            break


def show_menu():
    """展示功能面板"""
    print("=" * 80)
    print("欢迎使用圣育强学校学生管理系统 V1.0\n".center(60))
    print("【1】新增学生信息".ljust(30) + "【2】删除学生信息".rjust(30))
    print("【3】查找学生信息".ljust(30) + "【4】修改学生信息".rjust(30))
    print("【5】显示所有的学生信息".ljust(30) + "【6】退出系统".rjust(25))
    print("-" * 80)
    print("提示：使用数字键选择菜单，按回车键继续...".center(60))
    print("=" * 80)


def add_student():
    """添加学生信息"""
    name_str = input("请输入学生的姓名：")
    grade_str = input("请输入学生的班级：")
    number_str = input("请输入学生的学号：")
    gender_str = input("请输入学生的性别：")
    student_dict = {
        "name": name_str,
        "gender": gender_str,
        "number": number_str,
        "grade": grade_str,
    }
    gl_students_list.append(student_dict)
    print("已经成功添加%s的信息！" % student_dict["name"])
    print("+" * 80)
    print("姓名\t\t\t班级\t\t\t学号\t\t\t性别".ljust(0))
    print("%s\t\t\t%s\t\t\t%s\t\t\t%s".ljust(0) %
          (student_dict["name"], student_dict["grade"], student_dict["number"],
           student_dict["gender"]))
    print("+" * 80)


def del_student():
    """删除学生信息"""
    del_name_str = input("请输入需要删除的学生信息的名字：")
    target_index_list = []
    for index, student_info in enumerate(gl_students_list):
        if student_info["name"] == del_name_str:
            target_index_list.append(index)
    if len(target_index_list) == 0:
        print("抱歉，没有找到%s的信息！" % del_name_str)
    elif len(target_index_list) > 1:
        print("找到了以下同名学生，请输入需要删除的学生的编号：")
        for i, index in enumerate(target_index_list):
            print(f"{i + 1}. 学号：{gl_students_list[index]['number']}")
        select_index = input("请选择需要删除的学生编号（输入数字）：")
        target_index = target_index_list[int(select_index) - 1]
        gl_students_list.pop(target_index)
        print("已经成功删除了%s的信息！" % del_name_str)
    else:
        gl_students_list.pop(target_index_list[0])
        print("已经成功删除了%s的信息！" % del_name_str)


def find_student():
    """查找学生信息"""
    # 如果存在多个同名学生，直接打印出全部结果并不是一个好的选择。这样可能会让用户感到困惑甚至误操作。
    # 例如，如果存在两个同名学生，此时将两个学生的信息同时输出，
    # 那么用户可能无法确定哪个学生是他需要查找的目标。
    # 因此，我们需要考虑如何在保证简单易用的情况下，解决重名的问题。
    find_flag = False
    find_name_str = input("请输入需要查找的学生信息的名字：")
    find_index_list = []
    for index, student_info in enumerate(gl_students_list):
        if student_info["name"] == find_name_str:
            find_index_list.append(index)
    if len(find_index_list) > 1:
        print("找到了多个同名学生，请输入需要查找的学生的学号：")
        for i, index in enumerate(find_index_list):
            print(f"{i + 1}. 学号：{gl_students_list[index]['number']}")
        select_index = input("请选择需要查找的学生编号（输入数字）：")
        target_index = find_index_list[int(select_index) - 1]
    elif len(find_index_list) == 1:
        target_index = find_index_list[0]
    else:
        target_index = -1
    if target_index != -1:
        target_student = gl_students_list[target_index]
        print("成功找到了%s的信息！" % find_name_str)
        print("+" * 80)
        print("姓名\t\t\t班级\t\t\t学号\t\t\t性别".ljust(0))
        print("%s\t\t\t%s\t\t\t%s\t\t\t%s".ljust(0) %
              (target_student["name"], target_student["grade"],
               target_student["number"], target_student["gender"]))
        print("+" * 80)
        find_flag = True
    if not find_flag:
        print("抱歉，没有找到%s的信息！" % find_name_str)


def info_input(tips, original_msg):
    """输入修改的学生信息，如果用户没有输入新的学生信息，则返回原来的信息

    Args:
        tips: 用户的提示用语
        original_msg: 学生原来的信息

    Returns:
        返回修改的学生信息
    """
    if len(tips) == 0:
        return original_msg
    else:
        new_msg = input(tips)
        return new_msg


def modify_student():
    """修改学生信息"""
    modify_name_str = input("请输入需要修改的学生信息的名字：")
    modify_student_info_list = []
    for student_info in gl_students_list:
        if student_info["name"] == modify_name_str:
            modify_student_info_list.append(student_info)

    if len(modify_student_info_list) == 0:
        print("抱歉，没有找到%s的信息！" % modify_name_str)
    elif len(modify_student_info_list) == 1:
        student_info = modify_student_info_list[0]
        print(f"您正在修改的学生信息如下：\n"
              f"姓名：{student_info['name']}\n"
              f"班级：{student_info['grade']}\n"
              f"学号：{student_info['number']}\n"
              f"性别：{student_info['gender']}\n")
        confirm = input("是否确认修改？（y/n）：")
        if confirm == "y":
            student_info['name'] = info_input("请输入新的学生姓名：",
                                              student_info["name"])
            student_info['grade'] = info_input("请输入新的学生班级：",
                                               student_info["grade"])
            student_info['number'] = info_input("请输入新的学生学号：",
                                                student_info["number"])
            student_info['gender'] = info_input("请输入新的学生性别：",
                                                student_info["gender"])
            print("\n修改成功！修改后的学生信息如下：\n")
            print("+" * 80)
            print("姓名\t\t\t班级\t\t\t学号\t\t\t性别".ljust(0))
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s".ljust(0) %
                  (student_info["name"], student_info["grade"],
                   student_info["number"], student_info["gender"]))
            print("+" * 80)
    else:
        print("找到%s位同名学生，请输入需要修改的学生的序号：" % len(modify_student_info_list))
        for i, student_info in enumerate(modify_student_info_list):
            print(
                f"{i+1}. 姓名：{student_info['name']}\t\t班级：{student_info['grade']}\t\t学号：{student_info['number']}\t\t性别：{student_info['gender']}"
            )
        idx = int(input()) - 1
        student_info = modify_student_info_list[idx]
        print(f"您正在修改的学生信息如下：\n"
              f"姓名：{student_info['name']}\n"
              f"班级：{student_info['grade']}\n"
              f"学号：{student_info['number']}\n"
              f"性别：{student_info['gender']}\n")
        confirm = input("是否确认修改？（y/n）：")
        if confirm == "y":
            student_info['name'] = info_input("请输入新的学生姓名：",
                                              student_info["name"])
            student_info['grade'] = info_input("请输入新的学生班级：",
                                               student_info["grade"])
            student_info['number'] = info_input("请输入新的学生学号：",
                                                student_info["number"])
            student_info['gender'] = info_input("请输入新的学生性别：",
                                                student_info["gender"])
            print("\n修改成功！修改后的学生信息如下：\n")
            print("+" * 80)
            print("姓名\t\t\t班级\t\t\t学号\t\t\t性别".ljust(0))
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s".ljust(0) %
                  (student_info["name"], student_info["grade"],
                   student_info["number"], student_info["gender"]))
            print("+" * 80)


def show_all():
    """展示现有的学生信息"""
    print("+" * 80)
    print("姓名\t\t\t班级\t\t\t学号\t\t\t性别".ljust(0))
    if len(gl_students_list) == 0:
        print("抱歉，暂时没有任何学生的信息，请先去添加新的学生信息！".center(60))
    else:
        for student_info in gl_students_list:
            print("%s\t\t\t%s\t\t\t%s\t\t\t%s".ljust(0) %
                  (student_info["name"], student_info["grade"],
                   student_info["number"], student_info["gender"]))
    print("+" * 80)
    input("按任意键返回主菜单")
