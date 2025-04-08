🌾 Smart Agriculture Monitoring using AWS IoT Core (Cloud-Based, No Hardware)
This project is a cloud-based simulation of a Smart Agriculture Monitoring System using AWS IoT Core and other AWS services. It simulates temperature, humidity, and soil moisture sensor data using Python and MQTT protocol, with no physical hardware required.

🚀 Features
Simulates environmental data for smart farming

Uses MQTT to publish sensor data to AWS IoT Core

Stores data in AWS DynamoDB via IoT Rules

Optional: Alerts using Amazon SNS

Optional: Data visualization using AWS QuickSight

🛠️ Technologies Used
Python

AWS IoT Core

AWS DynamoDB

AWS IAM

AWS SNS (optional)

AWS QuickSight (optional)

MQTT (via paho-mqtt)

📦 Project Structure
graphql
Copy
Edit
.
├── simulate_sensor.py         # Python script to simulate sensor data
├── certs/                     # Device certificates for AWS IoT
├── README.md                  # Project overview
└── docs/                      # PDF report and documentation
📌 AWS Setup Steps
Register a Thing in AWS IoT Core and download its certificates.

Create an IoT Rule to insert incoming data into DynamoDB.

Set up a DynamoDB table (e.g., SmartAgriData).

Use simulate_sensor.py to publish simulated data.

(Optional) Configure SNS to send alerts when thresholds are breached.

(Optional) Use AWS QuickSight to visualize sensor data.

🧪 How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/smart-agriculture-aws.git
cd smart-agriculture-aws
Install dependencies:

bash
Copy
Edit
pip install paho-mqtt
Update simulate_sensor.py with your MQTT endpoint and certificate paths.

Run the simulation:

bash
Copy
Edit
python simulate_sensor.py
📖 Report
The full project report is available under the docs/ directory: 📄 Smart_Agriculture_Monitoring_Project_Full_Report.pdf

📚 References
AWS IoT Core Documentation

MQTT Protocol: paho-mqtt

AWS DynamoDB Developer Guide

🤝 Acknowledgments
This project was completed under the guidance of Ms. P. Sree Lakshmi as part of the Cloud Based AIML Speciality course at K L Deemed to be University, Hyderabad.
