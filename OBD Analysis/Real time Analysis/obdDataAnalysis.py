import time
import datetime
import numpy as np
import plotly.express as px
import streamlit as st
import pandas as pd
from PIL import Image
import pickle
import obd  # install 0.4.0 version

icon = Image.open("icon.ico")
st.set_page_config(
    page_title="Drive Guard Driver Performance Prediction Dashboard📈",
    page_icon=icon,
    layout="wide",
)
is_collecting_data = False

# Define a list of options for the dropdown
options = ["Four-Wheeler Engine", "Two-Wheeler Engine"]

# Define a list of options for the dropdown
algoOptions = ["KNN", "Decision Tree", "Random-Forest", "Support Vector Machine", "Logistic Regression"]

# dashboard title
st.title("Drive Guard Real Time Driver Performance Prediction Dashboard📈")

# creating a single-element container
placeholder = st.empty()

# dd-mm-YY H:M:S
dt_string = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
df = pd.DataFrame(
    {'Time': [dt_string], 'RPM': [1445.5], 'Speed': [0.0], 'Throttle Position': [16.07843137254902],
     'Coolant Temperature': [51], 'Engine Load': [0.0], 'Run Time': [0], 'Acceleration Pos D':[0]})


def startdatacollection():
    global is_collecting_data, connection
    is_collecting_data = True

    try:
        # near real-time / live feed simulation
        while is_collecting_data:
            # Execute RPM OBD command
            response_rpm = connection.query(obd.commands.RPM)

            # Execute SPEED OBD command
            response_speed = connection.query(obd.commands.SPEED)

            # Execute Throttle Position OBD command
            response_tp = connection.query(obd.commands.THROTTLE_POS)

            # Execute Coolant Temperature OBD command
            response_ctemp = connection.query(obd.commands.COOLANT_TEMP)

            # Execute Engine Load OBD command
            response_ELoad = connection.query(obd.commands.ENGINE_LOAD)

            # Execute Engine Run Time OBD command
            response_RunTime = connection.query(obd.commands.RUN_TIME)

            # Execute Acceleration position OBD command
            response_accelPos = connection.query(obd.commands.RELATIVE_THROTTLE_POS)
            try:
                time.sleep(1)
                rows = [response_rpm.value, response_speed.value, response_tp.value, response_ctemp.value,
                        response_ELoad.value, response_RunTime.value,response_accelPos.value]
                timeline = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                rows.insert(0, timeline)
                print(rows)
                if len(rows) == 8:
                    print("len*8")
                    # Convert str to float data type
                    timevalue = np.array(rows[0])
                    rpm = np.array(float(rows[1]))
                    speed = np.array(float(rows[2]))
                    tp = np.array(float(rows[3]))
                    coolantTemp = np.array(float(rows[4]))
                    engineLoad = np.array(float(rows[5]))
                    runTime = np.array(float(rows[6]))
                    accelPos = np.array(float(rows[7]))
                    print("hii")
                    # add the new row to the DataFrame using loc accessor
                    df.loc[len(df)] = [timevalue, rpm, speed, tp, coolantTemp, engineLoad, runTime,accelPos]

                    # saving the dataframe
                    df.to_csv('RealTimeData.csv')

                    data_count = int(
                        df["RPM"].count()
                    )

                    # creating metrics
                    avg_rpm = np.mean(df["RPM"])
                    avg_speed = np.mean(df["Speed"])
                    avg_tp = np.mean(df["Throttle Position"])
                    avg_coolantTemp = np.mean(df["Coolant Temperature"])
                    avg_engineLoad = np.mean(df["Engine Load"])
                    print("hellow")

                    with placeholder.container():
                        print("45")
                        # create six columns for each metrics
                        dataCount, avgRpm, avgSpeed, avgTp, avgCoolantTemp, avgEngineLoad = st.columns(6)
                        currentRpm, currentSpeed, currentTp, currentCoolantTemp, currentEngineLoad, currentRunTime = st.columns(6)
                        print("hello")
                        # fill in those six columns with respective metrics
                        dataCount.metric(
                            label="Count 🧮",
                            value=data_count,
                        )
                        avgRpm.metric(
                            label="Avg(RPM) 🖩",
                            value=round(avg_rpm),
                        )
                        avgSpeed.metric(
                            label="Avg(Speed) 🖩",
                            value=round(avg_speed),
                        )
                        avgTp.metric(
                            label="Avg(Throttle Position) 🖩",
                            value=round(avg_tp),
                        )
                        avgCoolantTemp.metric(
                            label="Avg(Coolant Temperature) 🖩",
                            value=round(avg_coolantTemp),
                        )
                        avgEngineLoad.metric(
                            label="Avg(Engine Load) 🖩",
                            value=round(avg_engineLoad),
                        )

                        # fill in those six columns with respective metrics
                        currentRpm.metric(
                            label="Current RPM 🖩",
                            value=response_rpm.value,
                        )
                        currentSpeed.metric(
                            label="Current Speed 🖩",
                            value=round(response_speed.value),
                        )
                        currentTp.metric(
                            label="Current Throttle Position 🖩",
                            value=round(response_tp.value),
                        )
                        currentCoolantTemp.metric(
                            label="Current Coolant Temperature 🖩",
                            value=round(response_ctemp.value),
                        )
                        currentEngineLoad.metric(
                            label="Current Engine Load 🖩",
                            value=round(response_ELoad.value),
                        )
                        currentRunTime.metric(
                            label="Current Run Time 🖩",
                            value=round(response_RunTime.value),
                        )

                        # create two columns for charts
                        fig_rpm, fig_speed = st.columns(2)
                        with fig_rpm:
                            st.markdown("### RPM VS Time⏱️")
                            figRpm = px.line(
                                data_frame=df, y="RPM", x="Time"
                            )
                            if response_accelPos.value > 0 and response_rpm.value > 0:
                                st.text_area('Results:', "Rash Driving Detected")
                                print("figure1")
                                figRpm = px.scatter(timeline, response_rpm.value, label='Rash Driving Detected Points',
                                                             color='red', marker='.')
                            st.write(figRpm)

                        with fig_speed:
                            st.markdown("### Speed VS Time⏱️")
                            figSpeed = px.line(data_frame=df, y="Speed", x="Time")
                            st.write(figSpeed)

                        # create two columns for charts
                        fig_tp, fig_coolantTemp = st.columns(2)
                        with fig_tp:
                            st.markdown("### Throttle Position VS Time⏱️")
                            figTp = px.line(
                                data_frame=df, y="Throttle Position", x="Time"
                            )
                            st.write(figTp)

                        with fig_coolantTemp:
                            st.markdown("### Coolant Temperature 🌡️ VS Time⏱️")
                            fig_coolantTemp = px.line(data_frame=df, y="Coolant Temperature", x="Time")
                            if response_ctemp.value > 0:
                                st.text_area('Results:', "Over Heated Engine Detected")
                                fig_coolantTemp = px.scatter(timeline, response_ctemp.value, label='Over Heated Engine Points', color='red', marker='.')
                            st.write(fig_coolantTemp)

                        # create two columns for engine load and run time
                        fig_engineload, fig_runtime = st.columns(2)
                        with fig_engineload:
                            st.markdown("### Engine Load VS Time⏱️")
                            fig_engineload = px.line(data_frame=df, y="Engine Load", x="Time")
                            if dataCount>2 and (response_rpm.value - df['RPM'][dataCount-1]) > 0 and (response_ELoad.value - df['Engine Load'][dataCount-1]) > 0:
                                st.text_area('Results:', "Rash Driving Detected")
                                fig_engineload = px.scatter(timeline, response_ELoad.value,
                                                             label='Rash Driving Detected', color='red', marker='.')
                            st.write(fig_engineload)

                        with fig_runtime:
                            st.markdown("### Run Time VS Time⏱️")
                            fig_runtime = px.line(data_frame=df, y="Run Time", x="Time")
                            st.write(fig_runtime)

            except:
                print("try failed!")
                pass
    except:
        print("Connection Unsuccessful!")


# Define a function that takes a data frame and makes predictions
def predictusing(selectedAlgo):
    # Load the pre-trained model from disk
    if selectedAlgo == algoOptions[0]:
        with open('../Training/Models/KNNmodel.pkl', 'rb') as f:
            model = pickle.load(f)
    elif selectedAlgo == algoOptions[1]:
        with open('../Training/Models/DTmodel.pkl', 'rb') as f:
            model = pickle.load(f)
    elif selectedAlgo == algoOptions[2]:
        with open('../Training/Models/RFmodel.pkl', 'rb') as f:
            model = pickle.load(f)
    elif selectedAlgo == algoOptions[3]:
        with open('../Training/Models/SVMmodel.pkl', 'rb') as f:
            model = pickle.load(f)
    elif selectedAlgo == algoOptions[4]:
        with open('../Training/Models/LRmodel.pkl', 'rb') as f:
            model = pickle.load(f)
        # Make predictions using the pre-trained model

    df = pd.read_csv('RealTimeData.csv')
    temp = df.drop(df.columns[[0, 1]], axis=1)
    means = temp.mean()
    means_2d = means.values.reshape(1, -1)
    predictions = model.predict(means_2d)
    return predictions


# Define function to stop data collection
def compute(selectedAlgo):
    global is_collecting_data
    is_collecting_data = False
    # Call the predict function with the new data frame
    prediction = predictusing(selectedAlgo)

    # Return the prediction
    return prediction


def main():
    global connection
    with st.sidebar:
        st.markdown("# Real Time Data Uploader")
        # Add a dropdown with a default value to the app
        selected_option = st.selectbox("Select the device", options, index=0)

        # Add a button to the app
        if st.button("Start Data Collection", key="start"):
            # Create an OBD connection using a COM port
            connection = obd.OBD(portstr='COM3', baudrate=9600)
            # Check if the connection was successfully established
            if connection.is_connected():
                print("OBD connection successful!")
                startdatacollection()
            else:
                print("Failed to connect to OBD!")

        if st.button("Stop Data Collection", key="stop"):
            st.stop()

        # Add a dropdown with a default value to the app
        selectedAlgo = st.selectbox("Algorithm", algoOptions, index=0)

        if st.button("Compute", key="compute"):
            results = compute(selectedAlgo)
            # Create a textarea
            if results == 0:
                results_area = st.text_area('Results:', "Smooth Driving")
            elif results == 1:
                results_area = st.text_area('Results:', "Potholes Detected")
            elif results == 2:
                results_area = st.text_area('Results:', "High Fuel Consumption Detected")
            elif results == 3:
                results_area = st.text_area('Results:', "Hard Braking Detected")
            elif results == 4:
                results_area = st.text_area('Results:', "Rash Driving Detected")
            elif results == 5:
                results_area = st.text_area('Results:', "Engine Overheat Detected")
            elif results == 6:
                results_area = st.text_area('Results:', "Hump Detected Detected")


main()
