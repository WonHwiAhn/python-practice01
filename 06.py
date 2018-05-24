# 문제6.
# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

#str = int(input('숫자'))

# 임시 리스트
list = [3, 5, 7, 8, 9, 0, 5, 3, 21, 3, 5, 547, 45, 7, 423, 563, 67, 468, 56, 679]
multiple_num = 0
sum_multiple_num = 0

for value in list:
    if value % 3 == 0:
        multiple_num += 1
        sum_multiple_num += value

print('주어진 리스트에서 3의 배수의 개수 => ' + str(multiple_num))
print('주어진 리스트에서 3의 배수의 합 => ' + str(sum_multiple_num))