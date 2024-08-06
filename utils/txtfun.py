import time
import random
import os

from utils.fpath import *


def da_hour():
    t = time.localtime(time.time())
    data = time.strftime('%Y-%m-%d', t)
    hour = time.strftime('%H:%M', t)
    return data, hour


def setlog(proj, begin_t):
    data, end_t = da_hour()

    log_path = os.path.join(Log_Path, f"{data}.txt")
    info = f"{begin_t} - {end_t}\t{str(proj)}\n"

    if not os.path.exists(log_path):
        with open(log_path, 'w', encoding='utf-8') as file:
            file.write(f"{data}\n")

    with open(log_path, 'a', encoding='utf-8') as file:
        file.write(info)


def readlog():
    data, _ = da_hour()
    log_path = os.path.join(Log_Path, f"{data}.txt")

    try:
        with open(log_path, 'r', encoding='utf-8') as file:
            info = file.read()
    except FileNotFoundError:
        info = f"{data}\n"+"\t\t今日暂无记录"
        with open(log_path, 'w', encoding='utf-8') as file:
            file.write(f"{data}\n")
    if info == f"{data}\n":
        info = f"{data}\n" + "\t\t今日暂无记录"
    return info


def lyrics():
    info = []
    lyr_path = os.path.join(Res_Path, "lyr.txt")
    # 打开文件并逐行读取内容
    with open(lyr_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去除每行末尾的换行符，并添加到列表中
            info.append(line.strip())
    random.shuffle(info)
    return info


def readtxt(filename):
    filepath = os.path.join(BASE_DIR, "res", filename)
    with open(filepath, "r", encoding="utf-8") as file:
        info = file.read()
    return info