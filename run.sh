#!/bin/bash
mdkir -p historian 
echo "Insert simulation Time (in seconds) : "
read time
echo "Insert time granularity (in seconds) : "
read granularity
python3 main.py $time $granularity
echo "JSON files generated successfully\nJSON convertion to CSV .... " 
python3 convertoCSV.py 
python3 mergeDatasets.py
echo "CSV Dataset generated successfully "
# Adjust Daikon directory
export DAIKONDIR=/path_to_daikon_directory/; source $DAIKONDIR/scripts/daikon.bashrc
perl $DAIKONDIR/scripts/convertcsv.pl PLC1_PLC2_PLC3_Dataset.csv
java -cp $DAIKONDIR/daikon.jar daikon.Daikon --nohierarchy PLC1_PLC2_PLC3_Dataset.decls PLC1_PLC2_PLC3_Dataset.dtrace > daikon_results.txt
echo "Invariants generated successfully :"
value=`cat daikon_results.txt`  
echo "$value" 
echo "Insert variable name for potential invariants : "
read var
grep -n $var daikon_results.txt
echo "Insert one or two variables name to plot (none as second argument to plot):  "
read var1 
read var2
python3 plots.py $var1 $var2
echo "Insert variable name to plot histogram : "
read var3
python3 plot_hist.py $var3
