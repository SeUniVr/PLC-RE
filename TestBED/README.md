
# 1. Overview
- Docker project to build the PLCs
- Matlab-Simulink script of the physics
- Modbus connection script (To connect PLC1 and PLC2 over modbus)
- Simulink connection script (To connect the simulated sensors in Matlab-Simulink to the Docker containers of the PLCs)


# 2. Build
Edit the interface.cfg file accordingly. The ports of the containers must be inputted.
Build the simulink connection script, to interface the OpenPLC Simulink driver and the Simulink model using UDP Send and Receive blocks

To compile:  
g++ simlink.cpp -o simlink -pthread

## Matlab Simulink
![Model](/TestBED/simulink/Images/SimulinkSimplifiedModel.png "Simulink Simplified Model")
The model above is controlling a SWAT system composed of two tanks (Tank1 left, Tank2 right) with a level sensor on each tank and a pump on Tank1.
![Sensor1](/TestBED/simulink/Images/Sensor1OUT.png "Sensor1")
![Sensor2](/TestBED/simulink/Images/Sensor2OUT.png "Sensor2")
![Actuators](/TestBED/simulink/Images/ActuatorsInputs.png "Actuators")
- Open the file simulink/Model/SimplifedModel.slx in Matlab Simulink, that contains the aforementioned SWAT system
- Open the file simulink/Model/init.m, that contains the variables that define the water flow, the diameter of the pipes, etc...
![Init](/TestBED/simulink/Images/Init.png "Init")
- Run init.m
- Run SimplifedModel.slx
A monitor, like the one in the following picture should appear
![Monitor](/TestBED/simulink/Images/OutputMonitor.png "Monitor")

# 3. Run
