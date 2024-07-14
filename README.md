# Python_Lift

This is a simple elevator control system using Python and Tkinter with ttkbootstrap for a modern GUI.

## Features

- Two elevators (`A` and `B`), starting at different floors.
- Call buttons for each floor (0-6) to call the closest elevator.
- Display showing the current floor and movement direction of each elevator.
- Buttons to enter each elevator and select the destination floor.

## Requirements

- Python 3.x
- `ttkbootstrap` library

## Project Structure

- `elevator.py`: Contains the `Elevator` and `Building` classes.
- `elevatorGUI.py`: Contains the main elevator control GUI.
- `floorsGUI.py`: Contains the GUI for selecting destination floors.
- `main.py`: Initializes the building and GUI.

### How It Works

- The system directs the closest elevator to the called floor.
- Elevators handle multiple stops in a FIFO order.
- Users can enter an elevator to select a destination floor.

