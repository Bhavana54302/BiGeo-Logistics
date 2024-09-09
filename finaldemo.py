import tkinter as tk
from tkinter import ttk, messagebox

class Truck:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.outbound_distance = 0
        self.inbound_distance = 0
        self.trips = 0

    def add_outbound_distance(self, distance):
        self.outbound_distance += distance

    def add_inbound_distance(self, distance):
        self.inbound_distance += distance

    def total_distance(self):
        return self.outbound_distance + self.inbound_distance

    def add_trip(self, packets):
        self.trips += (packets // self.capacity) + (1 if packets % self.capacity != 0 else 0)

    def get_trips(self):
        return self.trips


def calculate_distances(spoke_packets, transfers, truck_capacity, distances):
    # Initialize trucks
    trucks = {
        't1': Truck('Truck 1 (s1)', truck_capacity),
        't2': Truck('Truck 2 (s2)', truck_capacity),
        't3': Truck('Truck 3 (s3)', truck_capacity),
        't4': Truck('Truck 4 (s4)', truck_capacity),
        't5': Truck('Truck 5 (s5)', truck_capacity),
    }

    # Calculate trips and distances
    trucks['t1'].add_outbound_distance(distances['s1']['hub'])
    trucks['t1'].add_trip(spoke_packets['s1'])
    for dest, packets in transfers['s1'].items():
        trucks['t1'].add_inbound_distance(distances['hub'][dest])
        trucks['t1'].add_trip(packets)

    trucks['t2'].add_outbound_distance(distances['s2']['hub'])
    trucks['t2'].add_trip(spoke_packets['s2'])
    for dest, packets in transfers['s2'].items():
        trucks['t2'].add_inbound_distance(distances['hub'][dest])
        trucks['t2'].add_trip(packets)

    trucks['t3'].add_outbound_distance(distances['s3']['hub'])
    trucks['t3'].add_trip(spoke_packets['s3'])

    trucks['t4'].add_outbound_distance(distances['s4']['hub'])
    trucks['t4'].add_trip(spoke_packets['s4'])

    trucks['t5'].add_outbound_distance(distances['s5']['hub'])
    trucks['t5'].add_trip(spoke_packets['s5'])

    total_distances = {truck.name: truck.total_distance() for truck in trucks.values()}
    total_trips = {truck.name: truck.get_trips() for truck in trucks.values()}

    return total_distances, total_trips


def display_results(total_distances, total_trips):
    result_window = tk.Toplevel(root)
    result_window.title("Truck Calculations")

    result_label = tk.Label(result_window, text="Total distances covered by each truck:", font=("Arial", 12))
    result_label.pack(pady=10)

    for truck_name, distance in total_distances.items():
        tk.Label(result_window, text=f"{truck_name}: {distance} km").pack()

    trip_label = tk.Label(result_window, text="\nTotal trips made by each truck:", font=("Arial", 12))
    trip_label.pack(pady=10)

    for truck_name, trips in total_trips.items():
        tk.Label(result_window, text=f"{truck_name}: {trips} trips").pack()


def run_calculation():
    spoke_packets = {
        's1': int(entry_s1.get()),
        's2': int(entry_s2.get()),
        's3': int(entry_s3.get()),
        's4': int(entry_s4.get()),
        's5': int(entry_s5.get()),
    }

    transfers = {
        's1': {'s2': 120, 's3': 200, 's4': 80, 's5': 150},
        's2': {'s1': 150, 's3': 250, 's4': 200, 's5': 110},
        's3': {'s1': 100, 's2': 300, 's4': 150, 's5': 90},
        's4': {'s1': 50, 's2': 150, 's3': 100, 's5': 130},
        's5': {'s1': 200, 's2': 250, 's3': 150, 's4': 70},
    }

    truck_capacity = 500

    distances = {
        's1': {'hub': 250},
        's2': {'hub': 380},
        's3': {'hub': 120},
        's4': {'hub': 200},
        's5': {'hub': 170},
        'hub': {'s1': 250, 's2': 380, 's3': 120, 's4': 200, 's5': 170}
    }

    total_distances, total_trips = calculate_distances(spoke_packets, transfers, truck_capacity, distances)
    display_results(total_distances, total_trips)


# Create main window
root = tk.Tk()
root.title("Truck Logistics Calculation")

tk.Label(root, text="Enter Spoke Packets:", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

# Entry fields for the number of packets at each spoke
tk.Label(root, text="s1 (Spoke 1):").grid(row=1, column=0, sticky='e')
entry_s1 = tk.Entry(root)
entry_s1.grid(row=1, column=1)

tk.Label(root, text="s2 (Spoke 2):").grid(row=2, column=0, sticky='e')
entry_s2 = tk.Entry(root)
entry_s2.grid(row=2, column=1)

tk.Label(root, text="s3 (Spoke 3):").grid(row=3, column=0, sticky='e')
entry_s3 = tk.Entry(root)
entry_s3.grid(row=3, column=1)

tk.Label(root, text="s4 (Spoke 4):").grid(row=4, column=0, sticky='e')
entry_s4 = tk.Entry(root)
entry_s4.grid(row=4, column=1)

tk.Label(root, text="s5 (Spoke 5):").grid(row=5, column=0, sticky='e')
entry_s5 = tk.Entry(root)
entry_s5.grid(row=5, column=1)

# Button to run the calculation
calculate_button = tk.Button(root, text="Calculate", command=run_calculation, font=("Arial", 12), bg="green", fg="white")
calculate_button.grid(row=6, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()


# This code calculates and prints out the total distances covered by each truck based on their routes and capacities. The output will show how much distance each truck travels during its trips between the hub and spokes.
#By running this code, you will get an accurate breakdown of how much distance each truck covers while delivering packets efficiently according to your specified requirements.