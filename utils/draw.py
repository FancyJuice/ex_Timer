# from utils import csv_fun as C
import matplotlib.pyplot as plt
# import os
from utils.fpath import *



def draw_bar_chart(xlabel, yvalue):
    plt.figure(num=1, figsize=(7, 5), )
    plt.rcParams['font.sans-serif'] = ['SimSun']
    plt.rcParams['axes.unicode_minus'] = False

    # 设置颜色列表，前两个柱状图为红色，其余为默认颜色
    colors = []
    for i in range(len(xlabel)):
        if i<2:
            colors.append('orangered')
        elif i<5:
            colors.append('tomato')
        elif i<8:
            colors.append('coral')
        else:
            colors.append('wheat')
    # print(xlabel)
    plt.bar(xlabel, yvalue, color=colors)
    plt.ylabel('时间/h', fontsize=14)  # 设置 y 轴标签
    plt.grid(True, linestyle='--')
    plt.tick_params(axis='both', which='major', labelsize=14)
    os.remove(RP_Path)
    plt.savefig(RP_Path, format='png', bbox_inches='tight')
    plt.close()
    # plt.show()


def pic_fun(fp):
    # projs_t = C.read_csv(fp)
    Xlabel = []
    Yvalue = []
    # k = 0
    # for projs, pro_t in projs_t.items():
    #     t = float(pro_t) / 3600
    #     t1 = round(t, 1)
    #     k += 1
    #     if t1 < 0.1 or k > 10:
    #         break
    #     Xlabel.append(projs)
    #     Yvalue.append(t1)
    # # 将Yvalue和对应的Xlabel打包成元组列表并根据Yvalue排序
    # sorted_data = sorted(zip(Yvalue, Xlabel))
    # # 解压缩排序后的元组列表
    # Yvalue, Xlabel = zip(*sorted_data)
    # # print(Xlabel)
    # # print(Yvalue)
    # draw_bar_chart(Xlabel, Yvalue)


if __name__ == '__main__':
    fp = os.path.join("../res/", "data.csv")
    projs_t = C.read_csv(fp)

    print(projs_t)
    Xlabel = []
    Yvalue = []
    k = 0
    for projs, pro_t in projs_t.items():
        t = float(pro_t) / 3600
        t1 = round(t, 1)
        k += 1
        if t1 < 0.1 or k > 10:
            break
        Xlabel.append(projs)
        Yvalue.append(t1)

    print(Xlabel)
    print(Yvalue)

    draw_bar_chart(Xlabel, Yvalue)
