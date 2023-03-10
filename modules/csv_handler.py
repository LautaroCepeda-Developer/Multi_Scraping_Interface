import csv

# dialects: 'excel' 'excel-tab' 'unix'
path = str #File path
fileName = str #File name

completeRoute = path + "\\" + fileName + ".csv" #Complete route for the file constructor

def fileCreator(route):
    file = open(route,"w") #File creator

