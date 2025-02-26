from src.secret_santa import SecretSanta

def main():
    employees_file = "G:\Python\secret_santa\data\employees.csv"
    previous_assignments_file = "G:\Python\secret_santa\data\previous_assignments.csv"
    output_file = "G:\Python\secret_santa\data\output.csv"

    # Initialize the SecretSanta class
    santa = SecretSanta(employees_file, previous_assignments_file, output_file)

    # Read employees from the CSV file
    santa.read_employees()

    # Read last year's assignments
    santa.read_previous_assignments()

    # Generate new Secret Santa assignments
    assignments = santa.assign_secret_santa()

    # Write new assignments to output file
    santa.write_output(assignments)


if __name__ == "__main__":
    main()
