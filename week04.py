import pandas as pd
scores = [100,87,97,82]
average = pd.Series(scores).median()
print(average)
