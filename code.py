import random
import string  

def generate_password(length):
    
    letters = string.ascii_letters                    #gives letters
    digits = string.digits                            #gives numbers
    punctuation = string.punctuation                  #gives symbols
    characters = letters + digits + punctuation  
    '''#RANDOM PASSWORD
    password_list = []
    for _ in range(length):
        random_character = random.choice(characters)
        password_list.append(random_character)

    return ''.join(password_list)'''

    #1st character should be a letter
    password_list = []
    password_list.append(random.choice(letters))
    for _ in range(1,length):
        random_character = random.choice(characters)
        password_list.append(random_character)

    return ''.join(password_list)

    #1st character should be a upper case letter=> random.choice(letters).upper()
    #1st character should be a lower case letter=> random.choice(letters).lower()

if __name__ == "__main__":
    password_length = 8
    generated_password = generate_password(password_length)

    print(f"Generated Password: {generated_password}")
