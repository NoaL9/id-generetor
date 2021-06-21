def check_id_valid(ID):
	"""	Check if a new ID number is valid.
		:param ID: ID number.
		:type ID: int
		:return: A valid ID number.
		:rtype: int
	"""
	sum = 0  # Initialization of sum which will be the sum of ID's digit number after some menipulation
	lst = [int(x) for x in str(ID)]  # List of ID's digits
	for i in range(9):
		digit = lst[i]
		if i % 2 == 0:  # The position of the digit in the ID number is odd -> i, which is the index of lst, is 0,2,4,6 or 8
			sum = sum + digit
		else:  # The position of the digit in the ID number is even -> i, which is the index of lst, is 1,3,5 or 7
			digit = digit * 2
			if digit <= 9:
				sum = sum + digit
			else:  # digit is a double-digit number that can be at most 18 (9*2)
				unity_digit = digit % 10
				tens_digit = 1  # digit is one of 10, 12, 14, 16, or 18
				sum = sum + unity_digit + tens_digit
	if sum % 10 == 0:
		return(ID)

	
class IDIterator:
	"""A class used to generates a new ID number"""
	def __init__(self, id = 123456780):
		self._id = id
	def __iter__ (self):
		return self		
	def __next__ (self):
		if self._id >= 999999999:
			raise StopIteration()
		self._id += 1
		return(check_id_valid(self._id))
		
				

def id_generator(id = 123456780):
	"""	Generates a new and valid ID number.
		:param ID: ID number.
		:type ID: int
		:return: A valid ID number.
		:rtype: int
	"""
	try:
		lst = (i for i in range(id,999999999,1))
		id = (next(lst))
		while (id):									
			if check_id_valid(id):
				yield check_id_valid(id)
			id = (next(lst))
	except StopIteration as e:
		print("ID number is greater than 999999999.")
		print(e)
	
			
def main():	
	# Taking user inputs
	user_input = input("Enter ID:")
	user_input = user_input.strip()
	if not user_input:
		user_input = "123456780"
	id_maker = input("Generator or Iterator? (gen/it)?")
	id_maker = id_maker.strip()

	# If user choose iterator
	if id_maker == "it":
		print("ID by iteretor:")
		ID = IDIterator(int(user_input)-1)		
		c = 0
		while c < 10: # Print only the first 10 new and valid ID numbers.
			i = next(ID)
			if i:
				print(i)
				c += 1
				
	# If user choose generator
	elif id_maker == "gen":
		print("ID by generetor:")
		ID = id_generator(int(user_input))
		c = 0		
		while c < 10: # Print only the first 10 new and valid ID numbers.
			i = next(ID)
			if i:
				print(i)
				c += 1

	
if __name__ == "__main__":
    main()