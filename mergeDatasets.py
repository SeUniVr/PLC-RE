import pandas as pd 
	

#Read Dataset files
datasetPLC1 = pd.read_csv('PLC1Dataset.csv')
datasetPLC2 = pd.read_csv('PLC2Dataset.csv')
datasetPLC3 = pd.read_csv('PLC3Dataset.csv')




# Add previous values IW0, Coil0, Coil1 for Daikon to process
def add_prev(data_set, data_var, column_name):
	prev_val = list()
	prev_val.append("NULL")
	for i in range(len(data_var)-1) : 
		prev_val.append(data_var[i])
	data_set.insert(len(data_set.columns),column_name, prev_val)



#datasetPLC1.drop(['PLC1_state','prev_PLC1_InputRegisters_IW0', 'prev_PLC1_Coils_QX00','prev_PLC1_Coils_QX01'], axis='columns', inplace=True)

add_prev(datasetPLC1, datasetPLC1["PLC1_InputRegisters_IW0"], 'prev_PLC1_InputRegisters_IW0')
add_prev(datasetPLC1, datasetPLC1["PLC1_Coils_QX00"], 'prev_PLC1_Coils_QX00')
add_prev(datasetPLC1, datasetPLC1["PLC1_Coils_QX01"], 'prev_PLC1_Coils_QX01')
add_prev(datasetPLC2, datasetPLC2["PLC2_InputRegisters_IW0"], 'prev_PLC2_InputRegisters_IW0')
add_prev(datasetPLC2, datasetPLC2["PLC2_Coils_QX00"], 'prev_PLC2_Coils_QX00')
add_prev(datasetPLC3, datasetPLC3["PLC3_InputRegisters_IW0"], 'prev_PLC3_InputRegisters_IW0')

# Add safety borders
datasetPLC1.insert(len(datasetPLC1.columns),'PLC1_Max_safety', datasetPLC1["PLC1_MemoryRegisters_MW1"][1] - 3)
datasetPLC1.insert(len(datasetPLC1.columns),'PLC1_Min_safety', datasetPLC1["PLC1_MemoryRegisters_MW0"][1] + 3)
datasetPLC2.insert(len(datasetPLC2.columns),'PLC2_Max_safety', datasetPLC2["PLC2_MemoryRegisters_MW2"][1] - 1)
datasetPLC2.insert(len(datasetPLC2.columns),'PLC2_Min_safety', datasetPLC2["PLC2_MemoryRegisters_MW1"][1] + 1)


# Add state transient/stable on PLC1_InputRegisters_IW0
PLC1_state = list()
for x in datasetPLC1["PLC1_InputRegisters_IW0"] :
	if (x in [52,53,54,78,79,80]):
		PLC1_state.append("stable")
	else:
		PLC1_state.append("transient")	
datasetPLC1.insert(len(datasetPLC1.columns),'PLC1_state', PLC1_state)



# Concatenate the single PLCs datasets
df_list = list()
df_list.append(datasetPLC1)
df_list.append(datasetPLC2)
df_list.append(datasetPLC3)

merge_datasets = pd.concat(df_list, axis=1).reset_index(drop=True)

# Drop first row ( Daikon doesnt process missing values)
merge_datasets = merge_datasets.iloc[365: , :]
merge_datasets.dropna()


#print(merge_datasets.isnull().sum())
print(merge_datasets)

# Daikon cant process a csv of more that 64801 lines
#merge_datasets.iloc[0:64800].to_csv(r'PLC1_PLC2_PLC3_Dataset.csv', index=False)
merge_datasets.to_csv(r'PLC1_PLC2_PLC3_Dataset.csv', index=False)

"""
datasetPLC = pd.read_csv('PLC1_PLC2_PLC3_Dataset.csv') 
captureMessage = pd.read_csv('CleanCaptureWrite.csv')

df_list = list()
df_list.append(datasetPLC)
df_list.append(captureMessage)
merge_datasets = pd.concat(df_list, axis=1).reset_index(drop=True)
merge_datasets = merge_datasets.iloc[1: , :]
merge_datasets.iloc[0:3555].to_csv(r'PLC1_PLC2_PLC3_Dataset_Message.csv', index=False)
"""
