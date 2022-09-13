import tkinter as tk

def Background(i, master_frame, color="white", end_col=15, height=None):
    for j in range(end_col):
        if height is None:
            frm_bg = tk.Frame(
                master=master_frame,
                relief=tk.FLAT,
                border=2,
                bg=color
            )
        else:
            frm_bg = tk.Frame(
                master=master_frame,
                relief=tk.FLAT,
                border=2,
                height=height,
                bg=color
            )
        frm_bg.grid(row=i,column=j,sticky="nsew")
