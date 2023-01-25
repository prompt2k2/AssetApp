import string as s 
from random import *

password = "".join(choice(s.ascii_letters + s.digits + s.punctuation) for x in range(randint(6,22)))

print("Your new password is: " + password)



    