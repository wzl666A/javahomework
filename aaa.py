#统计文件的字符数、词数、行数
file_add = input("请输入文件名:")

f = open(file_add,encoding='utf-8')
c = 0
w = 0
l = 0
for line in f:
    c = c + len(line)
    word = line.split()
    w = w + len(word)
    l = l + 1
else:
    print("字符数=%s" % c)
    print("词数=%s" % w)
    print("行数=%s" % l)
f.close()


#统计文件的注释行、空行、代码行
file_add = input("请再次输入文件名:")
f = open(file_add,encoding='utf-8')

code = 0
comment = 0
blank = 0
is_comment = False
start_comment_index = 0
for index,line in enumerate(f,start=1):
    line = line.strip()

    if not is_comment:
        if line.startswith("'''") or line.startswith('"""'):
                is_comment = True
                start_comment_index = index

        elif line.startswith('#'):
                comment = comment + 1
        elif line == '':
                blank = blank + 1
        else:
                code = code + 1

    else:
        if line.endswith("'''") or line.endswith('"""'):
                is_comment = False
                comment += index - start_comment_index + 1
        else:
            pass

print("代码行数=%d" % code)
print("空行数=%d" % blank)
print("注释行数=%d" % comment)
f.close()