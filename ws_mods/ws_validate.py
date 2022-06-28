from validator_collection import checkers

def validate(inUrl):
    
    while True:
        check = checkers.is_url(inUrl)
        if check == True:
            break
        else:
            print("\nERROR: Invalid URL Entry.")
            print("Use appropriate prefixes (http[s]://) and suffixes (.com, .org, etc.).")
            print("Enter a valid URL to scrub...")
            inUrl = input(">> ")
    return inUrl