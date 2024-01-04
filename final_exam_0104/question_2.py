

class drink_store:
    def __init__(self, store_name):
        self.store_name = store_name


    class Drinks():    # 飲料類別
        def __init__(self, name, price, sugar):
            self.name = name
            self.price = price
            self.sugar = sugar
            
        class ColdDrink(): # 冷飲類別
            def __init__(self, name, sugar, ice):
                super().__init__(name, sugar)
                self.ice = ice


        class HotDrink(): # 熱飲類別
            def __init__(self, name,  sugar):
                super().__init__(name, sugar)


# object2 = ColdDrink("少糖奶茶", 60, "少糖", "少冰")
# object3 = HotDrink("熱奶茶", 40, "全糖")


    class newDrink(Drinks): # 使用繼承方式來定義類別
        def __init__(self, name, price, sugar):
            super().__init__(name, price, sugar)

        def modify_name(self): # 修改飲料名稱
            print("\n")
            self.name = input("請輸入新的飲料名稱: ")
            print("飲料名稱已修改為: ", self.name)

        def modify_sugar(self): # 修改糖度
            self.sugar = input("請輸入新的糖度: ")
            print("糖度已修改為: ", self.sugar)

        def modify_price(self):     # 修改價錢
            self.price = input("請輸入新的價錢: ")
            print("價錢已修改為: ", self.price)


    object = Drinks("珍珠奶茶", 50, "半糖") # 物件1

    newDrink(object.name, object.price, object.sugar).modify_name() # 修改飲料名稱
    newDrink(object.name, object.price, object.sugar).modify_sugar() # 修改糖度
    newDrink(object.name, object.price, object.sugar).modify_price()    # 修改價錢
    print("新的飲料名稱: ", object.name, "新的價錢: ", object.price, "新的糖度: ", object.sugar) # 印出修改後的飲料名稱、價錢、糖度

    class employee:
        def __init__(self, name, work_year, work_hour): 
            self.name = name
            self.work_year = work_year
            self.work_hour = work_hour

        def get_name(self): # 取得姓名
            print("姓名為: "+self.name)
            return self.name

        def get_work_year(self): # 取得工作年資
            print(self.name+"工作年資為: "+str(self.work_year))
            return self.work_year

        def get_work_hour(self): # 取得工時
            print(self.name+ "工時為: "+str(self.work_hour))
            return self.work_hour

        def caculate_salary(self): # 計算薪水

            print(self.name+"薪水為: "+str(int(200 * self.work_hour)))
            return 200 * self.work_hour

        def add_work_hour(self): # 加班
            num = int(input("請輸入加班時數: "))
            self.work_hour += num
            print(self.name+"加班後工時為: ", self.work_hour)


    object_employee = employee("小明", 3, 8) # 物件員工
    print("\n")
    object_employee.get_name()
    object_employee.get_work_year()
    object_employee.get_work_hour()
    object_employee.caculate_salary()
    object_employee.add_work_hour()
    object_employee.caculate_salary()

    object_employee = employee("小修", 6, 12) # 物件員工
    print("\n")
    object_employee.get_name()
    object_employee.get_work_year()
    object_employee.get_work_hour()
    object_employee.caculate_salary()
    object_employee.add_work_hour()
    object_employee.caculate_salary()

    object_employee = employee("小哲", 4, 10) # 物件員工
    print("\n")
    object_employee.get_name()
    object_employee.get_work_year()
    object_employee.get_work_hour()
    object_employee.caculate_salary()
    object_employee.add_work_hour()
    object_employee.caculate_salary()

store_name_object = drink_store("小明奶茶店")   # 物件店名
print(store_name_object.store_name)