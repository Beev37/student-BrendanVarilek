import math

angle = float(input("Woah what kind of angle is that (in degrees): "))
cos = math.cos(math.radians(angle))
sin = math.sin(math.radians(angle))
print(f"The cosine of {angle} is {cos}.")
print(f"The sine of {angle} is {sin}.")