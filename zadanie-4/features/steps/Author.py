from behave import *
from src.Author import Author

@given(u'there is a firstname equal to {firstname}')
def step_imp(context, firstname):
	context.firstname=firstname


@given(u'there is a firstname equal to ')
def step_imp(context):
	context.firstname=''

@given(u'lastname is {lastname}')
def step_imp(context, lastname):
	context.lastname=lastname

@given(u'lastname is ')
def step_imp(context):
	context.lastname=''

@given(u'email is {email}')
def step_imp(context, email):
	context.email=email

@given(u'email is ')
def step_imp(context):
	context.email=''

@when('creating an author')
def step_imp(context):
    try:
        context.author = Author(context.firstname, context.lastname, context.email)
    except ValueError as e:
        context.e = e

@then('author is {created}')
def step_imp(context, created):
	if created == 'created':
		assert isinstance(context.author, Author)
	else:
		assert isinstance(context.e, ValueError)