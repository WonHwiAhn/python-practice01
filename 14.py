# 문제14
# 숨겨진 카드의 수를 맞추는 게임입니다.
# 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
# 아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면
# "더 높게", 다시 75이라고 입력하면 "더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다.
# 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.

import random

random_value = random.randint(1, 100)

user_select = 'y'
count = 1
print('수를 결정하였습니다. 맞추어 보세요\n 1 - 100')

while user_select == 'y' or user_select == 'Y':
    print(random_value)
    print(str(count) + '>>', end='')
    user_value = input()

    if random_value < int(user_value):
        print('더 작게!')
    elif random_value > int(user_value):
        print('더 높게!')
    else:
        random_value = random.randint(1, 100)
        print('맞았습니다.')
        print('다시 하겠습니까(y/n)?')
        user_select = input()