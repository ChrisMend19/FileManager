import tkinter as tk
from tkinter import filedialog, Text
import os # maybe import fileManager

def main():
    addApp()

root = tk.Tk()
root.resizable(False, False)

apps = []

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()
    # fix right here changed exe to applications cause mac doesnt use exe
    filename = filedialog.askopenfile(initialdir=os.getcwd(), title="Select File", filetypes=(("files", "*.*"), ("all files", ".*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        app = tk.Label(frame, text=app.name, font=(None, 10), bg="grey").pack()



canvas = tk.Canvas(root, height=700, width=700, bg="#263D42").pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9,relheight=0.825,relx=0.05,rely=0.05)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", highlightbackground="#263D42", command=addApp).pack()
runApp = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", highlightbackground="#263D42").pack()

root.mainloop()

if __name__ == "__main__":
    main()