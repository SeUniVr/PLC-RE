from array import array
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

df = pd.read_csv('../daikon/Daikon_Invariants/PLC_Dataset.csv')

for x in range(1,len(sys.argv)):

	data = pd.DataFrame(df,columns=[str(sys.argv[x])])
	data.plot()
	plt.xlabel("Time")
	plt.legend([str(sys.argv[x])],bbox_to_anchor = (0.5, 1.1))
	plt.grid()
	plt.show()
