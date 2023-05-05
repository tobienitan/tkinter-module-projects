from tkinter import *
from tkinter import messagebox # this is not a class in the tkinter module
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint, choice, shuffle
import string
def generate_password():
    join_letters = str(string.ascii_lowercase + string.ascii_uppercase )
    print(join_letters)
    letters = []
    letters[:0] = join_letters

    join_number = '0123456789'
    numbers = []
    numbers[:0] = join_number

    join_symbol = "!£$%^&*+"
    symbols = []
    symbols[:0] = join_symbol

    password_letters = [choice(letters) for let in range(randint(4, 8))]

    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_symbols = [choice(symbols) for sym in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    password2 = ''.join(password_list)
    password_entry.insert(0, password2)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }


    if len(website) == 0 or  len(password) == 0:
        messagebox.showinfo(title='Oops', message='sorry must have an entry') #brings out a pop up
    else:
        try:
             entity = open('data.json', "r")

        except FileNotFoundError:
            with open('data.json', 'w') as entity: # open in write mode creates a file if it doesnot exist
                json.dump(new_data, entity, indent=4)  # to write data
                #reading old data
        else:
            data = json.load(entity)  # what this line does is it loads the json data and converts it to a python dictionary
            #updating old data with new data
            data.update(new_data)
            entity.close()

            with open('data.json', 'w') as entity:
                #saving the updated data
                json.dump(data, entity, indent=4)

        finally:
           website_entry.delete(0, END)
           password_entry.delete(0, END)

# ------------------------- FIND PASSWORD -------------------------------#

def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as entity:
            data = json.load(entity)
    except FileNotFoundError:
            messagebox.showinfo(title='Error!', message='file not found')
    else:
         if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\n password: {password}')
         else:
             messagebox.showinfo(title='Sorry', message=f'website: {website} does not exit in database')




# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, width=200, height=200)

canvas = Canvas(width=200, height=200, highlightthickness=0)  # we create canvas using the canvas widget
logo_img = PhotoImage(file='logo.png')  # to load image
canvas.create_image(100, 100, image=logo_img)  # to add an image to the canvas 100 and 100 are image positions
canvas.grid(row=0, column=1)

website_text = Label(text='Website:')
website_text.grid(row=1, column=0)

email_username_text = Label(text='Email/Username:')
email_username_text.grid(row=2, column=0)

password_text = Label(text='Password:')
password_text.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()  # makes the cursor appear in the entry automatically

email_username_entry = Entry(width=35)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, 'enitanoluwatobidamilare@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=3, column=2)

search_button = Button(text='Search', command=find_password)
search_button.grid(row=1, column=2)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()

