"""This file contains the program \"training_zones.py\", which takes in user info and
outputs health information bout their heart rate."""

def main():
    """The intent of this function is to take a user's age and resting heart rate,
    and output their rate reserve, and their training zone breakdown"""

    age = float(input("Please enter your age: "))
    resting_hr = float(input("Please enter your resting heart rate: "))
    print("===============================================")

    max_heart_rate = float(208 - (0.7 * age))
    hr_reserve = float(max_heart_rate - resting_hr)
    hr_zones = {}
    zone_num = 0
    perc_low = .4
    perc_high = .4999
    #interesting thing happened w/ "perc_high" value. if it is set to .499 (one less 9 than
    #current value), the resulting boundaries between ranges are grater than 0.01, and if
    #you set that value to 0.49999 (one more 9 than current value), then the boundaries
    #between ranges are non-existent. i'm very curious.

    while zone_num <= 4:
        zone_num += 1
        perc_low += .1
        perc_high += .1
        if zone_num == 4:
            perc_high += .0001
        hr_zones[zone_num] = (round(float((resting_hr + (hr_reserve*perc_low))), 2),
        round(float((resting_hr + (hr_reserve*perc_high))), 2))

    print(f"Your heart rate reserve is: {round(hr_reserve, 2)} bpm")
    print("Here is a breakdown of your training zones: ")
    zone_num = 1
    hr_index = 1
    for _ in range(len(hr_zones)):
        print(f"Zone {zone_num}: {hr_zones[hr_index][0]} to {hr_zones[hr_index][1]} bpm")
        zone_num += 1
        hr_index += 1


main()
