import math

length = float(input("Enter room length in feet: "))
width = float(input("Enter room width in feet: "))

area = length * width

# Add 10% extra tiles
total_tiles_needed = area * 1.10

# 12 tiles per box
boxes_needed = math.ceil(total_tiles_needed / 12)

print(f"You need {boxes_needed} boxes of tiles.")