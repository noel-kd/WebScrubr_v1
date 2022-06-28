from bs4 import BeautifulSoup

def pullWrite(scrubFile, page):

    f = open(scrubFile, 'x')
    with open(scrubFile, 'w') as f:
        print("Pulling source...")
        soupPage = BeautifulSoup(page.content, 'html.parser')
        f.write(soupPage.prettify())
        #urllib.request.urlretrieve(inUrl, scrubFile)
        print(f"Source successfully written to '{scrubFile}'.")