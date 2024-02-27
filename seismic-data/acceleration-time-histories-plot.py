import pandas as pd
import matplotlib.pyplot as plt

# Replace with the path to your .AT2 file
file_path = 'C:\/Users\/Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Spectral Matching/RSN3_HUMBOLT_FRN225.AT2'

# Read the data from the .AT2 file
# This might need adjustment depending on the actual file format
# Skipping initial rows if there are headers or metadata (adjust the number as needed)
data = pd.read_csv(file_path, skiprows=4, delim_whitespace=True, header=None, names=['Time', 'Acceleration'])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(data['Time'], data['Acceleration'], label='Acceleration', color='blue', linewidth=1.5)
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g)')
plt.title('Acceleration Time History')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('acceleration_time_history.png')

# Show the plot
plt.show()
