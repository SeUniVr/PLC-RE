#!/bin/bash
mkdir -p historian 
mkdir -p PLC_CSV
mkdir -p Daikon_Invariants
echo "Insert simulation Time (in seconds) : "
read time
echo "Insert time granularity (in seconds) : "
read granularity
python3 main.py $time $granularity 
#Capture messages between plcs  ( to be saved in process-mining/data/ )
#sudo tshark -i br-bedded2bd376 -w capture.pcap
echo "JSON files generated successfully\nJSON convertion to CSV .... " 
python3 convertoCSV.py
python3 mergeDatasets.py
echo "CSV Dataset generated successfully "
#Adjust Daikon directory
export DAIKONDIR=/home/labo/Desktop/daikon-5.8.10; source $DAIKONDIR/scripts/daikon.bashrc
cd Daikon_Invariants/
perl $DAIKONDIR/scripts/convertcsv.pl PLC1_PLC2_PLC3_Dataset.csv
java -cp $DAIKONDIR/daikon.jar daikon.Daikon --nohierarchy PLC1_PLC2_PLC3_Dataset.decls PLC1_PLC2_PLC3_Dataset.dtrace > daikon_results.txt
echo "Invariants generated successfully :"
value=`cat daikon_results.txt`  
echo "$value" 
echo "Insert variable name for potential invariants : "
read var
grep -n $var daikon_results.txt
cd ..
echo "Insert first variable to plot :  "
read var1 
echo "Insert second variable to plot (none if there is none):  "
read var2
python3 plots.py $var1 $var2
echo "Insert variable name to plot histogram : "
read var3
python3 plot_hist.py $var3 

cd process-mining
./gradlew build
./gradlew runMessages
./gradlew runReadings
./gradlew Merge

# Next steps are : 1/Launch fluxicon disco and 2/give the file 'process-mining/data/MergeEvents.csv' as 
# input to plot the process mining graphs
