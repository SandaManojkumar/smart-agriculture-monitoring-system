# 🌾 Smart Agriculture Monitoring System using AWS IoT Core (Cloud-Based, No Hardware)

This project simulates a **Smart Agriculture Monitoring System** using **AWS IoT Core** and other cloud services. It replicates real-time environmental sensor data (e.g., temperature, humidity, soil moisture) and publishes it to AWS IoT Core using MQTT — **all without physical hardware**.

---

## 📌 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [AWS Setup](#aws-setup)
- [How to Run](#how-to-run)
- [Folder Structure](#folder-structure)
- [Project Report](#project-report)
- [References](#references)
- [Acknowledgments](#acknowledgments)

---

## 🚀 Features

- Simulates temperature, humidity, and soil moisture data.
- Publishes sensor data to AWS IoT Core via MQTT.
- Stores incoming data in DynamoDB using IoT Rules.
- *(Optional)* Sends alerts via AWS SNS based on thresholds.
- *(Optional)* Visualizes trends using AWS QuickSight.

---

## 🛠️ Technologies Used

- Python (paho-mqtt)
- AWS IoT Core
- AWS DynamoDB
- AWS IAM
- AWS SNS *(optional)*
- AWS QuickSight *(optional)*

---

## 🏗️ System Architecture

1. Simulated sensors generate data using Python.
2. Data is published to AWS IoT Core over MQTT.
3. IoT Rule routes the data to DynamoDB.
4. *(Optional)* AWS SNS sends notifications if thresholds are crossed.
5. *(Optional)* AWS QuickSight provides visualization dashboards.

![architecture-diagram](docs/system_architecture.png) <!-- Add your architecture diagram in docs/ -->

---

## ⚙️ AWS Setup

1. Create a **Thing** in AWS IoT Core.
2. Download your **Device Certificate**, **Private Key**, and **Amazon Root CA**.
3. Attach an IoT Policy to allow publishing.
4. Create a **DynamoDB table** (e.g., `SmartAgriData`) with `timestamp` as the primary key.
5. Create an **IoT Rule** to forward messages to DynamoDB.
6. *(Optional)* Set up **SNS Topic** and subscription for alerts.
7. *(Optional)* Connect **QuickSight** to DynamoDB for dashboards.

---
## 📚 References
AWS IoT Core Documentation

AWS DynamoDB Developer Guide

MQTT Protocol - paho-mqtt



---

## 🧪 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/smart-agriculture-aws.git
cd smart-agriculture-aws

# Install dependencies
pip install paho-mqtt

# Configure simulate_sensor.py with your:
# - AWS IoT endpoint
# - Certificate, private key, and CA file paths

# Run the simulation
python simulate_sensor.py

