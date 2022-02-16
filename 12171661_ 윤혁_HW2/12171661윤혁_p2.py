class menuInfo:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=int(price)
        self.stock=int(stock)

class Menu:
    orderList = {}
    total = 0
    def addMenu(self,f):
        datalist=f.readlines()
        for data in datalist:
            a=data.rstrip().split(", ")
            self.orderList[a[0]] = menuInfo(a[1],a[2],a[3])

    def printMenu(self):
        print("="*34)
        for k in self.orderList.keys():
             print(k+"."+self.orderList[k].name+"   "+"금액: "+
                str(self.orderList[k].price)+"원 재고: "+str(self.orderList[k].stock))
        print("end를 입력하시면 주문서로 돌아갑니다.")
        print("=" * 34)

class Order(Menu):
    orderResult = [0,0,0,0,0,0]
    totalResult=0
    totalPrice=0
    def orderMenu(self,menuNum):
        self.printMenu()

        if menuNum=='end':
            self.totalResult = self.orderResult[1] + self.orderResult[2] + self.orderResult[3] + self.orderResult[4] + \
                          self.orderResult[5]
            print("주문내역")
            print("총 주문 수량: "+str(self.totalResult)+" 개, 총 주문 금액: "+
                  str(self.totalPrice)+"원")
            Order.totalPrice = self.totalPrice
            initialView()

        for keys in self.orderList.keys():
            if not menuNum in Menu.orderList.keys():
                print("존재하지 않는 메뉴입니다")
                k = input("input: ")
                print()
                self.orderMenu(k)
            else:
                print("선택한 메뉴의 수량을 입력해주세요")
                k=input("input: ")
                print()
                if int(Menu.orderList[menuNum].stock)==0:
                    print("품절되었습니다. 다른 메뉴를 선택해주세요")
                    print()
                    print("메뉴번호를 다시 입력해주세요")
                    k=input("input: ")
                    print()
                    self.orderMenu(k)
                if Menu.orderList[menuNum].stock-int(k)>=0:
                    Menu.orderList[menuNum].stock -= int(k)
                    self.orderResult[int(menuNum)] += int(k)

                    self.totalPrice += int(k)*int(Menu.orderList[menuNum].price)
                    print("추가로 주문할 메뉴 번호를 입력해주세요")
                    k=input("input: ")
                    print()
                    self.orderMenu(k)
                else:
                    print("수량이 부족합니다")
class Manage(Menu):
    ManageResult=[0,0,0,0,0,0]
    totalResult = 0
    totalPrice = 0
    def Management(self,menuNum):
        Menu.printMenu(self)
        if menuNum=="end":
            self.totalResult=self.ManageResult[1]+self.ManageResult[2]+self.ManageResult[3]+self.ManageResult[4]+self.ManageResult[5]
            print("총 주문 수량: "+str(self.totalResult)+" 개, 총 주문 금액: "+str(self.totalPrice)+"원")
            initialView()
        for keys in Menu.orderList.keys():
            if not menuNum in Menu.orderList.keys():
                print("존재하지 않는 메뉴입니다")
            else:
                print("선택한 메뉴의 수량을 입력해주세요")
                k=input("input: ")
                print()
                Menu.orderList[menuNum].stock+=int(k)
                self.ManageResult[int(menuNum)]+=int(k)
                self.totalPrice+=int(k)*Menu.orderList[menuNum].price
                print("추가로 입고할 메뉴 번호를 입력해주세요")
                k = input("input: ")
                self.Management(k)
    def toSale(self):
        print("총 매출은 "+str(Order.totalPrice)+"원입니다")
        initialView()

def initialView():
    print("="*18)
    print("       주문서       ")
    print("="*18)
    print("1. 커피 주문하기")
    print("2. 커피 매출 확인")
    print("3. 커피 입고하기")
    print("4. 종료하기")
    print("="*18)
    print("원하시는 주문 번호를 입력해주세요")
    k=input("input: ")
    print()
    if k=="1":
        print("주문할 메뉴 번호를 입력해주세요")
        menuNum=input("input: ")
        print()
        o.orderMenu(menuNum)
    elif k=="2":
        ma.toSale()
    elif k=="3":
        print("입고할 메뉴 번호를 입력해주세요")
        menuNum = input("input: ")
        print()
        ma.Management(menuNum)
    elif k=="4":
        exit()
m = Menu()
o = Order()
ma = Manage()
f = open("cafe.txt", 'r',encoding='UTF8')
m.addMenu(f)

initialView()
