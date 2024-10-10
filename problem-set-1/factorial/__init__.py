import check50
import re

@check50.check()
def fileExists():
    """ among us checking file is the exist """
    check50.exists("factorial.py")


@check50.check(fileExists)
def checkForRecursion():
    """ checking if ur factorial function uses recursion """
    with open("factorial.py") as file:
        file_content = file.read()
        if not re.search(r"def factorial\(.*\):.*\n.*factorial\(.*\)", file_content, re.DOTALL):
            raise check50.Failure("factorial function does not use recursion")


@check50.check(fileExists)
def check_for_exit_none():
    """ check if program quit after no user input """
    check50.run("python3 factorial.py").stdin("").exit()


@check50.check(fileExists)
def check_for_exit_negative():
    """ check if program quit after a negative input """
    check50.run("python3 factorial.py").stdin("-69").exit()


@check50.check(fileExists)
def check_for_exit_zero():
    """ check if program quit after zero input"""
    check50.run("python3 factorial.py").stdin("0").exit()


@check50.check(fileExists)
def test0():
    """ check 5! (expected 120) """
    check50.run("python3 factorial.py").stdin("5").stdout(program_output(120), "120\n").exit()


@check50.check(fileExists)
def test1():
    """ check 1! (expected 1) """
    check50.run("python3 factorial.py").stdin("1").stdout(program_output(1), "1\n").exit()


@check50.check(fileExists)
def test2():
    """ check 7! (expected 5040) """
    check50.run("python3 factorial.py").stdin("7").stdout(program_output(5040), "5040\n").exit()


def program_output(num):
    return fr"(^|[^\d]){num}(?!\d)"
