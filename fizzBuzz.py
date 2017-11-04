def fizzBuzz():
    count = 0
    while count < 100:
        count += 1
        if count % 15 == 0:
            print("Fizzbuzz")
        elif count % 3 == 0:
            print("Fizz")
        elif count % 5 == 0:
            print("Buzz")  
        else:
            print(count)
            
fizzBuzz()
