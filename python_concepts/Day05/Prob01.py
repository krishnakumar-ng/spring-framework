
FL = open("Employee.csv", "r")

for line in FL.readlines():
    name = line.split(",")[1]
    print(name)

FL.close()