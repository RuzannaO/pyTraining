import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# nice dataframe creation
indices=["Avagyan Avag","Baghdasaryan Babken","Garanyan Gourgen"]
df = pd.DataFrame(columns=['Name', 'Sirname', 'sex', 'appx age', 'status'])
df['Name']=['Arman','Narek','Norik','zarmik']
df['status']=['student','tutor','student','tutor']
df.set_index('status',inplace=True)

print(df)
