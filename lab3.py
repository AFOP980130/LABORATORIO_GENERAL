import pandas as pd

link = ("https://docs.google.com/spreadsheets/d/1x5zsd27AT0ySLKlkJFmGlBDLA2pTJ93Q-8f07wqpH4U/export?format=csv")

df = pd.read_csv(link)

print(df)

for i in df:
    try:
        print (i)
    except SyntaxError:
        print("Error de sintax")
        