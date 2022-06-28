from . import ws_printline

def parse(scrubFile, inUrl, lineCount):
    
    while True:
        with open(scrubFile, 'r') as f:
            term = input("Enter a search term >>  ")

            count = 0
            flag = False
            found = []

            for line in f:
                count += 1
                if term in line:
                    flag = True
                    found.append(count)

            if flag == False:
                print(f"Term \"{term}\" not found in {inUrl} source.")
            else:
                print(f"Term \"{term}\" found in:")
                for i in range(0, len(found)):
                    print(f" '{scrubFile}' line {found[i]}")
                
                #Option to print an identified (or any) line
                display = input("Display a specific line? Y/N >>  ")
                display = display.upper()
                if display == 'Y':
                    ws_printline.printLine(scrubFile, lineCount)

                #Search again
                choice2 = input("Search for another term? Y/N >>  ")
                choice2 = choice2.upper()
                if choice2 == 'N':
                    break