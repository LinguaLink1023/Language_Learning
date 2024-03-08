from car import Car, ElectricCar
from battery import Battery

tesla_modelx_01 = ElectricCar(make='Tesla', model='modelX', battery=Battery(65))
tesla_modelx_01.battery.describ_battery()
tesla_modelx_01.battery.get_range()