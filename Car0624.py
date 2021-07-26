import datetime


class CarMessage(object):
    def __init__(self, num, owner, color, type, connect, money, endtime):
        # 汽车属性
        self.num = num
        self.color = color
        self.type = type
        self.owner = owner
        self.connect = connect
        self.money = money
        self.entime = endtime

    def __str__(self):
        print('车牌号：<%s> 车主：<%s> 颜色:<%s> 车型:<%s> 联系方式：<%s> 余额：<%s> 停车时间：<%s> '
              % (self.num, self.owner, self.color, self.type, self.connect, self.money, self.entime))


class Park(object):
    def init(self):  # 对停车场初始化车辆
        self.car_list.append(CarMessage('001', 'python', '黑', '大卡', '123456789', 34, datetime.datetime.now()))
        self.car_list.append(
            CarMessage('002', 'hello', '黑', '小汽车', '123456789', 87,
                       datetime.datetime.now() - datetime.timedelta(minutes=10)))
        self.car_list.append(
            CarMessage('003', 'java', '白', '小汽车', '123456789', 55,
                       datetime.datetime.now() - datetime.timedelta(hours=1)))
        self.car_list.append(
            CarMessage('004', 'westos', '黑', '小卡', '123456789', 60,
                       datetime.datetime.now() - datetime.timedelta(days=2)))
        self.car_list.append(
            CarMessage('005', 'root', '白', '中卡', '123456789', 24,
                       datetime.datetime.now() - datetime.timedelta(minutes=60)))

    def __init__(self):
        self.max_car = 200
        self.car_list = []
        self.cur_car = len(self.car_list)

    def Menu(self):
        self.init()
        while True:
            print("""
          停车场管理系统
        1）停车
        2）取车
        3）余额查询
        4）显示已存放车辆
        5）查询
        6）编辑车辆信息
        7）退出

      """)
            choice = input("请输入你的选择：")
            if choice == '1':
                self.park()
            elif choice == '2':
                self.exit()
            elif choice == '3':
                car = input("请输入车牌号：")
                self.pay(car)
            elif choice == '4':
                for i in self.car_list:
                    CarMessage.__str__(i)
            elif choice == '5':
                self.find()
            elif choice == '6':  # 编辑车辆信息
                self.edit()
            elif choice == '7':
                exit(0)
            else:
                print('请输入正确选项！！！')

    def park(self):
        if self.cur_car < self.max_car:
            car_num = input('请输入你的车牌号：')
            res = self.check(car_num)  # 判断该车牌是否有停车记录
            if res is None:
                self.car_list.append(CarMessage(car_num, input('车主：'), input('颜色：'), input('车型<小汽车、小卡、中卡和大卡>：'),
                                                input('联系方式：'), int(input('余额')), datetime.datetime.now()))
                print('汽车可以进入')
            else:
                print('车辆已在停车场内部')

        else:
            print('车位已满，无法停车')

    def exit(self):
        car_num = input("请输入你的车牌号：")
        res = self.check(car_num)
        if res is not None:
            self.pay(res)
            self.car_list.remove(res)
            print('一路平安,出行平安')

        else:
            print('你的车辆不在停车场内部，请通知管理员！')

    def pay(self, car):
        # res = self.check(car)
        money = (datetime.datetime.now() - car.endtime).seconds / 60
        print("当前余额：%s" % (money))
        while True:
            if car.money >= money:  # 判断余额是否够支付
                car.money -= money
                print('自动付款%s成功' % (money))
                break
            else:
                print('余额不足请充值')
                car.money += int(input('充值金额：'))
                print('充值成功')

    def check(self, car_num):
        for i in self.car_list:
            if car_num == i.num:
                return i
        else:
            return None

    def find(self):
        while True:
            print('''
      1）根据车牌查询
      2）根据车型查询
      3）返回
      ''')
            choice = input("请输入你的选择:")
            if choice == '1':
                num = input('车牌号：')
                res = self.check(num)
                if res is not None:
                    CarMessage.__str__(res)

                else:
                    print("查无此车！")

            elif choice == '2':
                type = input("车型<小汽车、小卡、中卡和大卡>：")
                if type in ['小汽车', '小卡', '中卡', '大卡']:
                    for i in self.car_list:
                        if i.type == type:
                            CarMessage.__str__(i)
                else:
                    print('不存在%s这种车型' % (type))


            elif choice == '3':
                break
            else:
                print('请输入正确选项\n')

    def edit(self):  # 更改车辆信息
        num = input('请输入车牌号：')
        res = self.check(num)
        if res is not None:
            CarMessage.__str__(res)
            print('信息修改：\n车牌号：%s' % (num))
            res.owner = input('车主：')
            res.clor = input('颜色：')
            while True:
                type = input("车型<小汽车、小卡、中卡和大卡>：")
                if type in ['小汽车', '小卡', '中卡', '大卡']:
                    res.type = type
                    break
                else:
                    print('不存在%s这种车型,请重新输入\n' % (type))

            res.connect = input('联系方式：')
            res.money = int(input('余额：'))
            res.entime = datetime.datetime.strptime(input('进入停车场时间(eg:2021-06-24 11:14:10)：'),
                                                    '%Y-%m-%d %H:%M:%S')
            print('信息修改成功...')

        else:
            print('没有车牌%s的车辆信息' % (num))


p = Park()
p.Menu()
