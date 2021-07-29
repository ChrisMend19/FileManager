import tkinter as tk
from tkinter import filedialog, Text, Label, ttk, font, Scrollbar, Listbox, END
from ttkthemes import themed_tk as tkk
import os # maybe import fileManager
import shutil

# todo: test out app for bugs

# Mouse Pressed
def click(event):
    for i in myList.curselection():
        global selectedFile # probably remove global, but it works for now
        selectedFile = myList.get(i)
        if (myList.get(i),os.getcwd()) not in selectedFiles and os.path.isfile(myList.get(i)):
            selectedFiles.append((myList.get(i),os.getcwd()))
   
    if myList.get(i) not in myList2.get(0, tk.END) and selectedFile:
        if os.path.isfile(selectedFile):
            myList2.insert(END, selectedFile)

def clickRemove(event):
    for i in myList2.curselection():
        global selectedFileRemove
        selectedFileRemove = myList2.get(i)

def moveBackDirectory():
    os.chdir("..")
    currentDirectory = currentDir.cget("text")
    currentDirectoryList = currentDirectory.split('/')
    lastDir = "/" + currentDirectoryList[-1]
    directoryUpTo162 = len(os.getcwd()[162:].split("/"))
    if directoryUpTo162 > 10:
        change = False # only used to skip elif and else
    elif lastDir == "/." and currentDirectory.count("/.") > 0:
        currentDirectory = currentDirectory[:-2]
    else:
        currentDirectory = currentDirectory.replace(lastDir,"")
    currentDir.config(text=currentDirectory)

    files = os.listdir(os.getcwd())
    files = sorted(files)
    myList.delete(0, END)
    for file in files:
        myList.insert(END, file)
        if os.path.isdir(file):
            myList.itemconfig(END, {'fg': 'blue'})

def moveForwardDirectory():
    currentDirectory = currentDir.cget("text")
    
    if selectedFile and os.path.isdir(selectedFile):
        moveDirectory = currentDirectory + "/" + selectedFile
        if "\n" not in selectedFile:
            changeMoveDir = moveDirectory.replace("\n","")
            changeMoveDir = changeMoveDir.replace(".","") # 
        os.chdir(os.getcwd() + "/" + selectedFile)
        if len(moveDirectory) > 76 and "\n" not in moveDirectory: # add new lines if neccessary
            moveDirectory += "\n"
        elif len(moveDirectory) > 162 and moveDirectory.count("/.") < 11:
            moveDirectory = moveDirectory.replace(selectedFile, "")
            moveDirectory += "."
        elif len(moveDirectory) > 162 and moveDirectory.count("/.") >= 11:
            moveDirectory = moveDirectory.replace("/" + selectedFile, "")
        currentDir.config(text=moveDirectory)
        files = os.listdir(os.getcwd())
        files = sorted(files) # possibly move into function to clean up. used in move back directory
        myList.delete(0, END)
        for file in files:
            myList.insert(END, file)
            if os.path.isdir(file):
                myList.itemconfig(END, {'fg': 'blue'})
    elif selectedFile and os.path.isfile(selectedFile):
        print("File selected, Select Folder")
    else:
        print("No Folder Selected")

def removeSelectedFile():
    for file in selectedFiles:
        if selectedFileRemove == file[0]:
            idx = myList2.get(0, tk.END).index(selectedFileRemove)
            myList2.delete(idx)
            selectedFiles.remove((file[0],file[1]))

def moveFiles():
    moveDirectory = os.getcwd()
    
    if selectedFiles:
        for i in range(len(selectedFiles)):
            fileCurrentDirectory = selectedFiles[0][1] + "/" + selectedFiles[0][0] # moving first file
            fileMoveDirectory = moveDirectory + "/" + selectedFiles[0][0] 
            noDuplicateBool = checkForDuplicates(moveDirectory, selectedFiles[0][0])
            if noDuplicateBool:
                os.rename(fileCurrentDirectory,fileMoveDirectory)
                selectedFiles.remove(selectedFiles[0]) #removing first file
            else:
                print("Duplicate File Name")
                selectedFiles.clear()
        files = os.listdir(os.getcwd())
        files = sorted(files)
        myList.delete(0, END)
        for file in files:
            myList.insert(END, file)
            if os.path.isdir(file):
                myList.itemconfig(END, {'fg': 'blue'})
        myList2.delete(0, END)
        selectFile = None

def checkForDuplicates(moveDirectory,movedFile):
    currentFiles = os.listdir(moveDirectory)
    for file in currentFiles:
        if file == movedFile:
            return False
    return True

def showDirectories(): 
    # print(selectedFiles)
    myList2_List = myList2.get(0, tk.END)
    if myList2_List:
        if myList2_List[0] == selectedFiles[0][0]:
            myList2.delete(0, END)
            for file in selectedFiles:
                direct = file[1] + "/" + file[0]
                myList2.insert(END,direct)
        else:
            myList2.delete(0, END)
            for file in selectedFiles:
                myList2.insert(END,file[0])

# Intializing Root
root = tk.Tk()
root.resizable(False, False)
root.geometry('{}x{}'.format(700, 700))

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Themes
# theme = ttk.Style(root) 
# theme.theme_use('classic')
# window = tkk.ThemedTk()
# window.get_themes()
# window.set_theme("plastik")

# Fonts
directoryFont = font.Font(family='Lucida Grande', name='appDirectoryFont', size=12)

# Data
apps = []
currentPath = os.getcwd()
files = os.listdir(currentPath)
files = sorted(files)
selectedFile = None
selectedFileRemove = None

# Canvas
canvas = tk.Canvas(root, height=700, width=700, bg="white") # for some reason remove doesnt show with root
canvas.grid()

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

nextDirectory = tk.Button(frame_directory_nextButton, text="-->", fg="white", highlightbackground="#535353", command=moveForwardDirectory)
nextDirectory.grid(row=0, column=0)

# Directory Text
currentDir = tk.Label(frame_directory, text=currentPath, font=directoryFont, bg="#535353", fg="white")
currentDir.grid(row=0, column=0)

# Selected Files Text
selectFiles = tk.Label(root, text="Selected Files", font=directoryFont, bg="#535353", fg="white")
selectFiles.grid(row=0, column=0, pady=(0,240))

# Display Files Container
frame_currentfiles = tk.Frame(root, bg="#535353", width=600, height=200, padx=0)
frame_currentfiles.grid(row=0, column=0, pady=75, sticky = "n")

# Scroll Bar
scroll_bar = Scrollbar(frame_currentfiles, orient='vertical')
scroll_bar.grid(row=0, column=1, sticky="ns")

# List of Files
myList = Listbox(frame_currentfiles, yscrollcommand = scroll_bar.set)
myList.grid(row=0, column=0)
myList.bind('<ButtonRelease-1>', click) # click function
scroll_bar.config(command=myList.yview)
for file in files:
    myList.insert(END, file)
    if os.path.isdir(file):
        myList.itemconfig(END, {'fg': 'blue'})
    
selectedFiles = [] # 

# Display Selected Files Container
frame_selectedfiles = tk.Frame(root, bg="#535353", width=600, height=200, padx=0)
frame_selectedfiles.grid(row=0, column=0, pady=375, sticky = "n")

# Scroll Bar of Selected Files
scroll_bar = Scrollbar(frame_selectedfiles, orient='vertical')
scroll_bar.grid(row=0, column=1, sticky="ns")

# List of Selected Files
myList2 = Listbox(frame_selectedfiles, yscrollcommand = scroll_bar.set)
myList2.grid(row=0, column=0)
myList2.bind('<ButtonRelease-1>', clickRemove) # click function
scroll_bar.config(command=myList2.yview)
# for file in selectedFiles:
#     myList2.insert(END, file)
#     if os.path.isdir(file):
#         myList2.itemconfig(END, {'fg': 'blue'})

# print selected files. Temp function to test functionality
frame_print_selected_files = tk.Frame(canvas, bg="black", width=100, height=20)
frame_print_selected_files.grid(row=0, column=0, sticky = "s")

removeDirectory = tk.Button(frame_print_selected_files, text="Show Directories", fg="white", highlightbackground="#535353", command=showDirectories)
removeDirectory.grid(row=0, column=0)

# Remove Button
frame_directory_removeButton = tk.Frame(canvas, bg="black", width=100, height=20)
frame_directory_removeButton.grid(row=0, column=0, padx=(0,490), pady=(415,0), sticky = "s")

removeDirectory = tk.Button(frame_directory_removeButton, text="Remove from Selected Files", fg="white", highlightbackground="#535353", command=removeSelectedFile)
removeDirectory.grid(row=0, column=0)

# Move Button
frame_directory_moveButton = tk.Frame(canvas, bg="black", width=100, height=20)
frame_directory_moveButton.grid(row=0, column=0, padx=(595,0), pady=(415,0), sticky = "s")

moveDirectory = tk.Button(frame_directory_moveButton, text="Move Files", fg="white", highlightbackground="#535353", command=moveFiles)
moveDirectory.grid(row=0, column=0)

root.mainloop()

