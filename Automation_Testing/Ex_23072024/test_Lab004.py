import pytest
import allure


@allure.title("TC#1 - Verify that 2-2 is equal to 0")
@allure.description("This is a smoke Test case which checks - verify that 202 is equal to 0")
@pytest.mark.smoke
def test_sub():
    assert 2-2 == 0

@allure.title("TC#2 - verify that 3-3 is equal to 0")
@allure.description("This is a regression Test case which checks - verify that 3-3 is equal to 0")
@pytest.mark.regression
def test_sub1():
    assert 3-3 == 0


@allure.title("TC#3 - verify that 1-1 is equal to 0")
@allure.description("This is a smoke Test case which checks - verify that 1-1 is equal to 0")
@pytest.mark.smoke
def test_sub2():
    assert 1-1 == 0

@allure.title("TC#4 - verify that 0-0 is equal to 0")
@allure.description("This is a sanity Test case which checks - verify that 0-0 is equal to 0")
@pytest.mark.sanity
def test_sub3():
    assert 0-0 == 0

@allure.title("TC#5 - verify that 0-0 is not equal to 0")
@allure.description("This is a skip Test case which checks - verify that 0-0 is not equal to 0")
@pytest.mark.skip(reason="Not working")
def test_sub4():
    assert 0-0 != 0



@allure.title("TC#5 - verify that 0-0 is not equal to 0")
@allure.description("This is a regresssion Test case which checks - verify that 0-0 is not equal to 0")
@pytest.mark.regression
def test_sub5():
    assert 0-0 != 0

# http://192.168.1.4:49863/index.html