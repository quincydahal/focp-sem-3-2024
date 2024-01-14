import sys
txtfile = sys.argv[1]
with open(txtfile, "rt") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = f"{i+1}. {lines[i].strip()}"

for i in lines:
    print(i)