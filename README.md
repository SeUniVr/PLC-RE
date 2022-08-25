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
  ```
 sudo apt update
 sudo apt install software-properties-common
 sudo add-apt-repository ppa:deadsnakes/ppa
 sudo apt install python3.8
 sudo apt install python3-pip
 pip3 install pandas matplotlib numpy json glob scipy  modbus_tk
 pip3 install -U ray
  ```
- openjdk 14
 ```
 sudo apt install openjdk-14-jdk
 ```

- perl 5
```
sudo apt install perl
```

- TShark - Wireshark 3.4.8
```
sudo apt install wireshark
```
- Daikon 5.8.10 : [installation](Installation_Daikon.sh)
- Fluxicon Disco 3.2.4 : [installation](https://fluxicon.com/disco/)


# 3. Information gathering

## 3.1 PLC registers reading
 Execute the script **main.py** to generate the data logs of the PLCs registers 
 ```
  python3 main.py
  
```
The output are JSON Files containg the values of all the PLC registers.

## 3.2 Modbus message captures
Tshark to generate pcap files, then wireshark to convert to csv

# 4. Information processing

## 4.1 Data processing

Execute the script 	**convertoCSV.py** then **mergeDatasets.py** to convert the JSON files to a CSV datasets.  
The resulted files are saved in the directory PLC_CSV and process-mining/data.
 ```
  python3 convertoCSV.py
  python3 mergeDatasets.py
  
```
The outputs of this executions are two CSV files. 
The file saved in process-mining/data is a timestamped dataset, it will be used for the business process mining. 
The file saved in PLC_CSV is an enriched dataset with a partial bounded history of registers, and additional informations such as stable states, slope values of measurements and relative setpoints. This dataset will be used for the invariant detection. 

 

## 4.2 Invariant inference
The invariant generation is done using Daikon. To install Daikon follow the [guide](Installation_Daikon.sh). 
Execute the bash script **run.sh** to generate the invariants. 
```
  ./run.sh
  
```
The results of invariant analysis will be saved in the file Daikon_Invariants/daikon_results.txt.

This script offers a query system to target specific invariants and to specify conditional invariants.





## 4.3 Interactive graphs and statistical analysis
Execute the script **plots.py** to plot the run charts of one or many variables. 
```
  python3 plots.py var1 var2 .... varn
```
Execute the script **plot_hist.py** to plot the histograms and statistical informations of a variable.
```
  python3 plot_hist.py var
  
```

## 4.4 Business process mining
