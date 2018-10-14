from math import sqrt

def reduce_rad(rad):
	perfect = 0
		
	for i in range(4,rad):

		if i > perfect and sqrt(i).is_integer():
			if(rad/i).is_integer():
				perfect = i
	if perfect == 0: perfect = 1
	outside = str
	return(str(sqrt(perfect))+'√('+str(rad/perfect)+')')


i_character = ''
imaginary = False
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

try: 
	rad = sqrt(b**2-(4*a*c))
	radicand = b**2-(4*a*c)

except: 
	imaginary = True
	radicand = -1*(b**2-(4*a*c))
	rad = sqrt(radicand)

if imaginary == True:
	i_character = 'i'

if rad.is_integer() == False:
	rad = reduce_rad(radicand)
	print('Solution 1:\n')
	print(-b, '+', rad, i_character)
	print('_________________\n')
	print('      ',2*a)
	print('\nSolution 2:\n')
	print(-b, '-', rad, i_character)
	print('_________________\n')
	print('      ',2*a)
else: 
	print('Solution 1:')
	print((-b+rad)/2*a)
	print('Solution 2:')
	print((-b-rad)/2*a)


	


