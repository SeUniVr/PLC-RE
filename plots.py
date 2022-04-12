import pandas as pd
import matplotlib.pyplot as plt
import numpy
import sys

df = pd.read_csv('PLC1_PLC2_PLC3_Dataset.csv')

var1 = str(sys.argv[1])
var2 = str(sys.argv[2])

if var2 != "none" :
	data = pd.DataFrame(df,columns=[var1,var2])
	data.plot()
	plt.xlabel("Time")
	plt.legend([var1,var2],bbox_to_anchor = (0.5, 1.1))
	plt.grid()
	plt.show()
else :
	data = pd.DataFrame(df,columns=[var1])
	data.plot()
	plt.xlabel("Time")
	plt.legend([var1],bbox_to_anchor = (0.5, 1.1))
	plt.grid()
	plt.show()
