import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

# starting code
win = tk.Tk()
win.title("gui")
# widgets = label, buttons, radio buttons



# create label
name_label = ttk.Label(win, text="enter your name : ")
name_label.grid(row=0, column=0, sticky=tk.W)
# pack, grid

email_label = ttk.Label(win, text="enter your email : ")
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(win, text="enter your age : ")
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text="select your gender : ")
gender_label.grid(row=3, column=0, sticky=tk.W)



# create entry box
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=16, textvariable=name_var)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=16, textvariable=email_var)
email_entrybox.grid(row=1, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=16, textvariable=age_var)
age_entrybox.grid(row=2, column=1)



# create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=14, textvariable=gender_var, state='readonly')
gender_combobox['value']= ('--SELECT--','Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)



# radio button
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win, text="student", value='student', variable=usertype)
radiobtn1.grid(row=4, column=0)

radiobtn2 = ttk.Radiobutton(win, text="teacher", value='teacher', variable=usertype)
radiobtn2.grid(row=4, column=2)



# check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text="check if you want to subscribe to our newsletter", variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)



# create button
# def action():
#     username = name_var.get()
#     user_email = email_var.get()
#     userage = age_var.get()
#     user_gender = gender_var.get()
#     user_type = usertype.get()
#     if checkbtn_var.get() == 0:
#         subscribed = 'Not Subscribed'
#     else:
#         subscribed = 'Subscribed'

#     with open('file.txt', 'a') as f:
#         f.write(f'{username},{user_email},{userage},{user_gender},{user_type},{subscribed}\n')

#     name_entrybox.delete(0 , tk.END)
#     email_entrybox.delete(0 , tk.END)
#     age_entrybox.delete(0 , tk.END)




# write to csv
def action():
    username = name_var.get()
    user_email = email_var.get()
    userage = age_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subscribed = 'No'
    else:
        subscribed = 'Yes'

    # write to csv
    with open('file.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['Username', 'Email', 'Age', 'Gender', 'Type', 'Subscription'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'Username':username,
            'Email':user_email,
            'Age':userage,
            'Gender':user_gender,
            'Type':user_type,
            'Subscription':subscribed
        })

    name_entrybox.delete(0 , tk.END)
    email_entrybox.delete(0 , tk.END)
    age_entrybox.delete(0 , tk.END)


submit_button = ttk.Button(win, text="Submit", command=action)
submit_button.grid(row=6, column=0, sticky=tk.W)




win.mainloop()