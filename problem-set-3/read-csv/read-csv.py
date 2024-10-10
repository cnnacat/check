import csv


def printCSV():
    with open("house-points.csv", 'r') as infile:
        fieldnames = ["House", "Points"]
        reader = csv.DictReader(infile, fieldnames=fieldnames)

        for row in reader:
            print(row["House"], row["Points"])


def main():
    printCSV()

 
if __name__ == "__main__":
    main()