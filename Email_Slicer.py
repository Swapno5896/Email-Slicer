user_input = input('Enter Email Adderss : ').strip()
user_name = user_input[:user_input.find('@')]
domain_name = user_input[user_input.find('@')+1:]
print(f"user name is {user_name} and domain name is {domain_name}")