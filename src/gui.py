import tkinter as tk

import json
import pandas as pd

import pathlib

from colour import Color

from custom_widgets import Background

# Defining "global" variables
PATH_TO_TOP = f"{pathlib.Path(__file__).resolve().parent.parent}"
STAT_LABELS = [
    "Player",
    "Serves","Aces","Missed Serves",
    "Received","Pass Rating",
    "Swings","Swing Kills",
    "Blocks","Block Kills",
    "Bump Kills",
    "Hitting Errors","Errors"]

class InfoSetter:

    def __init__(self, i, j, info_label, value="") -> None:
        self.value = value
        frm_game_info = tk.Frame(
                master=window,
                relief=tk.FLAT,
                bg="black"
            )
        frm_game_info.grid(row=i,column=j,sticky="nsew")

        self.lbl_info = tk.Label(
            master=frm_game_info,
            text=f"{info_label}:",
            font="bold",
            fg="white",
            bg="black",
            anchor="w"
        )
        self.lbl_info.pack(fill=tk.BOTH, padx=0, pady=0)

        self.ent_info = tk.Entry(
            master=frm_game_info,
            width=5,
            bg="white"
        )
        self.ent_info.pack(padx=2, pady=2, side=tk.LEFT)

    def set_info(self):
        """
        Resets the info title
        """
        self.value = self.ent_info.get()

class StatChangeWidget:

    def __init__(self, i, j, value, stat_label, color) -> None:
        self.value = value
        self.stat_label = stat_label

        frm = tk.Frame(
            master=window,
            relief=tk.GROOVE,
            borderwidth=1,
            bg=color
        )

        frm.grid(row=i,column=j)

        self.btn_increase = tk.Button(master=frm, text="+", bg=color, command=self.increment)
        self.label = tk.Label(master=frm, text=f"{self.value}", bg=color)
        self.btn_decrease = tk.Button(master=frm, text="-", bg=color, command=self.decrement)
        for widget in [self.btn_increase,self.label,self.btn_decrease]:
            widget.pack(padx=0,pady=0)

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

    def __init__(self, i, j, value, stat_label, color) -> None:
        self.value = value
        self.stat_label = stat_label

        frm = tk.Frame(
            master=window,
            relief=tk.GROOVE,
            borderwidth=1,
            bg=color
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
            btn_increase.pack(padx=0, pady=0, side=tk.LEFT)

        frm_mid = tk.Frame(
            master=frm,
            relief=tk.FLAT
        )
        frm_mid.pack()
        self.label = tk.Label(master=frm_mid, text=f"{value}", bg=color)
        self.label.pack(padx=0, pady=0)

        frm_dec = tk.Frame(
            master=frm,
            relief=tk.FLAT,
            borderwidth=1
        )
        frm_dec.pack()
        for dec, fxn in zip([1,2,3], [self.dec_one, self.dec_two, self.dec_three]):
            btn_increase = tk.Button(master=frm_dec, text=f"-{dec}", command=fxn)
            btn_increase.pack(padx=0, pady=0, side=tk.LEFT)

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

    def __init__(self, row, color) -> None:
        self.row = row
        self.player = ""
        self.colors = list(Color(color).range_to(Color("white"),13))

        self.stats = {label: 0 for label in STAT_LABELS if label != "Player"}

        frm = tk.Frame(
            master=window,
            relief=tk.GROOVE,
            borderwidth=1,
            bg=self.colors[0]
        )
        # First Column: Player Name
        frm.grid(row=self.row, column=0, padx=5, pady=5)

        self.lbl_player = tk.Label(master=frm, text=f"Enter Name", bg="white")
        self.lbl_player.pack(fill=tk.BOTH, padx=5, pady=5)

        self.ent_player = tk.Entry(master=frm, width=8)
        self.ent_player.pack(fill=tk.BOTH, padx=5,pady=5)

        btn_update = tk.Button(master=frm, text="update", command=self.set_player, bg=self.colors[0])
        btn_update.pack(fill=tk.BOTH, padx=5,pady=5)

        # Stat Columns
        for j, stat_label in zip(range(1,13), self.stats.keys()):
            if j == 5:
                self.stats[stat_label] = ReceiveStatChangeWidget(self.row, j, 0, stat_label, color=self.colors[j])
            else:
                self.stats[stat_label] = StatChangeWidget(self.row, j, 0, stat_label, color=self.colors[j])

        # Last Column: Save Stats
        frm_save = tk.Frame(
            master=window,
            relief=tk.FLAT,
            borderwidth=1
        )
        frm_save.grid(row=self.row, column=14, padx=5, pady=5)

        btn_save = tk.Button(master=frm_save, text="save", command=self.save_stats)
        btn_save.pack(padx=5,pady=5)

    def set_player(self):
        """
        Sets the name of the player
        """
        self.lbl_player["text"] = self.ent_player.get()
        self.player = self.lbl_player["text"]

    def save_stats(self):
        """
        Saves the players stats
        """
        stat_values = {}
        for key, widget in self.stats.items():
            stat_values[key] = widget.value

        stat_values["Player"] = self.player
        with open(f"{PATH_TO_TOP}/data/raw/{self.player}-stats.json", "w") as f:
            json.dump(stat_values, f)

class SwitchWidget:

    def __init__(self, i, j, switch_no=0) -> None:
        self.row = i
        self.score = "0 - 0"

        frm = tk.Frame(
            master=window,
            relief=tk.GROOVE,
            borderwidth=1,
            bg="white"
        )

        frm.grid(row=self.row, column=j, padx=5, pady=5)

        self.lbl = tk.Label(master=frm, text=f"Switch {switch_no}")
        self.lbl.pack(fill=tk.BOTH, padx=5, pady=5)

        frm_switch = tk.Frame(
            master=frm,
            relief=tk.GROOVE,
            borderwidth=1
        )
        frm_switch.pack(fill=tk.BOTH, padx=0, pady=1)

        self.top_team_score = tk.Entry(master=frm_switch, width=2)
        self.top_team_score.pack(side=tk.LEFT, padx=0, pady=0)

        lbl_dash = tk.Label(master=frm_switch, text=f" - ")
        lbl_dash.pack(side=tk.LEFT, padx=0, pady=0)

        self.bot_team_score = tk.Entry(master=frm_switch, width=2)
        self.bot_team_score.pack(side=tk.LEFT, padx=0, pady=0)

        btn_update = tk.Button(master=frm, text="set", command=self.set_score)
        btn_update.pack(fill=tk.BOTH, padx=0,pady=1)

    def set_score(self):
        """
        Updates the score to what is in the text entry
        """
        self.score = f"{self.top_team_score['text']} - {self.bot_team_score['text']}"

# Setting up Window
window = tk.Tk()
window.title("Beach Volleyball Stat Counter")
window.iconbitmap(f"{PATH_TO_TOP}/assets/hlb.ico")

# Date and Game (Row 0)
# ---------------------
# Creating info widgets
year = InfoSetter(i=0,j=1,info_label="Year",value="1900")
month = InfoSetter(i=0,j=2,info_label="Month",value="01")
day = InfoSetter(i=0,j=3,info_label="Day",value="01")
game_number = InfoSetter(i=0,j=4,info_label="Game",value="0")
# creating frame for label
frm_date_and_game = tk.Frame(
    master=window,
    relief=tk.SUNKEN,
)
frm_date_and_game.grid(row=0,column=5)
# creating label from info widgets
lbl_info = tk.Label(
    master=frm_date_and_game,
    text=f"{month.value}/{day.value}/{year.value}: Game {game_number.value}",
    anchor="w"
)
lbl_info.pack(padx=5, pady=5, side=tk.LEFT)

# date and game set button  
def show_info():
    """
    Shows the info the user inputs into the game info
    """
    for widget in [year, month, day, game_number]:
        widget.set_info()
    
    lbl_info["text"] = f"{month.value}/{day.value}/{year.value}: Game {game_number.value}"

# creating button and linking to function
btn_set_info = tk.Button(master=frm_date_and_game, text="set", command=show_info)
btn_set_info.pack(padx=2, pady=2, side=tk.LEFT)

# Header (Row 1)
# --------------
# looping through stat labels and creating columns
for j, stat_label in zip(range(13),STAT_LABELS):
    frm_title = tk.Frame(
        master=window,
        relief=tk.FLAT,
    )
    frm_title.grid(row=1, column=j, padx=5, pady=5)
    label = tk.Label(master=frm_title, text=stat_label)
    label.pack(padx=5, pady=5)

# Players (Rows 2 - 6)
# -------
# looping through four players and creating sub-widgets
player_widgets = {}
for player, row, color in zip([1,2,0,3,4],[2,3,4,5,6],["red","green","black","blue","yellow"]):
    # putting a background
    if row == 4:
        Background(row,window,color,15,height=20)
    else:
        # adding the players
        Background(row,window,color,15)
        if row != 4:
            player_widgets[f"player{player}"] = PlayerStatWidget(row,color)

# Switches (Row 7)
# ----------------
switch_widgets = {}
for possible_switches in range(6):
    SwitchWidget(i=7, j=possible_switches+1, switch_no=possible_switches+1)

# Plays (Row 8)
# -------------

# Save (Row 9)
# ------------
def save_data():
    """
    Aggregates and saves the data from each of the players
    """
    combined_data = {label: [] for label in STAT_LABELS}
    for p_widget in player_widgets.values():
        for stat_label, stat_widget in p_widget.stats.items():
            combined_data[stat_label].append(stat_widget.value)

        combined_data["Player"].append(p_widget.player)

    meta = f"{year.value}_{month.value}_{day.value}-game{game_number.value}"
    df = pd.DataFrame(combined_data)
    df.to_csv(f"{PATH_TO_TOP}/data/processed/stats-{meta}.csv", index=False)

# save_button
frm_save = tk.Frame(
    master=window,
    relief=tk.FLAT,
)
frm_save.grid(row=9,column=0)
save_button = tk.Button(master=frm_save, text="Save Data", command=save_data)
save_button.pack(padx=5, pady=5)

# Running
# -------
window.mainloop()