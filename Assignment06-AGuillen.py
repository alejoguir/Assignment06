# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   AGuillen,11/19/2023,Created Script/
#   <Alejandro Guillen>,<11/19/2023>,<Functions Python>
# ------------------------------------------------------------------------------------------ #
import json
from json import JSONDecodeError

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = 'Enrollments.json'
student_table: list = []


# Processing --------------------------------------- #
class Fileprocessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    AGuillen,11.19.2023,Created Class

    """

    # When the program starts, read the file data into a list of lists (table)
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            print('The file data was loaded successfully')
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
            # file = open(file_name, 'w')
            # json.dump(student_data, file)  # Loading initial data [] from collection students
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    AGuillen,11.19.2023,Created Class
    AGuillen,11.20.2023,Added menu output and input functions
    AGuillen,11.21.2023,Added a function to display the data
    AGuillen,11.22.2023,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message:str, error: Exception=None):
        """
        This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        AGuillen,11.26.2023,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        print(menu)
        print()


    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice


    @staticmethod
    def add_data_to_table(student_data: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")

            student_data.append({"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name})
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_current_data(student_data: list):
        try:
            print("-" * 50)
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-"*50)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


# Load the data from file to list students when the program starts
student_table = Fileprocessor.read_data_from_file(file_name=FILE_NAME, student_data=student_table)

while True:
    # Present the menu of choices
    IO.output_menu(menu=MENU)
    # Input user data
    menu_choice = IO.input_menu_choice()
    if menu_choice == "1":
        student_table = IO.add_data_to_table(student_data=student_table)
        continue
    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        student_table = IO.output_current_data(student_data=student_table)
        continue
    # Save the data to a file
    elif menu_choice == "3":
        student_table = Fileprocessor.write_data_to_file(file_name=FILE_NAME, student_data=student_table)
        continue
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
