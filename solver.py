B = [4, 4, 2, 2, 4, 4]
amount = 0
base = 4
solved = 1

print(f"B0 = {B[0]} B1 = {B[1]} B2 = {B[2]} B3 = {B[3]} B4 = {B[4]} B5 = {B[5]}")
print(" ")

for v in range(base):
    for x in range(base):
        for c in range(base):
            for b in range(base):
                B = [4, 4, 2, 2, 4, 4]
                print(f" {v} {x} {c} {b}")
                if base == 4 :
                    for z in range(1, 5):
                        #set changing sequence
                        if z == 1 :
                            amount = v
                        if z == 2 :
                            amount = x
                        if z == 3 :
                            amount = c
                        if z == 4 :
                            amount = b

                        B[z] = B[z] + amount
                        B[z+1] = B[z+1] + amount
                        B[z-1] = B[z-1] + amount

                        if B[z-1] >= (base + 1) :
                            B[z-1] = B[z-1] - base
                        if B[z+1] >= (base + 1) :
                            B[z+1] = B[z+1] - base
                        if B[z] >= (base + 1) :
                            B[z] = B[z] - base

                        if z == 1 :
                            B[4] = B[0]
                            B[5] = B[1]
                        if z == 2 :
                            B[5] = B[1]
                        if z == 3 :
                            B[0] = B[4]
                        if z == 4 :
                            B[1] = B[5]
                            B[0] = B[4]

                if base == 3 :
                    for z in range(1, 5):
                        #set changing sequence
                        if z == 1 :
                            amount = v
                        if z == 2 :
                            amount = x
                        if z == 3 :
                            amount = c
                        if z == 4 :
                            amount = b

                        #Increase values by the amount
                        B[z] = B[z] + amount
                        B[z+1] = B[z+1] + amount
                        B[z-1] = B[z-1] + amount
                        
                        #oddities
                        if z == 3 :
                            B[z+1] = B[z+1] - amount
                        if z == 4 :
                            B[z-1] = B[z-1] - amount

                        #Make high numbers loop back
                        if B[z-1] >= (base + 1) :
                            B[z-1] = B[z-1] - base
                        if B[z+1] >= (base + 1) :
                            B[z+1] = B[z+1] - base
                        if B[z] >= (base + 1) :
                            B[z] = B[z] - base

                        #Change corners
                        if z == 1 :
                            B[4] = B[0]
                            B[5] = B[1]
                        if z == 2 :
                            B[5] = B[1]
                        if z == 3 :
                            B[z+1] = B[z+1] - amount
                            B[0] = B[4]
                        if z == 4 :
                            B[z-1] = B[z-1] - amount
                            B[1] = B[5]
                            B[0] = B[4]

                print(f"B0 = {B[0]} B1 = {B[1]} B2 = {B[2]} B3 = {B[3]} B4 = {B[4]} B5 = {B[5]}")
                
                if B[1] == solved and B[2] == solved and B[3] == solved and B[4] == solved :
                    solution = (f"The sequence is {v} {x} {c} {b} ")
                    print(f"Solved with the sequence {v} {x} {c} {b} ")
                    break
print(solution)
