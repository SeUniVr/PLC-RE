import pandas as pd 
	

#Read Dataset files
datasetPLC1 = pd.read_csv('PLC_CSV/PLC1Dataset.csv')
datasetPLC2 = pd.read_csv('PLC_CSV/PLC2Dataset.csv')
datasetPLC3 = pd.read_csv('PLC_CSV/PLC3Dataset.csv')


# Concatenate the single PLCs datasets for process mining
df_list_mining = list()
df_list_mining.append(datasetPLC1)
df_list_mining.append(datasetPLC2)
df_list_mining.append(datasetPLC3)
mining_datasets = pd.concat(df_list_mining, axis=1).reset_index(drop=True)
mining_datasets.to_csv(r'process-mining/data/PLC1_PLC2_PLC3_Dataset.csv', index=False)


# Add previous values IW0, Coil0, Coil1 for Daikon to process
def add_prev(data_set, data_var, column_name):
	prev_val = list()
	prev_val.append("NULL")
	for i in range(len(data_var)-1) : 
		prev_val.append(data_var[i])
	data_set.insert(len(data_set.columns),column_name, prev_val)


# drop timestamps not needed in Daikon
datasetPLC1.drop(['timestamps'], axis='columns', inplace=True)

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



# Drop first rows ( Daikon doesnt process missing values)
merge_datasets = merge_datasets.iloc[365: , :]



#print(merge_datasets.isnull().sum())
print(merge_datasets)

# Daikon cant process a csv of more that 64801 lines
#merge_datasets.iloc[0:64800].to_csv(r'PLC1_PLC2_PLC3_Dataset.csv', index=False)
merge_datasets.to_csv(r'Daikon_Invariants/PLC1_PLC2_PLC3_Dataset.csv', index=False)


