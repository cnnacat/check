import check50


@check50.check()
def fileExists():
    """ check file exist """
    check50.exists("triangle.py")
    check50.include("1.txt", "6.txt", "9.txt", "12.txt")


@check50.check(fileExists)
def check_reject_negative():
    """ check reject negative """
    check50.run("python3 triangle.py").stdin("-69").reject()


@check50.check(fileExists)
def check_reject_empty():
    """ check reject empty input """
    check50.run("python3 triangle.py").stdin("").reject()


@check50.check(fileExists)
def check_reject_zero():
    """ check reject zero """
    check50.run("python3 triangle.py").stdin("0").reject()


@check50.check(fileExists)
def check_input_1():
    """ check if output correct if input = 1"""
    program_output = check50.run("python3 triangle.py").stdin("-1").reject().stdin("1").stdout()
    expected_output = open("1.txt").read()
    check_output(expected_output, program_output)


@check50.check(fileExists)
def check_input_6():
    """ check if output correct if input = 6"""
    program_output = check50.run("python3 triangle.py").stdin("6").stdout()
    expected_output = open("6.txt").read()
    check_output(expected_output, program_output)


@check50.check(fileExists)
def check_input_9():
    """ check if output correct if input = 9"""
    program_output = check50.run("python3 triangle.py").stdin("9").stdout()
    expected_output = open("9.txt").read()
    check_output(expected_output, program_output)


@check50.check(fileExists)
def check_input_12():
    """ check if output correct if input = 12"""
    program_output = check50.run("python3 triangle.py").stdin("12").stdout()
    expected_output = open("12.txt").read()
    check_output(expected_output, program_output)



def check_output(expected_output, program_output):
    # split expected and actual outputs into lines (into a list)
    expected_lines = expected_output.splitlines()
    output_lines = program_output.splitlines()


    # remove any empty lines from the actual output
    cleaned_output_lines = []
    for line in output_lines:
        if line != "":
            cleaned_output_lines.append(line)


    # check if num of lines match for expected and input
    if len(cleaned_output_lines) != len(expected_lines):
        raise check50.Mismatch(expected_lines, cleaned_output_lines, help="The number of lines in the output does not match the expected output.")


    # compare each line of expected to input
    for expected_line, output_line in zip(expected_lines, cleaned_output_lines):
        if expected_line != output_line:

            # check for trailing whitespace issues
            if expected_line.rstrip() == output_line.rstrip():
                help = "Did you add too much trailing whitespace to the end of your triangle?"

            # check for additional characters at the beginning of each line
            elif expected_line == output_line[1:]:
                help = "Are you printing an additional character at the beginning of each line?"

            else:
                help = "The output does not match the expected format."

            raise check50.Mismatch(expected_lines, cleaned_output_lines, help=help)


    # if match, return correct
    return
