import check50


@check50.check()
def fileExists():
    """ am ongus """
    check50.exists("unique-words.py", "harry-potter.txt")


@check50.check(fileExists)
def correctOutput():
    """ test if program outputs expected value"""
    program_output = check50.run("python3 unique-words.py").stdout()
    expected_output = {'Nearly': 1, 'ten': 1, 'years': 2, 'had': 7, 'passed': 2, 'since': 1, 'the': 16, 'Dursleys': 2, 'woken': 1, 'up': 2, 'to': 1, 'find': 1, 'their': 2, 'nephew': 1, 'on': 6, 'front': 3, 'step': 1, 'but': 3, 'Privet': 1, 'Drive': 1, 'hardly': 1, 'changed': 1, 'at': 4, 'all': 2, 'The': 2, 'sun': 1, 'rose': 1, 'same': 2, 'tidy': 1, 'gardens': 1, 'and': 4, 'lit': 1, 'brass': 1, 'number': 1, 'four': 1, 'door': 1, 'it': 3, 'crept': 1, 'into': 1, 'living': 1, 'room': 2, 'which': 1, 'was': 5, 'almost': 1, 'exactly': 1, 'as': 1, 'been': 2, 'night': 1, 'when': 1, 'Mr': 1, 'Dursley': 2, 'seen': 1, 'that': 3, 'fateful': 1, 'news': 1, 'report': 1, 'about': 1, 'owls': 1, 'Only': 1, 'photographs': 2, 'mantelpiece': 1, 'really': 1, 'showed': 2, 'how': 1, 'much': 1, 'time': 1, 'Ten': 1, 'ago': 1, 'there': 2, 'lots': 1, 'of': 3, 'pictures': 1, 'what': 1, 'looked': 1, 'like': 1, 'a': 5, 'large': 2, 'pink': 1, 'beach': 1, 'ball': 1, 'wearing': 1, 'differentcolored': 1, 'bonnets': 1, '': 1, 'Dudley': 1, 'no': 2, 'longer': 1, 'baby': 1, 'now': 1, 'blond': 1, 'boy': 2, 'riding': 1, 'his': 3, 'first': 2, 'bicycle': 1, 'carousel': 1, 'fair': 1, 'playing': 1, 'computer': 1, 'game': 1, 'with': 1, 'father': 1, 'being': 1, 'hugged': 1, 'kissed': 1, 'by': 1, 'mother': 1, 'held': 1, 'sign': 1, 'another': 1, 'lived': 1, 'in': 1, 'house': 1, 'too': 1, 'Yet': 1, 'Harry': 1, 'Potter': 1, 'still': 1, 'asleep': 1, 'moment': 1, 'not': 1, 'for': 1, 'long': 1, 'His': 1, 'Aunt': 1, 'Petunia': 1, 'awake': 1, 'her': 1, 'shrill': 1, 'voice': 1, 'made': 1, 'noise': 1, 'day': 1}
    if program_output != expected_output:
        check50.Mismatch(expected_output, program_output, help=None)
    