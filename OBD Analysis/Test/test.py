import obd

# Create an OBD connection using a COM port
connection = obd.OBD(portstr='COM3', baudrate=9600)

# Check if the connection was successfully established
if connection.is_connected():
    print("OBD connection successful")
else:
    print("Failed to connect to OBD")

# Execute RPM OBD command
cmd = obd.commands.RPM
response = connection.query(cmd)
print(f"Engine RPM: {response.value} {response.unit}")

# Execute SPEED OBD command
cmd = obd.commands.SPEED
response = connection.query(cmd)
print(f"Vehicle SPEED: {response.value} {response.unit}")

# Execute Throttle Position OBD command
cmd = obd.commands.THROTTLE_POS
response = connection.query(cmd)
print(f"Throttle Position: {response.value} {response.unit}")

# Execute Coolant Temperature OBD command
cmd_CTemp = obd.commands.COOLANT_TEMP
response_ctemp = connection.query(cmd_CTemp)
print(f"Coolant Temperature: {response_ctemp.value} {response_ctemp.unit}")

# Execute Engine Load OBD command
cmd_ELoad = obd.commands.ENGINE_LOAD
response_ELoad = connection.query(cmd_ELoad)
print(f"Engine Load: {response_ELoad.value} {response_ELoad.unit}")

# Execute Engine Run Time OBD command
cmd_RunTime = obd.commands.RUN_TIME
response_RunTime = connection.query(cmd_RunTime)
print(f"Run Time: {response_RunTime.value} {response_RunTime.unit}")



# Close the connection
connection.close()
