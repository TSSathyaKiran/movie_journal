import pandas as pd
import re
import requests
from requests.exceptions import RequestException

def get_720p_poster_url(poster_url):
    """
    Updates the size and crop parameters of an IMDb poster URL to a 720p height.
    A standard 2:3 aspect ratio is assumed, resulting in a 480x720 pixel image.

    Args:
        poster_url (str): The original URL from the dataset.

    Returns:
        str: The updated URL with the new resolution, or the original URL if no match is found.
    """
    # This regex pattern finds the base URL, the size parameters, and the file extension.
    # It specifically looks for the format "_V1..._AL_.jpg"
    pattern = r'^(.*)\._V1.*?(\.jpg)$'
    match = re.match(pattern, poster_url)

    if match:
        # Define the target dimensions for a 720p-height poster (480x720)
        target_width = 480
        target_height = 720
        
        # Reconstruct the URL with the new, specific size parameters
        # IMDb's URL format is usually ..._V1_UX[width]_CR0,0,[width],[height]_AL_.jpg
        new_url = f"{match.group(1)}._V1_UX{target_width}_CR0,0,{target_width},{target_height}_AL_.jpg"
        
        # In case the URL already has a different format, this fallback still returns a valid URL
        return new_url
        
    return poster_url

def check_url_validity(url):
    """
    Checks if a URL is valid and returns a 200 status code.
    
    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    try:
        # Using a timeout to prevent the script from hanging on bad URLs.
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except RequestException as e:
        print(f"Error checking URL {url}: {e}")
        return False

def update_poster_urls_in_csv(input_filename, output_filename):
    """
    Reads a CSV, updates the Poster_Link column, and saves the new data.

    Args:
        input_filename (str): The name of the original CSV file.
        output_filename (str): The name of the new CSV file to save.
    """
    try:
        # Read the CSV file into a pandas DataFrame.
        df = pd.read_csv(input_filename)
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return

    print("Updating poster URLs to 720p height...")
    
    # Apply the new function to the 'Poster_Link' column.
    df['Poster_Link'] = df['Poster_Link'].apply(get_720p_poster_url)
    
    print("New URLs created. Saving to a new file...")
    
    # Save the updated DataFrame to a new CSV file.
    df.to_csv(output_filename, index=False)
    
    print(f"Update complete! The new file '{output_filename}' has been created.")
    print("Your original file remains unchanged.")

if __name__ == "__main__":
    input_file = "imdb_top_1000.csv"
    output_file = "updated_movies_720p.csv"
    update_poster_urls_in_csv(input_file, output_file)
