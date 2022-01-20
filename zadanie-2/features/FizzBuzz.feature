Feature: FizzBuzz
  Scenario Outline: FizzBuzz
    Given there is FizzBuzz
    When I give <number>
    Then Its <result>
    Examples:
      | number | result |
      | 25 | Buzz |
      | 9 | Fizz |
      | 15 | FizzBuzz |
      | 7 | 7 |