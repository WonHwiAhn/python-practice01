# 문제9.
# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

str = input('입력> ')
str_reverse = ''

for index in range(len(str), 0, -1):
    str_reverse += str[index-1:index]
    # str[::-1]

print(str_reverse)