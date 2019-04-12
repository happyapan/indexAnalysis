import sys


def pr(value, title):
    print('-' * 25 + title + '-' * 25)
    if value is not None:
        for one in value:
            print('%s: %10d天 %10.10s%%' % (one[0], one[1], one[2]))
    p_line()


def p_file(file_path, value, title):
    savedStdout = sys.stdout  # 保存标准输出流
    with open(file_path, 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        print('-' * 25 + title + '-' * 25)
        if value is not None:
            for one in value:
                print('%s: %10d天 %10.10s%%' % (one[0], one[1], one[2]))
        # p_line()
    sys.stdout = savedStdout  # 恢复标准输出流


def p_line():
    print('-' * 50)
