# pandas 

import pandas as pd

listdata=[
    ['John', 'math', 23],
    ['John', 'english', 25],
    ['Mary', 'math', 22],
    ['Mary', 'english', 21],
    ['John', 'history', 23],
    ['Mark', 'STEM', 25],
    ['Mark', 'history', 24],
    ['Mark', 'english', 22],
    ['Mark', 'math', 21]
      
]

df = pd.DataFrame(listdata, columns=['name', 'subject', 'score'])
print(df)
print(df.head(3))
