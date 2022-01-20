Feature: Author
  Zadaniem klasy jest sprawdzenie czy tworzenie obiektu author działa poprawnie

  Scenario Outline: Create new author
    Given there is a firstname equal to <firstname>
    And lastname is <lastname>
    And email is <email>
    When creating an author
    Then author is <created>

    Examples:
      | firstname | lastname | email                | created |
      | Daria       | Pionk | dp@gmail.com  | created |
      | Pionk       | Daria      | pd@gmail.com | created |
      | Kasia    | Bojarska    | kb@wp.pl         | created |
      |           | Nazwisko | dskfsl@wp.pl | not created |
      | Imie      |           |dfgdfg@gmail.com | not created |
      | Imie       | Nazwisko |                 | not created | 