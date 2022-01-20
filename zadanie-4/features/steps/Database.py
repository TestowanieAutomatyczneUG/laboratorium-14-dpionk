from behave import *
from src.Database import Database
from unittest.mock import *

use_step_matcher('parse')


@given('a book database')
def step_imp(context):
    context.database = Database()


@given('we use {function}, should return {result}')
def step_imp(context, function, result):
    context.database.function = Mock(getattr(Database, function))
    context.database.function.return_expected_result = str(result)

@when('calling function {function}')
def step_imp(context, function ):
    context.result = context.database.function()


@then('we should get {expected_result}')
def step_imp(context, expected_result):
    assert context.result == str(expected_result)