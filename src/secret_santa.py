import csv
import random
import sys
from typing import List, Dict, Tuple

class SecretSanta:
    def __init__(self, employees_file: str, previous_assignments_file: str, output_file: str):
        self.employees_file = employees_file
        self.previous_assignments_file = previous_assignments_file
        self.output_file = output_file
        self.employees = []  # Stores employee list
        self.previous_assignments = {}  # Stores last year's assignments

    # Reads the employee CSV file and stores data_old.
    def read_employees(self) -> None:
        try:
            with open(self.employees_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.employees = [{"name": row["Employee_Name"], "email": row["Employee_EmailID"]} for row in reader]
        except Exception as e:
            print(f"Error reading employee file: {e}")
            sys.exit(1)

    #Reads last year's assignments to avoid repeating secret children.
    def read_previous_assignments(self) -> None:
        try:
            with open(self.previous_assignments_file, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.previous_assignments = {row["Employee_EmailID"]: row["Secret_Child_EmailID"] for row in reader}
        except FileNotFoundError:
            print("Previous assignments file not found. Proceeding without history.")

    #Assigns each employee a secret child, ensuring constraints are met.
    def assign_secret_santa(self) -> List[Tuple[str, str, str, str]]:
        available_children = [emp.copy() for emp in self.employees]  # Create a list of available children
        assignments = []

        random.shuffle(available_children)  # Shuffle list to ensure randomness

        # Filter out self and last year's assigned child
        for emp in self.employees:
            possible_choices = []

            for child in available_children:
                if child["email"] != emp["email"] and child["email"] != self.previous_assignments.get(emp["email"], ""):
                    possible_choices.append(child)  # Add to the list if conditions are met

            if not possible_choices:
                print("Error: Unable to assign secret children without conflicts.")
                sys.exit(1)

            # Randomly choose a secret child from possible choices
            chosen_child = random.choice(possible_choices)
            assignments.append((emp["name"], emp["email"], chosen_child["name"], chosen_child["email"]))
            available_children.remove(chosen_child)  # Ensure each person gets assigned only once

        return assignments

    #Writes the new assignments to a CSV file.
    def write_output(self, assignments: List[Tuple[str, str, str, str]]) -> None:

        with open(self.output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Employee_Name", "Employee_EmailID", "Secret_Child_Name", "Secret_Child_EmailID"])
            writer.writerows(assignments)
        print(f"Assignments successfully written to {self.output_file}")
