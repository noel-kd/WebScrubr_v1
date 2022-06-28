import os

def makef(mainPath):

    #Create dir scrubfiles if not exist
    scrubPath = mainPath + '/ws_scrubfiles'
    fpExists = os.path.exists(scrubPath)
    os.chdir(mainPath)
    if not fpExists:
        os.makedirs(scrubPath)
    
    if os.getcwd() != scrubPath:
        os.chdir(scrubPath)
    fileNum = 1
    while os.path.exists(f'scrub{fileNum}.html'):
        fileNum += 1
    scrubFile = f'scrub{fileNum}.html'
    return scrubFile