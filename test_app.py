from app import myphone



def test_myphone():
    assert myphone()== "9315723279"

def reverse_text(text):
    return text[::-1]

def test_reverse_text():
    assert reverse_text('python') == 'nohtyp'


def sum(i,j):
    return i+j


def test_sum():
    i=2
    j=3
    assert sum(i,j)==5

# very basic flow if assertion matches our expected ans then test passes else fails
# the libray we are using for testing is pytest it traverse the current folder and if anyfile 
# name start with test it run those file give the result of test(pass or fail)