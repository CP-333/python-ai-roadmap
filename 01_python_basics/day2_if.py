name = input("请输入你的名字：")

while True:
    try:
        age = int(input("请输入你的年龄："))
        break
    except:
        print("请输入正确的数字")

goal = input("请输入你的学习目标：").strip().upper()

if age <= 12:
    identity = "儿童"
elif age <= 17:
    identity = "青少年"
else:
    identity = "成年人"

if goal == "AI":
    message = "选择AI是一个很好的方向"
elif goal == "编程":
    message = "选择编程不错，基础也很重要"
else:
    message = f"选择{goal}也很好，坚持就行"

print(f"你好{name},你是一个{identity},{message}")
