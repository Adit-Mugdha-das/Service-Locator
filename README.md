# Internet-Service-Locator
# Google Places Data Fetcher 🌍

This project is a Python script that interacts with the Google Places API to fetch and display information about nearby places of interest based on user-provided coordinates and search radius.
**Project Owner:** Adit Mugdha Das 👨‍💻

## Features ✨

- **Fetch Nearby Places**: Allows users to find places (e.g., businesses, landmarks) around a specified location. 🏢
- **Custom Search**: Users can specify the search radius (in kilometers) and keyword to filter results (default: `internet service provider`). 🔍
- **Data Validation**: Validates the latitude and longitude inputs against the ranges for Bangladesh. ✅
- **Network Handling**: Automatically detects and handles network disconnections, retrying operations once connectivity is restored. 🌐
- **Detailed Information**: Fetches additional details such as:
  - Place name 🏷️
  - Address 📍
  - Latitude and longitude 🗺️
  - Phone number ☎️
  - Website 🌐
- **Save Results**: Outputs the fetched data to an Excel file (`.xlsx` format). 📊
- **Interactive Map**: Creates an interactive HTML map showing the locations of the fetched places. 🗺️
- **Automated File Creation**: No need to manually create output files; the script generates them for you! 📂
- **Quick and Easy Information Retrieval**: Get all the details of nearby internet service providers in one file without manually searching Google. ⚡
- **Bangladesh-Specific Support**: This script is designed to work within Bangladesh's latitude and longitude ranges. 🌏

## ⚠️ Attention ⚠️
This script is specifically built for use **only within Bangladesh**. It will not work for locations outside the defined latitude and longitude range.

## Prerequisites ⚙️

### API Key 🔑
You need a valid Google Maps API key with access to the Places API. Replace the placeholder `"Your Api Key"` in the script with your actual API key.

### Python Libraries 🐍
Make sure the following Python libraries are installed:
- `pandas`
- `requests`
- `folium`

Install them using pip if not already installed:
```bash
pip install pandas requests folium
```

## How to Use 🚀

1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script using Python:
   ```bash
   python <script_name>.py
   ```
4. Follow the prompts:
   - Enter `latitude,longitude` (e.g., `23.8103,90.4125` for Dhaka).
   - Enter the search radius in kilometers.
   - Enter the desired output file name (without extension).
5. The script will:
   - Fetch data about nearby places. 🌟
   - Save the data to an Excel file (e.g., `output_filename.xlsx`). 📄
   - Create an interactive map (`map.html`) showing the fetched places. 🗺️

## Example Usage 📝

1. **Input**:
   ```
   Enter latitude,longitude: 23.8103,90.4125
   Enter search radius (km): 2
   Enter output file name (without extension): dhaka_places
   ```
2. **Output**:
   - Excel file: `dhaka_places.xlsx` 📄
   - Interactive map: `map.html` 🗺️

## Script Structure 🛠️

### Functions 🔧
1. `check_network()`: Verifies internet connectivity. 🌐
2. `get_place_details(place_id)`: Fetches detailed information (phone number, website) for a specific place. 📞
3. `get_nearby_places(lat, lng, radius, keyword)`: Retrieves nearby places based on coordinates and search radius. 📍
4. `fetch_places_for_coordinates(keyword)`: Handles user input and coordinates validation. ✅
5. `create_map(places, output_file)`: Generates an interactive map of the fetched places. 🗺️

### Main Execution Flow 🏗️
The script:
1. Accepts user inputs for coordinates, radius, and output file name. 📝
2. Fetches and validates data from the Google Places API. 🌍
3. Saves the results to an Excel file. 📄
4. Optionally generates an interactive map. 🗺️

## Features in Detail 📖

### Robust Input Validation ✅
- Ensures latitude is within `[20.34, 26.63]`.
- Ensures longitude is within `[88.01, 92.67]`.
- Prompts the user until valid inputs are provided.

### Intelligent Network Handling 🌐
- Automatically detects network disconnections.
- Retries the operation once the connection is restored.
- Ensures seamless user experience.

### Comprehensive Data 📊
- Fetches not just the name and address, but also:
  - Phone number ☎️
  - Website 🌐
  - Precise geographic coordinates 🗺️

### Outputs 📤
1. **Excel File**: Tabular data with all fetched details. 📄
2. **Interactive Map**: Visual representation of locations, with popups showing detailed information. 🗺️

## Acknowledgments 🙏
- [Google Maps API](https://developers.google.com/maps/documentation/places/overview) for providing the data. 🌍
- [Pandas](https://pandas.pydata.org/) for data handling. 📊
- [Folium](https://python-visualization.github.io/folium/) for creating interactive maps. 🗺️


---
Feel free to contribute to this project by submitting issues or pull requests! 🤝
