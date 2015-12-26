# Seoul Restaurant Guide Search
# Asks for 3 inputs - area, rating and type of food
# Displays matching results from the database
# Written by Sam Chapman - 2015

import sqlite3
conn = sqlite3.connect('SRG.db')
c = conn.cursor()

area = raw_input("Enter your district: ")
rate = int(raw_input("Enter a minimum rating (1-4): "))
food = raw_input("Enter a food type: ")
print ""

c.execute('SELECT * FROM restaurants WHERE address LIKE ? AND rating > ? AND type LIKE ? 
    ORDER BY rating DESC', ('%'+area+'%', rate-1, '%'+food+'%'))

while True:
   	row = c.fetchone()
    	
   	if row == None:
   		print '*' * 75
   		break

   	print '*' * 75
   	print 'Name:    ',row[1]
   	print 'Rating:  ',row[3]
   	print 'Price:   ',row[2]
   	print 'Type:    ',row[4]
   	print 'Website: ',row[5]
   	print 'Address: ',row[6]
   	print 'Subway:  ',row[7]
   	print 'Phone:   ',row[8]
   	print '*' * 75
