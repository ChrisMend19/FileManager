# def addApp():
#     for widget in frame_currentfiles.winfo_children():
#         widget.destroy()
#     # fix right here changed exe to applications cause mac doesnt use exe
#     filename = filedialog.askopenfile(initialdir=os.getcwd(), title="Select File", filetypes=(("files", "*.*"), ("all files", ".*")))
#     apps.append(filename)
#     #print(filename)
#     for app in apps:
#         app = tk.Label(frame_currentfiles, text=app.name, font=(None, 10), bg="grey").pack()

# def printDesktopItems(files,h):
#     rowCounter = 0
#     colCounter = 0
#     for file in files:
#         if rowCounter == 10:
#             rowCounter = 0
#             colCounter += 1
#         if colCounter == 6:
#             colCounter = 0
#             rowCounter 
#         fileBut = tk.Button(frame_currentfiles, text=file, fg="white", highlightbackground="grey") # figure out to allign files
#         fileBut.grid(row=rowCounter,column=colCounter)
#         rowCounter += 1
