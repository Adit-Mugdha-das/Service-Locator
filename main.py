import pandas as pd
import requests
import folium
import time

# Google API details
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"  # Replace with your actual API key
PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
PLACE_DETAILS_API_URL = "https://maps.googleapis.com/maps/api/place/details/json"

# Valid latitude and longitude ranges
valid_lat_range = (20.34, 26.63)
valid_lon_range = (88.01, 92.67)

# Function to check network connectivity
def check_network():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Function to fetch place details (phone and website)
def get_place_details(place_id):
    params = {
        "place_id": place_id,
        "fields": "formatted_phone_number,website",
        "key": API_KEY
    }
    while True:
        if check_network():
            try:
                response = requests.get(PLACE_DETAILS_API_URL, params=params)
                if response.status_code == 200:
                    return response.json().get("result", {})
                else:
                    print(f"Error fetching details for Place ID {place_id}: {response.status_code}, {response.text}")
                    return {}
            except Exception as e:
                print(f"Request failed for Place ID {place_id}: {e}")
                return {}
        else:
            print("Network is disconnected, trying to reconnect once...")
            time.sleep(5)
            if check_network():
                print("Network reconnected, resuming operation...")

# Function to fetch nearby places with pagination support
def get_nearby_places(lat, lng, radius, keyword):
    all_results = []
    params = {
        "location": f"{lat},{lng}",
        "radius": radius,
        "keyword": keyword,
        "key": API_KEY
    }

    while True:
        if check_network():
            response = requests.get(PLACES_API_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                results = data.get("results", [])
                all_results.extend(results)

                # Check for next_page_token
                next_page_token = data.get("next_page_token")
                if next_page_token:
                    print("Fetching more results...")
                    time.sleep(2)  # Required delay before using next_page_token
                    params["pagetoken"] = next_page_token
                else:
                    break  # No more pages
            else:
                print(f"Error: {response.status_code}, {response.text}")
                break
        else:
            print("Network is disconnected, trying to reconnect once...")
            time.sleep(5)
            if check_network():
                print("Network reconnected, resuming operation...")

    return all_results

# Function to process user input coordinates and type of place
def fetch_places_for_coordinates():
    while True:
        try:
            user_input = input("Enter latitude,longitude: ")
            lat, lng = map(float, user_input.split(","))
            invalid_entries = []
            if not (valid_lat_range[0] <= lat <= valid_lat_range[1]):
                invalid_entries.append("latitude")
            if not (valid_lon_range[0] <= lng <= valid_lon_range[1]):
                invalid_entries.append("longitude")
            
            if invalid_entries:
                print(f"Invalid {', '.join(invalid_entries)}. Please enter valid values.")
                continue
            
            break
        except ValueError:
            print("Invalid input format. Please enter latitude and longitude separated by a comma.")
    
    while True:
        try:
            radius_km = float(input("Enter search radius (km): "))
            radius = int(radius_km * 1000)  # Convert km to meters
            break
        except ValueError:
            print("Invalid radius. Please enter a valid number.")

    keyword = input("Enter the type of place you want to search (e.g., school, restaurant, etc.): ").strip()
    print(f"Fetching places for coordinates: ({lat}, {lng}) with radius {radius_km} km and keyword '{keyword}'")
    places = get_nearby_places(lat, lng, radius=radius, keyword=keyword)
    
    if not places:
        print(f"No places found for ({lat}, {lng}) with keyword '{keyword}'.")
    
    all_places = []
    for place in places:
        place_id = place.get("place_id")
        details = get_place_details(place_id) if place_id else {}
        all_places.append({
            "Input Latitude": lat,
            "Input Longitude": lng,
            "Name": place.get("name"),
            "Address": place.get("vicinity"),
            "Latitude": place["geometry"]["location"]["lat"],
            "Longitude": place["geometry"]["location"]["lng"],
            "Phone Number": details.get("formatted_phone_number", "N/A"),
            "Website": details.get("website", "N/A")
        })
        
    time.sleep(1)  # Avoid hitting API rate limits

    print(f"Collected {len(all_places)} places.")
    return all_places

# Function to create an interactive map
def create_map(places, output_file):
    if not places:
        print("No places to map.")
        return
    
    map_center = [places[0]["Latitude"], places[0]["Longitude"]]
    m = folium.Map(location=map_center, zoom_start=12)

    for place in places:
        folium.Marker(
            location=[place["Latitude"], place["Longitude"]],
            popup=(f"<b>{place['Name']}</b><br>"
                   f"{place['Address']}<br>"
                   f"Phone: {place['Phone Number']}<br>"
                   f"<a href='{place['Website']}' target='_blank'>Website</a>"),
        ).add_to(m)

    try:
        m.save(output_file)
        print(f"Map saved to {output_file}")
    except Exception as e:
        print(f"Error saving map: {e}")

# Main execution flow
if __name__ == "__main__":
    output_filename = input("Enter output file name (without extension): ")
    output_file = f"{output_filename}.xlsx"
    map_file = "map.html"  # Map generation is enabled now

    places_data = fetch_places_for_coordinates()
    
    if places_data:
        pd.DataFrame(places_data).to_excel(output_file, index=False)
        print(f"Details saved to {output_file}")
        create_map(places_data, map_file)  # Generate the map
