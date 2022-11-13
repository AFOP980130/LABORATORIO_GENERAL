import pandas as pd


df = pd.read_csv("https://docs.google.com/spreadsheets/d/1x5zsd27AT0ySLKlkJFmGlBDLA2pTJ93Q-8f07wqpH4U/export?format=csv")

print(df)

for i in df:
    try:
        print (i)
    except SyntaxError:
        print("Error de sintax")
        