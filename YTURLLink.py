# %%
# !pip install pywhatkit
# !pip install six.moves

import urllib.request as ur
import re
import csv



# %%
html = ur.urlopen('https://www.youtube.com/results?search_query=BlackAdam+official+Trailer')

videoId = re.findall(r"watch\?v=(\S{11})",html.read().decode())

# print(videoId)
print("https://www.youtube.com/watch?v="+videoId[0])

# %%
import csv
import urllib.request  # Import the correct library for opening URLs

# Define your list of items
items = ["BlackAdam", "TheBeekeeper", "IronMan"]

# Open the CSV file in write mode with error handling
try:
    with open("my_items.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["YTLink"])  # Assuming you want only YouTube links

        # Loop through the list and write YouTube links to the CSV
        for item in items:
            url = f"https://www.youtube.com/results?search_query={item}+officialTrailer"  # Use f-string for cleaner formatting
            try:
                with urllib.request.urlopen(url) as response:
                    html_content = response.read().decode()
                    video_id = re.findall(r"watch\?v=(\S{11})", html_content)
                    if video_id:  # Check if video IDs are found
                        youtube_link = f"https://www.youtube.com/watch?v={video_id[0]}"
                        writer.writerow([youtube_link])
                    else:
                        writer.writerow(["No video found for {}".format(item)])  # Handle cases where no video is found
            except urllib.error.URLError as e:
                writer.writerow(["Error fetching link for {}: {}".format(item, e)])  # Handle URL errors

except OSError as e:  # Handle file system errors
    print("Error creating CSV file:", e)

print("Items saved successfully (or errors logged) to 'my_items.csv'")


# %%


html = ur.urlopen('https://www.youtube.com/results?search_query=BlackAdam+official+Trailer')

videoId = re.findall(r"watch\?v=(\S{11})",html.read().decode())

# print(videoId)
print("https://www.youtube.com/watch?v="+videoId[0])



