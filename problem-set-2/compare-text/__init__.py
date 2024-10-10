import check50


@check50.check()
def fileExists():
    """check file exist"""
    check50.exists("compare-text.py", "harry-potter.txt", "lotr.txt")
    check50.include("expected_output.txt")


@check50.check(fileExists)
def correctOutput():
    """ check correct output """
    program_output = check50.run("python3 compare-text.py").stdout()
    expected_output = open("expected_output.txt", 'r').read()

    if program_output != expected_output:
        check50.Mismatch(expected_output, program_output, help=None)
    
    