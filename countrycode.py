# Dictionary containing country names and their codes
SPCMcountry_code = {
    'India': '0091',
    'Australia': '0025',
    'Nepal': '00977'
}

# Search dictionary for country code of India
print("Country code for India -")
print(SPCMcountry_code.get('India', 'Not Found'))

# Search dictionary for country code of Japan
print("Country code for Japan -")
print(SPCMcountry_code.get('Japan', 'Not Found'))