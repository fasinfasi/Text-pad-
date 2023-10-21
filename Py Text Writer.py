from tkinter import *
from tkinter import filedialog

def submit(): 
    input = text.get("1.0",END)
    print(input)
    
def save_file():
    # open file for save text
    file_save = filedialog.asksaveasfile( defaultextension='.txt',
                                         filetypes=[
                                             ("Text file",".txt"),
                                             ("HTML",".html"),
                                             ("All files",".*")])
                                        
    
    
    filetext = str(text.get(1.0,END))
    file_save.write(filetext)
    
def openfile():
    # open file when click open file button
    file_path = filedialog.askopenfilename(title="My file details",
                                           filetypes=(("text files","*.txt"),
                                                      ("All files","*.*")))
                                          
    print(file_path)
    file = open(file_path,'r') #File reading command 
    print(file.read()) #Display content of that selected file
    file.close()

window = Tk()
text = Text(window,
            bg="Light yellow",
            fg="purple",
            font=("Ink free",25),
            width=20,
            height=8,
            padx=20,
            pady=20
            )
            
text.pack()

button_submit = Button(window, text="Submit", command=submit)
button_submit.pack()

button_save = Button(window, text="Save", command=save_file)
button_save.pack()

button_file = Button(window, text="Open File", command=openfile)
button_file.pack()

window.mainloop()