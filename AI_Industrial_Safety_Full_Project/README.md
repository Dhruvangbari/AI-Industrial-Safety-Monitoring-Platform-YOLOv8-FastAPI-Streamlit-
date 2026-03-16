
# AI Industrial Safety Monitoring Platform
# 🏭 AI Industrial Safety Monitoring Platform

An enterprise-level AI powered safety monitoring system designed to automatically detect workplace safety violations using computer vision.

The system monitors workers through CCTV or IP cameras and identifies whether required safety equipment such as helmets or face masks are present.

It is built using a scalable architecture suitable for smart factories, construction sites, and industrial automation environments.

---

# 🚀 Features

### 🧠 AI Safety Detection
Detects the following objects:

- Person
- Safety Helmet
- Face Mask

Automatically identifies safety violations and logs them for analysis.

---


### 🎥 Multi Camera Monitoring
Supports multiple video streams including:

- Webcam
- CCTV
- RTSP cameras
- IP cameras

Allows monitoring of multiple areas simultaneously.

---

### 📊 Real Time Dashboard
A Streamlit dashboard displays:

- Violation logs
- Safety statistics
- Data visualizations

This allows supervisors to quickly analyze safety incidents.

---

### 🌐 REST API Integration
The system includes a FastAPI backend that provides:

- Violation data endpoints
- Integration with external applications
- Smart factory system connectivity

---

### 🧾 Evidence Logging
When a violation occurs:

• Timestamp is recorded  
• Evidence image is stored  
• Violation entry is added to logs  

This enables traceable safety auditing.

---

# 🏗 System Architecture

Camera Stream  
↓  
YOLOv8 Detection Engine  
↓  
Object Tracking Layer  
↓  
Safety Compliance Engine  
↓  
Violation Logger  
↓  
API + Dashboard

---

# 📂 Project Structure


Enterprise-level AI safety monitoring system for detecting industrial safety violations using computer vision.

## Features
- Helmet detection
- Mask detection
- Person detection
- Violation logging
- Evidence image capture
- REST API backend
- Streamlit analytics dashboard

## Run Detection
python app/main.py

## Run API
uvicorn app.api:app --reload

## Run Dashboard
streamlit run dashboard/dashboard.py
