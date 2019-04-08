def pr(value, title):
    print('-' * 25 + title + '-' * 25)
    for one in value:
        print('%s: %10d天 %10.10s%%' % (one[0], one[1], one[2]))
    p_line()


def p_line():
    print('-' * 50)
