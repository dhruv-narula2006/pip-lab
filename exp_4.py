# 4. WAP to print the current date in the following format:
#  "Sun May 29 02:26:23 IST 2026"

from datetime import datetime  
# 1st datetime is module, 2nd datetime is a class in the module
now  = datetime.now()  # now is a method defined under datetime
print(now.strftime("%a %b %d %H:%M:%S IST %Y")) 
# strftime is a method defined under datetime