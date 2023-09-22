import math
a = int(input("Enter the value of a: ")) #a এর মান ইনপুট দিতে হবে
b = int(input("Enter the value of b: ")) #b এর মান ইনপুট দিতে হবে
c = int(input("Enter the value of c: ")) #c এর মান ইনপুট দিতে হবে
d = b*b - 4*a*c #নিশ্চায়ক নির্ণয় করা হয়েছে
if(d>0): #শর্ত যদি D > 0 হলে, দুটি মূল থাকবে।
 x1 = -b + math.sqrt( d ) / 2*a #১ম মূল সূত্র বসানো হয়েছে
 x2 = -b - math.sqrt( d ) /2*a #২য় মূল সূত্র বসানো হয়েছে
 print("X1 = ",x1) #১ম মূল প্রদর্শন করা হয়েছে
 print("X2 = ",x2) #২য় মূল প্রদর্শন করা হয়েছে
elif(d == 0): #শর্ত যদি D = 0 হলে, ঠিক একটি মূল আছে
 x = -b / 2*a #একটি মূল বের হবে
 print("X = ",x) #মুলটি প্রদর্শন করা হয়েছে
else:
 print("Roots are imaginary") #কাল্পনিক

