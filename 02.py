# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

str = input('수를 입력하세요: ')

if str.isdigit() is False:
    print('정수가 아닙니다.')
elif int(str)%2 == 0:
    print('짝수입니다.')
elif int(str)%2 != 0:
    print('홀수입니다.')