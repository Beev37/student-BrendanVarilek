import zoneinfo


age = float(input("Please enter your age: "))
resting_hr = float(input("Please enter your resting heart rate: "))
print("===============================================")

max_heart_rate = float(208 - (0.7 * age))
hr_reserve = float(max_heart_rate - resting_hr)
hr_zones = {}
zone_num = 0
perc_low = .4
perc_high = .499999999

while zone_num <= 5:
    zone_num += 1
    perc_low, perc_high += .1
    hr_zones[zone_num] = ((float((resting_hr + (hr_reserve*perc_low))), float((resting_hr + (hr_reserve*perc_high)))))

print(f"Your heart rate reserve is: {hr_reserve} bpm")
print("Here is a breakdown of your training zones: ")
