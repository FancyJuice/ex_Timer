import time


def version_control(v_path, flag=False):
    t = time.localtime(time.time())
    data = time.strftime('%m%d', t)

    with open(v_path, 'r', encoding='utf-8') as file:
        version_line = file.readline()
    v_ = "01"
    version = version_line
    if version_line is None or len(version_line) < 6:
        version = data + v_
        with open(v_path, 'w', encoding='utf-8') as file:
            file.write(version)
    elif flag:
        if version_line[:4] == data:
            v = int(version_line[4:])
            v_ = '{:02d}'.format(v + 1)
        version = data + v_
        with open(v_path, 'w', encoding='utf-8') as file:
            file.write(version)
    return version


if __name__ == '__main__':
    version_control("../res/version.txt")
    print("hello")
