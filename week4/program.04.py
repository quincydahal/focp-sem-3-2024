#1
def get():
    num = float(input("Enter a number: "))
    return num

def test(number):
    if 0 <= number <= 100:
        return True
    
    else:
        return False
    
def display(result):
    print("The result is:",result)
    

number = get()
result = test(number)
display(result)


#2
def get():
    sentence = input("Enter a sentence")
    return sentence

def upper(sent):
    u_count = 0
    for i in sent:
        if i.isupper():
            u_count += 1
    return u_count        

def lower(sent):
    l_count = 0
    for i in sent:
        if i.islower():
            l_count += 1
    return l_count

def display(upper_case, lower_case):
    print('Number of Upper Case Letters :', upper_case)
    print('Number of Lower Case Letters :', lower_case)

sent = get()
upper_case = upper(sent)
lower_case = lower(sent)
display(upper_case, lower_case)


#3
def get():
    greetings = input(f"Enter you name: ")
    return greetings

def display(greet):
    if greet == {}:
        print("Hello stranger")
        
    else:
        greet = greet.capitalize()
        print(f"Hello {greet}. How are you?")

greet = get()
display(greet)


#4
def get():
    """Asks for user input and removes the last character if necessary."""
    user_string = input("Enter a string: ")
    return user_string

def calculate(word):
    if len(word) <= 1:
        return(word)

    else:
        return(word[:-1])
    
def display(result):
    print("The string is: ",result)
    
word = get()
result = calculate(word)
display(result)


#5
def get():
    temperature = float(input("Enter the temperature: "))
    unit_of_temperature = input("Enter the unit of the temperature(c/f): ")
    unit_of_temperature = unit_of_temperature.lower()
    return(temperature, unit_of_temperature)

def calculate_faherenheit(temp):
    faherenheit = (temp*9/5)+32
    return(faherenheit)

def calculate_centigrade(temp):
    centigrade = ((temp-32)*5)/9
    return (centigrade)

def display(FC, CF, u_temp):
    if u_temp =="c" or u_temp == "centigrade":
        print("The value in centigrade is: ",CF)
    elif u_temp == "f"or u_temp == "faharenheit":
        print("The value in faherenheit is: ",FC)

    else:
        print("!!! Invalid value !!!")

temp, u_temp = get()
FC = calculate_faherenheit(temp)
CF = calculate_centigrade(temp)
display(FC, CF, u_temp)


#6
def get():
    temperature = float(input("Enter the temperature: ")) 
    print(f"The value in centigrade is: {temperature} C")
    return(temperature)

def calculate_faherenheit(temp):
    faherenheit = (temp*9/5)+32
    return(faherenheit)

def display(CF):
        print("The value in faherenheit is: ",CF,"F")

temp = get()
FC = calculate_faherenheit(temp)
display(FC)


#7
from statistics import mean
def get():
    new_list = []
    for _ in range (1,7):
        temperature = float(input("Enter temperature: "))
        new_list.append(temperature)
    return new_list

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

def calculate_mean(temp):
    # sums = sum(temp)
    # means = sums / len(temp)
    means = mean(temp)
    return means

def display(max, min, means):
    print("The maximum value is: ",max)
    print("The minimum value is: ",min)
    print("The mean value is: ",means)


temp = get()
max = calculate_max(temp)
min = calculate_min(temp)
means = calculate_mean(temp)
display(max, min, means)


#8
from statistics import mean
def get():
    new_list = []
    loop = 1
    while loop == 1:
        temperature = float(input("Enter temperature: "))
        new_list.append(temperature)
        if temperature == {}:
            continue
        elif temperature:
            break
        else:
            pass
    return new_list

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

def display(max, min, means,temp):
    print("The maximum value is: ",max)
    print("The minimum value is: ",min)
    print("The mean value is: ",means)


temp = get()
max = calculate_max(temp)
min = calculate_min(temp)
means = caluculate_mean(temp)
display(max, min, means)
