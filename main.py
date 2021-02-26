import pyshorteners
while True:
    url_input = input("Would you like to create a shorten link?(y, n): ")
    if url_input.lower() in ("y", "yes"):
        urlLink = input("Paste your link that you want to shorten: ")
        shortening = pyshorteners.Shortener()
        shorteningProcess = shortening.tinyurl.short(urlLink)
        print(shorteningProcess)
    elif url_input.lower() in ("n", "no"):
        print("Welp goodbye!")
        break