# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# Print original values and types
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

# Integer conversions 
# int_a = int(a)  # ValueError
int_b = int(b)

# int_c = int(c)  # ValueError
# int_d = int(d)  # ValueError

print(int_b, type(int_b))

# Float conversions
float_a = float(a)
float_b = float(b)

# float_c = float(c)  # ValueError
# float_d = float(d)  # ValueError

print(float_a, type(float_a))
print(float_b, type(float_b))

# Convert a into float then integer
a_int = int(float(a))

print(a_int, type(a_int))

# Slicing numeric portions
c_number = int(c[:3])
d_number = int(d[-2])

print(c_number, type(c_number))
print(d_number, type(d_number))

# Strip spaces
print(a.strip())
print(d.strip())