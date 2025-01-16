from tkinter import Tk, Label, BOTH

import globalVariables
import miscs
import scanAttacks

root = Tk()

width = 230
height = 120

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = screen_width - width - 10

y = screen_height - height - 35

root.geometry(f"{width}x{height}+{x}+{y}")
root.attributes("-topmost", True)
root.title("DFOA Alert")
root.iconbitmap("icon.ico")
root.resizable(False, False)

label_warning = Label(root, bg="black", fg="red", text="No attacks yet.", font=("Arial", 15), anchor="center")
label_warning.pack(fill=BOTH, expand=True)

globalVariables.root = root
globalVariables.label = label_warning

miscs.multithreading(lambda: scanAttacks.scan_oa_attacks())

root.mainloop()
