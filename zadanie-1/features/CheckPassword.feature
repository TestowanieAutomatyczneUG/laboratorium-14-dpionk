Feature: CheckPassword

	Klasa sprawdza, czy podany ciąg znaków spełnia wymagania prawidłowego hasła (co najmniej 8 znaków, 1 wielka litera,1 mała, cyfra i znak specjalny)

	Scenario Outline: Password checker 
	Given there is a password checker
	When the password is <password>
	Then we get <result>

	Examples:
		| password			| result		|
		| "kF$4"			| False			|
		| "gdfgfd345435"	| False			|
		|"sdfdFFFF5464565"  | False			|
		|"dsfsdFFFF$$$$2021"| True 			|
