# Define Function and Argument

def fizz_buzz(number):

# Return if number is divisible by 3
	if (number % 3 == 0) and (number % 5 != 0):
		return 'Fizz'

# Return if Number is divisible by 3 & 5
	elif (number % 3 == 0) and (number % 5 == 0):
		return 'FizzBuzz'

#Return if Number is divisible by 5	
	elif (number % 3 != 0) and (number % 5 == 0):
		return 'Buzz'

	else:
		return number