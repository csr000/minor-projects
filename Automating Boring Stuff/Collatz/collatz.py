def collatz(n):
    try:
        n = int(n)
        if n>1:
            print(n) 
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                print(n) 
            elif n % 2 != 0:
                n = 3 * n + 1
                print(n) 
    except ValueError:
        print("Enter nothing else but numbers only")
    
    


collatz('a')