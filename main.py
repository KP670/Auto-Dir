import os


def use_directory():
    
    try:
        directory = input("Enter the path of the directory you want to use: ")
        os.chdir(directory)    
    except:
        print("Invalid directory")
        use_directory()
    return os.getcwd()

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
    

def create_folders(folder_name, num_folders):
    i = 0    
    
    # Create folders until num_folders is reached
    while i <= num_folders:
        print("Creating folder {} of {}".format(i, num_folders))
        
        #Skip current folder creation upon error
        try: os.mkdir("./"+ folder_name + "" + str(i))
        except: i=i+1
        i=i+1

    input("Press enter to exit")

if __name__ == "__main__":
        use_directory()
        folder_name = set_folder_name()
        no_folders = num_folders_to_create()
        create_folders(folder_name, no_folders)