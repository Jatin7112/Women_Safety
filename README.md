# 🛡️Women Safety and Complaint Management System

## Project Overview
The Women Safety and Complaint Management System is a web-based platform designed to enhance women's safety by providing multiple complaint registration options, emergency reporting features, and a smart route finder that prioritizes safety-related locations such as police stations, hospitals, and fuel stations.

## 🚀Features

### Complaint Management
- Anonymous Complaint with video upload support.
- Direct Complaint with personal details and video upload support.
- Instant Complaint for emergency situations.
- Unique Tracking ID generation for complaint tracking.

### 📍Smart Route Finder
- Finds safer routes.
- Displays nearby Police Stations, Hospitals, and Petrol Pumps.
- Automatically detects user location.
- Interactive map interface.

# 📂 Project Structure

```text
Project Folder
│
├── app.py                  # Flask backend
│
├── templates/              # Frontend interface
│   ├── home.html
│   ├── index.html
│   └── route_finder.html
│
├── complaint/              # Folder containing CSV data
│   ├── instant_complaint.csv
│   ├── direct_complaint.csv
│   └── anonymous_complaint.csv
│
├── complaint_video/        # Video storage folder
│
└── README.md                                                                                ```

## File Description

### app.py
Main backend application file responsible for:
- Connecting frontend and backend
- Handling complaint submissions
- Managing video uploads
- Generating tracking IDs
- Storing complaint data in CSV files

### home.html
Main landing page containing:
- Instant Complaint feature
- Women safety information
- Website navigation

### index.html
Complaint registration page containing:
- Anonymous Complaint
- Direct Complaint
- Video Upload feature

### route_finder.html
Smart route finder page that:
- Finds routes with nearby police stations, hospitals, and petrol pumps
- Auto-detects user location
- Displays routes on an interactive map

## Complaint Files

### instant_complaint.csv
Stores:
- Tracking ID
- Complaint Description
- Phone NO

### direct_complaint.csv
Stores:
- Tracking ID
- Name
- Email
- Contact Number
- Complaint Details

### anonymous_complaint.csv
Stores:
- Tracking ID
- Complaint Details
- No personal information

## complaint_video
Stores videos uploaded through:
- Anonymous Complaints
- Direct Complaints

## ⚙️Technologies Used
Frontend:
- HTML
- CSS
- JavaScript

Backend:
- Python
- Flask

Database:
- CSV Files

Maps & Routing:
- Leaflet.js
- OpenStreetMap
- OSRM
- Overpass API

## 🔧Installation

1. Install dependencies:
pip install flask

2. Run application:
python app.py

3. Open browser:
http://127.0.0.1:5000

## Future Enhancements
- Admin Dashboard
- User Authentication
- SMS/Email Notifications
- Complaint Status Tracking
- Database Integration
- Real-Time Emergency Alerts

## Disclaimer
This project is developed for educational and social welfare purposes to promote women's safety and provide an accessible complaint reporting platform.

## Author

**Jatin Rajoria**

AI Enthusiast | Python Developer | Generative AI Learner



