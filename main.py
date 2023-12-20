import os
from time import sleep

def use_directory():
    try:
        directory = input("Enter the path of the directory you want to use: ")
        os.chdir(directory)
        return os.getcwd()
    except FileNotFoundError:
        print("Directory does not exist")
        return use_directory()    

    except KeyboardInterrupt:
        input("You have cancelled this operation")
        raise SystemExit
    except:
        print("Invalid directory")
        use_directory()

def set_folder_name():
    folder_name = input("Enter the name of the folder: ")
    return folder_name

def num_folders_to_create():
    # Upon ValueError, perform a recursion
    try:
        num_folders = int(input("How many folders do you want to create? "))
        
        # Perform a recursion when the number of folders is negative
        if num_folders < 0:
            print("Please enter a positive integer")
            num_folders = None
        
            return num_folders_to_create()
        
        else:
            return num_folders  
    
    except ValueError:
        print("Please enter a positive integer")
        num_folders = None
    
        return num_folders_to_create()
    except KeyboardInterrupt:
        input("You have cancelled this operation")
        raise SystemExit    

def create_folders(folder_name, num_folders):
    i = 1    
    
    # Create folders until num_folders is reached
    while i <= num_folders:
        print("Creating folder {} of {}".format(i, num_folders))
        
        try: os.mkdir("./"+ folder_name + "" + str(i))
        
        except KeyboardInterrupt:
            input("You have cancelled this operation")
            choice = user_choice()
            if (choice == "N"):
                input("You have kept the created folders")
                raise SystemExit
            
            elif (choice == "Y"):
                cleanup(folder_name, i)

                
        #Skip current folder creation upon error
        except FileExistsError: 
            i=i+1
        i=i+1

def user_choice():

    try:
        user_input = input("Do you want to discard all changes?\n[Y/ yes/ 1] [N/ no/ 0]:").upper()

        print(user_input)
        if (user_input == "Y" or user_input == "YES"):
            return "Y"
        elif (user_input == "N" or user_input == "NO"):
            return "N"
        elif (user_input == "0"):
            raise TypeError
        else:
            input("User input is not one of the choices")
            return user_choice()

    except TypeError:
        try:
            user_input = int(user_input)
            if (user_input == 1):
                return "Y"
            if (user_input == 0):
                return "N"
            else:
                input("Invalid Input")
                return user_choice()
        except ValueError:
            input("Invalid Input")
            return user_choice()

def cleanup(folder_name, num_folders):
        i = 0
        
        while i <= num_folders:
            print("Deleting folder {} of {}".format(i, num_folders))
            try: 
                os.rmdir("./"+ folder_name + "" + str(i))

            except FileExistsError: 
                i=i+1
            i=i+1
        print("Clean up completed")
        raise SystemExit
            
if __name__ == "__main__":
        use_directory()
        folder_name = set_folder_name()
        no_folders = num_folders_to_create()
        create_folders(folder_name, no_folders)
        input("Press enter to exit")