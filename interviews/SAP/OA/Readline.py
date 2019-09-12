import sys 

for line in sys.stdin:

    print(line.rstrip())

    if line.rstrip() == "done":
        break

        

        
    