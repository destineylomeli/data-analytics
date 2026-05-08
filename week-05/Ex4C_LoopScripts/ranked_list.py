foods = ["Tacos", "Ramen", "Jerk Chicken", "Injera", "Pierogi"]

for index, food in enumerate(foods, start=1):

    if index == 1:
        print(index, ".", food, "<- top pick!", sep="")
    else:
        print(index, ".", food, sep="")
    
# Bonus: Reverse Order
foods = ["Tacos", "Ramen", "Jerk Chicken", "Injera", "Pierogi"]

for index, food in enumerate(reversed(foods), start=1):
    print(index, ".", food, sep="")
