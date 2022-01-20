from behave import *
from src.sample.FizzBuzz import FizzBuzz

@given('there is FizzBuzz')
def step_impl(context):
    context.fizzBuzz = FizzBuzz()


@when('I give {number}')
def step_impl(context, number):
    context.result = context.fizzBuzz.game(int(number))

@then('Its Fizz')
def step_impl(context):
    assert context.result == "Fizz"


@then('Its FizzBuzz')
def step_impl(context):
    assert context.result == "FizzBuzz"


@then('Its Buzz')
def step_impl(context):
    assert context.result == "Buzz"

@then('Its {result}')
def step_impl(context, result):
    assert context.result == int(result)