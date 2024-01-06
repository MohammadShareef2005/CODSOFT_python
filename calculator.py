print('''
         ____     _       _        ____    _   _    _         _       _____   U  ___ u   ____     
U /"___|U  /"\  u  |"|    U /"___|U |"|u| |  |"|    U  /"\  u  |_ " _|   \/"_ \/U |  _"\ u  
\| | u   \/ _ \/ U | | u  \| | u   \| |\| |U | | u   \/ _ \/     | |     | | | | \| |_) |/  
 | |/__  / ___ \  \| |/__  | |/__   | |_| | \| |/__  / ___ \    /| |\.-,_| |_| |  |  _ <    
  \____|/_/   \_\  |_____|  \____| <<\___/   |_____|/_/   \_\  u |_|U \_)-\___/   |_| \_\   
 _// \\  \\    >>  //  \\  _// \\ (__) )(    //  \\  \\    >>  _// \\_     \\     //   \\_  
(__)(__)(__)  (__)(_")("_)(__)(__)    (__)  (_")("_)(__)  (__)(__) (__)   (__)   (__)  (__)  
''')
def add (a,b):
    return a+b
def mul (a,b):
    return a*b
def sub(a, b):
    return a-b
def div (a, b):
    return a/b
def check(o, l):
    if o=='/' and l==0:
        print("Undefined Number")
        return False
    else:
        return True

def calculat(operand, fn, ln ):

    if operand=='+':
        solution= add(fn, ln)
    elif operand=='-':
        solution= sub(fn, ln)
    elif operand=='*':
        solution= mul(fn, ln)
    elif operand=='/':
        
        solution= div(fn, ln)
    else:
        print("Select the correct operend ")
        return
    print(f"{fn} {operand} {ln} = {solution}")
    print(f" Type 'y' to continue the calculation with {solution} or type 'n' to exit")
    n=input().lower()
    if n=='y':
        m=input("pick an operator : ")
        new=int(input("What's the next number ? "))
        if check(m, new):
          calculat(m , solution, new)
    else:
        return

first_number=int(input("Enter the first number : "))
print("Select one operation")
print("additon         - +")
print("subtraction     - -")
print("division        - /")
print("multiplication  - * ")
oper=input()
last_number=int(input("Enter the second number : "))
if check(oper, last_number):
  calculat(oper, first_number, last_number)
print("Thank you")