Feature: Database

  Scenario: Get books
    Given a book database
    And we use get_books, should return ['Czuła przewodniczka', 'Igrzyska Śmierci', 'Zbrodnia i Kara']
    When calling function get_books
    Then we should get ['Czuła przewodniczka', 'Igrzyska Śmierci', 'Zbrodnia i Kara']

  Scenario: Get book
    Given a book database
    And we use get_book, should return {'title': 'Zbrodnia i Kara', 'author': 'Fyodor Dostoevsky', 'isbn': '978-83-7181-510-2'}
    When calling function get_book
    Then we should get {'title': 'Zbrodnia i Kara', 'author': 'Fyodor Dostoevsky', 'isbn': '978-83-7181-510-2'}

  Scenario: Get book that does not exist
    Given a book database
    And we use get_book, should return not found
    When calling function get_book
    Then we should get not found

  Scenario: Get author
    Given a book database
    And we use get_author, should return {'firstname': 'Fyodor', 'lastname': 'Dostoevsky', 'email': 'fd@gmail.com'}
    When calling function get_author
    Then we should get {'firstname': 'Fyodor', 'lastname': 'Dostoevsky', 'email': 'fd@gmail.com'}
 
  Scenario: Get author that does not exist
    Given a book database
    And we use get_author, should return not found
    When calling function get_author
    Then we should get not found
 
  Scenario: Add book 
    Given a book database
    And we use add_book, should return book added
    When calling function add_book
    Then we should get book added
 
  Scenario: Delete book
    Given a book database
    And we use delete_book, should return book deleted
    When calling function delete_book
    Then we should get book deleted

  Scenario: Delete book which does not exist
    Given a book database
    And we use delete_book, should return not found
    When calling function delete_book
    Then we should get not found