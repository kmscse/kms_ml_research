import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from scipy.ndimage import gaussian_filter
import seaborn as sns
from adjustText import adjust_text
import matplotlib.patches as mpatches

# Load the earthquake data from your local file
file_path = 'file path'
earthquake_data = pd.read_excel(file_path)

# List of specific record sequence numbers (RSNs) to emphasize
specific_rsns = [
    3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 34, 35, 36, 41,
    51, 97, 98, 101, 106, 107, 109, 112, 135, 145, 158, 193, 209, 210, 217, 225, 230, 233, 236, 240, 244,
    246, 251, 257, 270, 314, 320, 321, 322, 370, 391, 394, 405, 416, 418, 423, 446, 485, 499, 502, 511,
    543, 548, 559, 562, 585, 589, 707, 718, 719, 731, 825, 832, 901, 942, 1630, 1641, 1650, 1668, 1675,
    1682, 1691, 1756, 1759, 1843, 1868, 1917, 1990, 2002, 2011, 2047, 2119, 3684, 3744
]

# Filter the data to include only the specific RSNs
filtered_data = earthquake_data[earthquake_data['Record Sequence Number'].isin(specific_rsns)]

# Initialize a figure for plotting
plt.figure(figsize=(10, 15))

# Create a basemap of California
m = Basemap(projection='merc', llcrnrlat=32, urcrnrlat=42,
            llcrnrlon=-125, urcrnrlon=-114, lat_ts=20, resolution='i')

# Draw map boundaries and coastlines
m.drawmapboundary(fill_color='white')
m.fillcontinents(color='silver', lake_color='grey') #lake_color='aqua
m.drawcoastlines()

# Draw country boundaries and states
m.drawcountries()
m.drawstates()

# Read the shapefile for California and fill it
m.readshapefile('file path', 'california', drawbounds=True, color='magenta')

# Assuming 'california_info' and 'california' are returned by readshapefile
for info, shape in zip(m.california_info, m.california):
    if info['NAME'] == 'California':
        x, y = zip(*shape)
        m.plot(x, y, marker=None, color='magenta')


m.drawcoastlines()
m.drawcountries()
m.drawstates()

# Convert latitude and longitude to x and y coordinates
coordinates = m(list(filtered_data['Longitude']), list(filtered_data['Latitude']))
x, y = coordinates

# Define the bins for the histogram
x_bins = np.linspace(min(x), max(x), 101)  # 100 bins + 1 for the edge
y_bins = np.linspace(min(y), max(y), 101)  # 100 bins + 1 for the edge

# Compute the 2d histogram
zi, x_edges, y_edges = np.histogram2d(y, x, bins=(y_bins, x_bins), weights=filtered_data['Magnitude'], density=True)

# Smooth the histogram with a gaussian filter
zi_smooth = gaussian_filter(zi, sigma=5)

# Create the meshgrid for the x and y edges
x_center = (x_edges[:-1] + x_edges[1:]) / 2
y_center = (y_edges[:-1] + y_edges[1:]) / 2
x_contour, y_contour = np.meshgrid(x_center, y_center)

# Plot the smoothed histogram as a colorized contour map
m.contourf(x_contour, y_contour, zi_smooth, levels=15, cmap="viridis", alpha=0.5, latlon=True)

# Plot the earthquakes on the basemap
scatter = m.scatter(x, y, s=filtered_data['Magnitude']**2.5, c=filtered_data['Magnitude'], cmap='viridis', alpha=0.75)

# Add a colorbar and a legend
plt.colorbar(label='Magnitude')
plt.clim(4, 8)

# Annotate with earthquake names and years
texts = []
for _, row in filtered_data.iterrows():
    x_point, y_point = m(row['Longitude'], row['Latitude'])
    texts.append(plt.text(x_point, y_point, f"{row['Earthquake Name']} {row['Year']}", fontsize=5, ha='left', va='top', color='blue'))

adjust_text(texts, x=x, y=y)

# Draw parallels and meridians.
parallels = np.arange(32., 43., 1.)
meridians = np.arange(-125., -113., 1.)

# Labels = [left, right, top, bottom]
m.drawparallels(parallels, labels=[True, False, False, False])
m.drawmeridians(meridians, labels=[False, False, False, True])


# Create a discrete colormap for the legend
magnitude_bins = [4, 5, 6, 7, 8]  # The magnitude divisions for your legend
magnitude_colors = scatter.cmap(scatter.norm(magnitude_bins))  # Get the corresponding colors from the scatter plot

# Create a list of patches for the legend
legend_patches = [
    mpatches.Patch(color=magnitude_colors[i], label=f'M < {magnitude_bins[i+1]}') for i in range(len(magnitude_bins)-1)
]

# Add the custom legend to the plot
plt.legend(handles=legend_patches, loc='upper right', title='Magnitude')

# Get the lower left-hand corner of the map
lllon, lllat = m.llcrnrlon, m.llcrnrlat

# Place the text at the lower left-hand corner, with a slight offset
offset_pacific = 1 
text_x_pacific, text_y_pacific = m(lllon + offset_pacific, lllat + offset_pacific)


# Now place the texts using plt.text
plt.text(text_x_pacific, text_y_pacific, "North Pacific Ocean", fontsize=20, ha='left', va='bottom', color='black', rotation=-48)

text = {
    "California" : {
        "lat": 41.4622,
        "lon": -122.1035,
    },
    "San Francisco": {
        "lat": 37.7749,
        "lon": -122.4194
    },
    "Los Angeles": {
        "lat": 34.0522,
        "lon": -118.2437
    },
    "San Diego": {
        "lat": 32.7157,
        "lon": -117.1611
    },
    "San Jose": {
        "lat": 37.3382,
        "lon": -121.8863
    },
    "Sacramento": {
        "lat": 38.5816,
        "lon": -121.4944
    }
    }

keys = text.keys()
x_California, y_California = m(text["California"]["lon"], text["California"]["lat"])
x_SanFrancisco, y_SanFrancisco = m(text["San Francisco"]["lon"], text["San Francisco"]["lat"])
x_LosAngeles, y_LosAngeles = m(text["Los Angeles"]["lon"], text["Los Angeles"]["lat"])
x_SanDiego, y_SanDiego = m(text["San Diego"]["lon"], text["San Diego"]["lat"])
x_SanJose, y_SanJose = m(text["San Jose"]["lon"], text["San Jose"]["lat"])
x_Sacramento, y_Sacramento = m(text["Sacramento"]["lon"], text["Sacramento"]["lat"])

for key in keys:
    if key == "California":
        text = "California"
        plt.text(x_California, y_California, text, fontsize=20, ha='center', va='center', color='black')
    if key == "San Francisco":
        text = "San Francisco"
        plt.text(x_SanFrancisco, y_SanFrancisco, text, fontsize=12, ha='center', va='center', color='black')
    if key == "Los Angeles":
        text = "Los Angeles"
        plt.text(x_LosAngeles, y_LosAngeles, text, fontsize=12, ha='center', va='center', color='black')
    if key == "San Diego":
        text = "San Diego"
        plt.text(x_SanDiego, y_SanDiego, text, fontsize=12, ha='center', va='center', color='black')
    if key == "San Jose":
        text = "San Jose"
        plt.text(x_SanJose, y_SanJose, text, fontsize=12, ha='center', va='center', color='black')
    if key == "Sacramento":
        text = "Sacramento"
        plt.text(x_Sacramento, y_Sacramento, text, fontsize=12, ha='center', va='center', color='black')

plt.title('100 Earthquakes Shaping California\'s Seismic Landscape')
plt.show()
