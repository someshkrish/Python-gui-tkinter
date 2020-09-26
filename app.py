import tkinter as tk
from tkinter import filedialog, Text
import os
import subprocess, sys

# creates GUI
root = tk.Tk()
apps = []

# This is to create a text file to store the apps which we have chosen
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

# Function to add apps
def addApp():
    # this for loop destroy the previously added apps in the list and starts the list from first
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir="/", title="Select Files",
                                          filetypes=(("executables", "*.deb"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)

    # this for loop adds the directory path to the frame
    for app in apps:
        label = tk.Label(frame, text=app, bg="white")
        label.pack()

# Function to run apps
def runApp():
    # for windows
    # inside the loop write the following statement in line 31 and 32
    # os.startfile(app)
    for app in apps:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, app])


# canvas fixes the height, width and bg to root window
canvas = tk.Canvas(root, height=500, width=700, bg="#f56a79")
canvas.pack()

# Adding a container to canvas
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

# Adding button like add apps and run apps
openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="#de4463", bg="white", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="#de4463", bg="white", command=runApp)
runApps.pack()

# This makes the previously selected app to display in the frame when we run the program
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

# Displaying GUI
root.mainloop()

# creating a text file to store the directory path of the apps which we are going to choose
with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')
