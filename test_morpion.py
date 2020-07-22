import pytest 
from morpion import Morpion

@pytest.fixture 
def morpion_human():
    return Morpion()

@pytest.fixture 
def morpion_computer():
    return Morpion(human=False)

def test_init_human(morpion_human):
    mode = morpion_human.mode 
    assert mode, "Should be set to True"

def test_init_computer(morpion_computer):
    mode = morpion_computer.mode 
    assert not mode, "Should be set to False"


