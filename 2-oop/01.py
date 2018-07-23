'''
定义一个学生类，用来形容学生
'''

# 定义一个空类
class student():
# 此处定义一个空类
    pass

# 定义一个对象
mingyue = student()

# 在定义一个类，用来描述Python的学生
class python_student():
   # 用None给不大确定的值赋值
    name = None
    age = 18
    course = "Python"

   # 定义一个功能函数
   # 1.def 的缩进层级
   # 2. 系统默认由一个self参数
    def do_homework(self):
        print("在做作业")

        # 推荐子啊函数末尾使用return 语句
        return None

# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = python_student()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递参数
yueyue.do_homework()
