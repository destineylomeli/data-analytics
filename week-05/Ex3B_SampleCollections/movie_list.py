movies = [
    "Spider-Man",
    "Coraline",
    "Madagascar",
    "Friday"
]

# Description statement 
print(f"The list movies includes my top {len(movies)} favorite movies")

# Print full list
print(movies)

# Using sorted()
print(sorted(movies))

# Original list again
print(movies)

# Using .sort()
movies.sort()

# List after .sort()
print(movies)

# sorted() temporarily sorts the list
# .sort() permanetly changes the list order

# Add another movie
movies.append("13 going 30")

# Updated description 
print(f"The list movies include my top {len(movies)} favorite movies")

# Updated list
print(movies)