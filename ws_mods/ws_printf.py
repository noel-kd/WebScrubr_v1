def printf(scrubFile, inUrl):
    
    with open(scrubFile, 'r') as f:  
        print(f"Displaying source code for '{inUrl}'...\n")  
        print(f.read())
        print("\n*** End Of File ***")