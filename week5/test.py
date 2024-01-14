#q6
import sys
import shutil

def copy_file(file_name):
    '''Copy file from one file to another.'''
    shutil.copyfile(file_name, 'destination.txt')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Invalid input")

    else:
        file_name = sys.argv[1]
    
    copy_file(file_name)   
