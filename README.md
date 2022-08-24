# 1. Overview
- PLC registers reading
- Modbus message captures
- Data processing
- Interactive graphs and statistical analysis
- Invariant inference
- Business process mining


# 2. Requirements

- Operating system: Unix-like environments, including Linux, Mac OS X, and Windows Subsystem for Linux (WSL) 
- Python3.8 libraries: pandas, matplotlib, numpy, ray, json, glob, modbus_tk, scipy 
- openjdk 11.0.15 
- perl 5 
- TShark - Wireshark 3.4.8
- Daikon 5.8.10 
- Fluxicon Disco 3.2.4 

# 3. Information gathering

## 3.1 PLC registers reading
 Execute the script **main.py** to generate the data logs of the PLCs registers 
 ```
  python3 main.py
  
```
The output are JSON Files containg the values of every PLC registers.

## 3.2 Modbus message captures
Tshark to generate pcap files, then wireshark to convert to csv

# 4. Information processing

## 4.1 Data processing

Execute the script 	**convertoCSV.py** then **mergeDatasets.py** to convert the JSON files to a CSV datasets.  
The resulted files are savec in the directory PLC_CSV.
 

## 4.2 Invariant inference
The invariant generation is done using Daikon. To install Daikon follow the [guide](Installation_Daikon.sh). 
Execute the bash script **run.sh** to generate the invariants. 
```
  ./run.sh
  
```
The results of invariant generation will be saved in the file Daikon_Invariants/daikon_results.txt.




## 4.3 Interactive graphs and statistical analysis
Execute the script **plots.py** to plot the run charts of one or many variables. 
```
  python3 plots.py var1 var2 .... varn
```
Execute the script **plot_hist.py** to plot the histograms and statistical informations of a variable
```
  python3 plot_hist.py var
  
```

## 4.4 Business process mining
