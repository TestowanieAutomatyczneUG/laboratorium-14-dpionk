class ISBNnumber:
	def validate(n):
		isbn = n.replace('-','')
		if len(isbn) != 13:
			return False
		sum = 0
		index = 0
		for i in isbn:
			index += 1
			if (index)%2 == 0:
				sum += int(i)*3
			else:
				sum += int(i)*1
		return sum % 10 == 0

print(ISBNnumber.validate('978-1-56619-909-4'))