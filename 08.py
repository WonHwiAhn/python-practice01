# 문제 8.
# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

list = []
i = 0
sum = 0

for i in range(0, 5):
    list.append(int(input('>')))

for i in range(0, len(list)):
    sum += list[i]
    i += 1

print('평균: ' + str(sum/5))