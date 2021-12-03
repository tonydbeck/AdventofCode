horizontal = 0
depth = 0
result = 0
input = open("input2.txt", "r")
ar = input.readlines()
for x in ar:
    command = x.split(" ")
    if command[0] == "up":
        depth = depth - int(command[1])
        print("Upwards we go " + str(command[1]))
        print("Position: D " + str(depth) + " H " + str(horizontal))
    elif command[0] == "down":
        depth = depth + int(command[1])
        print("downwards we go " + str(command[1]))
        print("Position: D " + str(depth) + " H " + str(horizontal))
    elif command[0] == "forward":
        horizontal = horizontal + int(command[1])
        print("forwards we go "  + str(command[1]))
        print("Position: D " + str(depth) + " H " + str(horizontal))
    else:
        print(command + " error")

result = depth * horizontal
print("The Result is: " + str(result))

              
    
