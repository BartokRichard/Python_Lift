class Elevator:
    def __init__(self, name, current_floor):
        self.name = name
        self.current_floor = current_floor
        self.target_floors = []  # List to maintain target floors
        self.direction = None  # 'up' or 'down' or None

    def move(self):
        if self.target_floors:
            target_floor = self.target_floors[0]
            if self.current_floor < target_floor:
                self.current_floor += 1
                self.direction = 'up'
            elif self.current_floor > target_floor:
                self.current_floor -= 1
                self.direction = 'down'
            if self.current_floor == target_floor:
                self.direction = None
                self.target_floors.pop(0)  # Remove the reached floor

    def set_target(self, floor):
        self.target_floors.append(floor)  # Add floor to the list
        if self.direction is None:
            if self.current_floor < floor:
                self.direction = 'up'
            elif self.current_floor > floor:
                self.direction = 'down'

    def __str__(self):
        return f"{self.name} is on floor {self.current_floor}, moving {self.direction}"

class Building:
    def __init__(self):
        self.floors = list(range(7))
        self.elevators = {
            'A': Elevator('A', 0),
            'B': Elevator('B', 6)
        }

    def call_elevator(self, floor):
        distances = {name: abs(elevator.current_floor - floor) for name, elevator in self.elevators.items()}
        closest_elevator = min(distances, key=distances.get)
        self.elevators[closest_elevator].set_target(floor)
        return closest_elevator

    def step(self):
        for elevator in self.elevators.values():
            elevator.move()

    def get_elevator_status(self):
        return {name: str(elevator) for name, elevator in self.elevators.items()}
