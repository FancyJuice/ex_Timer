import csv
from utils import timefun as T
import os
from utils.fpath import *
from utils import draw as dw

def read_csv(file_path):
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        # 如果文件不存在或为空，则返回空的字典
        return {}
    with open(file_path, 'r', newline='', encoding='utf-8') as file:

        csv_reader = csv.reader(file)

        # 读取第一行数据（项目名称）
        projs = next(csv_reader)

        # 读取第二行数据（对应项目的时间）
        pro_t = next(csv_reader)

        # 将水果名称和价格一一对应，形成字典
        projs_t = dict(zip(projs, pro_t))

    return projs_t


def show_all(projs_t):
        # 显示读取的数据
        print("项目名称\t时间\n")
        for projs, pro_t in projs_t.items():
            t = T.time_s2(float(pro_t))
            print(f"{projs}\t\t{t}")


def show_a2(file_path):
    # 显示读取的数据
    projs_t = read_csv(file_path)
    s = "项目名称"
    s.ljust(8)
    print(f"{s}\t已花费时间\n")
    for projs, pro_t in projs_t.items():
        t = T.time_s2(float(pro_t))
        print(f"{projs}\t\t{t}")
    print()

def show_info(file_path):
    projs_t = read_csv(file_path)
    s = "项目名称"
    info = f"{s.ljust(10)}\t已花费时间\n"

    Xlabel = []
    Yvalue = []
    k = 0


    for projs, pro_t in projs_t.items():
        t = T.time_s2(float(pro_t))
        info += f"· {projs.ljust(10)}\t{t}\n"
        t = float(pro_t) / 3600
        t1 = round(t, 1)
        k += 1
        if t1 >= 0.1 and k <= 10:
            Xlabel.append(projs)
            Yvalue.append(t1)
    # print(Xlabel)
    dw.draw_bar_chart(Xlabel, Yvalue)
    return info


def show_pros(file_path):
    projs_t = read_csv(file_path)
    s = "已有项目：\n"
    for projs, pro_t in projs_t.items():
        s = s + projs + " "
    return s


def show_projs():
    projs_t = read_csv(File_Path)
    info1 = "已有项目："
    info2 = ""
    for projs, pro_t in projs_t.items():
        info2 = info2 + projs + " "
    return info1, info2



def write_csv(file_path, fruits, prices):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)

        # 写入水果名称和价格
        csv_writer.writerow(fruits)
        csv_writer.writerow(prices)



def change(file_path):
    proj = input("请输入项目名：")
    os.system('cls' if os.name == 'nt' else 'clear')
    projs_t = read_csv(file_path)
    if proj in projs_t:
        # 显示时间
        t = T.time_s2(float(projs_t[proj]))
        print(f"{proj} 已花费时间: {t}")
    else:
        print("欢迎开始新项目\n")
        # 添加水果并设置价格为0
        projs_t[proj] = 0.0
    edt = T.time_c2(proj)
    t = float(projs_t[proj]) + edt
    projs_t[proj] = t

    # 更新CSV文件
    write_csv(file_path, list(projs_t.keys()), list(projs_t.values()))

    show_all(projs_t)

def check(file_path, proj):
    projs_t = read_csv(file_path)
    if proj in projs_t:
        return True
    else:
        return False

def change_info(file_path, proj):
    projs_t = read_csv(file_path)
    if proj in projs_t:
        t = T.time_s2(float(projs_t[proj]))
        info1 = f"{proj} 已花费时间: {t}"

    else:
        info1 = f"欢迎开始新项目 {proj}"
    return info1

def change_3(file_path, proj, edt):
    projs_t = read_csv(file_path)
    if proj not in projs_t:
        projs_t[proj] = 0.0
    t = float(projs_t[proj]) + edt
    projs_t[proj] = t

    projs_n = sorted(projs_t.items(), key=lambda x: -float(x[1]))
    projs_t = dict(projs_n)
    # 更新CSV文件
    write_csv(file_path, list(projs_t.keys()), list(projs_t.values()))

def change_2(file_path, proj):
    projs_t = read_csv(file_path)
    if proj in projs_t:
        # 显示时间
        t = T.time_s2(float(projs_t[proj]))
        info1 = f"{proj} 已花费时间: {t}"

    else:
        info1 = "欢迎开始新项目\n"
        projs_t[proj] = 0.0
    edt = T.time_c2(proj)
    t = float(projs_t[proj]) + edt
    projs_t[proj] = t

    # 更新CSV文件
    write_csv(file_path, list(projs_t.keys()), list(projs_t.values()))

def del_(file_path):
    proj = input("请输入项目名：")
    os.system('cls' if os.name == 'nt' else 'clear')
    projs_t = read_csv(file_path)
    del projs_t[proj]
    write_csv(file_path, list(projs_t.keys()), list(projs_t.values()))
    print("更新完成")
    show_all(projs_t)

def del_2(file_path, proj):
    projs_t = read_csv(file_path)
    if proj in projs_t:
        del projs_t[proj]
        write_csv(file_path, list(projs_t.keys()), list(projs_t.values()))

def add_1(file_path, proj, t):
    t = float(t)
    t *= 3600
    projs_t = read_csv(file_path)
    if proj in projs_t:
        projs_t[proj] = float(projs_t[proj]) + t
    else:
        projs_t[proj] = t
    projs_n = sorted(projs_t.items(), key=lambda x: -float(x[1]))
    projs_t = dict(projs_n)
    write_csv(file_path, list(projs_t.keys()), list(projs_t.values()))


if __name__ == "__main__":
    file_path = "data.csv"
    show_a2(file_path)
    flag = True
    while flag:
        key = input("停止请按：N ")
        if key=="N" or key=="n":
            break
        change(file_path)


