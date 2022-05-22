from quickselect import quickselect
from time import time
import os
from random import *
import csv
path1 = 'C:\semester-project-quick-select-qsort\data'
rez2 = os.listdir(path1)
for j in rez2:
    path2 = path1 + f"\{j}"
    rez3 = os.listdir(path2)
    for k in rez3:
        path3 = path2 + f"\{k}"
        rez4 = os.listdir(path3)
        for l in rez4:
            list_of_nums=[]
            with open(f"{path3}\{l}", encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file,delimiter="\n")
                for row in csv_reader:
                    list_of_nums.append(int(row[0]))
            t1 = time()
            d = randint(0,len(list_of_nums))
            quickselect(list_of_nums,d)
            t2 = time()
            print(t2-t1,f"{path3}\{l}")
        print(f"закончился файл {path3}")
    print(f"закончился файл {path2}")
print(f"закончился файл {path1}")           
                


