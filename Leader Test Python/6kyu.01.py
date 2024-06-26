"""def dig_pow(n, p):
    total = 0
    
    num_str = str(n)
    
    for i in range(len(num_str)):
        digit = int(num_str[i])
        total += digit ** (p + i)
        
    if total % n == 0:
        return total // n
    
    else:
        return -1"""

#total = 0

#ეს ხაზი ახდენს ცვლადის მთლიანი ინიციალიზაციას და აყენებს მის მნიშვნელობას 0-ზე. 
#ეს ცვლადი გამოყენებული იქნება n-ის ციფრების ჯამის შესანახად, აყვანილი p-ის ხარისხებამდე.
#ციფრი = int(num_str[i])

#ეს სტრიქონი ამოიღებს i-s ციფრს num_str-დან და დააბრუნებს მას მთელ რიცხვად int() ფუნქციის გამოყენებით. 
#ეს კეთდება ისე, რომ შემდგომ ჩვენ შეგვიძლია შევასრულოთ არითმეტიკული მოქმედებები ციფრზე.

#total += digit ** (p + i)

#ეს სტრიქონი ითვლის ჯამის i-ის ჯამს. ის ამაღლებს ციფრს p + i ხარისხამდე ** ოპერატორის გამოყენებით და შედეგ ამატებს მთლიან ცვლადს.

#if total % n == 0:

#ეს ხაზი ამოწმებს არის თუ არა ჯამი n-ის მთელი რიცხვი ჯერადი. 
#% ოპერატორი ითვლის n-ზე ჯამის გაყოფის ნარჩენს. თუ ნაშთი არის 0, ეს ნიშნავს, რომ ჯამი არის n-ის მთელი რიცხვი.