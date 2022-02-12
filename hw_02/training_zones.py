import zoneinfo


age = float(input("Please enter your age: "))
resting_hr = float(input("Please enter your resting heart rate: "))
print("===============================================")

max_heart_rate = float(208 - (0.7 * age))
hr_reserve = float(max_heart_rate - resting_hr)
hr_zones = {}
zone_num = 0
perc_low = .4
perc_high = .5

while zone_num <= 5:
    zone_num += 1
    perc_low += .1
    perc_high += .1
    hr_zones[zone_num] = (round(float((resting_hr + (hr_reserve*perc_low))), 3), round(float((resting_hr + (hr_reserve*perc_high))), 3))

print(f"Your heart rate reserve is: {round(hr_reserve, 3)} bpm")

print("Here is a breakdown of your training zones: ")
