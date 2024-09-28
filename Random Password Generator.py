import random
import string

def generate_random_password(length=12):
    # Define the character set
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    
    # Combine all characters
    all_characters = lower + upper + digits
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    # Shuffle the password
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)
    
    return shuffled_password

# Generate a password
password_length = 12  # You can change the length here
random_password = generate_random_password(password_length)
print("Generated Password:", random_password)
