import pandas as pd
import sys
import matplotlib.pyplot as plt
from scipy import stats


df = pd.read_csv('PLC1_PLC2_PLC3_Dataset.csv')

cleanedColumn = [x for x in df["PLC1_InputRegisters_IW0"] if str(x) != 'nan']

#p-value 
print(stats.shapiro(cleanedColumn))
print("\n \n")
#15%, 10%, 5%, 2.5%, 1% to assume normality 
print(stats.anderson(cleanedColumn, dist='norm'))

df.hist(column=str(sys.argv[1]))
plt.show()