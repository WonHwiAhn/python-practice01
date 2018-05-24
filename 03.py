# 문제3. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'
s_div = s.split('/')
s_div1 = s.rsplit('/', 1)

# print(s_div1)

path = ''
file_name = ''
i = 0 # for index값

for path_name in s_div:

    if i == 0:
        print(path_name, end="'")
    elif i == len(s_div)-1:
        file_name = path_name
        print(path_name, end="'")
    else:
        print(path_name, end="', '")

    i+=1
else:
    print("\n'"+s_div1[0]+"', '" + s_div1[1]+"'")