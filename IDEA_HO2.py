import tkinter as tk

window = tk.Tk()
window.title("Chrysler Anne's Profile")
window.geometry("600x600")
window.resizable(False, True)
window.config(bg="violet")

label=tk.Label(window, text ="Student Profile", font=("courier new", 32,"bold"), fg="black", bg="violet", anchor="s")
label.pack(padx=(10),pady=(20))

label=tk.Label(window, text="Name: Chrysler Anne L. Idea", font=("courier new", 14, "bold"), fg="black", bg="violet")
label.pack(padx=(10), pady=(10), anchor="w")

label=tk.Label(window, text="Age: 18", font=("courier new", 14,"bold"), fg="black", bg="violet")
label.pack(padx=(10), pady=(10), anchor="w")

label=tk.Label(window, text="Course: BSIT-1C", font=("courier new", 14,"bold"), fg="black", bg="violet")
label.pack(padx=(10), pady=(10), anchor="w")

label=tk.Label(window, text="Birthday: July 15, 2007", font=("courier new", 14,"bold"), fg="black", bg="violet")
label.pack(padx=(10), pady=(10), anchor="w")

label=tk.Label(window, text="Motto:", font=("courier new", 14,"bold"), fg="black", bg="violet")
label.pack(padx=(10), pady=(10), anchor="w")

label=tk.Label(window, text="Everything happens for a reason.", font=("courier new", 14, "bold", "italic"), fg="black", bg="violet")
label.pack(anchor="s")

window.mainloop()
