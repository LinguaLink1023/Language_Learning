class SyrupMixer:
    test_volume = 10
    def __init__(self, model='Classic', max_water_volume=20, max_sugar_volume=15):
        self.model = model
        self.max_water_volume = max_water_volume
        self.max_sugar_volume = max_sugar_volume
        self.water_volume = 0
        self.sugar_volume = 0
        
    def add_water(self, volume):
        if self.water_volume + volume > self.max_water_volume:
            print(f"超出了最大容水量{self.max_water_volume}，无法添加")
            return
        self.water_volume += volume
        print(f"添加了{volume}升的水，当前水的总量为{self.water_volume}升")
        
    def add_sugar(self, volume):
        if self.sugar_volume + volume > self.max_sugar_volume:
            print(f"超出了最大容糖量{self.max_sugar_volume}，无法添加")
            return
        self.sugar_volume += volume
        print(f"添加了{volume}升的糖，当前糖的总量为{self.sugar_volume}升")
        
    def mix(self):
        total_volume = self.water_volume + self.sugar_volume
        if total_volume > 0:
            sugar_ratio = self.sugar_volume / total_volume
            print(f"混合了糖和水，糖的比例为{sugar_ratio * 100}%")
        else:
            print("没有添加任何水与糖，无法混合")
            
    def warning(self):
        print("warning warning warning!")
        
            