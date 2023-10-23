from tkinter import * 
from tkinter import messagebox 
root=Tk()

root.title("Cardiovascular Checkup")
root.geometry("600x600")

q1 = Label(root, text = "Do you experience shortness of breath during routine activities")
q1.pack()
q1_choice = StringVar(value="0")

q1_yes_button = Radiobutton(root, text="Yes", Variable= q1_choice , value = "yes") 
q1_yes_button.pack()

q1_no_button = Radiobutton(root, text="No", Variable= q1_choice , value = "no") 
q1_no_button.pack()


q2 = Label(root, text = "Do you feel any of these symptoms - confusion, disorientation or loss of memory?")
q2.pack()
q2_choice = StringVar(value="0")

q2_yes_button = Radiobutton(root, text="Yes", Variable= q2_choice , value = "yes") 
q2_yes_button.pack()

q2_no_button = Radiobutton(root, text="No", Variable= q2_choice , value = "no") 
q2_no_button.pack()


q3 = Label(root, text = "Do you experience shortness of breath while at rest or laying down?")
q3.pack()
q3_choice = StringVar(value="0")

q3_yes_button = Radiobutton(root, text="Yes", Variable= q3_choice , value = "yes") 
q3_yes_button.pack()

q3_no_button = Radiobutton(root, text="No", Variable= q3_choice , value = "no") 
q3_no_button.pack()



root.mainloop()
