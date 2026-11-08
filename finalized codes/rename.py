#renaming Audio files according to the format, no spaces between first name and last name, and underscore between name and sequence number.
import os
def rename_files(directory):
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    for filename in os.listdir(directory):          #iterate through each file in the directory
        actual_path = os.path.join(directory, filename)
        
        if os.path.isfile(actual_path):             #checking if input path is a file
            
            name, ext = os.path.splitext(filename)
            # Split the name into first name and last name
            names = name.split()
            if len(names) > 1:
                
                new_name = "".join(names)         # Remove spaces between the first name and last name
                
                new_name = f"{new_name}{ext}"     # Add new file name to extension
                
                new_path = os.path.join(directory, new_name)
                os.rename(actual_path, new_path)
                print(f"Renamed- {filename} to {new_name}")
directory_path = "C:/Users/Hams R/OneDrive/Documents/internaudio"
rename_files(directory_path)