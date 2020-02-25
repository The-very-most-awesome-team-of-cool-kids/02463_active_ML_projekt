# Wine dataset

import pandas as pd 

col_Names=["Cultivar", "Alcohol", "Malic Acid", "Ash", "Alcalinity of Ash", "Magnesium",
"Total Phenols", "Flavanoids", "Nonflavanoid Phenols", "Proanthocyanins", "Colour Intensity", "Hue", "OD280/OD315 of Diluted Wines",
"Proline"]
data = pd.read_csv("wine.data",names=col_Names)
print(data)