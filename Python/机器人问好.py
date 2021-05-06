class Robot:
    def __init__(self):
        self.name = input("我是您的机器人，帮我取个名呗")
        self.yourname = input("我该怎么称呼您呢？")
        print("你好，我叫%s。亲爱的%s主人，很高兴认识你"%(self.name,self.yourname))

    def say_wish(self):
        for i in range(3):
            wish = input("告诉我一个你的愿望吧")
            print("你的第%s个愿望是："%(str(i+1)))
            for i in range(3):
                print(wish)
    
    def age(self):
        agenumber = input("您几岁了？")
        print("你现在才%s岁呢，还年轻"%(agenumber))

    def function_execution(self):
        self.say_wish()
        self.age()

robot1 = Robot()
robot1.function_execution()