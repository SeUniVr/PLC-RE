import pandas as pd 
import glob
import csv
	

#CSV files converted from JSON PLCs readings (convertoCSV.py)
filenames = glob.glob("PLC_CSV/*.csv")


def cleanNull(filenames):
	for f in filenames :
		with open(f, newline='') as f_input:
		    csv_input = csv.reader(f_input)
		    header = next(csv_input)   # read header
		    columns = zip(*list(csv_input))   # read rows and transpose to columns
		    data = [(h, c) for h, c in zip(header, columns) if set(c) != set('0')]
		    
		with open(f, 'w', newline='') as f_output:
		    csv_output = csv.writer(f_output)
		    csv_output.writerow(h for h, c in data)   # write the new header
		    csv_output.writerows(zip(*[c for h, c in data]))
		print(f + 'done')


# Removing empty registers (the registers with values equal to 0 are not used in the control of the CPS)
cleanNull(filenames)



df_list_mining = list()
for f in filenames :
	#Read Dataset files
	datasetPLC = pd.read_csv(f)
	# Concatenate the single PLCs datasets for process mining
	df_list_mining.append(datasetPLC)



mining_datasets = pd.concat(df_list_mining, axis=1).reset_index(drop=True)
# Save dataset with the timestamp for the process mining.
mining_datasets.to_csv(r'../process-mining/data/PLC_Dataset.csv', index=False)

print(mining_datasets)

print('************************************************************************************')
print ('************* DATASET FOR PROCESS MINING GENERATED SUCCESSFULLY *******************')
print('************************************************************************************')



# drop timestamps is NOT needed in Daikon
inv_datasets = mining_datasets.drop(['TimeStamp'], axis=1, errors='ignore')

#Enrich the dataset with a partial bounded history of registers
# Add previous values of registers
def add_prev(data_set):
	#Set registers names that holds measurements and actuations
	val_cols = inv_datasets.columns[inv_datasets.columns.str.contains(pat = 'inputregisters|InputRegisters|inputregister|Coils|coils|coil')]
	for col in val_cols:
		prev_val = list()
		prev_val.append("NULL")
		data_var = inv_datasets[col]
		for i in range(len(data_var)-1) : 
			prev_val.append(data_var[i])
		data_set.insert(len(data_set.columns),'prev_'+col, prev_val)


# Add previous values of Inputregisters and Coils
add_prev(inv_datasets)


# Add safety borders : The user can set the safety border by modifying the name of the register and the value of safety
#inv_datasets.insert(len(inv_datasets.columns),'PLC1_Max_safety', inv_datasets["PLC1_MemoryRegisters_MW1"][1] - 3)
#inv_datasets.insert(len(inv_datasets.columns),'PLC1_Min_safety', inv_datasets["PLC1_MemoryRegisters_MW0"][1] + 3)
#inv_datasets.insert(len(inv_datasets.columns),'PLC2_Max_safety', inv_datasets["PLC2_MemoryRegisters_MW2"][1] - 1)
#inv_datasets.insert(len(inv_datasets.columns),'PLC2_Min_safety', inv_datasets["PLC2_MemoryRegisters_MW1"][1] + 1)


# Add state transient/stable on PLC1_InputRegisters_IW0 
#PLC1_state = list()
#for x in datasetPLC1["PLC1_InputRegisters_IW0"] :
#	if (x in [52,53,54,78,79,80]):
#		PLC1_state.append("stable")
#	else:
#		PLC1_state.append("transient")	
#datasetPLC1.insert(len(datasetPLC1.columns),'PLC1_state', PLC1_state)






# Drop first rows (Daikon does not process missing values)
inv_datasets = inv_datasets.iloc[5: , :]



print(inv_datasets)

# Daikon can NOT process a csv of more that 64801 lines
#inv_datasets.iloc[0:64800].to_csv(r'PLC_Dataset.csv', index=False)


inv_datasets.to_csv(r'../daikon/Daikon_Invariants/PLC_Dataset.csv', index=False)

print('****************************************************************************************')
print ('************* DATASET FOR INVARIANT ANALYSIS GENERATED SUCCESSFULLY *******************')
print('****************************************************************************************')
