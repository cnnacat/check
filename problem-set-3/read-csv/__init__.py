import check50
import re

@check50.check()
def fileExists():
    check50.exists("read-csv.py")
    check50.include("house-points.csv")


@check50.check(fileExists)
def checkForFileOpen():
    """checking if the csv file was opened"""
    with open("read-csv.py") as file:
        file_content = file.read()
        if not re.search(r"def\s+printCSV\s*\(\s*\)\s*:\s*.*?house-points\.csv", file_content, re.DOTALL):
            raise check50.Failure("csv file was never opened in the code")
        

@check50.check(fileExists)
def checkOutput():
    """ checking for expected output """
    program_output = check50.run("python3 read-csv.py").stdout()
    expected_output = open("house-points.csv", 'r').read()

    if expected_output != program_output:
        check50.Mismatch(expected_output, program_output, help=None)

    