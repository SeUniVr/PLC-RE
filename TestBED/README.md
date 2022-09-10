
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

On Windows: use Cygwin  
https://www.cygwin.com/

# 3. Run


 