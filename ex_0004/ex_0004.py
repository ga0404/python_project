import pandas as pd
import re
file = open("data/zen.txt")
text = file.read()
#text = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", text)
text = re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", text)
text = pd.Series(text)
print(text.value_counts())
print(text.count())
file.close()