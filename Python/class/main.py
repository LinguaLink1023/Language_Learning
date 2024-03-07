from car import Car

porsche_macan_01 = Car(make='Porsche', model='Macan')
print(f"当前车辆的生产时间为{porsche_macan_01.produce_time}")
porsche_macan_01.read_odometer()
porsche_macan_01.car_service()
print(f"最近一次保养时间为:{porsche_macan_01.last_service_date}")