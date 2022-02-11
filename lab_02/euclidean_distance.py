def main():
    import math

    n = 0
    coords = {}
    while True:
        n += 1
        if n == 1:
            coords["x1"] = float(input("Enter value for x1: "))
        elif n == 2:
            coords["x2"] = float(input("Enter value for x2: "))
        elif n == 3:
            coords["y1"] = float(input("Enter value for y1: "))
        elif n == 4:
            coords["y2"] = float(input("Enter value for y2: "))
        else:
            break


    distance = round(math.sqrt(((coords["x2"]-coords["x1"])**2)+((coords["y2"]-coords["y1"])**2)), 3)

    print(distance)
    return distance

main()