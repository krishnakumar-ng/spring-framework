
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    empDetails = csv.reader(CSVR)

    # colnames = next(empDetails)
    prtyTbl = PrettyTable(next(empDetails))

    # print(*colnames)

    for row in empDetails:
        # print(*row)
        prtyTbl.add_row(row)

print(prtyTbl)

