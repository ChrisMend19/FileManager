import tkinter as tk
from tkinter import filedialog, Text, Label, ttk, font, Scrollbar, Listbox, END
from ttkthemes import ThemedTk
import os # maybe import fileManager
import shutil

# todo:
# printDesktopItems function finsish

def main():
    print("main")

# def addApp():
#     for widget in frame_currentfiles.winfo_children():
#         widget.destroy()
#     # fix right here changed exe to applications cause mac doesnt use exe
#     filename = filedialog.askopenfile(initialdir=os.getcwd(), title="Select File", filetypes=(("files", "*.*"), ("all files", ".*")))
#     apps.append(filename)
#     #print(filename)
#     for app in apps:
#         app = tk.Label(frame_currentfiles, text=app.name, font=(None, 10), bg="grey").pack()

def printDesktopItems(files,h): # 6 columns fit
    rowCounter = 0
    colCounter = 0
    for file in files:
        if rowCounter == 10:
            rowCounter = 0
            colCounter += 1
        if colCounter == 6:
            colCounter = 0
            rowCounter 
        fileBut = tk.Button(frame_currentfiles, text=file, fg="white", highlightbackground="grey") # figure out to allign files
        fileBut.grid(row=rowCounter,column=colCounter)
        rowCounter += 1

def click(event):
    for i in myList.curselection(): #clicked is not defined for some reason
        print(myList.get(i))
    #     selectedFiles.append(i)
    # print(selectedFiles)
    # widget = event.widget
    # # print(widget.curselection())
    # index = int(widget.curselection()[0])
    # value = widget.get(index)
    # print(value)

def moveBackDirectory():
    os.chdir("..")
    currentDir.config(text=os.getcwd())

    files = os.listdir(os.getcwd())
    files = sorted(files)
    myList.delete(0, END)
    for file in files:
        myList.insert(END, file)
        if os.path.isdir(file):
            myList.itemconfig(END, {'fg': 'blue'})

# Intializing Root
root = tk.Tk()
root.resizable(False, False)
root.geometry('{}x{}'.format(700, 700))

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Themes
theme = ttk.Style(root) # idk if its actually doing anything
theme.theme_use('classic')

# Fonts
directoryFont = font.Font(family='Lucida Grande', name='appDirectoryFont', size=12)

# Data
apps = []
currentPath = os.getcwd()
files = os.listdir(currentPath)
files = sorted(files)

# Canvas
# canvas = tk.Canvas(root, height=700, width=700, bg="#393939")
# canvas.grid()

# Menu Bar
frame_directory = tk.Frame(root, bg="#535353", width=600, height=20, padx=0)
frame_directory.grid(row=0, column=0, pady=20, sticky = "n")

# frame_directory_background = tk.Frame(root, bg="#535353", width=600, height=20, padx=0)
# frame_directory_background.grid(row=0, column=0, pady=20, sticky = "n")

# Directory Buttons
frame_directory_prevButton = tk.Frame(root, bg="black", width=30, height=20)
frame_directory_prevButton.grid(row=0, column=0, padx=(0,640), pady=20, sticky = "n")

frame_directory_nextButton = tk.Frame(root, bg="black", width=30, height=20)
frame_directory_nextButton.grid(row=0, column=0, padx=(640,0), pady=20, sticky = "n")

backDirectory = tk.Button(frame_directory_prevButton, text="<--", fg="white", highlightbackground="#535353", command=moveBackDirectory)
backDirectory.grid(row=0, column=0)

nextDirectory = tk.Button(frame_directory_nextButton, text="-->", fg="white", highlightbackground="#535353")
nextDirectory.grid(row=0, column=0)

# Directory Text
currentDir = tk.Label(frame_directory, text=currentPath, font=directoryFont, bg="#535353", fg="white")
currentDir.grid(row=0, column=0)

# Display Files Container
frame_currentfiles = tk.Frame(root, bg="#535353", width=600, height=200, padx=0)
frame_currentfiles.grid(row=0, column=0, pady=75, sticky = "n")

# Scroll Bar
scroll_bar = Scrollbar(frame_currentfiles, orient='vertical')
scroll_bar.grid(row=0, column=1, sticky="ns")

# List of Files
myList = Listbox(frame_currentfiles, yscrollcommand = scroll_bar.set)
myList.grid(row=0, column=0)
myList.bind('<ButtonRelease-1>', click)
scroll_bar.config(command=myList.yview)
for file in files:
    myList.insert(END, file)
    if os.path.isdir(file):
        myList.itemconfig(END, {'fg': 'blue'})
    
selectedFiles = []

# Display Selected Files Container
frame_selectedfiles = tk.Frame(root, bg="#535353", width=600, height=200, padx=0)
frame_selectedfiles.grid(row=0, column=0, pady=375, sticky = "n")

# Scroll Bar of Selected Files
scroll_bar = Scrollbar(frame_selectedfiles, orient='vertical')
scroll_bar.grid(row=0, column=1, sticky="ns")

# List of Selected Files
myList = Listbox(frame_selectedfiles, yscrollcommand = scroll_bar.set)
myList.grid(row=0, column=0)
# myList.bind('<ButtonRelease-1>', click)
scroll_bar.config(command=myList.yview)
for file in selectedFiles:
    myList.insert(END, file)
    if os.path.isdir(file):
        myList.itemconfig(END, {'fg': 'blue'})

# printDesktopItems(files,0) # work here

# frame_selectedfiles = tk.Frame(root, bg="#535353")
# frame_selectedfiles.place(relwidth=0.96,relheight=0.43,relx=0.02,rely=0.555) # once alligned set to variables 

# openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", highlightbackground="grey", command=addApp).pack()
# runApp = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", highlightbackground="grey").pack()

# print(currentPath)
root.mainloop()

if __name__ == "__main__":
    main()