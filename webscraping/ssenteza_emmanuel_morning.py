# kindly install the requests library and the pandas library as
# they are the ones required for this project on web scraping
import requests
import pandas as pd

url_recordings_api = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"
species_data = []

response = requests.get(url_recordings_api)

if response.status_code == 200:
    data = response.json()
    if "recordings" in data:
        for recording in data["recordings"]:
            species_data.append(
                {
                    "Species": recording["en"],
                    "general name": recording["gen"],
                    "specific name": recording["sp"]

                }
            )


df = pd.DataFrame(species_data)

# Save the DataFrame to a CSV file
csv_file_path = "bird_species_data_not_filtered.csv"
df.to_csv(csv_file_path, index=False, header=[
          col.upper() for col in df.columns])

# remove duplicates based on 'Species' column
df.drop_duplicates(subset=["Species"], inplace=True)

# Save the filtered DataFrame to a CSV
csv_file_path = "bird_species_data_filtered.csv"
df.to_csv(csv_file_path, index=False, header=[
          col.upper() for col in df.columns])

print("CSV file generated successfully.")
