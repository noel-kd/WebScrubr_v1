#! python3
import os
import requests
import pyfiglet
from ws_mods import ws_validate, ws_makef, ws_pullwrite, ws_getcount, ws_parse, ws_printline, ws_printf, ws_rerun

mainPath = os.getcwd()

while True:
    #Display title banner
    banner = pyfiglet.figlet_format("Web Scrubr", font = 'standard')
    print (banner, "---- scrub and parse webpage source  |  @noel-kd ----\n") #Last updated: 27Jun22

    #Request initial URL input
    inUrl = input("Enter a URL to scrub >>  ")

    #Validate URL
    inUrl = ws_validate.validate(inUrl)
    
    #Get page source
    getFail = True
    while getFail == True:
        try:
            page = requests.get(inUrl)
            getFail = False
        except:
            print("\nERROR: Page Not Found.")
            inUrl = input("Enter a valid URL to scrub >>  ")

            #Validate URL
            inUrl = ws_validate.validate(inUrl)

    #Create output file
    scrubFile = ws_makef.makef(mainPath)

    #Pulling and writing source    
    ws_pullwrite.pullWrite(scrubFile, page)

    #Get line count
    lineCount = ws_getcount.getCount(scrubFile)

    #Menu options
    menu = True
    while menu == True:
        print("-------------------------------")
        print(" 1. Search source for key term")
        print(" 2. Display a specific line")
        print(" 3. Display entire source file")
        print(" 4. Restart")
        print(" 5. Quit")
        option = input("Select an option >>  ")

        if option == '1':
            #Parse source for key term
            ws_parse.parse(scrubFile, inUrl, lineCount)
            menu = True
        
        elif option == '2':
            #Select line and print selected line 
            ws_printline.printLine(scrubFile, lineCount)
            menu = True

        elif option == '3':
            #Display entire source
            ws_printf.printf(scrubFile, inUrl)
            menu = True

        elif option == '4':
            #Restart
            ws_rerun.rerun()
            menu = False

        elif option == '5':
            #Quit
            menu = False
        else:
            print("Invalid entry.")
            menu = True

    #Option 4 catch
    if option == '5':
        break

input("\nPress Enter to Exit...")