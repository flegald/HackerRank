"""Tests for Save The Prisoner"""
import sys
sys.path.append("..")

from SaveThePrisoner import poison_sweets

def test_simple():
    assert poison_sweets(1, 1, 1) == 1

def test_no_loop():
    assert poison_sweets(10, 3, 1) == 2

def test_loop():
    assert poison_sweets(10, 5, 8) == 2

def test_longer_loop():
    assert poison_sweets(10, 9, 8) == 6

def test_more_sweets_than_prisoners():
    assert poison_sweets(10, 15, 8) == 2

def test_double_loop():
    assert poison_sweets(10, 25, 8) == 2


#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]