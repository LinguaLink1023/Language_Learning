import time
from datetime import datetime
from battery import Battery

class Car:
    tear_counts = 4
    wheel_counts = 1
    __MAX_LITER = 100
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.produce_time = datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S") 
        self.odometer_reading = 0
        self.__gas_remain = 0
        
    def read_odometer(self):
        print(f"这辆车行驶了{self.odometer_reading}公里")
        
    def increment_odometer(self, kilometers):
        if kilometers >= 0:
            self.odometer_reading += kilometers
        else:
            print("新增的行驶里程不能是负数!")    
            
    def car_service(self):
        timestamp = time.time()  # 获取当前的时间戳
        # 使用datetime.fromtimestamp()将时间戳转换为datetime对象
        dt_object = datetime.fromtimestamp(timestamp)
        # 使用strftime()将datetime对象格式化为字符串      
        self.last_service_date = dt_object.strftime("%Y-%m-%d %H:%M:%S") 
              
    def read_gas_remaining(self):
        print(f"当前还剩{self.__gas_remain}升汽油")
            
    def gas_used(self, liter):
        if self.__gas_remain - liter > 0:
            self.__gas_remain -= liter
        else:
            print("当前剩余油量不足")
        
    def gas_add(self, liter):
        if self.__gas_remain + liter <= Car.__MAX_LITER:
            self.__gas_remain += liter
        else:
            print("超出了油箱的最大容量，已自动加满")
            self.__gas_remain = Car.__MAX_LITER
            
class ElectricCar(Car):
    def __init__(self, make, model, battery):
        super().__init__(make, model)
        self.battery = battery
        
    def read_gas_remaining(self):
        print("电动车没有油箱")
            
    def gas_used(self, liter):
        print("电动车没有油箱")
        
    def gas_add(self, liter):
        print("电动车没有油箱")

        
        

        
            