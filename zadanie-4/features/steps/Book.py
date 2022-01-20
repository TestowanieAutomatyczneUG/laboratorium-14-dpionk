from behave import *
from src.Book import Book
from src.Author import Author

@given('there is an title {title}')
def step_impl(context, title):
    context.title = title


@given('there is an author {firstname}, {lastname}, {email}')
def step_impl(context, firstname, lastname, email):
    context.author = Author(firstname, lastname, email)


@given('there is an ISBN number equal to {isbn}')
def step_impl(context, isbn):
    context.isbn = isbn

@when('we try to create a book')
def step_imp(context):
    try:
        context.book = Book(context.title, context.author, context.isbn)
    except Exception as e:
        context.e = True

@then('the book is {created}')
def step_imp(context,created):
	if created == 'created':
		assert context.book
	else:
		assert context.e