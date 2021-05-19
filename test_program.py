import pytest

from Calculate import DataResult


def test_one():
    test_cls = DataResult("example_data.csv")

    test_data = [{'Comp': [0, 0, 0, 0, 0, 0, 0, 0, 110.0, 280.0, 200.0],
                  'Non-Comp': [0, 45.2, 110.0, 110.0, 147.0, 50.0, 125.0, 150.0, 55.0, 140.0, 100.0],
                  'Non-C': [45.2, 110.0, 110.0, 147.0, 50.0, 125.0, 150.0, 55.0, 140.0, 100.0, 200.0],
                  'Test1': [0, 0, 0, 50.0, 125.0, 150.0, 55.0, 140.0, 100.0, 100.0, 200.0],
                  'ABC': [0, 0, 0, 0, 0, 0, 0, 185.0, 100.0, 100.0, 200.0],
                  'Test3': [0, 0, 0, 0, 0, 0, 0, 0, 10.0, 20.0, 320.0]}]

    assert test_cls.fin_results == test_data


def test_two():
    test_cls = DataResult("test_two_data.csv")

    test_data = [{'Comp': [0, 0, 0, 0, 0, 0, 0, 110.0, 280.0, 200.0],
                  'Non-Comp': [45.2, 110.0, 110.0, 147.0, 50.0, 125.0, 150.0, 55.0, 140.0, 100.0]}]

    assert test_cls.fin_results == test_data


def test_three():
    test_cls = DataResult("test_three_data.csv")

    test_data = [{'Test3': [50.0, 125.0, 150.0, 55.0, 140.0, 100.0, 100.0, 200.0],
                  'calc': [0, 0, 0, 0, 185.0, 100.0, 100.0, 200.0],
                  'nonc': [0, 0, 0, 0, 0, 10.0, 20.0, 320.0]}]

    assert test_cls.fin_results == test_data
