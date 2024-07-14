# elevatorGUI.py

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import StringVar, Toplevel

class ElevatorGUI:
    def __init__(self, root, call_elevator_callback, enter_elevator_callback, update_status_callback):
        self.root = root
        self.call_elevator_callback = call_elevator_callback
        self.enter_elevator_callback = enter_elevator_callback
        self.update_status_callback = update_status_callback
        self.status_vars = {}
        self.enter_buttons = {}
        self.create_widgets()
        self.root.after(1000, self.update_status)

    def create_widgets(self):
        self.root.title("Elevator Control System")

        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True)

        status_frame = ttk.Frame(main_frame, padding="10")
        status_frame.pack(side=TOP, fill=X)

        for name in ['A', 'B']:
            var = StringVar()
            self.status_vars[name] = var
            label = ttk.Label(status_frame, textvariable=var, bootstyle="info")
            label.pack(anchor="center")
            self.enter_buttons[name] = ttk.Button(main_frame, text=f"Enter {name}", command=lambda name=name: self.enter_elevator_callback(name), bootstyle="success")
            self.enter_buttons[name].pack(side=TOP, pady=5, fill=X)
            self.enter_buttons[name].pack_forget()  # Initially hide the button

        button_frame = ttk.Frame(main_frame, padding="10")
        button_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.floor_buttons = []
        for i in range(7):
            frame = ttk.Frame(button_frame, padding="5")
            frame.pack(side=TOP, fill=X)

            label = ttk.Label(frame, text=f"Floor {i}", width=10)
            label.pack(side=LEFT, padx=5)

            call_button = ttk.Button(frame, text="Call", command=lambda i=i: self.call_elevator_callback(i), bootstyle="primary-outline")
            call_button.pack(side=LEFT, padx=5)

            self.floor_buttons.append(call_button)

    def update_status(self):
        self.update_status_callback()
        self.root.after(1000, self.update_status)
