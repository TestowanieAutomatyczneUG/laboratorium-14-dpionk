from behave import *
from src.CheckPassword import CheckPassword
from assertpy import *

@given('There is a password checker')
def step_imp(context):
	context.passwordChecker = CheckPassword().ValidPassword


@when('the password is {password}')
def step_imp(context, password):
	context.result = context.passwordChecker(password)

@then('we get {result}')
def step_imp(context, result):
	assert_that(str(context.result)).is_equal_to(result)
	