import random
import string

valid_input = False

while not valid_input:
    user_input = input("What is the number of ec2 instances you want to create names for?")
    
    if user_input.isdigit():
        name_quantity = int(user_input)
        valid_input = True
        
    else:
        print("Please enter a valid number.")
        
department_name = input("What is your department?")

for _ in range(name_quantity):
    random_chars = ' '.join(random.choices(string.ascii_letters, k=5))
    random_numbers = random.randint(100, 500)
    random_id = f'{department_name} {random_chars} {random_numbers}'
    print(random_id)
    