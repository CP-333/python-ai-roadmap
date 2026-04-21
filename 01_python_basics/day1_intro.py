name = input("请输入你的名字：")
try:
    age = int(input("请输入你的年龄："))
except:
    print("请输入正确的数字")
goal = input("请输入你的目标：")

print(f"你好，我叫{name}, 今年{age}岁, 我想学{goal}")
