class fried_chicken:
    def __init__(self, ingredient, flavor, spicy, crispy, price):
        self.ingredient = ingredient
        self.flavor = flavor
        self.spicy = spicy
        self.crispy = crispy
        self.price = price

        # 建構子 (Constructor) 成分 口味 辣度 酥脆度 價格

    def sub_function1(self): # 副函式1
        print("副函式1: ")
        print("炸雞的成分是", self.ingredient)
        print("炸雞的口味是", self.flavor)

    def sub_function2(self): # 副函式2
        print("副函式2: ")
        print("炸雞的辣度是", self.spicy)
        print("炸雞的酥脆度是", self.crispy)

    def sub_function3(self): # 副函式3
        print("副函式3: ")
        print("炸雞的價格是", self.price)


object1 = fried_chicken('雞胸','原味','中辣','特別酥脆','100') # 物件1
object1.sub_function1()
object1.sub_function2()
object1.sub_function3()

object2 = fried_chicken('雞腿','蒜味','小辣','普通酥脆','80') # 物件2
object2.sub_function1()
object2.sub_function2()
object2.sub_function3()

object3 = fried_chicken( '雞翅','香辣味','大辣','普通酥脆','60')    # 物件3
object3.sub_function1()
object3.sub_function2()
object3.sub_function3()

object4 = fried_chicken( '雞排','胡椒味','不辣','特別酥脆','120')   # 物件4
object4.sub_function1()
object4.sub_function2()
object4.sub_function3()
