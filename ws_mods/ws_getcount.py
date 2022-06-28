def getCount(scrubFile):
    
    with open(scrubFile, 'r') as f:
        lineCount = 0
        for line in f:
            lineCount += 1
        print(f"Source contains {lineCount} lines.")
        return lineCount