🌾 Smart Agriculture Monitoring System using AWS IoT Core (Cloud-Based, No Hardware)
This project simulates a Smart Agriculture Monitoring System using AWS IoT Core and other cloud services. It replicates sensor data (e.g., temperature, humidity, soil moisture) and publishes it to AWS IoT Core using MQTT — all without physical hardware.
________________________________________
📌 Table of Contents
•	Features
•	Technologies Used
•	System Architecture
•	AWS Setup
•	How to Run
•	Folder Structure
•	Project Report
•	References
•	Acknowledgments
________________________________________
🚀 Features
•	Simulates temperature, humidity, and soil moisture data
•	Publishes sensor data to AWS IoT Core using MQTT
•	Stores incoming data in AWS DynamoDB via IoT Rules
•	(Optional) Sends alerts using AWS SNS
•	(Optional) Visualizes data trends using AWS QuickSight
________________________________________
🛠️ Technologies Used
•	Python (paho-mqtt)
•	AWS IoT Core
•	AWS DynamoDB
•	AWS IAM
•	AWS SNS (optional)
•	AWS QuickSight (optional)
________________________________________
🏗️ System Architecture
1.	Simulated sensors generate data using Python.
2.	Data is transmitted via MQTT to AWS IoT Core.
3.	IoT Rule routes data to DynamoDB table.
4.	(Optional) AWS SNS sends alerts based on thresholds.
5.	(Optional) AWS QuickSight visualizes sensor data.
________________________________________
⚙️ AWS Setup
1.	Create an IoT Thing in AWS IoT Core.
2.	Download certificates (.crt, .key, Amazon Root CA).
3.	Create an IoT Rule to insert incoming data into DynamoDB.
4.	Create a DynamoDB table (e.g., SmartAgriData).
5.	(Optional) Set up an SNS topic and email subscription.
6.	(Optional) Configure QuickSight for dashboards.
________________________________________
🧪 How to Run
Clone the repository:
bash
CopyEdit
git clone https://github.com/your-username/smart-agriculture-aws.git cd smart-agriculture-aws 
Install Python dependencies:
bash
CopyEdit
pip install paho-mqtt 
Update simulate_sensor.py with:
•	Your AWS IoT endpoint
•	Certificate/key file paths
Then run the script:
bash
CopyEdit
python simulate_sensor.py 
________________________________________
📁 Folder Structure
.
├── simulate_sensor.py         # Simulated sensor publisher
├── certs/                     # AWS IoT certificates
├── docs/                      # Project report and diagrams
├── README.md                  # This file
________________________________________
📄 Project Report
A full project report is available in the docs/ directory:
📘 Smart_Agriculture_Monitoring_Project_Report.pdf
________________________________________
📚 References
•	AWS IoT Core Documentation
•	AWS DynamoDB Developer Guide
•	MQTT Protocol (paho-mqtt)
________________________________________
🙏 Acknowledgments
This project was completed under the guidance of
Ms. P. Sree Lakshmi
Cloud Based AIML Speciality Course
K L Deemed to be University, Hyderabad

