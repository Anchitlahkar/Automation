import datetime
import os
import webbrowser
from Calculator import calculate
from Graph import graph

print("Use '?' for checking the avalable commands\n")

while True:
    userInput = input("Please Enter User Command\n")
    query = userInput.lower()

    if query == '?':
        print('''Use This words in Your Commands to get your result:\n
                Use 'The Time':    to check the current time\n 
                Use 'What':     to get you answer\n
                Use 'Calculate':    to calculate\n
                Use 'Graph': to represent a CVS file to graph\n
                Use 'Where': to find out location\n
                Use 'Play Song': to play some songs
                Use 'Exit': to exit the program\n''')

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime, "\n")

    elif 'what' in query:
        url = 'http://google.com/search?q=' + query
        webbrowser.get().open(url)
        print('hear is what i found for: \t' + query, "\n")

    elif 'calculate' in query:
        calculate()

    elif 'graph' in query:
        os.system('CLS')
        graph()
        input()
        os.system('CLS')

    elif 'where' in query:
        query = query.replace("where is", "")
        url = 'http://google.nl/maps/place/' + query + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location for ' + query)
        print("\n")

    elif 'song' in query:
        url = 'https://open.spotify.com/?_ga=2.44886887.274455931.1619941002-1246093746.1618936003' + query
        webbrowser.get().open(url)

    elif 'exit' in query:
        exit()
