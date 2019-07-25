import sys
import os


def get_root_path():
    # print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
    # print(os.path.abspath(os.path.dirname(os.getcwd())))
    # print(os.path.abspath(os.path.join(os.getcwd(), "..")))
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def pr(value, title):
    print('-' * 25 + title + '-' * 25)
    if value is not None:
        for one in value:
            print('%s: %10d天 %10.10s%%' % (one[0], one[1], one[2]))
    p_line()


def p_list(value):
    if value is not None:
        index = 1
        for one in value:
            print("%s %s " % (index, str(one)))
            index=index+1
    p_line()


def p_file(file_path, values, title):
    savedStdout = sys.stdout  # 保存标准输出流
    with open(file_path, 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        print('-' * 25 + title + '-' * 25)
        if values is not None:
            for one in values:
                print('%s: %10d天 %10.10s%%' % (one[0], one[1], one[2]))
                # p_line()
    sys.stdout = savedStdout  # 恢复标准输出流


def p_file_no_format(file_path, value):
    savedStdout = sys.stdout  # 保存标准输出流
    with open(file_path, 'w') as file:
        sys.stdout = file  # 标准输出重定向至文件
        if value is not None:
            print('%s' % value)
    sys.stdout = savedStdout  # 恢复标准输出流

def p_file_no_format_add(file_path, values):
    savedStdout = sys.stdout  # 保存标准输出流
    with open(file_path, 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        if values is not None:
            for one in values:
                print('%s' % one)
    sys.stdout = savedStdout  # 恢复标准输出流

def p_file_list(file_path, values):
    savedStdout = sys.stdout  # 保存标准输出流
    with open(file_path, 'w') as file:
        sys.stdout = file  # 标准输出重定向至文件
        if values is not None:
            for one in values:
                print('%s,%s,%s' % (one[0], one[1], one[2]))
                # p_line()
    sys.stdout = savedStdout  # 恢复标准输出流


def p_file_list_with_no_format_add(file_path, values):
    savedStdout = sys.stdout  # 保存标准输出流
    with open(file_path, 'at') as file:
        sys.stdout = file  # 标准输出重定向至文件
        if values is not None:
            for one in values:
                print('%s' % one)
                # p_line()
    sys.stdout = savedStdout  # 恢复标准输出流


def p_file_list_with_no_format(file_path, values):
    savedStdout = sys.stdout  # 保存标准输出流
    with open(file_path, 'w') as file:
        sys.stdout = file  # 标准输出重定向至文件
        if values is not None:
            for one in values:
                print('%s' % one)
                # p_line()
    sys.stdout = savedStdout  # 恢复标准输出流


def p_line():
    print('-' * 50)


def read_file_list(file_path):
    values = []
    try:
        with open(file_path, 'r') as f1:
            files_lines = f1.readlines()
            for i in range(0, len(files_lines)):
                values.append(files_lines[i].rstrip('\n'))
    except:
        print("NO File Found %s" % file_path)
    return values
