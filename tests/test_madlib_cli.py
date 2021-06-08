from madlib_cli import __version__
from madlib_cli.madlib import read_template, parse_template, merge
sample1 = 'in the {wild} west, {people} used {to} be {cooler} than now'

def test_version():
    assert __version__ == '0.1.0'


# testing the read function

def test_read_template():
    assert read_template('../assets/aa.txt') == 'file not found'
    assert read_template('../file/aa.txt') == 'file not found'

# testing the parsing function
def test_parse_template():
    assert parse_template(sample1) == ['wild','people','to','cooler']
    assert parse_template('czxxzcmkl') == []
    assert parse_template('') == []

# testing the merging function
def test_merge():
    answers = ['east', 'humans', 'eat', 'hbd']
    TIB = ['wild','people','to','cooler']
    assert merge(answers,sample1,TIB) == 'in the east west, humans used eat be hbd than now'
    assert merge(5, 'this was fun' ,TIB) == 'merging error'