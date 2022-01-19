from behave import *
from src.ISBNnumber import ISBNnumber

@given('there is a ISBN Number validator')
def step_imp(context):
	context.validate = ISBNnumber.validate

@when('the given number is {number}')
def step_imp(context,number):
	context.result = context.validate(number)

@then('we get {result}')
def step_imp(context,result):
	assert str(context.result) == result