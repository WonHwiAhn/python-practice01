# 문제12
# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

for i in range(1, 100):
    divmod_value = divmod(i, 10)
    # print(divmod_value)

    if divmod_value[1] == 3 or divmod_value[1] == 6 or divmod_value[1] == 9:
        print(str(i) + ' 짝', end='')
        if divmod_value[0] == 3 or divmod_value[0] == 6 or divmod_value[0] == 9:
            print('짝')
        else:
            print('')



    #else:
    #    print()