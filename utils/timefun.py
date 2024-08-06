import time


def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return int(hours), int(minutes), int(seconds)


def timecount():
    input("按下 Enter 键开始计时（按下1）...")

    start_time = time.time()  # 记录开始时间

    input("按下 Enter 键停止计时（按下2）...")

    end_time = time.time()  # 记录结束时间

    elapsed_time = end_time - start_time  # 计算经过的时间
    return elapsed_time

def time_c2(proj):
    print(f"{proj} 开始计时中")
    start_time = time.time()  # 记录开始时间

    input("按下 Enter 键停止计时...\n")

    end_time = time.time()  # 记录结束时间

    elapsed_time = end_time - start_time  # 计算经过的时间
    time_show(elapsed_time)
    return elapsed_time


def time_show(elapsed_time):
    formatted_time = format_time(elapsed_time)
    print(f"您此次花费的的时间为: {formatted_time[0]} 小时, {formatted_time[1]} 分钟, {formatted_time[2]} 秒\n")

def time_s2(elapsed_time):
    formatted_time = format_time(elapsed_time)
    s = f"{formatted_time[0]} 小时, {formatted_time[1]} 分钟, {formatted_time[2]} 秒"
    return s


def main():
    elapsed_time = timecount()  # 计算经过的时间
    time_show(elapsed_time)

if __name__ == "__main__":
    main()
