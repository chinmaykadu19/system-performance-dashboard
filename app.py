import streamlit as st
import psutil
import pandas as pd
import plotly.express as px
import time

st.set_page_config(page_title="System Performance Dashboard", layout="wide")

st.title("💻 System Performance Analytics Dashboard")

# Create empty lists to store data
cpu_data = []
memory_data = []
disk_data = []
time_data = []

# Collect data button
if st.button("Start Monitoring"):

    placeholder = st.empty()

    for i in range(20):

        cpu = psutil.cpu_percent()
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        cpu_data.append(cpu)
        memory_data.append(memory)
        disk_data.append(disk)
        time_data.append(i)

        df = pd.DataFrame({
            "Time": time_data,
            "CPU Usage (%)": cpu_data,
            "Memory Usage (%)": memory_data,
            "Disk Usage (%)": disk_data
        })

        with placeholder.container():

            col1, col2, col3 = st.columns(3)

            col1.metric("CPU Usage", f"{cpu}%")
            col2.metric("Memory Usage", f"{memory}%")
            col3.metric("Disk Usage", f"{disk}%")

            st.subheader("Usage Trends")

            fig = px.line(df, x="Time", y=["CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)"],
                          title="System Usage Over Time")

            st.plotly_chart(fig, use_container_width=True)

        time.sleep(1)

st.subheader("About Project")
st.write("This dashboard analyzes system performance metrics using Python, Pandas, and Streamlit.")