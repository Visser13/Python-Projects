import random
import tkinter as tk
from tkinter import filedialog

def main():

    lowercase_list = generate_lowercase_letters()
    uppercase_list = generate_uppercase_letters()
    nummber_list = generate_number()

    lowercase_upper = len(lowercase_list)
    uppercase_upper = len(uppercase_list)
    nummber_upper = len(nummber_list)

    password_length = 12
    password_amount = 1000
    password_list = []

    password_count = 0

    while password_count < password_amount:

        password = ""
        random_number = 0
        char_count = 0

        while char_count < password_length:
            random_number = int(random.randrange(1,100))
        
            if random_number < 33:
                password = password + lowercase_list[random.randrange(1,lowercase_upper)]
            elif random_number > 66:
                password = password + uppercase_list[random.randrange(1,uppercase_upper)]
            else:
                password = password + nummber_list[random.randrange(1,nummber_upper)]        
            
            char_count += 1

        password_count += 1
        password_list.append(password)
    
    folder_path = "passwords.txt"
    save(folder_path, password_list)
    

def select_folder_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askdirectory(title="Select a folder.")
    return file_path

def save(path, string_list):
    f = open(path, "w")
    count = 0
    while count < len(string_list):
        f.write(string_list[count])
        f.write("\n")
        count += 1
    f.close

def generate_lowercase_letters ():
    result = ["a","b","c","d","e","f","g","h","i","j","k","m","n","p","q","r","s","t","u","v","w","x","y","z"]
    return result

def generate_uppercase_letters ():
    result = ["A","B","C","D","E","F","G","H","J","K","L","M","N","P","Q","R","S","T","U","V","W","X","Y","Z"]
    return result

def generate_number ():
    result = ["1","2","3","4","5","6","7","8","9","0"]
    return result


main()
