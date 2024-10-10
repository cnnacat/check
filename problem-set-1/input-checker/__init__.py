import check50
import re

@check50.check()
def fileExists():
    """ check if file is alive and exists and not dinosaur status """
    check50.exists("input-checker.py")


@check50.check(fileExists)
def test_indefinite_loop():
    """ test if program handles words """
    check50.run("python3 input-checker.py").stdin("sussy").reject().stdin("4.20").reject().stdin("1").exit()


@check50.check(fileExists)
def test_output():
    """ check if program outputs as expected """
    check50.run("python3 input-checker.py").stdin("69").stdout(program_output(69), "69\n").exit()    


def program_output(num):
    return fr"(^|[^\d]){num}(?!\d)"