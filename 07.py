# 문제7.
# 키보드에서 정수로 된 돈의 액수를 입력 받아
# 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전
# 각 몇 개로 변환 되는지 작성하시오.

money_unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

money = int(input('금액을 입력해주세요: '))

print('금액: ' + str(money) + '원')

for unit in money_unit:
    print(str(unit) + '원: ' + str(money//unit) + '개')
    money %= unit

