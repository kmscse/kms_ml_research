import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# file path
csv_file_path = 'material-stress-strain-curve-rebar.csv'

# Load the CSV data into a DataFrame
data = pd.read_csv(csv_file_path)
# Convert stress from N/mm^2 to MPa (1 N/mm^2 = 1 MPa)
data['Stress (MPa)'] = data['Stress (N/mm2)']

# Setup the plot
plt.figure(figsize=(10, 8))

# Plot the stress-strain curve
plt.plot(data['Strain'], data['Stress (MPa)'], marker='s', color='magenta', label='Axial')
plt.legend(loc='center left')

# Highlight the maximum and minimum points
max_point = data.loc[data['Stress (MPa)'].idxmax()]
min_point = data.loc[data['Stress (MPa)'].idxmin()]
plt.scatter(max_point['Strain'], max_point['Stress (MPa)'], color='red', zorder=5)
plt.scatter(min_point['Strain'], min_point['Stress (MPa)'], color='blue', zorder=5)
# plt.text(max_point['Strain'], max_point['Stress (MPa)'], verticalalignment='bottom', horizontalalignment='right', color='red')
# plt.text(min_point['Strain'], min_point['Stress (MPa)'], verticalalignment='top', horizontalalignment='left', color='blue')

# Annotate points with Point ID
for _, row in data.dropna().iterrows():
    plt.annotate(row['Point ID'], (row['Strain'], row['Stress (MPa)']), textcoords="offset points", xytext=(0,10), ha='center')

# Set titles and labels
plt.title('Material Stress-Strain Plot (Rebar)', fontsize=16)
plt.xlabel('Strain', fontsize=14)
plt.ylabel('Stress (MPa)', fontsize=14)

# Add grid, legend, and set limits
plt.grid(True)
plt.legend()
plt.xlim(-0.15, 0.15)
plt.ylim(-800, 800)
plt.yticks(np.arange(-800, 801, 100))

# Adding a horizontal line at zero stress and vertical line at zero strain
plt.axhline(0, color='grey', lw=1)
plt.axvline(0, color='grey', lw=1)

# Annotate the maximum and minimum points with detailed information
max_annotation = f"Max: ({max_point['Strain']:.4f}, {max_point['Stress (MPa)']:.2f}) [Axial, Point {max_point['Point Number']}]"
min_annotation = f"Min: ({min_point['Strain']:.4f}, {min_point['Stress (MPa)']:.2f}) [Axial, Point {min_point['Point Number']}]"
plt.annotate(max_annotation, (max_point['Strain'], max_point['Stress (MPa)']), textcoords="offset points", xytext=(0,10), ha='center', color='red')
plt.annotate(min_annotation, (min_point['Strain'], min_point['Stress (MPa)']), textcoords="offset points", xytext=(0,-15), ha='center', color='blue')

# Show the plot
plt.tight_layout()
plt.show()
