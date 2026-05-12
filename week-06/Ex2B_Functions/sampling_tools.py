import random

products = [
    'Laptop',
    'Monitor',
    'Keyboard',
    'Mouse',
    'Webcam',
    'Headset',
    'Docking Station',
    'USB Hub',
    'Desk Lamp',
    'Surge Protector'
]

# Product of the Day
product_day = random.choice(products)
print(f"Product of the Day: {product_day}")

# 3 products for survey
survey_products = random.sample(products, 3)
print(f"Survey products: {survey_products}")

# Shuffle products
random.shuffle(products)
print(f"Shuffled products: {products}")

# Random transaction count
transactions = random.randint(50, 300)
print(f"Daily transaction count: {transactions}")