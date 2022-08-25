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
 Disco is not supported by Unix-like operating systems. The users can use [Wine](https://www.winehq.org/) to install and run this software.

# 3. Information gathering

## 3.1 PLC registers reading
 Execute the script **_main.py_** to generate the data logs of the PLCs registers 
 ```
  python3 main.py 
```
The output are JSON Files containg the values of all the PLC registers.

## 3.2 Modbus message captures
Tshark to generate pcap files, then wireshark to convert to csv

# 4. Information processing

## 4.1 Data processing

Execute the script 	**_convertoCSV.py_** then **_mergeDatasets.py_** to convert the JSON files to a CSV datasets.    
The outputs are two CSV files saved in the directories _PLC_CSV_ and _process-mining/data_.  
 ```
  python3 convertoCSV.py
  python3 mergeDatasets.py 
```   
The file saved in _process-mining/data_ is a timestamped dataset, it will be used for the business process mining.   
The file saved in _PLC_CSV_ is an enriched dataset with a partial bounded history of registers, and additional informations such as stable states, slope values of measurements and relative setpoints. This dataset will be used for the invariant detection.   

 

## 4.2 Invariant inference
The invariant generation is done using [Daikon](https://plse.cs.washington.edu/daikon/). To install Daikon follow the [guide](Installation_Daikon.sh).     
Execute the bash script **_run.sh_** to generate the invariants. 
```
  ./run.sh 
```
  
This script offers a query system to target specific invariants and to specify conditional invariants.  
The users have the possibility to insert a variable name in order to display the associated invariants.   
The users can customize the [splitter info file](https://plse.cs.washington.edu/daikon/download/doc/daikon/Enhancing-Daikon-output.html#Splitter-info-file-format) **_Daikon_Invariants/Inv_conditions.spinfo_** by specifying the conditions that Daikon should use to create conditional invariants.   
*Spinfo file example :*
```
PPT_NAME aprogram.point:::POINT
VAR1 > VAR2
VAR1 == VAR3 && VAR1 != VAR4
```

The results of the invariant analysis will be saved in the location **_Daikon_Invariants/daikon_results.txt_**.

## 4.3 Interactive graphs and statistical analysis

Execute the script **_Runchartplots.py_** :    
```
  python3 chartplots.py var1 var2 .... varn
```
The outputs of this execution are a run-sequence plots of the specified variables in function of the simulation time.  
  
Execute the script **_Histplots_stats.py_** : 
```
  python3 Histplots_stats.py var  
```
The outputs of this execution are a histogram and statistical informations of a given variable.  
These informations include :
- The mean, median, standard deviation, the maximum and minimum values.  
- The statistical distribtuions.  
Two tests are used Chi-squared test for uniformity and Shapiro-Wilk test for normality.


## 4.4 Business process mining
