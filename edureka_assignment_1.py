# Assignment1 Q1
text = 'Discover, Learning, with, Edureka'
count_of_a = text.count('a')
print('Number of "a" in string :' + str(count_of_a))
count_of_o = text.count('o')
print('Number of "o" in string :' + str(count_of_o))
count_of_L = text.count('L')
print('Number of "L" in string :' + str(count_of_L))
count_of_N = text.count('N')
print('Number of "N" in string :' + str(count_of_N))

#Q2

text1 = 'www.edureka.in'
substr1 = text1[:3]
substr11 = substr1.replace('w','')
substr2 = text1[12:]
substr22 = substr2.replace('w','')
substr3 = text1[3:12]
text2 = substr11 + substr3 + substr22
print("Remove all w\'s before and after .edureka. is : " +text2)

#Q2 b

substrLcBefore =  ''.join(c for c in substr1 if c.islower())
substrAfterRemoveLcBefore =  substr1.replace(substrLcBefore,'')

substrLcAfter =  ''.join(c for c in substr2 if c.islower())

substrAfterRemoveLcAfter =  substr2.replace(substrLcAfter,'')


text3 = substrAfterRemoveLcBefore + substr3 + substrAfterRemoveLcAfter
print("Remove all lowercase letter before and after .edureka. is : " +text3)

#Q2 c
newstring = ''
for a in text1:
	if(a.isprintable()) == True:
		newstring+=' '
	else:
		newstring+= a
print("Remove all printable characters: " +newstring)

#Q3 a

print(type(0X7AEb))
b = 3+4j
print(type(b))
c= 1234
print(type(c))

d = 3.14e-2
print(type(d))
		
#Q4 a

print("My name is %s and first character is: %c" % ('Kaushal', 'K'))

#Q4 b

print("Signed decimal integer: %i" % (9898))

#Q4 c
variable =  14
print("Octal integer: %o" % (variable))

#Q4 d
variable =  14
print("Hexadecimal integer(Uppercase letter):  %X" % (variable))

#Q4 e
variable =  14
print("Floating point real number:  %f" % (variable))

#Q4 f
variable =  14
print("Exponential notation (with lowercase 'e'):  %e" % (variable))

