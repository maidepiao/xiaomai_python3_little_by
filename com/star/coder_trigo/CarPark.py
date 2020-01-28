from datetime import datetime

print('请选择操作指令：A 汽车入库停车 L 汽车出库收费')

price = 2
park_dict = {}
while True:
    command = input('请输入指令 A 或者 L:')
    if command.upper() == 'A':
        car_no = input('汽车入库停车，请输入车牌号:')
        park_dict[car_no] = datetime.now()
    elif command.upper() == 'L':
        car_no = input('汽车出库计费，请输入车牌号:')
        if car_no in park_dict:
            start = park_dict[car_no]
            end = datetime.now()
            park_time = (end - start).seconds//60;
            park_cost = park_time*2
            print('停车开始时间:%s\n停车结束时间:%s\n停车分钟数:%s\n应收金额:%f\n'
                  %(start.strftime('%Y-%m-%d %H:%M:%S'),end.strftime('%Y-%m-%d %H:%M:%S'),park_time,park_cost))
            with open("D:/park"+str(start.date())+'.txt', "a", encoding="utf-8") as f:
                f.write('车牌:%s,收费%.2f \r'%(car_no,park_cost))
        else:
            print('查无车辆[{:s}],请确认'.format(car_no))
    print('-' * 100)

