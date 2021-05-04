n = int(input("Write the no. of lines of pattern, please!\n"))

bool = input("Choose option:\n 'true' for printing straight pattern\n 'false' for printing inversed pattern\n")

if bool == "true":
#printing pattern
    for i in range(0,n):
        for j in range(0,i+1):
             print('* ',end="")
        print("\n")
#printing pattern(inversed)
elif bool == "false":
    for i in range(0,n):
        for j in range(0,n-i):
            print('* ',end="")
        print("\n")