import math
a = int(input("Enter 1st value: ")) #প্রথম বাহুর দৈর্ঘ্য
b = int(input("Enter 2nd value: ")) #দ্বিতীয় বাহুর দৈর্ঘ্য
c = int(input("Enter 3rd value: ")) #তৃত্বীয় বাহুর দৈর্ঘ্য
s = (a+b+c)/2 #এখানে ৩টি বাহুর দৈর্ঘ্যকে ২ দ্বারা ভাগ করা হয়েছে
area = math.sqrt(s*(s-a)*(s-b)*(s-c)) #ত্রিভুজের ক্ষেত্রফল সূত্র ব্যবহার করা হয়েছে
print("Area of the triangle is: %.2f" % area+"sq.") #প্রদর্শণ করা হয়েছে