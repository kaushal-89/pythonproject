#Q1
total = input('What is the total amount for your online shopping?')
country = input('Shipping within the US or Canada?')
if country == "US":
	if int(total) <= 50:
		print("Shipping Costs $6.00")
	elif int(total) <= 100:
		print("Shipping Costs $9.00")
	elif int(total) <= 150:
		print("Shipping Costs $12.00")
	else:
		print("FREE")
if country == "Canada":
	if total <= "50":
		print("Shipping Costs $8.00")
	elif int(total) <= 100:
		print("Shipping Costs $12.00")
	elif int(total) <= 150:
		print("Shipping Costs $15.00")
	else:
		print("FREE")
		
		
#Q2
name = input('Enter your name')
print('Hello '+name)

#Q3
fahrenheit = input('Enter fahrenheit temperature ')
celsius = (int(fahrenheit) - 32) / 1.8
print('%0.1f degree Fahrenheit is equal to %0.1f degree Celsius' %(float(fahrenheit),float(celsius)))

#Q4
hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
pay = float(hours) * float(rate)
print('Pay: %f' %(pay))

#Q5
a = [4,7,3,2,5,9]
for l in a:
	print('Position of %i is %i' %(l,a.index(l)))
	
#Q6
import string
alphabet_dict = {i:j for (i, j) in zip(string.ascii_lowercase[:27], range(1,27))}
print(alphabet_dict)

#Q7
dict1 = {'a':1,'b':2}
dict1_reverse = {v: k for k,v in dict1.items()}
print(dict1_reverse)

#Q8
L = ['a','b','c','d']
dict_result = {k:v for v,k in enumerate(L,start=1)}
print(dict_result)

#Q9
score = input('Enter score between 0.0 and 1.0: ')
if float(score) > 0.0 and float(score) < 1.0:
	if float(score)>=0.9:
		print('Grade is A')
	elif float(score)>=0.8:
		print('Grade is B')
	elif float(score)>=0.7:
		print('Grade is C')
	elif float(score)>=0.6:
		print('Grade is D')
	elif float(score)<0.6:
		print('Fail')
else:
	print('Error')
	
	




