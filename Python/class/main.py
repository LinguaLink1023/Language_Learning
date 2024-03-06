from syrup_mixer import SyrupMixer

device_pepsi_01 = SyrupMixer(model='Advanced', max_water_volume=30, max_sugar_volume=20)
device_pepsi_02 = SyrupMixer(model='Advanced', max_water_volume=30, max_sugar_volume=20)
device_pepsi_03 = SyrupMixer(model='Advanced', max_water_volume=30, max_sugar_volume=20)
device_pepsi_04 = SyrupMixer(model='Advanced', max_water_volume=30, max_sugar_volume=20)

device_wahaha_01 = SyrupMixer(model='Essential', max_water_volume=30, max_sugar_volume=20)
device_wahaha_02 = SyrupMixer(model='Essential', max_water_volume=30, max_sugar_volume=20)
device_wahaha_03 = SyrupMixer(model='Essential', max_water_volume=30, max_sugar_volume=20)
device_wahaha_04 = SyrupMixer(model='Essential', max_water_volume=30, max_sugar_volume=20)

print(f"当前图纸SyrupMixer总共生产了{SyrupMixer.counts}台设备")
print(f"娃哈哈的第3台是总共生产的第{device_wahaha_03.id}台")