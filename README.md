# 🌍️ Service Locator

### Google Places Data Fetcher 🌍  

This project is a **Python script** that interacts with the **Google Places API** to fetch and display information about nearby places of interest based on user-provided **coordinates, search radius**, and **place type** (e.g., schools, restaurants, hospitals, etc.).  

---

### 👤 **Project Owner**  
**Adit Mugdha Das** ✨  

---

## ⭐ Features  

- **Fetch Nearby Places**:  
  Allows users to find places (e.g., businesses, landmarks) around a specified location. 🏢  

- **Custom Search**:  
  Specify the **search radius** (in kilometers) and **keyword** to filter results (e.g., `school`, `restaurant`). 🔍  

- **Data Validation**:  
  Automatically validates **latitude and longitude** inputs to ensure they fall within the valid **ranges for Bangladesh**. ✅  

- **Network Handling**:  
  Automatically detects and handles **network disconnections**, retrying operations once connectivity is restored. 🌐  

- **Detailed Information**:  
  Fetches additional details for each place, such as:  
  - Name 🏷️  
  - Address 📍  
  - Latitude & Longitude 🌎  
  - Phone Number ☎️  
  - Website 🌐  

---

## ⚠️ **Important Notice**  

🔴 **This script works only for locations within Bangladesh.**  
- **Latitude Range:** `20.34° N` to `26.63° N`  
- **Longitude Range:** `88.01° E` to `92.67° E`  

🛒 Any coordinates outside this range will be rejected.

---

## 🗰️ Setup Instructions  

### 1⃣ **Install Python & Dependencies**  
- Install **Python (3.x)** if not already installed.  
- Install the required dependencies:  
  ```bash
  pip install pandas requests folium openpyxl
  ```

### 2⃣ **Get a Google Maps API Key**  
To use the **Google Places API**, you need an API key:  
1. Go to [Google Cloud Console](https://console.cloud.google.com/).  
2. Enable the **Places API** under the API library.  
3. Generate an **API Key** from the credentials page.  
4. Replace `"YOUR_GOOGLE_MAPS_API_KEY"` in the script:  
   ```python
   API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
   ```

---

### 🚀 **How to Run**  

1⃣ **Run the script**:  
   Open a terminal or command prompt and run the script:  
   ```bash
   python script.py
   ```

2⃣ **Enter location details**:  
   - Enter **latitude, longitude** (e.g., `23.8103,90.4125`).  
   - Enter the **search radius** in kilometers (e.g., `5`).  
   - Enter the **place type** you want to search for (e.g., `restaurant`, `school`, `hospital`, etc.).  

3⃣ **Output Files Generated**:  
   - **Excel File (`output.xlsx`)** → Contains a list of places with detailed information.  
   - **HTML Map (`map.html`)** → Displays all locations on an interactive map.

---

## 📂 **Project Structure**  

```
🗋 Service-Locator
 ├── 🖄 script.py          # Main Python script
 ├── 🖄 requirements.txt   # Dependencies list
 ├── 🖄 README.md          # Documentation
 ├── 🖄 map.html           # Generated interactive map
 ├── 🖄 output.xlsx        # Excel file with results
```

---

## 🗂️ **Example Output (Excel File)**  

| Name            | Address                    | Latitude | Longitude | Phone Number | Website       |
|------------------|----------------------------|----------|-----------|--------------|---------------|
| ABC Restaurant   | 123 Main St, Dhaka         | 23.8103  | 90.4125   | 0123456789   | www.abc.com   |
| XYZ School       | 456 School Rd, Chattogram  | 22.3569  | 91.7832   | N/A          | N/A           |

---

## 📍 **Interactive Map Preview**  

The generated **`map.html`** file can be opened in any web browser to view all locations.  

- Each place is marked with a **pin** 🖍️.  
- Clicking on a pin shows the **name, address, phone number, and website** (if available).  

---

## ⚠️ **Google API Limitations**  

- The **Google Places API free tier** has **daily request limits**.  
- The `next_page_token` requires a **2-second delay** before fetching the next page.  
- Some places may not provide **phone numbers** or **websites**.  

---

## 🛠️ **Troubleshooting**  

- **Problem:** Script says `"Invalid Latitude/Longitude"`  
  **Solution:** Ensure the coordinates are within Bangladesh.  

- **Problem:** Script is not fetching phone numbers or websites.  
  **Solution:** Some places may not provide this information via the Google Places API.  

- **Problem:** `"Network Disconnected"` error appears.  
  **Solution:** Check your internet connection and restart the script.  

---

## 📜 **License**  

This project is **open-source** and licensed under the **MIT License**.  

---

### 🎮 **Happy Mapping! 🌏**

