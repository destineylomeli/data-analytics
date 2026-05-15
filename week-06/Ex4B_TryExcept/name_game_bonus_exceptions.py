while True:

    try:

        user_name = input("Enter your name: ")

        if user_name == "":
            raise ValueError("Input cannot be empty.")
        
        if user_name.isdigit():
            raise TypeError("Numbers are not valid names.")
        
        if len(user_name) == 1:
            raise ValueError("Name is too short.")
        
        print(f"Hello, {user_name}!")

        break

    except ValueError as ve:
        print("ValueError:", ve)

    except TypeError as te:
        print("TypeError:", te)

    finally:
        print("Try entering another name.\n")

# =========================================================================
# Question 2A Answer
# =========================================================================

# Yes, some inputs may seem invalid but still work if the program does not
# specifically check for them. 
#
# Logic that can help:
# - if statements
# - len()
# - isdigit()
# - isnumeric()
# - try/except blocks


# ==========================================================================
# Question 2B Answer
# ==========================================================================

# ValueError occurrs when:
# - the input is empty
# - the name is too short
#
# TypeError occurts when: 
# - numbers are entered instead of letters
#
# These exceptions occur in the try block during input validation. 


# ==========================================================================
# CHALLENGE ANSWERS
# ==========================================================================

# Raise SystemExit() completely stops the program.
# It can be used instead of break when you want to fully exit the script.
# Unexpected results can happen if important code after it never runs.
