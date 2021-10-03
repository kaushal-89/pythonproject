#Q1
import random
i = 1;
levels = ['easy','intermediate','hard']
ques_types = ['M','A','S','D']
#Addition question answer list
easy_add_list_q_a = [("5","What is 3+2 ?"),("15","What is 9+6 ?"), ("11","What is 6+5 ?")]
medium_add_list_q_a = [("40","What is 30+10 ?"),("100","What is 25+75 ?"),("39","What is 34+5 ?")]
hard_add_list_q_a = [("138","What is 34+104 ?"),("18988","What is 9898+9090 ?"),("9932","What is 9897+35 ?")]

#substration question answer list
easy_add_list_q_s = [("9","What is 14-5 ?"),("10","What is 13-3 ?"),("10","What is 15-5 ?")]
medium_add_list_q_s = [("41","What is 54-13 ?"),("60","What is 80-20 ?"),("38","What is 50-12 ?")]
hard_add_list_q_s = [("824","What is 897-73"),("66868","What is 67654-786 ?"),("5868","What is 6766-898 ?")]

#multiplication question answer list
easy_add_list_q_m = [("4","What is 2*2 ?"),("12","What is 6*2 ?"),("22","What is 11*2 ?")]
int_add_list_q_m = [("24","What is 12*2 ?"),("60","What is 15*4 ?"),("192","What is 16*12 ?")]
hard_add_list_q_m = [("234","What is 26*9 ?"),("804","What is 67*12 ?"),("41952","What is 456*92 ?")]

#division question answer list
easy_add_list_q_d = [("2","What is 4/2 ?"),("5","What is 10/2 ?"),("2","What is 8/4 ?")]
medium_add_list_q_d = [("9","What is 45/5 ?"),("48","What is 96/2 ?"),("6","What is 30/5 ?")]
hard_add_list_q_d = [("15","What is 750/50 ?"),("5120","What is 10240/2 ?"),("24","What is 480/20 ?")]

def quiz():
    x = input("Choose level (easy, intermediate, and hard): ")
    if(levels.count(str(x)) > 0):
        valid_y = 0
        while (valid_y < 1):
            try:
                y = input("Please give us the number of question you want to attempt: ")
                y = int(y)
            except ValueError as e:
                print("Please enter only numbers")
                continue
            else:
                valid_y = 1
                valid_z = 0
                while (valid_z < 1):
                    z = input("Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): ")
                    if (ques_types.count(str(z)) > 0):
                        valid_z = 1
                        q = 1
                        while (q <= int(y)):
                            if x == levels[0]:
                                if z == 'A':
                                    ques = random.choice(easy_add_list_q_a)
                                    print(ques[1])
                                elif z == 'S':
                                    ques = random.choice(easy_add_list_q_s)
                                    print(ques[1])
                                elif z == 'M':
                                    ques = random.choice(easy_add_list_q_m)
                                    print(ques[1])
                                elif z == 'D':
                                    ques = random.choice(easy_add_list_q_d)
                                    print(ques[1])
                            elif x == levels[1]:
                                if z == 'A':
                                    ques = random.choice(medium_add_list_q_a)
                                    print(ques[1])
                                elif z == 'S':
                                    ques = random.choice(medium_add_list_q_s)
                                    print(ques[1])
                                elif z == 'M':
                                    ques = random.choice(int_add_list_q_m)
                                    print(ques[1])
                                elif z == 'D':
                                    ques = random.choice(medium_add_list_q_d)
                                    print(ques[1])
                            else:
                                if z == 'A':
                                    ques = random.choice(hard_add_list_q_a)
                                    print(ques[1])
                                elif z == 'S':
                                    ques = random.choice(hard_add_list_q_s)
                                    print(ques[1])
                                elif z == 'M':
                                    ques = random.choice(hard_add_list_q_m)
                                    print(ques[1])
                                elif z == 'D':
                                    ques = random.choice(hard_add_list_q_d)
                                    print(ques[1])

                            a = input()
                            if int(a) == int(ques[0]):
                                print("That's right -- well done")
                            else:
                                print("incorrect answer")
                            q = q + 1

                        valid_ce = 0
                        while valid_ce < 1:
                            cont = input("Continue or exit (Continue:C, Exit: E): ")
                            if cont == 'C':
                                valid_ce = 1
                                quiz()
                            elif cont == 'E':
                                break
                            else:
                                print("incorrect input")

                    else:
                        print("Incorrect type")
                        continue

    else:
        print("Incorrect level")
        quiz()

quiz()
#Q2
def power(x, y):
    if (y == 0): return 1
    elif (int(y % 2) == 0): 
        return (power(x, int(y / 2)) * power(x, int(y / 2))) 
    else: 
        return (x * power(x, int(y / 2)) * power(x, int(y / 2)))

#x = 2; y = 3
x = int(input('Enter base value: '))
y = int(input('Enter power value: '))
print(power(x, y))

#Q3

mylist = [["john", 1, "a"], ["larry", 0, "b"]]
mylist.sort(key=lambda x:x[0])
print("Sort by first item:")
print(mylist)
mylist.sort(key=lambda x:x[1])
print("Sort by second item:")
print(mylist)

#Q4
import operator
mylist = [["john", 1, "a"],["larry", 0, "b"]]
mylist.sort(key=operator.itemgetter(0))
print(mylist)
mylist.sort(key=operator.itemgetter(1))
print(mylist)
mylist.sort(key=operator.itemgetter(1,2))
print(mylist)
	




