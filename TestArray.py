
items = 25
matrix = [[0 for x in range(items)] for y in range(items)]

def setMatrix():
	for i in range(items):
		for j in range(items):
			matrix[j][i]=i+1

def readMatrix():
	for i in range(matrix[::-1]):
		matrix[10][i] = 0
		print(matrix)		

def main():
    print("Hello World!")
    setMatrix()
    print(matrix)
    readMatrix()

if __name__ == "__main__":
    main()