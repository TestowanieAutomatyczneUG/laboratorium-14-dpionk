Feature: ISBN Number
  Scenario Outline: ISBN Number
    Given there is a ISBN Number validator
    When the given number is <number>
	Then we get <result>
		Examples:
			| number 			| result |
			| 978-3-16-148410-0 | True |
			| 9783161484100 	| True |
			| 1-4028-9462-7  	| False  |
			| 99921-58-10-4		| False |
			| 97-801-3-60-918-13 	| True |
			| 09507-56 			| False |
      		| 54337646532123	| False |
      		| 978-1-56619-909-4		| True |
      		| 234 				| False |