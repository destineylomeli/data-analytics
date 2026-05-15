f = open("about_me.txt", "r")

print("FULL FILE:\n")
print(f.read())

f.close()

# ---------------------------------------------------------------------
# READ(50) 
# ---------------------------------------------------------------------

f = open("about_me.txt", "r")

print("\nFIRST 50 CHARACTERS:\n")
print(f.read(50))

print("\nNEXT 50 CHARACTERS:\n")
print(f.read(50))

f.close()

# The second read(50) continues reading where the first one stopped.

# ------------------------------------------------------------------------
# READLINE()
# ------------------------------------------------------------------------

f = open("about_me.txt", "r")

print("\nREADLINE EXAMPLES:\n")

print(f.readline(10))
print(f.readline())

for i in range(1, 5):
    print(f.readline())

f.close()

# Readline() reads one line at a time.
# Readline(10) only reads the first 10 characters.

# -------------------------------------------------------------------------
# READLINES()
# -------------------------------------------------------------------------

f = open("about_me.txt", "r")

print("\nREADLINES EXAMPLES:\n")

print(f.readlines(1))

f.seek(0)

print(f.readlines(10))

f.seek(0)

print(f.readlines(100))

f.seek(0)

print(f.readlines(-1))

f.close()

# Readlines() stores the lines in a list.
# Readlines(100) reads about 100 characters worth of lines.
# Readlines(-1) reads the entire file.

# ----------------------------------------------------------------------------------
# VARIABLES
# ----------------------------------------------------------------------------------

f = open("about_me.txt", "r")

# first variable
first_var = f.read(50)

# second variable
second_var = []

for i in range(1, 5):
    second_var.append(f.readline())

# third variable
third_var = f.readlines(100)

print("\nSTEP 16 OUTPUT:\n")

print("First 50 characters:")
print(first_var)

print("\nNext four lines, as list by line:")
print(second_var)

print("\n Next 100 characters, as list by line:")
print(third_var)

f.close()