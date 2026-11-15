"""
PS 14 - Student Record Management System
Rungta International Skills University | B.Tech CSE

Concepts used:
  - Dictionary : records stored as {roll_number: record_tuple}
  - Tuple      : each record is an immutable (roll, name, course, marks)
  - List       : used to sort/collect records for the table display
  - CRUD       : one function per operation (add, view, search, update, delete)
"""

records = {}  # {roll_number: (roll, name, course, marks)}


# ---------------------------------------------------------------- validation
def valid_marks(marks):
    return isinstance(marks, int) and 0 <= marks <= 100


# ---------------------------------------------------------------------- CRUD
def add_record(roll, name, course, marks):
    """CREATE: add a new student record."""
    if roll in records:
        print(f"Roll number {roll} already exists.")
        return False
    if not valid_marks(marks):
        print("Marks must be between 0 and 100.")
        return False
    records[roll] = (roll, name, course, marks)
    print(f"Record added: {roll} | {name} | {course} | {marks}")
    return True


def view_records():
    """READ: display all records in a neat table."""
    if not records:
        print("No records found.")
        return
    rows = [records[r] for r in sorted(records)]  # list of tuples
    line = "+" + "-" * 10 + "+" + "-" * 20 + "+" + "-" * 12 + "+" + "-" * 8 + "+"
    print(line)
    print(f"| {'Roll No':<8} | {'Name':<18} | {'Course':<10} | {'Marks':<6} |")
    print(line)
    for roll, name, course, marks in rows:
        print(f"| {roll:<8} | {name:<18} | {course:<10} | {marks:<6} |")
    print(line)


def search_record(roll):
    """READ: find one record by roll number."""
    if roll not in records:
        print(f"Roll number {roll} not found.")
        return None
    r, name, course, marks = records[roll]
    print(f"{r} | {name} | {course} | {marks}")
    return records[roll]


def update_record(roll, new_marks):
    """UPDATE: change the marks of an existing student."""
    if roll not in records:
        print(f"Roll number {roll} not found.")
        return False
    if not valid_marks(new_marks):
        print("Marks must be between 0 and 100.")
        return False
    r, name, course, _ = records[roll]
    records[roll] = (r, name, course, new_marks)  # tuples are immutable: replace
    print(f"Marks updated: {new_marks}")
    return True


def delete_record(roll):
    """DELETE: remove a record by roll number."""
    if roll not in records:
        print(f"Roll number {roll} not found.")
        return False
    del records[roll]
    print(f"Record deleted: {roll}")
    return True


# ------------------------------------------------------------- input helpers
def read_int(prompt):
    """Ask until the user types a whole number (never crashes)."""
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Please enter a valid number.")


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty.")


# --------------------------------------------------------- built-in self test
def run_test_cases():
    """Runs the 4 test cases from the problem sheet, in order, on the same records."""
    records.clear()
    print("\n--- Test Case 1: Normal Input ---")
    add_record(101, "Aman", "BTech", 78)
    print("\n--- Test Case 2: Boundary / Minimum Input ---")
    add_record(102, "Riya", "BTech", 100)
    print("\n--- Test Case 3: Invalid Input ---")
    add_record(101, "Neha", "BTech", 70)
    add_record(103, "Ravi", "BTech", 150)
    print("\n--- Test Case 4: Different Valid Scenario ---")
    search_record(101)
    update_record(101, 85)
    delete_record(999)
    print()


# ---------------------------------------------------------------------- menu
def menu():
    print("\n===== Student Record Management System =====")
    print("1. Add record")
    print("2. View all records")
    print("3. Search record")
    print("4. Update marks")
    print("5. Delete record")
    print("6. Run the 4 test cases")
    print("7. Exit")


def main():
    while True:
        menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            roll = read_int("Roll number: ")
            name = read_text("Name: ")
            course = read_text("Course: ")
            marks = read_int("Marks (0-100): ")
            add_record(roll, name, course, marks)
        elif choice == "2":
            view_records()
        elif choice == "3":
            search_record(read_int("Roll number to search: "))
        elif choice == "4":
            roll = read_int("Roll number to update: ")
            marks = read_int("New marks (0-100): ")
            update_record(roll, marks)
        elif choice == "5":
            delete_record(read_int("Roll number to delete: "))
        elif choice == "6":
            run_test_cases()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()