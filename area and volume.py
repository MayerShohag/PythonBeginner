import math
radius = float(input("Enter radius value : ")) #ব্যাসার্ধ ইনপুট দিতে হবে
area = 4*math.pi * radius * radius #ক্ষেত্রফলের সূত্র বসানো হয়েছে
volume = (4/3)*math.pi* radius * radius * radius #আয়তনের সূত্র বসানো হয়েছে
print("Area is %.2f"%area) #ক্ষেত্রফল প্রদর্শন করা হয়েছে
print("Volume %.2f"%volume) #আয়তন প্রদর্শন করা হয়েছে

