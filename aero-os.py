import tkinter as tk

root = tk.Tk()

root.title("AERO-OS")
root.geometry("800x480")
root.configure(bg="#6EC6FF")

title = tk.Label(
    root,
    text="AERO-OS",
    font=("Arial", 32, "bold"),
    bg="#6EC6FF",
    fg="white"
)
title.pack(pady=50)

notes = tk.Button(
    root,
    text="📝 Notes",
    font=("Arial", 16)
)
notes.pack(pady=10)

calc = tk.Button(
    root,
    text="🧮 Calculator",
    font=("Arial", 16)
)
calc.pack(pady=10)

root.mainloop()
