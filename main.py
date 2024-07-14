import ttkbootstrap as ttk
from elevator import Building
from elevatorGUI import ElevatorGUI
from floorsGUI import ElevatorControlGUI
from tkinter import TOP, Toplevel

class MainApp:
    def __init__(self, root):
        self.root = root
        self.building = Building()
        self.gui = ElevatorGUI(root, self.call_elevator, self.enter_elevator, self.update_status)
        self.status_vars = self.gui.status_vars
        self.enter_buttons = self.gui.enter_buttons
        self.update_status()  

    def call_elevator(self, floor):
        closest_elevator = self.building.call_elevator(floor)
        self.update_status()
        print(f"Elevator {closest_elevator} called to floor {floor}")

    def enter_elevator(self, elevator_name):
        new_window = Toplevel(self.root)
        elevator = self.building.elevators[elevator_name]
        ElevatorControlGUI(new_window, elevator, self.set_destination)

    def set_destination(self, elevator, floor):
        elevator.set_target(floor)

    def update_status(self):
        for name, var in self.status_vars.items():
            elevator = self.building.elevators[name]
            status_text = f"{elevator.name} is on floor {elevator.current_floor}, moving {elevator.direction}"
            if not elevator.target_floors and elevator.direction is None:
                self.enter_buttons[name].pack(side=TOP, pady=5)
            else:
                self.enter_buttons[name].pack_forget()
            var.set(status_text)
        self.building.step()

if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    app = MainApp(root)
    root.mainloop()
