from urllib.request import urlopen


def read_text():
    quotes = open(r"C:\Users\Home\Downloads\movie_quotes.txt")
    content = quotes.read()
    quotes.close()
    check_profanity(content)


# def check_profanity(text):
#     response = urlopen("http://www.wdylike.appspot.com/?q=" + text)
#     output = response.read()
#     print(output)
#     response.close()


def check_profanity():
    response = urlopen("http://www.wdylike.appspot.com/?q=" + "shit")
    output = response.read()
    print(output)
    response.close()


check_profanity()
