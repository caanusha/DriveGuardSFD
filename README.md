# DriveGuardSFD
Maintenance Prediction and Driver Performance Analysis

The current system lacks a comprehensive mechanism to effectively monitor and address driver driving performance, resulting in unsafe behaviors such as aggressive driving, speeding, sudden braking, and more. This poses risks to the well-being of passengers, particularly women and those with children, and compromises the overall safety of the rides provided.

Furthermore, there is a need to ensure the well-being of drivers themselves. The existing system fails to provide a robust mechanism for evaluating and improving driver skills, depriving them of valuable resources and guidance to enhance their driving abilities. This not only impacts their own safety but also hinders their ability to provide a secure and comfortable ride for passengers.

To address these concerns, we propose the implementation of the Smart Failure Detection system. This system utilizes Artificial Intelligence and Machine Learning techniques to predict maintenance needs in vehicles by analyzing sensor data such as sound, vibration, temperature, and humidity. By providing proactive alerts and predictions, it enables timely action to be taken by vehicle owners and maintenance teams, preventing potential breakdowns and enhancing vehicle safety. This approach also helps reduce maintenance costs and improves operational efficiency by empowering owners and maintenance teams to proactively address maintenance needs and optimize vehicle performance.

In addition, to tackle passenger safety issues, we suggest implementing an OBD device-based solution that monitors driver driving performance. This solution utilizes OBD technology to track and analyze driver behavior, offering real-time feedback, coaching and training opportunities, risk assessment, and the promotion of responsible driving habits. By employing this solution, ride safety for all users will be enhanced, passengers will gain confidence, and a framework for continuous improvement in driver performance and accountability will be established.

#How to use?

For DriveGuard application, follow below steps: 
Materials: OBD Device

Connect the OBD device to the car
Connect the bluetooth of OBD to the laptop
Once successfully connected, usually the device connects to COM3 and COM4 of your laptop
Run following command to run the streamlit
streamlit run obdDataAnalysis.py

The webpage opens up and now can be used
For SFD, following are the steps which needs to be followed:

Materials:

Arduino board (e.g., Arduino Uno), Sound sensor module, Vibration sensor module, DHT11 humidity and temperature sensor module, breadboard, Jumper wires, USB cable Computer with Arduino IDE installed.

Step 1: Connect the sound sensor module Connect the sound sensor module to the Arduino board using jumper wires. The sound sensor has three pins: VCC, GND, and AOUT. Connect the VCC pin to the 5V pin on the Arduino board, the GND pin to the GND pin on the board, and the AOUT pin to an analog input pin on the board (e.g., A0).

Step 2: Connect the vibration sensor module Connect the vibration sensor module to the Arduino board using jumper wires. The vibration sensor has three pins: VCC, GND, and SIG. Connect the VCC pin to the 5V pin on the Arduino board, the GND pin to the GND pin on the board, and the SIG pin to an analog input pin on the board (e.g., A1).

Step 3: Connect the DHT11 humidity and temperature sensor module Connect the DHT11 humidity and temperature sensor module to the Arduino board using jumper wires. The sensor module has three pins: VCC, GND, and DATA. Connect the VCC pin to the 5V pin on the Arduino board, the GND pin to the GND pin on the board, and the DATA pin to a digital input/output pin on the board (e.g., pin 2).

Step 4: Open the Arduino IDE and copy-paste the Arduino code to read data from the sensors and send it to the serial monitor "COM3"

Step 5: Execute the Python code (ModelTraining.ipynb) to read sensor data from the serial port "COM3" and use that data to train using DNN machine learning model to train the sensor data. Need to train using both Good and Bad Engine data to accurately predict the Engine state

Step 6: Execute the Python code (SmartMaintenancePrediction.py) to predict the Engine State which reads sensor data from the serial port "COM3" and use that data to predict the Engine State using trained DNN machine learning model

Youtube Demo Link - https://youtu.be/cbxN01bEHkM
