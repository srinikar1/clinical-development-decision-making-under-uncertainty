#List of functions used to read and write files
import os

# -------------------------------------------------
#write a string to a file
def write_to_file (file_name, string):
    f = open(file_name, "a")
    f.write(string + '\n')
    f.close()
    pass

# -------------------------------------------------
#Write a dataframe for a file
def df_to_csv (df, filename):
    df.to_csv(filename)


# -------------------------------------------------
#Remove a file from the file system.
def remove_file (file_name):
    if(os.path.isfile("file_name")):
        #os.remove() function to remove the file
        os.remove("file_name")
        #Printing the confirmation message of deletion
        print("File Deleted successfully")
    else:
        print("File does not exist")
        #Showing the message instead of throwing an error
