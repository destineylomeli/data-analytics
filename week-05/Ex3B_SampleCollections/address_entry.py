contact_info = {
    "name": "Lewis Gaby",
    "address": "123 Main Street",
    "city": "San Jose",
    "state": "CA",
    "zip": "45678"
}

# Print formatted address
print(f"""
{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

# Remove name
del contact_info["name"]

# Create full_name dictionary
full_name = {
    "first name": "Lewis",
    "last name": "Gaby"
}

# Add honorific
full_name.update({
    "honorific": "Mr."
})

# Add full_name to contact_info
contact_info.update({
    "full_name": full_name 
})


# Print updated address
print(f"""
{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']}{contact_info['zip']}
""")