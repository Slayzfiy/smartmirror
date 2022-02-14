from tkinter import Frame, Label
import json


class Countdown(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.config = json.load(open("data/config.json", "r"))["countdown"]
        self.event_frequency = self.config["event_frequency"]
        self.bgcolor = self.config["background_color"]
        self.fgcolor = self.config["foreground_color"]

        self.configure(bg=self.bgcolor)
        self.grid(column=self.config["position_x"], row=self.config["position_y"], sticky="nesw")

        self.innerFrame = Frame(self, bg=self.bgcolor)
        for i in range(1):
            self.innerFrame.grid_rowconfigure(i, weight=1)

        self.label_text = Label(self.innerFrame, text="text", bg=self.bgcolor, font=("Segeo UI", 25), fg=self.fgcolor)
        self.label_text.grid(row=0)

        self.has_event = True
        self.innerFrame.pack()

    def event(self):
        #do stuff
        pass