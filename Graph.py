import pandas as pd
import plotly_express as pe

def graph():
    location = input('please Enter the location of the CVS file\n')
    Xvalue = input('\nPlease enter the X Value\n')
    Yvalue = input('\nPlease enter the Y Value\n')
    title = input('\nPlease enter the Title of the graph\n')
    color = input("\nWhat should be the color of the graph base on?\n")
    graphValue = input('\nwhat type of graph Do you want?\n')


    df = pd.read_csv(location)
    print(df)

    graph = graphValue.lower()

    if 'line' in graph:
        graph = pe.line(df, x=Xvalue, y=Yvalue,
                    color=color, title=title)
        graph.show()


    elif 'line' in graph:
        graph = pe.bar(df, x=Xvalue, y=Yvalue,
                   title=title, color=color)
        graph.show()


    elif 'scatter' in graph:
        graph = pe.scatter(df, x=Xvalue, y=Yvalue, color=color,
                       title=title)
        graph.show()

if __name__ == '__main__':
    graph()


