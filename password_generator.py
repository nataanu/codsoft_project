#importing string and random module 
import string
import random

#specifying the charaters for password
letters=string.ascii_letters
digits=string.digits
specialSymbol=string.punctuation
random_string=letters+specialSymbol+digits

#asking user to specify the length
length=int(input("Please specify the length of your password :"))

#joining every thing together
password = "".join(random.choices(random_string,k=length))

#displaying the generated password
print("This is your generated Password : ",password)
