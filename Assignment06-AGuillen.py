# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   AGuillen,11/19/2023,Created Script/
#   <Alejandro Guillen>,<11/19/2023>,<Functions Python>
# ------------------------------------------------------------------------------------------ #
import json

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
FILE_NAME: str = 'Enrollments.json'  # File to hold data and update

# Define the Data Variables
student_table: list = []    # Table of student data


# Processing --------------------------------------- #

class Fileprocessor:
    """
    A collection of processing layer functions that work with Json files

    AGuillen,11.19.2023,Created Class

    """

    # When the program starts, read the file data into a list of lists (table)
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list student_data

        :param file_name: file_name: string data with name of file to read from
        :param student_data: list of rows to be filled with file data
        :return: list student_data updated
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            print('The file data was loaded successfully')
        except FileNotFoundError as e:
            IOProcessor.output_error_messages("Text file must exist before running this script!", e)
            # file = open(file_name, 'w')
            # json.dump(student_data, file)  # Loading initial data [] from collection students
        except Exception as e:
            IOProcessor.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of rows

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file
        :return: None
        """

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except TypeError as e:
            IOProcessor.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IOProcessor.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()


# Presentation --------------------------------------- #
class IOProcessor:
    """
    A collection of presentation layer functions that manage user input and output

    AGuillen,11.19.2023,Created Class
    AGuillen,11.20.2023,Added menu output and input functions
    AGuillen,11.21.2023,Added a function to display the data
    AGuillen,11.22.2023,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        :param message: technical error message
        :param error: Exception object with technical message to display

        :return: None
        """

        print(message, end="\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_messages(message: str):
        """
        This function displays a custom messages to the user

        :param message:

        :return: None
        """
        print(message, end="\n")

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        :return: None
        """

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
            if choice not in ("1", "2", "3", "4"):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IOProcessor.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def add_data_to_table(student_data: list):
        """
        Query the user for first name, last name and course and add it to the table student_data
        :param student_data: list of students

        :return: The list of students, with the new student appended to it
        """

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
            IOProcessor.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IOProcessor.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_current_data(student_data: list):
        """ This function displays the current data students enrolled

        :param student_data: list of student object data to be displayed

        :return: The list of current students
        """

        try:
            print("-" * 50)
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            print("-"*50)
        except Exception as e:
            IOProcessor.output_error_messages("There was a non-specific error!", e)
        return student_data


# Load the data from file to list students when the program starts
student_table = Fileprocessor.read_data_from_file(file_name=FILE_NAME, student_data=student_table)

while True:
    # Present the menu of choices
    IOProcessor.output_menu(menu=MENU)
    # Input user data
    menu_choice = IOProcessor.input_menu_choice()
    if menu_choice == "1":
        student_table = IOProcessor.add_data_to_table(student_data=student_table)
        print("\n Here is the updated data")
        IOProcessor.output_current_data(student_data=student_table)
        continue
    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        IOProcessor.output_current_data(student_data=student_table)
        continue
    # Save the data to a file
    elif menu_choice == "3":
        Fileprocessor.write_data_to_file(file_name=FILE_NAME, student_data=student_table)
        continue
    # Stop the loop
    elif menu_choice == "4":
        IOProcessor.output_messages("Program Ended")
        break
    else:
        IOProcessor.output_messages("Please only choose option 1, 2, or 3")
