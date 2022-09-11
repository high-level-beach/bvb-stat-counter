from doctest import master
from ssl import PROTOCOL_TLSv1_1
import tkinter as tk

import pathlib

path_to_top = f"{pathlib.Path(__file__).parent.parent}"

class StatChangeWidget:

    def __init__(self, i, j, value=0) -> None:
        self.value = value
        frm = tk.Frame(
            master=window,
            relief=tk.GROOVE,
            borderwidth=1
        )

        frm.grid(row=i,column=j)

        self.btn_increase = tk.Button(master=frm, text="+", command=self.increment)
        self.label = tk.Label(master=frm, text=f"{self.value}")
        self.btn_decrease = tk.Button(master=frm, text="-", command=self.decrement)
        for widget in [self.btn_increase,self.label,self.btn_decrease]:
            widget.pack(padx=5,pady=5)

        self.row = i
        self.col = j

    def increment(self):
        """
        Increases value
        """
        self.value += 1
        self.label["text"] = f"{self.value}"

    def decrement(self):
        """
        Decreases value
        """
        self.value -= 1
        self.label["text"] = f"{self.value}"

class ReceiveStatChangeWidget:

    def __init__(self, i, j, value=0) -> None:
        self.value = value

        frm = tk.Frame(
            master=window,
            relief=tk.GROOVE,
            borderwidth=1
        )
        frm.grid(row=i,column=j)

        frm_inc = tk.Frame(
            master=frm,
            relief=tk.FLAT,
            borderwidth=1
        )
        frm_inc.pack()
        for inc, fxn in zip([1,2,3],[self.inc_one,self.inc_two,self.inc_three]):
            btn_increase = tk.Button(master=frm_inc, text=f"+{inc}", command=fxn)
            btn_increase.pack(padx=5, pady=5, side=tk.LEFT)

        frm_mid = tk.Frame(
            master=frm,
            relief=tk.FLAT,
            borderwidth=1
        )
        frm_mid.pack()
        self.label = tk.Label(master=frm_mid, text=f"{value}")
        self.label.pack(padx=5, pady=5)

        frm_dec = tk.Frame(
            master=frm,
            relief=tk.FLAT,
            borderwidth=1
        )
        frm_dec.pack()
        for dec, fxn in zip([1,2,3], [self.dec_one, self.dec_two, self.dec_three]):
            btn_increase = tk.Button(master=frm_dec, text=f"-{dec}", command=fxn)
            btn_increase.pack(padx=5, pady=5, side=tk.LEFT)

        self.row = i
        self.col = j

    def inc_one(self):
        """
        Increase by 1
        """
        self.value += 1
        self.label["text"] = f"{self.value}"

    def inc_two(self):
        """
        Increase by two
        """
        self.value += 2
        self.label["text"] = f"{self.value}"

    def inc_three(self):
        """
        Increase by three
        """
        self.value += 3
        self.label["text"] = f"{self.value}"

    def dec_one(self):
        """
        Decrease by 1
        """
        self.value -= 1
        self.label["text"] = f"{self.value}"

    def dec_two(self):
        """
        Decrease by two
        """
        self.value -= 2
        self.label["text"] = f"{self.value}"

    def dec_three(self):
        """
        Decrease by three
        """
        self.value -= 3
        self.label["text"] = f"{self.value}"

class PlayerStatWidget:

    def __init__(self, row) -> None:
        self.row = row

        frm = tk.Frame(
            master=window,
            relief=tk.GROOVE,
            borderwidth=1
        )
        frm.grid(row=self.row, column=0, padx=5, pady=5)

        self.lbl_player = tk.Label(master=frm, text=f"Enter Name")
        self.lbl_player.pack(padx=5, pady=5)

        self.ent_player = tk.Entry(master=frm, width=10)
        self.ent_player.pack(padx=5,pady=5)

        btn_update = tk.Button(master=frm, text="update", command=self.set_player)
        btn_update.pack(padx=5,pady=5)

        for j in range(1,13):
            if j == 5:
                ReceiveStatChangeWidget(self.row, j, 0)
            else:
                StatChangeWidget(self.row, j, 0)

    def set_player(self):
        """
        Sets the name of the player
        """
        self.lbl_player["text"] = self.ent_player.get()

# Setting up Window
window = tk.Tk()
window.title("Beach Volleyball Stat Counter")
window.iconbitmap(f"{path_to_top}/assets/hlb.ico")

stat_labels = [
    "Player",
    "Serves","Aces","Missed Serves",
    "Received","Pass Rating",
    "Swings","Swing Kills",
    "Blocks","Block Kills",
    "Bump Kills",
    "Hitting Errors","Errors"]

# Header
for j, stat_label in zip(range(13),stat_labels):
    frm_title = tk.Frame(
        master=window,
        relief=tk.FLAT,
    )
    frm_title.grid(row=0, column=j, padx=5, pady=5)
    label = tk.Label(master=frm_title, text=stat_label)
    label.pack(padx=5, pady=5)

frm = tk.Frame(
    master=window,
    relief=tk.GROOVE,
    borderwidth=1
)

widget_p1 = PlayerStatWidget(1)
widget_p2 = PlayerStatWidget(2)
widget_p3 = PlayerStatWidget(3)
widget_p4 = PlayerStatWidget(4)

# Running
window.mainloop()