# who_will_pay_the_bill_tonight
import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(",")

num_names = len(names)

random_name = random.randint(0,num_names-1)

who_pay_the_bill = names[random_name]
print (who_pay_the_bill+" is going to buy the bill today")