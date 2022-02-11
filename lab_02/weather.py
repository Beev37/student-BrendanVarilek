#What is the difference between the highest and the lowest temperature values predicted
#   for the 10 day forecast? 
high_temp_10day = int(55)
low_temp_10day = int(35)
maxmindelta_10day = int(high_temp_10day - low_temp_10day)
print("The difference between the highest and lowest temperatures over the 10 day forecast was: ", maxmindelta_10day, "F")

#What is the average temperature at noon predicted for the 10 day forecast?
noon_temps_10day = [47, 46, 48, 47, 48, 44, 46, 46, 47, 47]

sum_temp = 0
for temp in noon_temps_10day:
    sum_temp += temp

avg_temp_10day = sum_temp/10

print("Average temperature at noon, across the 10 day forecast is: ", avg_temp_10day, "F")

#What is the highest temperature predicted for the 10 day forecast, converted from Fahrenheit to Celcius?
def f2c (Fahrenheit):
    Celc = (5/9)*(float((Fahrenheit - 32)))
    return round(Celc, 2)

def find_highest_temp (temp_list):
    temp_list.sort()
    high_temp = float(temp_list[-1])
    return high_temp

outcome = int(find_highest_temp(noon_temps_10day))

Highest_temp_10day_C = f2c(find_highest_temp(noon_temps_10day))

print("The highest temperature predicted for the 10 day forecast in Celcius is: ", Highest_temp_10day_C, "C")
