def printLine(scrubFile, lineCount):
    
    while True:
        with open(scrubFile, 'r') as f:
            tryFlag = True
            while tryFlag == True:
                try:
                    lineNum = int(input("Enter a line number >>  "))
                    tryFlag = False
                except:
                    print("ERROR: Invalid Input.")
                    lineNum = int(input("Enter a line number >>  "))

            while (lineNum > lineCount) or (lineNum < 0):
                lineNum = int(input(f"File contains {lineCount} lines.\nEnter a valid line number >>  "))
            
            count = 0
            for line in f:
                count += 1
                if count == lineNum:
                    print(f"Displaying line {lineNum}...\n")
                    print(line)

            #Print another line
            choice1 = input("Display another line? Y/N >>  ")
            choice1 = choice1.upper()
            if choice1 == 'N':
                break