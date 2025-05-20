
def subtract_seven(num):
	num = num - 7
	return num
def main():
	num: int = 10
	num = subtract_seven(num)
	print("this should be Three: ", num)

if __name__ == '__main__':
	main()
