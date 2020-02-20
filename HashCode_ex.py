import numpy

path = "a_example.in"
	



def main():
	B,L,D = map(int, f.readline().split(' '))
	score = map(int, f.readline().split(' '))
	print(B ,L, D)
	print(score)
	library = []
	for l in range(0,L):
		num_book,time, num_scan = map(int, f.readline().split(' '))
		bookID = map(int, f.readline().split(' '))
		library.append(((num_book,time, num_scan), bookID))
	print(index)


if __name__ == '__main__':
	f = open(path, "r")
	main()