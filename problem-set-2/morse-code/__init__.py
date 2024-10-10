import check50
import re

@check50.check()
def fileExists():
    """ among us checking if ur file isn't an imposter"""
    check50.exists("morse-code.py")


@check50.check(fileExists)
def test0():
    """ attempting to translate "among us" """
    program_output = check50.run("python3 morse-code.py").stdin("among us").stdout()
    match = re.search(r"([-./].+)", program_output)
    if not match:
        raise check50.Failure("Output does not contain morse code. If it does if you run it independently, contact onscript. on discord")
    
    program_output = match.group(1).strip()
    expected_output = ".- -- --- -. --. / ..- ..."

    if program_output != expected_output:
        raise check50.Mismatch(expected_output, program_output, help=None)


@check50.check(fileExists)
def test1():
    """ attempting to translate "hello world" """
    program_output = check50.run("python3 morse-code.py").stdin("hello world").stdout()
    match = re.search(r"([-./].+)", program_output)
    if not match:
        raise check50.Failure("Output does not contain morse code. If it does if you run it independently, contact onscript. on discord")
    
    program_output = match.group(1).strip()
    expected_output = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

    if program_output != expected_output:
        raise check50.Mismatch(expected_output, program_output, help=None)


@check50.check(fileExists)
def test2():
    """ attempting to translate "bro i suck at regex" """
    program_output = check50.run("python3 morse-code.py").stdin("bro i suck at regex").stdout()
    match = re.search(r"([-./].+)", program_output)
    if not match:
        raise check50.Failure("Output does not contain morse code. If it does if you run it independently, contact onscript. on discord")
    
    program_output = match.group(1).strip()
    expected_output = "-... .-. --- / .. / ... ..- -.-. -.- / .- - / .-. . --. . -..-"

    if program_output != expected_output:
        raise check50.Mismatch(expected_output, program_output, help=None)