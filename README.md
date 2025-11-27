# Energy Power Plant Control Panel (SCADA Dashboard)

This project is a web-based SCADA/Dashboard application designed to monitor real-time energy data from Wind Power Plants (RES) and Solar Power Plants (GES). It was developed as part of an internship project at Konelsis.

## 🚀 Features

* **Real-Time Monitoring:** Reads instant data from field analyzers using the Modbus TCP protocol.
* **Dynamic Visualization:** Displays instant active power (kW) and daily production (MWh) in card format.
* **Mobile-First Design:** Fully responsive UI/UX optimized for tablets and mobile devices.
* **Detailed Analytics:** Lists detailed electrical parameters such as voltage, current, frequency, and reactive power for each power plant.

## 🛠 Tech Stack

* **Backend:** Python, FastAPI, Pymodbus (for Modbus TCP communication)
* **Frontend:** HTML5, CSS3, JavaScript
* **Styling:** Tailwind CSS
* **Data Format:** JSON API

## ⚙️ Installation & Usage

1. Install the required Python libraries:
   ```bash
   pip install fastapi uvicorn pymodbus
