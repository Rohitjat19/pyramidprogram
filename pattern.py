# Programs for printing pyramid patterns

def upper_pyramid(num):
	for rows in range(0, num):
		for column in range(0, rows + 1):
			print("*", end = " ")
		print(" ")

# lower pyramid patterns                                  
def lower_pyramid(num):
     for rows in range(num, 1, - 1):  
        for column in range(0, rows - 1):  
            print("*", end = ' ')  
        print(" ") 

num = 5
upper_pyramid(num)
lower_pyramid(num)

