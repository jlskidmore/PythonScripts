import csv
data = csv.reader(open("list1.txt"))
dict = {}

# loop through csv, create dictionary with first value as key, second value as value
with open("list1.txt") as file1:
    csv_reader = csv.reader(file1, delimiter=',')
    for row in csv_reader:
        dict.update({row[0]: row[1]})

# loop through list2 checking each line as key in dict
with open("list2.txt") as file2:
    txt_reader = csv.reader(file2, delimiter='\n')
    for i in txt_reader:
        if i[0] in dict:
            print("%s,%s" % (i[0], dict.get(i[0])))
        else:
            print("%s,is not in the list" % (i[0]))
