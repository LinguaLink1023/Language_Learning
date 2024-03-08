class Battery:
    def __init__(self, battery_size=40):
        self.batter_size = battery_size
        
    def describ_battery(self):
        print(f"本电池总容量{self.batter_size}度")
        
    def get_range(self):
        if self.batter_size == 40:
            print(f"{self.batter_size}度的电池续航里程为150英里")
        elif self.batter_size == 65:
            print(f"{self.batter_size}度的电池续航里程为225英里")