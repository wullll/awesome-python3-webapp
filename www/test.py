import random
import re
import logging
logging.basicConfig(level=logging.INFO)
# 将a-z 26个字母存放在列表中
num_list = []
for i in range(ord('a'), ord('z')+1):
    num_list.append(chr(i))
# 随机取一个数
random_num = random.randint(0, 25)
guess_num = num_list[random_num]
logging.log(logging.INFO, guess_num)
flag = True
while flag:
    # 开始猜字母游戏
    num_input = input("请猜一个英文字母:\n")
    # 检查输入的字符是否是英文字符
    #  使用正则表达式来匹配a-z
    # 去空格
    num_input = num_input.strip()
    if re.match(r'^[a-z]$', num_input):
        # assert num_input == guess_num, '您猜对了'
        # 判断是否大写，如果大写，则转成小写来进行比较
        if num_input.isupper():
            num_input = num_input.lower()
        if num_input is guess_num:
            print("恭喜您，您猜对了")
            flag = False
        elif num_input > guess_num:
            print("您猜的不对，往前猜猜？")
        elif num_input < guess_num:
            print("您猜错了，往后猜猜")
    else:
        print("您输入的字符不是字母，请输入单个字母")








