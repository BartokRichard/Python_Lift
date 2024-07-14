import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ElevatorControlGUI:
    def __init__(self, root, elevator, set_destination_callback):
        self.root = root
        self.elevator = elevator
        self.set_destination_callback = set_destination_callback
        self.create_widgets()

    def create_widgets(self):
        self.root.title(f"Control {self.elevator.name}")
        label = ttk.Label(self.root, text=f"Select floor for {self.elevator.name}:", bootstyle="info")
        label.pack(pady=10)

        for i in range(7):
            button = ttk.Button(self.root, text=f"Floor {i}", command=lambda i=i: self.set_destination(i), bootstyle="primary-outline")
            button.pack(pady=5)

    def set_destination(self, floor):
        self.set_destination_callback(self.elevator, floor)
        self.root.destroy()
