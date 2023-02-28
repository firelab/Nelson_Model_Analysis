# Nelson_Model_Analysis

This repository serves as a compilation of all the data and material used for the Nelson Model Analysis. 

Under the folder nelson_model you will find all of the files that makes the nelson model work correctly. In deadfuelmoisture.cpp,
a function call outerMeanMoisture was added to calculate the mean of moisture contained in the outershell of a log. Updates were also made to
meanWtdMoisture to allow for the mean of moisture in a log to be calculated again. 
The calculation of mean, median or outershell mean can now be changed in the computerFuelMoisture.cpp file. 

Under the folder input_generation are the scripts used to create files able to be ran by the moisture model. Input_script.py was created to grab and format
weather data from the Blue Mountain RAWs stations. lat_lon_script.py was used to format modis and viirs data to only include data near the
Blue Mountain Raws Station. Synthetic_input_script.py was used to generate the synthetic input found in the analysis and dashboard. 

The input folder includes the files that were ran through the model and output folder includes the outputs of those runs. 

Finally you can find graphs and data organized in excel sheets and csv in the Nelson Model Results folder. 
