import check50
import csv

@check50.check()
def fileExists():
    """ checking for file existence """
    check50.exists("write-csv.py")


@check50.check(fileExists) #potential failure point, standardize input/output
def writeToCSV():
    """attempting to write to csv"""
    check50.run("python3 write-csv.py").stdin("dataHeader1").stdin("dataHeader2").stdin("a1").stdin("b1").stdin("a2").stdin("b2").stdin("a3").stdin("b3")


@check50.check(fileExists)
def csvExists():
    """checking csv file exists (must be named "myCSV.csv"!!! also, since this check can't automatically create a file, myCSV.csv must exist first. so run the program once)"""
    check50.exists("myCSV.csv")
    check50.include("myCSV.csv")


@check50.check(csvExists) #potential failure point, standardize csv format
def checkCSVContent():
    """checking csv contents"""
    with open("myCSV.csv") as infile:
        fieldnames = ["dataHeader1", "dataHeader2"]

        # Init list and the data of the expected lists
        dataHeaderSet1 = []
        dataHeaderSet2 = []
        expectSet1 = ["a1", "a2", "a3"]
        expectSet2 = ["b1", "b2", "b3"]

        # Extract data
        reader = csv.DictReader(infile, fieldnames=fieldnames)
        for row in reader:
            dataHeaderSet1.append(row["dataHeader1"])
            dataHeaderSet2.append(row["dataHeader2"])

        if dataHeaderSet1 != expectSet1:
            check50.Mismatch(expectSet1, dataHeaderSet1, help=None)
        
        if dataHeaderSet2 != expectSet2:
            check50.Mismatch(expectSet2, dataHeaderSet2, help=None)

        