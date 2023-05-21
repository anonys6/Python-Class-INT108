def update_marks(marks_dict):
    name = input("Whose marks do you want to update? Enter student's name: ")
    if name in marks_dict:
        try:
            marks = int(input("Enter the marks (as integer): "))
            marks_dict[name] = marks
            print("Updation done!")
        except ValueError:
            print("Invalid input! Marks must be an integer.")
    else:
        print("\nEntered name is invalid!\nSelect again...\n")


def print_marks(marks_dict):
    print("\nPrinting all the student marks:")
    for name, marks in marks_dict.items():
        print(name, ":", marks)


def print_rank(marks_dict):
    sorted_marks = sorted(marks_dict.items(), key=lambda x: x[1], reverse=True)
    print("\nRank of all the students:")
    for i, (name, marks) in enumerate(sorted_marks, 1):
        print("Rank", i, "is:", name)


def main():
    marks_dict = {}

    while True:
        try:
            no_of_students = int(
                input("Enter the number of students (as an integer): "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer.")

    for i in range(1, no_of_students + 1):
        name = input(f"\nEnter the name of Student no. {i}: ")
        while True:
            try:
                marks = int(
                    input(f"Enter the marks {name} has gotten (as an integer): "))
                break
            except ValueError:
                print("Invalid input! Marks must be an integer.")
        marks_dict[name] = marks

    print("\nPrinting all the students marks:")
    print_marks(marks_dict)

    while True:
        print('\nType:\n1. Update the marks\n2. Print all the student marks\n3. Exit the program')
        user_input = input()
        if user_input == "1":
            update_marks(marks_dict)
        elif user_input == "2":
            print_marks(marks_dict)
        elif user_input == "3":
            print("You have exited the program.")
            break
        else:
            print("Please enter a valid input.\nTry again...\n")

    print("\nThe student who got the highest marks is:",
          max(marks_dict, key=marks_dict.get))
    print_rank(marks_dict)


if __name__ == "__main__":
    main()
