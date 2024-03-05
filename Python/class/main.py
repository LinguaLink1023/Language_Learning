from syrup_mixer import SyrupMixer

device_test = SyrupMixer(model='Test', max_water_volume=30, max_sugar_volume=20)

device_test.add_water(25)
device_test.add_sugar(18)
device_test.mix()
print(SyrupMixer.test_volume)