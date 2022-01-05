log_file = open("um-server-01.txt") #opens the file to import data


def sales_reports(log_file): #creating a function called 'sales report' that takes in one defined parameter
    for line in log_file: #iterating through the list
        line = line.rstrip() #going through each line and removing trailing characters
        day = line[0:3] #returns the info in the first column and the 4th
        if day == "Mon": #if loop that searches for 'Tuesday" in those columns
            print(line) #print the line if for loop criteria is met

def melons_over10(log_file):
    for line in log_file:
        line = line.rstrip()
        over10 = line[5]
        if over10 > "10":
            print(over10)

sales_reports(log_file) #returns the information

melons_over10(log_file)
