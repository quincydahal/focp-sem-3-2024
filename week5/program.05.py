#1
import platform

def get_operating_system():
    system_info = platform.system()
    return system_info

if __name__ == "__main__":
    os = get_operating_system()
    print(f"The operating system is: {os}")
    

#2
import sys
value = sys.argv[0: ]
print(f"There are {len(value)} number of arguments.")


#3
import sys
new_list = []
value = sys.argv[1:]
new_list.append(value)
new_list.sort()
print("The shortest value is: ",new_list)


#4
import sys
from statistics import mean
def get(value):
    try:
        new_list = [float(temperature) for temperature in value]
        
        return new_list
    
    except EOFError:
        print("Invalid input please try again.")

def calculate_max(temp):
    # maximum = temp[0]
    # for i in temp:
    #     if i > maximum:
    #         maximum = i

    maximum = max(temp)

    return maximum

def calculate_min(temp):
    # minimum = temp[0]
    # for i in temp:
    #     if i < minimum:
    #         minimum = i

    minimum = min(temp)

    return minimum

def caluculate_mean(temp):
    # sums = sum(temp)
    # means = sums / len(temp)
    means = mean(temp)
    return means

def display(max, min, means):
    print("The maximum value is: ",max)
    print("The minimum value is: ",min)
    print("The mean value is: ",means)


if __name__ == "__main__":

    if len(sys.argv ) >= 2:
        value = sys.argv[1:]
        temp = get(value)
        
    else:
        print("Invalid input!!!")

    max = calculate_max(temp)
    min = calculate_min(temp)
    means = caluculate_mean(temp)
    display(max, min, means)
    
    
#5
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
