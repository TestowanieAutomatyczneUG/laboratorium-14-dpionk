Feature: Book

    Scenario Outline: Create book
        Given there is an title <title>
        And there is an author Daria, Pionk, dp@gmail.com
        And there is an ISBN number equal to <isbn>
        When we try to create a book
        Then the book is <created>

        Examples:
            | title             | isbn          | created   |
            | The Hunger Games | 978-3-16-148410-0 | created  |
            | Milk & Honey         | 9783161484100 | created    |
            | Book         | 97-801-3-60-918-13  | created    |
            | Some book  | 978-1-56619-909-4 | created |
            | The Hunger Games: Catching Fire | 567           | not created |
            | Book          | True      |not created|
            | Another book         | ''            |not created|
            | Idk some book | 879877923  |not created|
            | Mockingjay | 45654654 |not created|