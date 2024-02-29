import numpy as np

def make_t_series(filepath, time_step):
    with open(filepath, 'r') as file:
        file_content = file.read()
    lines = file_content.strip().split('\n')
    start_line = 4
    t_series = []

    for line in lines[start_line:]:
        columns = line.split()
        values = [float(val) for val in columns[1:] if val]
        t_series.extend(values)
    
    t_series = np.array(t_series)
    t = np.arange(0, time_step * len(t_series), time_step)
    return t, t_series

def make_motion(filepath_a, filepath_v, filepath_d, t_step):
    t, t_series_a = make_t_series(filepath_a, t_step)
    _, t_series_v = make_t_series(filepath_v, t_step)
    _, t_series_d = make_t_series(filepath_d, t_step)
    
    # Determine the minimum length among the three series
    min_length = min(len(t_series_a), len(t_series_v), len(t_series_d))
    
    # Truncate the series and the time array to this minimum length
    t = t[:min_length]
    t_series_a = t_series_a[:min_length]
    t_series_v = t_series_v[:min_length]
    t_series_d = t_series_d[:min_length]
    
    # Now that all arrays have the same length, concatenate them
    data = np.column_stack((t, t_series_a, t_series_v, t_series_d))
    return data

def process_component(filepath_a, filepath_v, filepath_d, dt):
    data = make_motion(filepath_a, filepath_v, filepath_d, dt)
    return {
        'PGA': np.max(np.abs(data[:, 1])),
        'PGV': np.max(np.abs(data[:, 2])),
        'PGD': np.max(np.abs(data[:, 3]))
    }

# 
# ------------------------------------- Beginning of Earthquake1 to Earthqauke10 --------------------------------
# ------------------------------------- Earthquake 1 --------------------------------------------------
accelerationFilePaths_quake1 = [
    'Earthquake_01_(Humbolt Bay)_RSN3\RSN3_HUMBOLT_FRN225_A.txt', 
    'Earthquake_01_(Humbolt Bay)_RSN3\RSN3_HUMBOLT_FRN315_A.txt', 
    'Earthquake_01_(Humbolt Bay)_RSN3\RSN3_HUMBOLT_FRN-UP_A.txt'
]

velocityFilePaths_quake1 = [
    'Earthquake_01_(Humbolt Bay)_RSN3\RSN3_HUMBOLT_FRN225_V.txt',
    'Earthquake_01_(Humbolt Bay)_RSN3\RSN3_HUMBOLT_FRN315_V.txt',
    'Earthquake_01_(Humbolt Bay)_RSN3\RSN3_HUMBOLT_FRN-UP_V.txt'
]

displacementFilePaths_quake1 = [
    'Earthquake_01_(Humbolt Bay)_RSN3\RSN3_HUMBOLT_FRN225_D.txt',
    'Earthquake_01_(Humbolt Bay)_RSN3\RSN3_HUMBOLT_FRN315_D.txt',
    'Earthquake_01_(Humbolt Bay)_RSN3\RSN3_HUMBOLT_FRN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake1[i], velocityFilePaths_quake1[i], displacementFilePaths_quake1[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 1'
name = 'HUMBOLT'
record_sequence_number = 3
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake1_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake1_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 2 --------------------------------------------------
# Earthquake2
accelerationFilePaths_quake2 = [
    'Earthquake_02_(Imperial Valley-01)_RSN4\RSN4_IMPVALL.BG_B-ELC000_A.txt', 
    'Earthquake_02_(Imperial Valley-01)_RSN4\RSN4_IMPVALL.BG_B-ELC090_A.txt', 
    'Earthquake_02_(Imperial Valley-01)_RSN4\RSN4_IMPVALL.BG_B-ELC-UP_A.txt'
]

velocityFilePaths_quake2 = [
    'Earthquake_02_(Imperial Valley-01)_RSN4\RSN4_IMPVALL.BG_B-ELC000_V.txt',
    'Earthquake_02_(Imperial Valley-01)_RSN4\RSN4_IMPVALL.BG_B-ELC090_V.txt',
    'Earthquake_02_(Imperial Valley-01)_RSN4\RSN4_IMPVALL.BG_B-ELC-UP_V.txt'
]

displacementFilePaths_quake2 = [
    'Earthquake_02_(Imperial Valley-01)_RSN4\RSN4_IMPVALL.BG_B-ELC000_D.txt',
    'Earthquake_02_(Imperial Valley-01)_RSN4\RSN4_IMPVALL.BG_B-ELC090_D.txt',
    'Earthquake_02_(Imperial Valley-01)_RSN4\RSN4_IMPVALL.BG_B-ELC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake2[i], velocityFilePaths_quake2[i], displacementFilePaths_quake2[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 2'
name = 'Imperial Valley-01'
record_sequence_number = 4
earthquake_station = 'El Centro Array #9'

# Function to print the results in the desired format
def print_earthquake2_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

print_earthquake2_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 3 --------------------------------------------------
# Earthquake3
accelerationFilePaths_quake3 = [
    'Earthquake_03_(Northwest Calif-01)_RSN5\RSN5_NWCALIF.AB_A-FRN045_A.txt', 
    'Earthquake_03_(Northwest Calif-01)_RSN5\RSN5_NWCALIF.AB_A-FRN135_A.txt', 
    'Earthquake_03_(Northwest Calif-01)_RSN5\RSN5_NWCALIF.AB_A-FRNDWN_A.txt'
]

velocityFilePaths_quake3 = [
    'Earthquake_03_(Northwest Calif-01)_RSN5\RSN5_NWCALIF.AB_A-FRN045_V.txt', 
    'Earthquake_03_(Northwest Calif-01)_RSN5\RSN5_NWCALIF.AB_A-FRN135_V.txt', 
    'Earthquake_03_(Northwest Calif-01)_RSN5\RSN5_NWCALIF.AB_A-FRNDWN_V.txt'
]

displacementFilePaths_quake3 = [
    'Earthquake_03_(Northwest Calif-01)_RSN5\RSN5_NWCALIF.AB_A-FRN045_D.txt', 
    'Earthquake_03_(Northwest Calif-01)_RSN5\RSN5_NWCALIF.AB_A-FRN135_D.txt', 
    'Earthquake_03_(Northwest Calif-01)_RSN5\RSN5_NWCALIF.AB_A-FRNDWN_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake3[i], velocityFilePaths_quake3[i], displacementFilePaths_quake3[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 3'
name = 'Northwest Calif-01'
record_sequence_number = 5
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake3_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake3_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 4 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake4
accelerationFilePaths_quake4 = [
    r'C:\Users\Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Time Series Records for 100 Earthquakes (California US)\/Earthquake_04_(Imperial Valley-02)_RSN6\RSN6_IMPVALL.I_I-ELC180_A.txt', 
    r'C:\Users\Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Time Series Records for 100 Earthquakes (California US)\/Earthquake_04_(Imperial Valley-02)_RSN6\RSN6_IMPVALL.I_I-ELC270_A.txt',
    r'C:\Users\Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Time Series Records for 100 Earthquakes (California US)\/Earthquake_04_(Imperial Valley-02)_RSN6\RSN6_IMPVALL.I_I-ELC-UP_A.txt'
]

velocityFilePaths_quake4 = [
    r'C:\Users\Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Time Series Records for 100 Earthquakes (California US)\/Earthquake_04_(Imperial Valley-02)_RSN6\RSN6_IMPVALL.I_I-ELC180_V.txt', 
    r'C:\Users\Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Time Series Records for 100 Earthquakes (California US)\/Earthquake_04_(Imperial Valley-02)_RSN6\RSN6_IMPVALL.I_I-ELC270_V.txt', 
    r'C:\Users\Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Time Series Records for 100 Earthquakes (California US)\/Earthquake_04_(Imperial Valley-02)_RSN6\RSN6_IMPVALL.I_I-ELC-UP_V.txt'
]

displacementFilePaths_quake4 = [
    r'C:\Users\Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Time Series Records for 100 Earthquakes (California US)\/Earthquake_04_(Imperial Valley-02)_RSN6\RSN6_IMPVALL.I_I-ELC180_D.txt', 
    r'C:\Users\Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Time Series Records for 100 Earthquakes (California US)\/Earthquake_04_(Imperial Valley-02)_RSN6\RSN6_IMPVALL.I_I-ELC270_D.txt', 
    r'C:\Users\Acer\/OneDrive - UTS\/Desktop\/University of Portsmouth\/MSc Dissertation\/Ground Motion Database\/Time Series Records for 100 Earthquakes (California US)\/Earthquake_04_(Imperial Valley-02)_RSN6\RSN6_IMPVALL.I_I-ELC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake4[i], velocityFilePaths_quake4[i], displacementFilePaths_quake4[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 4'
name = 'Imperial Valley-02'
record_sequence_number = 6
earthquake_station = 'El Centro Array #9'

# Function to print the results in the desired format
def print_earthquake4_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake4_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 5 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake5
accelerationFilePaths_quake5 = [
    'Earthquake_05_(Northwest Calif-02)_RSN7\RSN7_NWCALIF.C_C-FRN045_A.txt', 
    'Earthquake_05_(Northwest Calif-02)_RSN7\RSN7_NWCALIF.C_C-FRN135_A.txt', 
    'Earthquake_05_(Northwest Calif-02)_RSN7\RSN7_NWCALIF.C_C-FRN-UP_A.txt'
]

velocityFilePaths_quake5 = [
    'Earthquake_05_(Northwest Calif-02)_RSN7\RSN7_NWCALIF.C_C-FRN045_V.txt', 
    'Earthquake_05_(Northwest Calif-02)_RSN7\RSN7_NWCALIF.C_C-FRN135_V.txt', 
    'Earthquake_05_(Northwest Calif-02)_RSN7\RSN7_NWCALIF.C_C-FRN-UP_V.txt'
]

displacementFilePaths_quake5 = [
    'Earthquake_05_(Northwest Calif-02)_RSN7\RSN7_NWCALIF.C_C-FRN045_D.txt', 
    'Earthquake_05_(Northwest Calif-02)_RSN7\RSN7_NWCALIF.C_C-FRN135_D.txt', 
    'Earthquake_05_(Northwest Calif-02)_RSN7\RSN7_NWCALIF.C_C-FRN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake5[i], velocityFilePaths_quake5[i], displacementFilePaths_quake5[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 5'
name = 'Northwest Calif-02'
record_sequence_number = 7
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake5_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake5_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 6 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake6
accelerationFilePaths_quake6 = [
    'Earthquake_06_(Northern Calif-01)_RSN8\RSN8_NCALIF.FH_F-FRN225_A.txt', 
    'Earthquake_06_(Northern Calif-01)_RSN8\RSN8_NCALIF.FH_F-FRN315_A.txt', 
    'Earthquake_06_(Northern Calif-01)_RSN8\RSN8_NCALIF.FH_F-FRN-UP_A.txt'
]

velocityFilePaths_quake6 = [
    'Earthquake_06_(Northern Calif-01)_RSN8\RSN8_NCALIF.FH_F-FRN225_V.txt', 
    'Earthquake_06_(Northern Calif-01)_RSN8\RSN8_NCALIF.FH_F-FRN315_V.txt', 
    'Earthquake_06_(Northern Calif-01)_RSN8\RSN8_NCALIF.FH_F-FRN-UP_V.txt'
]

displacementFilePaths_quake6 = [
    'Earthquake_06_(Northern Calif-01)_RSN8\RSN8_NCALIF.FH_F-FRN225_D.txt', 
    'Earthquake_06_(Northern Calif-01)_RSN8\RSN8_NCALIF.FH_F-FRN315_D.txt', 
    'Earthquake_06_(Northern Calif-01)_RSN8\RSN8_NCALIF.FH_F-FRN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake6[i], velocityFilePaths_quake6[i], displacementFilePaths_quake6[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 6'
name = 'Northern Calif-01'
record_sequence_number = 8
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake6_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake6_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 7 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake7
accelerationFilePaths_quake7 = [
    'Earthquake_07_(Borrego)_RSN9\RSN9_BORREGO_B-ELC000_A.txt', 
    'Earthquake_07_(Borrego)_RSN9\RSN9_BORREGO_B-ELC090_A.txt', 
    'Earthquake_07_(Borrego)_RSN9\RSN9_BORREGO_B-ELC-UP_A.txt'
]

velocityFilePaths_quake7 = [
    'Earthquake_07_(Borrego)_RSN9\RSN9_BORREGO_B-ELC000_V.txt', 
    'Earthquake_07_(Borrego)_RSN9\RSN9_BORREGO_B-ELC090_V.txt', 
    'Earthquake_07_(Borrego)_RSN9\RSN9_BORREGO_B-ELC-UP_V.txt'
]

displacementFilePaths_quake7 = [
    'Earthquake_07_(Borrego)_RSN9\RSN9_BORREGO_B-ELC000_D.txt', 
    'Earthquake_07_(Borrego)_RSN9\RSN9_BORREGO_B-ELC090_D.txt', 
    'Earthquake_07_(Borrego)_RSN9\RSN9_BORREGO_B-ELC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake7[i], velocityFilePaths_quake7[i], displacementFilePaths_quake7[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 7'
name = 'Borrego'
record_sequence_number = 9
earthquake_station = 'El Centro Array #9'

# Function to print the results in the desired format
def print_earthquake7_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake7_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 8 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake8
accelerationFilePaths_quake8 = [
    'Earthquake_08_(Imperial Valley-03)_RSN10\RSN10_IMPVALL.BG_C-ELC000_A.txt', 
    'Earthquake_08_(Imperial Valley-03)_RSN10\RSN10_IMPVALL.BG_C-ELC090_A.txt', 
    'Earthquake_08_(Imperial Valley-03)_RSN10\RSN10_IMPVALL.BG_C-ELC-UP_A.txt'
]

velocityFilePaths_quake8 = [
    'Earthquake_08_(Imperial Valley-03)_RSN10\RSN10_IMPVALL.BG_C-ELC000_V.txt', 
    'Earthquake_08_(Imperial Valley-03)_RSN10\RSN10_IMPVALL.BG_C-ELC090_V.txt', 
    'Earthquake_08_(Imperial Valley-03)_RSN10\RSN10_IMPVALL.BG_C-ELC-UP_V.txt'
]

displacementFilePaths_quake8 = [
    'Earthquake_08_(Imperial Valley-03)_RSN10\RSN10_IMPVALL.BG_C-ELC000_D.txt', 
    'Earthquake_08_(Imperial Valley-03)_RSN10\RSN10_IMPVALL.BG_C-ELC090_D.txt', 
    'Earthquake_08_(Imperial Valley-03)_RSN10\RSN10_IMPVALL.BG_C-ELC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake8[i], velocityFilePaths_quake8[i], displacementFilePaths_quake8[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 8'
name = 'Imperial Valley-03'
record_sequence_number = 10
earthquake_station = 'El Centro Array #9'

# Function to print the results in the desired format
def print_earthquake8_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake8_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 9 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake9
accelerationFilePaths_quake9 = [
    'Earthquake_09_(Northwest Calif-03)_RSN11\RSN11_NWCALIF.AB_B-FRN224_A.txt', 
    'Earthquake_09_(Northwest Calif-03)_RSN11\RSN11_NWCALIF.AB_B-FRN314_A.txt', 
    'Earthquake_09_(Northwest Calif-03)_RSN11\RSN11_NWCALIF.AB_B-FRN-UP_A.txt'
]

velocityFilePaths_quake9 = [
    'Earthquake_09_(Northwest Calif-03)_RSN11\RSN11_NWCALIF.AB_B-FRN224_V.txt', 
    'Earthquake_09_(Northwest Calif-03)_RSN11\RSN11_NWCALIF.AB_B-FRN314_V.txt', 
    'Earthquake_09_(Northwest Calif-03)_RSN11\RSN11_NWCALIF.AB_B-FRN-UP_V.txt'
]

displacementFilePaths_quake9 = [
    'Earthquake_09_(Northwest Calif-03)_RSN11\RSN11_NWCALIF.AB_B-FRN224_D.txt', 
    'Earthquake_09_(Northwest Calif-03)_RSN11\RSN11_NWCALIF.AB_B-FRN314_D.txt', 
    'Earthquake_09_(Northwest Calif-03)_RSN11\RSN11_NWCALIF.AB_B-FRN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake9[i], velocityFilePaths_quake9[i], displacementFilePaths_quake9[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 9'
name = 'Northwest Calif-03'
record_sequence_number = 11	
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake9_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake9_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 10 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake10
accelerationFilePaths_quake10 = [
    'Earthquake_10_(Kern County)_RSN12\RSN12_KERN.PEL_PEL090_A.txt', 
    'Earthquake_10_(Kern County)_RSN12\RSN12_KERN.PEL_PEL180_A.txt', 
    'Earthquake_10_(Kern County)_RSN12\RSN12_KERN.PEL_PEL-UP_A.txt'
]

velocityFilePaths_quake10 = [
    'Earthquake_10_(Kern County)_RSN12\RSN12_KERN.PEL_PEL090_V.txt', 
    'Earthquake_10_(Kern County)_RSN12\RSN12_KERN.PEL_PEL180_V.txt', 
    'Earthquake_10_(Kern County)_RSN12\RSN12_KERN.PEL_PEL-UP_V.txt'
]

displacementFilePaths_quake10 = [
    'Earthquake_10_(Kern County)_RSN12\RSN12_KERN.PEL_PEL090_D.txt', 
    'Earthquake_10_(Kern County)_RSN12\RSN12_KERN.PEL_PEL180_D.txt', 
    'Earthquake_10_(Kern County)_RSN12\RSN12_KERN.PEL_PEL-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake10[i], velocityFilePaths_quake10[i], displacementFilePaths_quake10[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 10'
name = 'Kern County'
record_sequence_number = 12
earthquake_station = 'LA - Hollywood Stor FF'

# Function to print the results in the desired format
def print_earthquake10_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake10_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 1 to Earthquake 10 --------------------------------

# ------------------------------------- Beginning of Earthquake11 to Earthqauke20 --------------------------------
# ------------------------------------- Earthquake 11 --------------------------------------------------
accelerationFilePaths_quake11 = [
    'Earthquake_11_(Northern Calif-02)_RSN16\RSN16_NCALIF.AG_A-FRN044_A.txt', 
    'Earthquake_11_(Northern Calif-02)_RSN16\RSN16_NCALIF.AG_A-FRN134_A.txt', 
    'Earthquake_11_(Northern Calif-02)_RSN16\RSN16_NCALIF.AG_A-FRN-UP_A.txt'
]

velocityFilePaths_quake11 = [
    'Earthquake_11_(Northern Calif-02)_RSN16\RSN16_NCALIF.AG_A-FRN044_V.txt', 
    'Earthquake_11_(Northern Calif-02)_RSN16\RSN16_NCALIF.AG_A-FRN134_V.txt', 
    'Earthquake_11_(Northern Calif-02)_RSN16\RSN16_NCALIF.AG_A-FRN-UP_V.txt'
]

displacementFilePaths_quake11 = [
    'Earthquake_11_(Northern Calif-02)_RSN16\RSN16_NCALIF.AG_A-FRN044_D.txt', 
    'Earthquake_11_(Northern Calif-02)_RSN16\RSN16_NCALIF.AG_A-FRN134_D.txt', 
    'Earthquake_11_(Northern Calif-02)_RSN16\RSN16_NCALIF.AG_A-FRN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake11[i], velocityFilePaths_quake11[i], displacementFilePaths_quake11[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 11'
name = 'Northern Calif-02'
record_sequence_number = 16
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake11_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake11_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 12 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake12
accelerationFilePaths_quake12 = [
    'Earthquake_12_(Southern Calif)_RSN17\RSN17_SCALIF_SLO234_A.txt', 
    'Earthquake_12_(Southern Calif)_RSN17\RSN17_SCALIF_SLO324_A.txt', 
    'Earthquake_12_(Southern Calif)_RSN17\RSN17_SCALIF_SLO-UP_A.txt'
]

velocityFilePaths_quake12 = [
    'Earthquake_12_(Southern Calif)_RSN17\RSN17_SCALIF_SLO234_V.txt', 
    'Earthquake_12_(Southern Calif)_RSN17\RSN17_SCALIF_SLO324_V.txt', 
    'Earthquake_12_(Southern Calif)_RSN17\RSN17_SCALIF_SLO-UP_V.txt'
]

displacementFilePaths_quake12 = [
    'Earthquake_12_(Southern Calif)_RSN17\RSN17_SCALIF_SLO234_D.txt', 
    'Earthquake_12_(Southern Calif)_RSN17\RSN17_SCALIF_SLO324_D.txt', 
    'Earthquake_12_(Southern Calif)_RSN17\RSN17_SCALIF_SLO-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake12[i], velocityFilePaths_quake12[i], displacementFilePaths_quake12[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 12'
name = 'Southern Calif'
record_sequence_number = 17
earthquake_station = 'San Luis Obispo'

# Function to print the results in the desired format
def print_earthquake12_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake12_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 13 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake13
accelerationFilePaths_quake13 = [
    'Earthquake_13_(Imperial Valley-04)_RSN18\RSN18_IMPVALL.BG_G-ELC000_A.txt', 
    'Earthquake_13_(Imperial Valley-04)_RSN18\RSN18_IMPVALL.BG_G-ELC090_A.txt', 
    'Earthquake_13_(Imperial Valley-04)_RSN18\RSN18_IMPVALL.BG_G-ELC-UP_A.txt'
]

velocityFilePaths_quake13 = [
    'Earthquake_13_(Imperial Valley-04)_RSN18\RSN18_IMPVALL.BG_G-ELC000_V.txt', 
    'Earthquake_13_(Imperial Valley-04)_RSN18\RSN18_IMPVALL.BG_G-ELC090_V.txt', 
    'Earthquake_13_(Imperial Valley-04)_RSN18\RSN18_IMPVALL.BG_G-ELC-UP_V.txt'
]

displacementFilePaths_quake13 = [
    'Earthquake_13_(Imperial Valley-04)_RSN18\RSN18_IMPVALL.BG_G-ELC000_D.txt', 
    'Earthquake_13_(Imperial Valley-04)_RSN18\RSN18_IMPVALL.BG_G-ELC090_D.txt', 
    'Earthquake_13_(Imperial Valley-04)_RSN18\RSN18_IMPVALL.BG_G-ELC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake13[i], velocityFilePaths_quake13[i], displacementFilePaths_quake13[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 13'
name = 'Imperial Valley-04'
record_sequence_number = 18
earthquake_station = '	El Centro Array #9'

# Function to print the results in the desired format
def print_earthquake13_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake13_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 14 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake14
accelerationFilePaths_quake14 = [
    'Earthquake_14_(Central Calif-01)_RSN19\RSN19_CTRCALIF_A-HCH181_A.txt', 
    'Earthquake_14_(Central Calif-01)_RSN19\RSN19_CTRCALIF_A-HCH271_A.txt', 
    'Earthquake_14_(Central Calif-01)_RSN19\RSN19_CTRCALIF_A-HCH-UP_A.txt'
]

velocityFilePaths_quake14 = [
    'Earthquake_14_(Central Calif-01)_RSN19\RSN19_CTRCALIF_A-HCH181_V.txt', 
    'Earthquake_14_(Central Calif-01)_RSN19\RSN19_CTRCALIF_A-HCH271_V.txt', 
    'Earthquake_14_(Central Calif-01)_RSN19\RSN19_CTRCALIF_A-HCH-UP_V.txt'
]

displacementFilePaths_quake14 = [
    'Earthquake_14_(Central Calif-01)_RSN19\RSN19_CTRCALIF_A-HCH181_D.txt', 
    'Earthquake_14_(Central Calif-01)_RSN19\RSN19_CTRCALIF_A-HCH271_D.txt', 
    'Earthquake_14_(Central Calif-01)_RSN19\RSN19_CTRCALIF_A-HCH-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake14[i], velocityFilePaths_quake14[i], displacementFilePaths_quake14[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 14'
name = 'Central Calif-01'
record_sequence_number = 19
earthquake_station = 'Hollister City Hall'

# Function to print the results in the desired format
def print_earthquake14_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake14_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 15 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake15
accelerationFilePaths_quake15 = [
    'Earthquake_15_(Northern Calif-03)_RSN20\RSN20_NCALIF.FH_H-FRN044_A.txt', 
    'Earthquake_15_(Northern Calif-03)_RSN20\RSN20_NCALIF.FH_H-FRN314_A.txt', 
    'Earthquake_15_(Northern Calif-03)_RSN20\RSN20_NCALIF.FH_H-FRN-UP_A.txt'
]

velocityFilePaths_quake15 = [
    'Earthquake_15_(Northern Calif-03)_RSN20\RSN20_NCALIF.FH_H-FRN044_V.txt', 
    'Earthquake_15_(Northern Calif-03)_RSN20\RSN20_NCALIF.FH_H-FRN314_V.txt', 
    'Earthquake_15_(Northern Calif-03)_RSN20\RSN20_NCALIF.FH_H-FRN-UP_V.txt'
]

displacementFilePaths_quake15 = [
    'Earthquake_15_(Northern Calif-03)_RSN20\RSN20_NCALIF.FH_H-FRN044_D.txt', 
    'Earthquake_15_(Northern Calif-03)_RSN20\RSN20_NCALIF.FH_H-FRN314_D.txt', 
    'Earthquake_15_(Northern Calif-03)_RSN20\RSN20_NCALIF.FH_H-FRN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake15[i], velocityFilePaths_quake15[i], displacementFilePaths_quake15[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 15'
name = 'Northern Calif-03'
record_sequence_number = 20
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake15_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake15_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 16 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake16
accelerationFilePaths_quake16 = [
    'Earthquake_16_(Imperial Valley-05)_RSN21\RSN21_IMPVALL.BG_E-ELC000_A.txt', 
    'Earthquake_16_(Imperial Valley-05)_RSN21\RSN21_IMPVALL.BG_E-ELC090_A.txt', 
    'Earthquake_16_(Imperial Valley-05)_RSN21\RSN21_IMPVALL.BG_E-ELC-UP_A.txt'
]

velocityFilePaths_quake16 = [
    'Earthquake_16_(Imperial Valley-05)_RSN21\RSN21_IMPVALL.BG_E-ELC000_V.txt', 
    'Earthquake_16_(Imperial Valley-05)_RSN21\RSN21_IMPVALL.BG_E-ELC090_V.txt', 
    'Earthquake_16_(Imperial Valley-05)_RSN21\RSN21_IMPVALL.BG_E-ELC-UP_V.txt'
]

displacementFilePaths_quake16 = [
    'Earthquake_16_(Imperial Valley-05)_RSN21\RSN21_IMPVALL.BG_E-ELC000_D.txt', 
    'Earthquake_16_(Imperial Valley-05)_RSN21\RSN21_IMPVALL.BG_E-ELC090_D.txt', 
    'Earthquake_16_(Imperial Valley-05)_RSN21\RSN21_IMPVALL.BG_E-ELC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake16[i], velocityFilePaths_quake16[i], displacementFilePaths_quake16[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 16'
name = 'Imperial Valley-05'
record_sequence_number = 21
earthquake_station = 'El Centro Array #9'

# Function to print the results in the desired format
def print_earthquake16_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake16_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 17 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake17
accelerationFilePaths_quake17 = [
    'Earthquake_17_(San Francisco)_RSN23\RSN23_SANFRAN_GGP010_A.txt', 
    'Earthquake_17_(San Francisco)_RSN23\RSN23_SANFRAN_GGP100_A.txt', 
    'Earthquake_17_(San Francisco)_RSN23\RSN23_SANFRAN_GGP-UP_A.txt'
]

velocityFilePaths_quake17 = [
    'Earthquake_17_(San Francisco)_RSN23\RSN23_SANFRAN_GGP010_V.txt', 
    'Earthquake_17_(San Francisco)_RSN23\RSN23_SANFRAN_GGP100_V.txt', 
    'Earthquake_17_(San Francisco)_RSN23\RSN23_SANFRAN_GGP-UP_V.txt'
]

displacementFilePaths_quake17 = [
    'Earthquake_17_(San Francisco)_RSN23\RSN23_SANFRAN_GGP010_D.txt', 
    'Earthquake_17_(San Francisco)_RSN23\RSN23_SANFRAN_GGP100_D.txt', 
    'Earthquake_17_(San Francisco)_RSN23\RSN23_SANFRAN_GGP-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake17[i], velocityFilePaths_quake17[i], displacementFilePaths_quake17[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 17'
name = 'San Francisco'
record_sequence_number = 23
earthquake_station = 'Golden Gate Park'

# Function to print the results in the desired format
def print_earthquake17_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake17_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 18 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake18
accelerationFilePaths_quake18 = [
    'Earthquake_18_(Central Calif-02)_RSN24\RSN24_CTRCALIF_B-HCH181_A.txt', 
    'Earthquake_18_(Central Calif-02)_RSN24\RSN24_CTRCALIF_B-HCH271_A.txt', 
    'Earthquake_18_(Central Calif-02)_RSN24\RSN24_CTRCALIF_B-HCH-UP_A.txt'
]

velocityFilePaths_quake18 = [
    'Earthquake_18_(Central Calif-02)_RSN24\RSN24_CTRCALIF_B-HCH181_V.txt', 
    'Earthquake_18_(Central Calif-02)_RSN24\RSN24_CTRCALIF_B-HCH271_V.txt', 
    'Earthquake_18_(Central Calif-02)_RSN24\RSN24_CTRCALIF_B-HCH-UP_V.txt'
]

displacementFilePaths_quake18 = [
    'Earthquake_18_(Central Calif-02)_RSN24\RSN24_CTRCALIF_B-HCH181_D.txt', 
    'Earthquake_18_(Central Calif-02)_RSN24\RSN24_CTRCALIF_B-HCH271_D.txt', 
    'Earthquake_18_(Central Calif-02)_RSN24\RSN24_CTRCALIF_B-HCH-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake18[i], velocityFilePaths_quake18[i], displacementFilePaths_quake18[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 18'
name = 'Central Calif-02'
record_sequence_number = 24
earthquake_station = 'Hollister City Hall'

# Function to print the results in the desired format
def print_earthquake18_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake18_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 19 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake19
def make_motion_earthquake19(filepath_a, filepath_v, filepath_d, t_step):
    t, t_series_a = make_t_series(filepath_a, t_step)
    _, t_series_v = make_t_series(filepath_v, t_step)
    _, t_series_d = make_t_series(filepath_d, t_step)
    
    # Debug: Print lengths for diagnosis
    print(f"Lengths - Acceleration: {len(t_series_a)}, Velocity: {len(t_series_v)}, Displacement: {len(t_series_d)}")
    
    # Ensure all series have the same length (choose your method here, e.g., truncating to shortest series)
    min_length = min(len(t_series_a), len(t_series_v), len(t_series_d))
    t = t[:min_length]
    t_series_a = t_series_a[:min_length]
    t_series_v = t_series_v[:min_length]
    t_series_d = t_series_d[:min_length]

    data = np.column_stack((t, t_series_a, t_series_v, t_series_d))
    return data


def process_component_earthquake19(filepath_a, filepath_v, filepath_d, dt):
    data = make_motion_earthquake19(filepath_a, filepath_v, filepath_d, dt)
    return {
        'PGA': np.max(np.abs(data[:, 1])),
        'PGV': np.max(np.abs(data[:, 2])),
        'PGD': np.max(np.abs(data[:, 3]))
    }


# Earthquake19
accelerationFilePaths_quake19 = [
    'Earthquake_19_(Northern Calif-04)_RSN25\RSN25_NCALIF.AG_B-FRN224_A.txt', 
    'Earthquake_19_(Northern Calif-04)_RSN25\RSN25_NCALIF.AG_B-FRN314_A.txt', 
    'Earthquake_19_(Northern Calif-04)_RSN25\RSN25_NCALIF.AG_B-FRN-UP_A.txt'
]

velocityFilePaths_quake19 = [
    'Earthquake_19_(Northern Calif-04)_RSN25\RSN25_NCALIF.AG_B-FRN224_V.txt', 
    'Earthquake_19_(Northern Calif-04)_RSN25\RSN25_NCALIF.AG_B-FRN314_V.txt', 
    'Earthquake_19_(Northern Calif-04)_RSN25\RSN25_NCALIF.AG_B-FRN-UP_V.txt'
]

displacementFilePaths_quake19 = [
    'Earthquake_19_(Northern Calif-04)_RSN25\RSN25_NCALIF.AG_B-FRN224_D.txt', 
    'Earthquake_19_(Northern Calif-04)_RSN25\RSN25_NCALIF.AG_B-FRN314_D.txt', 
    'Earthquake_19_(Northern Calif-04)_RSN25\RSN25_NCALIF.AG_B-FRN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component_earthquake19(accelerationFilePaths_quake19[i], velocityFilePaths_quake19[i], displacementFilePaths_quake19[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 19'
name = 'Northwest Calif-01'
record_sequence_number = 5
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake19_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake19_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 20 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake20
accelerationFilePaths_quake20= [
    'Earthquake_20_(Hollister-01)_RSN26\RSN26_HOLLISTR_B-HCH181_A.txt', 
    'Earthquake_20_(Hollister-01)_RSN26\RSN26_HOLLISTR_B-HCH271_A.txt', 
    'Earthquake_20_(Hollister-01)_RSN26\RSN26_HOLLISTR_B-HCH-UP_A.txt'
]

velocityFilePaths_quake20 = [
    'Earthquake_20_(Hollister-01)_RSN26\RSN26_HOLLISTR_B-HCH181_V.txt', 
    'Earthquake_20_(Hollister-01)_RSN26\RSN26_HOLLISTR_B-HCH271_V.txt', 
    'Earthquake_20_(Hollister-01)_RSN26\RSN26_HOLLISTR_B-HCH-UP_V.txt'
]

displacementFilePaths_quake20 = [
    'Earthquake_20_(Hollister-01)_RSN26\RSN26_HOLLISTR_B-HCH181_D.txt', 
    'Earthquake_20_(Hollister-01)_RSN26\RSN26_HOLLISTR_B-HCH271_D.txt', 
    'Earthquake_20_(Hollister-01)_RSN26\RSN26_HOLLISTR_B-HCH-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake20[i], velocityFilePaths_quake20[i], displacementFilePaths_quake20[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 20'
name = 'Hollister-01'
record_sequence_number = 26
earthquake_station = 'Hollister City Hall'

# Function to print the results in the desired format
def print_earthquake20_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake20_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 11 to Earthquake 20 --------------------------------

# ------------------------------------- Beginning of Earthquake21 to Earthqauke30 --------------------------------
# ------------------------------------- Earthquake 21 --------------------------------------------------
accelerationFilePaths_quake21 = [
    'Earthquake_21_(Hollister-02)_RSN27\RSN27_HOLLISTR_C-HCH181_A.txt', 
    'Earthquake_21_(Hollister-02)_RSN27\RSN27_HOLLISTR_C-HCH271_A.txt', 
    'Earthquake_21_(Hollister-02)_RSN27\RSN27_HOLLISTR_C-HCH-UP_A.txt'
]

velocityFilePaths_quake21 = [
    'Earthquake_21_(Hollister-02)_RSN27\RSN27_HOLLISTR_C-HCH181_V.txt', 
    'Earthquake_21_(Hollister-02)_RSN27\RSN27_HOLLISTR_C-HCH271_V.txt', 
    'Earthquake_21_(Hollister-02)_RSN27\RSN27_HOLLISTR_C-HCH-UP_V.txt'
]

displacementFilePaths_quake21 = [
    'Earthquake_21_(Hollister-02)_RSN27\RSN27_HOLLISTR_C-HCH181_D.txt', 
    'Earthquake_21_(Hollister-02)_RSN27\RSN27_HOLLISTR_C-HCH271_D.txt', 
    'Earthquake_21_(Hollister-02)_RSN27\RSN27_HOLLISTR_C-HCH-UP_D.txt   '
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake1[i], velocityFilePaths_quake1[i], displacementFilePaths_quake1[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 21'
name = 'Hollister-02'
record_sequence_number = 27
earthquake_station = 'Hollister City Hall'

# Function to print the results in the desired format
def print_earthquake21_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake21_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 22 --------------------------------------------------
def make_motion_earthquake22(filepath_a, filepath_v, filepath_d, t_step):
    # Extract time series data from the files
    t, t_series_a = make_t_series(filepath_a, t_step)
    _, t_series_v = make_t_series(filepath_v, t_step)
    _, t_series_d = make_t_series(filepath_d, t_step)
    
    # Find the shortest length among the arrays
    min_length = min(len(t_series_a), len(t_series_v), len(t_series_d))
    
    # Truncate the arrays to the shortest length
    t_series_a = t_series_a[:min_length]
    t_series_v = t_series_v[:min_length]
    t_series_d = t_series_d[:min_length]
    t = t[:min_length]  # Also truncate the time array to match the data arrays
    
    # Concatenate the truncated arrays
    data = np.column_stack((t, t_series_a, t_series_v, t_series_d))
    return data


def process_component_earthquake22(filepath_a, filepath_v, filepath_d, dt):
    data = make_motion_earthquake22(filepath_a, filepath_v, filepath_d, dt)
    return {
        'PGA': np.max(np.abs(data[:, 1])),
        'PGV': np.max(np.abs(data[:, 2])),
        'PGD': np.max(np.abs(data[:, 3]))
    }
    

accelerationFilePaths_quake22 = [
    'Earthquake_22_(Parkfield)_RSN28\RSN28_PARKF_C12050_A.txt', 
    'Earthquake_22_(Parkfield)_RSN28\RSN28_PARKF_C12320_A.txt', 
    'Earthquake_22_(Parkfield)_RSN28\RSN28_PARKF_C12DWN_A.txt'
]

velocityFilePaths_quake22 = [
    'Earthquake_22_(Parkfield)_RSN28\RSN28_PARKF_C12DWN_V.txt', 
    'Earthquake_22_(Parkfield)_RSN28\RSN28_PARKF_C12050_V.txt', 
    'Earthquake_22_(Parkfield)_RSN28\RSN28_PARKF_C12320_V.txt'
]

displacementFilePaths_quake22 = [
    'Earthquake_22_(Parkfield)_RSN28\RSN28_PARKF_C12DWN_D.txt', 
    'Earthquake_22_(Parkfield)_RSN28\RSN28_PARKF_C12050_D.txt', 
    'Earthquake_22_(Parkfield)_RSN28\RSN28_PARKF_C12320_D.txt'
]
dt = 0.005




# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component_earthquake22(accelerationFilePaths_quake22[i], velocityFilePaths_quake22[i], displacementFilePaths_quake22[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 22'
name = 'Parkfield'
record_sequence_number = 28	
earthquake_station = 'Cholame - Shandon Array #12'

# Function to print the results in the desired format
def print_earthquake22_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake22_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 23 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake3
accelerationFilePaths_quake23 = [
    'Earthquake_23_(Northern Calif-05)_RSN34\RSN34_NCALIF.AG_C-FRN224_A.txt', 
    'Earthquake_23_(Northern Calif-05)_RSN34\RSN34_NCALIF.AG_C-FRN314_A.txt', 
    'Earthquake_23_(Northern Calif-05)_RSN34\RSN34_NCALIF.AG_C-FRN-UP_A.txt'
]

velocityFilePaths_quake23 = [
    'Earthquake_23_(Northern Calif-05)_RSN34\RSN34_NCALIF.AG_C-FRN224_V.txt', 
    'Earthquake_23_(Northern Calif-05)_RSN34\RSN34_NCALIF.AG_C-FRN314_V.txt', 
    'Earthquake_23_(Northern Calif-05)_RSN34\RSN34_NCALIF.AG_C-FRN-UP_V.txt'
]

displacementFilePaths_quake23 = [
    'Earthquake_23_(Northern Calif-05)_RSN34\RSN34_NCALIF.AG_C-FRN224_D.txt', 
    'Earthquake_23_(Northern Calif-05)_RSN34\RSN34_NCALIF.AG_C-FRN314_D.txt', 
    'Earthquake_23_(Northern Calif-05)_RSN34\RSN34_NCALIF.AG_C-FRN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake23[i], velocityFilePaths_quake23[i], displacementFilePaths_quake23[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 23'
name = 'Northern Calif-05'
record_sequence_number = 34
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake23_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake23_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 24 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake24
accelerationFilePaths_quake24 = [
    'Earthquake_24_(Northern Calif-06)_RSN35\RSN35_NCALIF.AG_E-HCH181_A.txt', 
    'Earthquake_24_(Northern Calif-06)_RSN35\RSN35_NCALIF.AG_E-HCH271_A.txt', 
    'Earthquake_24_(Northern Calif-06)_RSN35\RSN35_NCALIF.AG_E-HCH-UP_A.txt'
]

velocityFilePaths_quake24 = [
    'Earthquake_24_(Northern Calif-06)_RSN35\RSN35_NCALIF.AG_E-HCH181_V.txt', 
    'Earthquake_24_(Northern Calif-06)_RSN35\RSN35_NCALIF.AG_E-HCH271_V.txt', 
    'Earthquake_24_(Northern Calif-06)_RSN35\RSN35_NCALIF.AG_E-HCH-UP_V.txt'
]

displacementFilePaths_quake24 = [
    'Earthquake_24_(Northern Calif-06)_RSN35\RSN35_NCALIF.AG_E-HCH181_D.txt', 
    'Earthquake_24_(Northern Calif-06)_RSN35\RSN35_NCALIF.AG_E-HCH271_D.txt', 
    'Earthquake_24_(Northern Calif-06)_RSN35\RSN35_NCALIF.AG_E-HCH-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake24[i], velocityFilePaths_quake24[i], displacementFilePaths_quake24[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 24'
name = 'Northern Calif-06'
record_sequence_number = 35
earthquake_station = 'Hollister City Hall'

# Function to print the results in the desired format
def print_earthquake24_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake24_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 25 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake25
accelerationFilePaths_quake25 = [
    'Earthquake_25_(Borrego Mtn)_RSN36\RSN36_BORREGO_A-ELC180_A.txt', 
    'Earthquake_25_(Borrego Mtn)_RSN36\RSN36_BORREGO_A-ELC270_A.txt', 
    'Earthquake_25_(Borrego Mtn)_RSN36\RSN36_BORREGO_A-ELC-UP_A.txt'
]

velocityFilePaths_quake25 = [
    'Earthquake_25_(Borrego Mtn)_RSN36\RSN36_BORREGO_A-ELC180_V.txt', 
    'Earthquake_25_(Borrego Mtn)_RSN36\RSN36_BORREGO_A-ELC270_V.txt', 
    'Earthquake_25_(Borrego Mtn)_RSN36\RSN36_BORREGO_A-ELC-UP_V.txt'
]

displacementFilePaths_quake25 = [
    'Earthquake_25_(Borrego Mtn)_RSN36\RSN36_BORREGO_A-ELC180_D.txt', 
    'Earthquake_25_(Borrego Mtn)_RSN36\RSN36_BORREGO_A-ELC270_D.txt', 
    'Earthquake_25_(Borrego Mtn)_RSN36\RSN36_BORREGO_A-ELC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake25[i], velocityFilePaths_quake25[i], displacementFilePaths_quake25[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 25'
name = 'Borrego Mtn'
record_sequence_number = 36
earthquake_station = 'El Centro Array #9'

# Function to print the results in the desired format
def print_earthquake25_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake25_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 26 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake26
accelerationFilePaths_quake26 = [
    'Earthquake_26_(Lytle Creek)_RSN41\RSN41_LYTLECR_ORR021_A.txt', 
    'Earthquake_26_(Lytle Creek)_RSN41\RSN41_LYTLECR_ORR291_A.txt', 
    'Earthquake_26_(Lytle Creek)_RSN41\RSN41_LYTLECR_ORRDWN_A.txt'
]

velocityFilePaths_quake26 = [
    'Earthquake_26_(Lytle Creek)_RSN41\RSN41_LYTLECR_ORR021_V.txt', 
    'Earthquake_26_(Lytle Creek)_RSN41\RSN41_LYTLECR_ORR291_V.txt', 
    'Earthquake_26_(Lytle Creek)_RSN41\RSN41_LYTLECR_ORRDWN_V.txt'
]

displacementFilePaths_quake26 = [
    'Earthquake_26_(Lytle Creek)_RSN41\RSN41_LYTLECR_ORR021_D.txt', 
    'Earthquake_26_(Lytle Creek)_RSN41\RSN41_LYTLECR_ORR291_D.txt', 
    'Earthquake_26_(Lytle Creek)_RSN41\RSN41_LYTLECR_ORRDWN_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake26[i], velocityFilePaths_quake26[i], displacementFilePaths_quake26[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 26'
name = 'Lytle Creek'
record_sequence_number = 41
earthquake_station = 'Castaic - Old Ridge Route'

# Function to print the results in the desired format
def print_earthquake26_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake26_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 27 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake27
accelerationFilePaths_quake27 = [
    'Earthquake_27_(San Fernando)_RSN51\RSN51_SFERN_PVE065_A.txt', 
    'Earthquake_27_(San Fernando)_RSN51\RSN51_SFERN_PVE155_A.txt', 
    'Earthquake_27_(San Fernando)_RSN51\RSN51_SFERN_PVEDWN_A.txt'
]

velocityFilePaths_quake27 = [
    'Earthquake_27_(San Fernando)_RSN51\RSN51_SFERN_PVE065_V.txt', 
    'Earthquake_27_(San Fernando)_RSN51\RSN51_SFERN_PVE155_V.txt', 
    'Earthquake_27_(San Fernando)_RSN51\RSN51_SFERN_PVEDWN_V.txt'
]

displacementFilePaths_quake27 = [
    'Earthquake_27_(San Fernando)_RSN51\RSN51_SFERN_PVE065_D.txt', 
    'Earthquake_27_(San Fernando)_RSN51\RSN51_SFERN_PVE155_D.txt', 
    'Earthquake_27_(San Fernando)_RSN51\RSN51_SFERN_PVEDWN_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake27[i], velocityFilePaths_quake27[i], displacementFilePaths_quake27[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 27'
name = 'San Fernando'
record_sequence_number = 51
earthquake_station = '2516 Via Tejon PV	'

# Function to print the results in the desired format
def print_earthquake27_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake27_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 28 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake28
accelerationFilePaths_quake28 = [
    'Earthquake_28_(Point Mugu)_RSN97\RSN97_PTMUGU_PHN180_A.txt', 
    'Earthquake_28_(Point Mugu)_RSN97\RSN97_PTMUGU_PHN270_A.txt', 
    'Earthquake_28_(Point Mugu)_RSN97\RSN97_PTMUGU_PHN-UP_A.txt'
]

velocityFilePaths_quake28 = [
    'Earthquake_28_(Point Mugu)_RSN97\RSN97_PTMUGU_PHN180_V.txt', 
    'Earthquake_28_(Point Mugu)_RSN97\RSN97_PTMUGU_PHN270_V.txt', 
    'Earthquake_28_(Point Mugu)_RSN97\RSN97_PTMUGU_PHN-UP_V.txt'
]

displacementFilePaths_quake28 = [
    'Earthquake_28_(Point Mugu)_RSN97\RSN97_PTMUGU_PHN180_D.txt', 
    'Earthquake_28_(Point Mugu)_RSN97\RSN97_PTMUGU_PHN270_D.txt', 
    'Earthquake_28_(Point Mugu)_RSN97\RSN97_PTMUGU_PHN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake28[i], velocityFilePaths_quake28[i], displacementFilePaths_quake28[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 28'
name = 'Point Mugu'
record_sequence_number = 97	
earthquake_station = 'Port Hueneme'

# Function to print the results in the desired format
def print_earthquake28_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake28_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 29 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake29
accelerationFilePaths_quake29 = [
    'Earthquake_29_(Hollister-03)_RSN98\RSN98_HOLLISTR_A-G01157_A.txt', 
    'Earthquake_29_(Hollister-03)_RSN98\RSN98_HOLLISTR_A-G01247_A.txt' 
]

velocityFilePaths_quake29 = [
    'Earthquake_29_(Hollister-03)_RSN98\RSN98_HOLLISTR_A-G01157_V.txt', 
    'Earthquake_29_(Hollister-03)_RSN98\RSN98_HOLLISTR_A-G01247_V.txt' 
]

displacementFilePaths_quake29 = [
    'Earthquake_29_(Hollister-03)_RSN98\RSN98_HOLLISTR_A-G01157_D.txt', 
    'Earthquake_29_(Hollister-03)_RSN98\RSN98_HOLLISTR_A-G01247_D.txt' 
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Use the length of one of the file path lists assuming all have the same number of elements
for i in range(len(accelerationFilePaths_quake29)):
    component_results = process_component(accelerationFilePaths_quake29[i], velocityFilePaths_quake29[i], displacementFilePaths_quake29[i], dt)
    # Append a descriptive component name if needed, or adjust as necessary
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 29'
name = 'Hollister-03'
record_sequence_number = 98
earthquake_station = 'Gilroy Array #1'

# Function to print the results in the desired format
def print_earthquake29_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake29_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 30 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake30
accelerationFilePaths_quake30 = [
    'Earthquake_30_(Northern Calif-07)_RSN101\RSN101_NCALIF.AG_D-CPM030_A.txt', 
    'Earthquake_30_(Northern Calif-07)_RSN101\RSN101_NCALIF.AG_D-CPM120_A.txt', 
    'Earthquake_30_(Northern Calif-07)_RSN101\RSN101_NCALIF.AG_D-CPMDWN_A.txt'
]

velocityFilePaths_quake30 = [
    'Earthquake_30_(Northern Calif-07)_RSN101\RSN101_NCALIF.AG_D-CPM030_V.txt', 
    'Earthquake_30_(Northern Calif-07)_RSN101\RSN101_NCALIF.AG_D-CPM120_V.txt', 
    'Earthquake_30_(Northern Calif-07)_RSN101\RSN101_NCALIF.AG_D-CPMDWN_V.txt'
]

displacementFilePaths_quake30 = [
    'Earthquake_30_(Northern Calif-07)_RSN101\RSN101_NCALIF.AG_D-CPM030_D.txt',    
    'Earthquake_30_(Northern Calif-07)_RSN101\RSN101_NCALIF.AG_D-CPM120_D.txt', 
    'Earthquake_30_(Northern Calif-07)_RSN101\RSN101_NCALIF.AG_D-CPMDWN_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake30[i], velocityFilePaths_quake30[i], displacementFilePaths_quake30[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 30'
name = 'Northern Calif-07'
record_sequence_number = 101	
earthquake_station = 'Cape Mendocino'

# Function to print the results in the desired format
def print_earthquake30_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake30_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 21 to Earthquake 30 --------------------------------

# ------------------------------------- Beginning of Earthquake31 to Earthqauke40 --------------------------------
# ------------------------------------- Earthquake 31 --------------------------------------------------
accelerationFilePaths_quake31 = [
    'Earthquake_31_(Oroville-01)_RSN106\RSN106_OROVILLE_A-ORV037_A.txt', 
    'Earthquake_31_(Oroville-01)_RSN106\RSN106_OROVILLE_A-ORV307_A.txt'
]

velocityFilePaths_quake31 = [
    'Earthquake_31_(Oroville-01)_RSN106\RSN106_OROVILLE_A-ORV037_V.txt', 
    'Earthquake_31_(Oroville-01)_RSN106\RSN106_OROVILLE_A-ORV307_V.txt'
]

displacementFilePaths_quake31 = [
    'Earthquake_31_(Oroville-01)_RSN106\RSN106_OROVILLE_A-ORV037_D.txt', 
    'Earthquake_31_(Oroville-01)_RSN106\RSN106_OROVILLE_A-ORV307_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake31)):
    component_results = process_component(accelerationFilePaths_quake31[i], velocityFilePaths_quake31[i], displacementFilePaths_quake31[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))

    
# Given metadata for the earthquake
title = 'Earthquake 31'
name = 'Oroville-01'
record_sequence_number = 106
earthquake_station = 'Oroville Seismograph Station'

# Function to print the results in the desired format
def print_earthquake31_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake31_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 32 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake32
accelerationFilePaths_quake32 = [
    'Earthquake_32_(Oroville-02)_RSN107\RSN107_OROVILLE_B-OAP180_A.txt', 
    'Earthquake_32_(Oroville-02)_RSN107\RSN107_OROVILLE_B-OAP270_A.txt', 
    'Earthquake_32_(Oroville-02)_RSN107\RSN107_OROVILLE_B-OAPDWN_A.txt'
]

velocityFilePaths_quake32 = [
    'Earthquake_32_(Oroville-02)_RSN107\RSN107_OROVILLE_B-OAP180_V.txt', 
    'Earthquake_32_(Oroville-02)_RSN107\RSN107_OROVILLE_B-OAP270_V.txt', 
    'Earthquake_32_(Oroville-02)_RSN107\RSN107_OROVILLE_B-OAPDWN_V.txt'
]

displacementFilePaths_quake32 = [
    'Earthquake_32_(Oroville-02)_RSN107\RSN107_OROVILLE_B-OAP180_D.txt', 
    'Earthquake_32_(Oroville-02)_RSN107\RSN107_OROVILLE_B-OAP270_D.txt', 
    'Earthquake_32_(Oroville-02)_RSN107\RSN107_OROVILLE_B-OAPDWN_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake32[i], velocityFilePaths_quake32[i], displacementFilePaths_quake32[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 32'
name = 'Oroville-02'
record_sequence_number = 107
earthquake_station = 'Oroville Airport'

# Function to print the results in the desired format
def print_earthquake32_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake32_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 33 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake33
accelerationFilePaths_quake33 = [
    'Earthquake_33_(Oroville-04)_RSN109\RSN109_OROVILLE_C-OMC246_A.txt', 
    'Earthquake_33_(Oroville-04)_RSN109\RSN109_OROVILLE_C-OMC336_A.txt', 
    'Earthquake_33_(Oroville-04)_RSN109\RSN109_OROVILLE_C-OMCDWN_A.txt'
]

velocityFilePaths_quake33 = [
    'Earthquake_33_(Oroville-04)_RSN109\RSN109_OROVILLE_C-OMC246_V.txt', 
    'Earthquake_33_(Oroville-04)_RSN109\RSN109_OROVILLE_C-OMC336_V.txt', 
    'Earthquake_33_(Oroville-04)_RSN109\RSN109_OROVILLE_C-OMCDWN_V.txt'
]

displacementFilePaths_quake33 = [
    'Earthquake_33_(Oroville-04)_RSN109\RSN109_OROVILLE_C-OMC246_D.txt', 
    'Earthquake_33_(Oroville-04)_RSN109\RSN109_OROVILLE_C-OMC336_D.txt', 
    'Earthquake_33_(Oroville-04)_RSN109\RSN109_OROVILLE_C-OMCDWN_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake33[i], velocityFilePaths_quake33[i], displacementFilePaths_quake33[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 33'
name = 'Oroville-04'
record_sequence_number = 109
earthquake_station = 'Medical Center'

# Function to print the results in the desired format
def print_earthquake33_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake33_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 34 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake34
accelerationFilePaths_quake34 = [
    'Earthquake_34_(Oroville-03)_RSN112\RSN112_OROVILLE_D-EBH000_A.txt', 
    'Earthquake_34_(Oroville-03)_RSN112\RSN112_OROVILLE_D-EBH090_A.txt', 
    'Earthquake_34_(Oroville-03)_RSN112\RSN112_OROVILLE_D-EBHDWN_A.txt'
]

velocityFilePaths_quake34 = [
    'Earthquake_34_(Oroville-03)_RSN112\RSN112_OROVILLE_D-EBH000_V.txt', 
    'Earthquake_34_(Oroville-03)_RSN112\RSN112_OROVILLE_D-EBH090_V.txt', 
    'Earthquake_34_(Oroville-03)_RSN112\RSN112_OROVILLE_D-EBHDWN_V.txt'
]

displacementFilePaths_quake34 = [
    'Earthquake_34_(Oroville-03)_RSN112\RSN112_OROVILLE_D-EBH000_D.txt', 
    'Earthquake_34_(Oroville-03)_RSN112\RSN112_OROVILLE_D-EBH090_D.txt', 
    'Earthquake_34_(Oroville-03)_RSN112\RSN112_OROVILLE_D-EBHDWN_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake34[i], velocityFilePaths_quake34[i], displacementFilePaths_quake34[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 34'
name = 'Oroville-03'
record_sequence_number = 112
earthquake_station = 'Broadbeck Residence'

# Function to print the results in the desired format
def print_earthquake34_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake34_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 35 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake35
accelerationFilePaths_quake35 = [
    'Earthquake_35_(Santa Barbara)_RSN135\RSN135_SBARB_CAD250_A.txt', 
    'Earthquake_35_(Santa Barbara)_RSN135\RSN135_SBARB_CAD340_A.txt', 
    'Earthquake_35_(Santa Barbara)_RSN135\RSN135_SBARB_CAD-UP_A.txt'
]

velocityFilePaths_quake35 = [
    'Earthquake_35_(Santa Barbara)_RSN135\RSN135_SBARB_CAD250_V.txt', 
    'Earthquake_35_(Santa Barbara)_RSN135\RSN135_SBARB_CAD340_V.txt', 
    'Earthquake_35_(Santa Barbara)_RSN135\RSN135_SBARB_CAD-UP_V.txt'
]

displacementFilePaths_quake35 = [
    'Earthquake_35_(Santa Barbara)_RSN135\RSN135_SBARB_CAD250_D.txt', 
    'Earthquake_35_(Santa Barbara)_RSN135\RSN135_SBARB_CAD340_D.txt', 
    'Earthquake_35_(Santa Barbara)_RSN135\RSN135_SBARB_CAD-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake35[i], velocityFilePaths_quake35[i], displacementFilePaths_quake35[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 35'
name = 'Santa Barbara'
record_sequence_number = 135
earthquake_station = 'Cachuma Dam Toe'

# Function to print the results in the desired format
def print_earthquake35_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake35_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 36 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake36
accelerationFilePaths_quake36 = [
    'Earthquake_36_(Coyote Lake)_RSN145\RSN145_COYOTELK_CYC160_A.txt', 
    'Earthquake_36_(Coyote Lake)_RSN145\RSN145_COYOTELK_CYC250_A.txt', 
    'Earthquake_36_(Coyote Lake)_RSN145\RSN145_COYOTELK_CYC-UP_A.txt'
]

velocityFilePaths_quake36 = [
    'Earthquake_36_(Coyote Lake)_RSN145\RSN145_COYOTELK_CYC160_V.txt', 
    'Earthquake_36_(Coyote Lake)_RSN145\RSN145_COYOTELK_CYC250_V.txt', 
    'Earthquake_36_(Coyote Lake)_RSN145\RSN145_COYOTELK_CYC-UP_V.txt'
]

displacementFilePaths_quake36 = [
    'Earthquake_36_(Coyote Lake)_RSN145\RSN145_COYOTELK_CYC160_D.txt', 
    'Earthquake_36_(Coyote Lake)_RSN145\RSN145_COYOTELK_CYC250_D.txt', 
    'Earthquake_36_(Coyote Lake)_RSN145\RSN145_COYOTELK_CYC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake36[i], velocityFilePaths_quake36[i], displacementFilePaths_quake36[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 36'
name = 'Coyote Lake'    
record_sequence_number = 145
earthquake_station = 'Coyote Lake Dam - Southwest Abutment'

# Function to print the results in the desired format
def print_earthquake36_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake36_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 37 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake37
accelerationFilePaths_quake37 = [
    'Earthquake_37_(Imperial Valley-06)_RSN158\RSN158_IMPVALL.H_H-AEP045_A.txt', 
    'Earthquake_37_(Imperial Valley-06)_RSN158\RSN158_IMPVALL.H_H-AEP315_A.txt', 
    'Earthquake_37_(Imperial Valley-06)_RSN158\RSN158_IMPVALL.H_H-AEP-UP_A.txt'
]

velocityFilePaths_quake37 = [
    'Earthquake_37_(Imperial Valley-06)_RSN158\RSN158_IMPVALL.H_H-AEP045_V.txt', 
    'Earthquake_37_(Imperial Valley-06)_RSN158\RSN158_IMPVALL.H_H-AEP315_V.txt', 
    'Earthquake_37_(Imperial Valley-06)_RSN158\RSN158_IMPVALL.H_H-AEP-UP_V.txt'
]

displacementFilePaths_quake37 = [
    'Earthquake_37_(Imperial Valley-06)_RSN158\RSN158_IMPVALL.H_H-AEP045_D.txt', 
    'Earthquake_37_(Imperial Valley-06)_RSN158\RSN158_IMPVALL.H_H-AEP315_D.txt', 
    'Earthquake_37_(Imperial Valley-06)_RSN158\RSN158_IMPVALL.H_H-AEP-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake37[i], velocityFilePaths_quake37[i], displacementFilePaths_quake37[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 37'
name = 'Imperial Valley-06'
record_sequence_number = 158
earthquake_station = 'Aeropuerto Mexicali'

# Function to print the results in the desired format
def print_earthquake37_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake37_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 38 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake38
accelerationFilePaths_quake38 = [
    'Earthquake_38_(Imperial Valley-07)_RSN193\RSN193_IMPVALL.A_A-BCR140_A.txt', 
    'Earthquake_38_(Imperial Valley-07)_RSN193\RSN193_IMPVALL.A_A-BCR230_A.txt', 
    'Earthquake_38_(Imperial Valley-07)_RSN193\RSN193_IMPVALL.A_A-BCR-UP_A.txt'
]

velocityFilePaths_quake38 = [
    'Earthquake_38_(Imperial Valley-07)_RSN193\RSN193_IMPVALL.A_A-BCR140_V.txt', 
    'Earthquake_38_(Imperial Valley-07)_RSN193\RSN193_IMPVALL.A_A-BCR230_V.txt', 
    'Earthquake_38_(Imperial Valley-07)_RSN193\RSN193_IMPVALL.A_A-BCR-UP_V.txt'
]

displacementFilePaths_quake38 = [
    'Earthquake_38_(Imperial Valley-07)_RSN193\RSN193_IMPVALL.A_A-BCR140_D.txt', 
    'Earthquake_38_(Imperial Valley-07)_RSN193\RSN193_IMPVALL.A_A-BCR230_D.txt', 
    'Earthquake_38_(Imperial Valley-07)_RSN193\RSN193_IMPVALL.A_A-BCR-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake38[i], velocityFilePaths_quake38[i], displacementFilePaths_quake38[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 38'
name = 'Imperial Valley-07'
record_sequence_number = 193
earthquake_station = 'Bonds Corner'

# Function to print the results in the desired format
def print_earthquake38_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake38_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 39 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake39
accelerationFilePaths_quake39 = [
    'Earthquake_39_(Imperial Valley-08)_RSN209\RSN209_IMPVALL.BG_F-WSM090_A.txt', 
    'Earthquake_39_(Imperial Valley-08)_RSN209\RSN209_IMPVALL.BG_F-WSM180_A.txt', 
    'Earthquake_39_(Imperial Valley-08)_RSN209\RSN209_IMPVALL.BG_F-WSM-UP_A.txt'
]

velocityFilePaths_quake39 = [
    'Earthquake_39_(Imperial Valley-08)_RSN209\RSN209_IMPVALL.BG_F-WSM090_V.txt', 
    'Earthquake_39_(Imperial Valley-08)_RSN209\RSN209_IMPVALL.BG_F-WSM180_V.txt', 
    'Earthquake_39_(Imperial Valley-08)_RSN209\RSN209_IMPVALL.BG_F-WSM-UP_V.txt'
]

displacementFilePaths_quake39 = [
    'Earthquake_39_(Imperial Valley-08)_RSN209\RSN209_IMPVALL.BG_F-WSM090_D.txt', 
    'Earthquake_39_(Imperial Valley-08)_RSN209\RSN209_IMPVALL.BG_F-WSM180_D.txt', 
    'Earthquake_39_(Imperial Valley-08)_RSN209\RSN209_IMPVALL.BG_F-WSM-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake39[i], velocityFilePaths_quake39[i], displacementFilePaths_quake39[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 39'
name = 'Imperial Valley-08'
record_sequence_number = 209
earthquake_station = 'Westmorland Fire Sta'

# Function to print the results in the desired format
def print_earthquake39_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake39_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 40 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake40
accelerationFilePaths_quake40 = [
    'Earthquake_40_(Livermore-01)_RSN210\RSN210_LIVERMOR_A-A3E146_A.txt', 
    'Earthquake_40_(Livermore-01)_RSN210\RSN210_LIVERMOR_A-A3E236_A.txt', 
    'Earthquake_40_(Livermore-01)_RSN210\RSN210_LIVERMOR_A-A3E-UP_A.txt'
]

velocityFilePaths_quake40 = [
    'Earthquake_40_(Livermore-01)_RSN210\RSN210_LIVERMOR_A-A3E146_V.txt', 
    'Earthquake_40_(Livermore-01)_RSN210\RSN210_LIVERMOR_A-A3E236_V.txt', 
    'Earthquake_40_(Livermore-01)_RSN210\RSN210_LIVERMOR_A-A3E-UP_V.txt'
]

displacementFilePaths_quake40 = [
    'Earthquake_40_(Livermore-01)_RSN210\RSN210_LIVERMOR_A-A3E146_D.txt', 
    'Earthquake_40_(Livermore-01)_RSN210\RSN210_LIVERMOR_A-A3E236_D.txt', 
    'Earthquake_40_(Livermore-01)_RSN210\RSN210_LIVERMOR_A-A3E-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake40[i], velocityFilePaths_quake40[i], displacementFilePaths_quake40[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 40'
name = 'Livermore-01'
record_sequence_number = 210
earthquake_station = 'APEEL 3E Hayward CSUH'

# Function to print the results in the desired format
def print_earthquake40_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake40_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 31 to Earthquake 40 --------------------------------

# ------------------------------------- Beginning of Earthquake41 to Earthqauke50 --------------------------------
# ------------------------------------- Earthquake 41 --------------------------------------------------
accelerationFilePaths_quake41 = [
    'Earthquake_41_(Livermore-02)_RSN217\RSN217_LIVERMOR_B-A3E146_A.txt', 
    'Earthquake_41_(Livermore-02)_RSN217\RSN217_LIVERMOR_B-A3E236_A.txt', 
    'Earthquake_41_(Livermore-02)_RSN217\RSN217_LIVERMOR_B-A3E-UP_A.txt'
]

velocityFilePaths_quake41 = [
    'Earthquake_41_(Livermore-02)_RSN217\RSN217_LIVERMOR_B-A3E146_V.txt', 
    'Earthquake_41_(Livermore-02)_RSN217\RSN217_LIVERMOR_B-A3E236_V.txt', 
    'Earthquake_41_(Livermore-02)_RSN217\RSN217_LIVERMOR_B-A3E-UP_V.txt'
]

displacementFilePaths_quake41 = [
    'Earthquake_41_(Livermore-02)_RSN217\RSN217_LIVERMOR_B-A3E146_D.txt', 
    'Earthquake_41_(Livermore-02)_RSN217\RSN217_LIVERMOR_B-A3E236_D.txt', 
    'Earthquake_41_(Livermore-02)_RSN217\RSN217_LIVERMOR_B-A3E-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake41[i], velocityFilePaths_quake41[i], displacementFilePaths_quake41[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 41'
name = 'Livermore-02'
record_sequence_number = 217
earthquake_station = 'APEEL 3E Hayward CSUH'

# Function to print the results in the desired format
def print_earthquake41_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake41_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 42 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake42
accelerationFilePaths_quake42 = [
    'Earthquake_42_(Anza (Horse Canyon)-01)_RSN225\RSN225_ANZA_PFT045_A.txt', 
    'Earthquake_42_(Anza (Horse Canyon)-01)_RSN225\RSN225_ANZA_PFT135_A.txt', 
    'Earthquake_42_(Anza (Horse Canyon)-01)_RSN225\RSN225_ANZA_PFT-UP_A.txt'
]

velocityFilePaths_quake42 = [
    'Earthquake_42_(Anza (Horse Canyon)-01)_RSN225\RSN225_ANZA_PFT045_V.txt', 
    'Earthquake_42_(Anza (Horse Canyon)-01)_RSN225\RSN225_ANZA_PFT135_V.txt', 
    'Earthquake_42_(Anza (Horse Canyon)-01)_RSN225\RSN225_ANZA_PFT-UP_V.txt'
]

displacementFilePaths_quake42 = [
    'Earthquake_42_(Anza (Horse Canyon)-01)_RSN225\RSN225_ANZA_PFT045_D.txt', 
    'Earthquake_42_(Anza (Horse Canyon)-01)_RSN225\RSN225_ANZA_PFT135_D.txt', 
    'Earthquake_42_(Anza (Horse Canyon)-01)_RSN225\RSN225_ANZA_PFT-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake42[i], velocityFilePaths_quake42[i], displacementFilePaths_quake42[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 42'
name = 'Anza (Horse Canyon)-01'
record_sequence_number = 225
earthquake_station = 'Anza - Pinyon Flat'

# Function to print the results in the desired format
def print_earthquake42_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake42_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 43 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake43
accelerationFilePaths_quake43 = [
    'Earthquake_43_(Mammoth Lakes-01)_RSN230\RSN230_MAMMOTH.I_I-CVK090_A.txt', 
    'Earthquake_43_(Mammoth Lakes-01)_RSN230\RSN230_MAMMOTH.I_I-CVK180_A.txt', 
    'Earthquake_43_(Mammoth Lakes-01)_RSN230\RSN230_MAMMOTH.I_I-CVK-UP_A.txt'
]

velocityFilePaths_quake43 = [
    'Earthquake_43_(Mammoth Lakes-01)_RSN230\RSN230_MAMMOTH.I_I-CVK090_V.txt', 
    'Earthquake_43_(Mammoth Lakes-01)_RSN230\RSN230_MAMMOTH.I_I-CVK180_V.txt', 
    'Earthquake_43_(Mammoth Lakes-01)_RSN230\RSN230_MAMMOTH.I_I-CVK-UP_V.txt'
]

displacementFilePaths_quake43 = [
    'Earthquake_43_(Mammoth Lakes-01)_RSN230\RSN230_MAMMOTH.I_I-CVK090_D.txt', 
    'Earthquake_43_(Mammoth Lakes-01)_RSN230\RSN230_MAMMOTH.I_I-CVK180_D.txt', 
    'Earthquake_43_(Mammoth Lakes-01)_RSN230\RSN230_MAMMOTH.I_I-CVK-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake43[i], velocityFilePaths_quake43[i], displacementFilePaths_quake43[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 43'
name = 'Mammoth Lakes-01'
record_sequence_number = 230
earthquake_station = 'Convict Creek'

# Function to print the results in the desired format
def print_earthquake43_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake43_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 44 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake44
accelerationFilePaths_quake44 = [
    'Earthquake_44_(Mammoth Lakes-02)_RSN233\RSN233_MAMMOTH.J_J-CVK090_A.txt', 
    'Earthquake_44_(Mammoth Lakes-02)_RSN233\RSN233_MAMMOTH.J_J-CVK180_A.txt', 
    'Earthquake_44_(Mammoth Lakes-02)_RSN233\RSN233_MAMMOTH.J_J-CVK-UP_A.txt'
]

velocityFilePaths_quake44 = [
    'Earthquake_44_(Mammoth Lakes-02)_RSN233\RSN233_MAMMOTH.J_J-CVK090_V.txt', 
    'Earthquake_44_(Mammoth Lakes-02)_RSN233\RSN233_MAMMOTH.J_J-CVK180_V.txt', 
    'Earthquake_44_(Mammoth Lakes-02)_RSN233\RSN233_MAMMOTH.J_J-CVK-UP_V.txt'
]

displacementFilePaths_quake44 = [
    'Earthquake_44_(Mammoth Lakes-02)_RSN233\RSN233_MAMMOTH.J_J-CVK090_D.txt', 
    'Earthquake_44_(Mammoth Lakes-02)_RSN233\RSN233_MAMMOTH.J_J-CVK180_D.txt', 
    'Earthquake_44_(Mammoth Lakes-02)_RSN233\RSN233_MAMMOTH.J_J-CVK-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake44[i], velocityFilePaths_quake44[i], displacementFilePaths_quake44[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 44'
name = 'Mammoth Lakes-02'
record_sequence_number = 233
earthquake_station = 'Convict Creek'

# Function to print the results in the desired format
def print_earthquake44_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake44_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 45 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake45
accelerationFilePaths_quake45 = [
    'Earthquake_45_(Mammoth Lakes-03)_RSN236\RSN236_MAMMOTH.AH_A-CVK090_A.txt', 
    'Earthquake_45_(Mammoth Lakes-03)_RSN236\RSN236_MAMMOTH.AH_A-CVK180_A.txt', 
    'Earthquake_45_(Mammoth Lakes-03)_RSN236\RSN236_MAMMOTH.AH_A-CVK-UP_A.txt'
]

velocityFilePaths_quake45 = [
    'Earthquake_45_(Mammoth Lakes-03)_RSN236\RSN236_MAMMOTH.AH_A-CVK090_V.txt', 
    'Earthquake_45_(Mammoth Lakes-03)_RSN236\RSN236_MAMMOTH.AH_A-CVK180_V.txt', 
    'Earthquake_45_(Mammoth Lakes-03)_RSN236\RSN236_MAMMOTH.AH_A-CVK-UP_V.txt'
]

displacementFilePaths_quake45 = [
    'Earthquake_45_(Mammoth Lakes-03)_RSN236\RSN236_MAMMOTH.AH_A-CVK090_D.txt', 
    'Earthquake_45_(Mammoth Lakes-03)_RSN236\RSN236_MAMMOTH.AH_A-CVK180_D.txt', 
    'Earthquake_45_(Mammoth Lakes-03)_RSN236\RSN236_MAMMOTH.AH_A-CVK-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake45[i], velocityFilePaths_quake45[i], displacementFilePaths_quake45[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 45'
name = 'Mammoth Lakes-03'
record_sequence_number = 236
earthquake_station = 'Convict Creek'

# Function to print the results in the desired format
def print_earthquake45_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake45_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 46 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake46
accelerationFilePaths_quake46 = [
    'Earthquake_46_(Mammoth Lakes-04)_RSN240\RSN240_MAMMOTH.AH_B-CVK090_A.txt', 
    'Earthquake_46_(Mammoth Lakes-04)_RSN240\RSN240_MAMMOTH.AH_B-CVK180_A.txt', 
    'Earthquake_46_(Mammoth Lakes-04)_RSN240\RSN240_MAMMOTH.AH_B-CVK-UP_A.txt'
]

velocityFilePaths_quake46 = [
    'Earthquake_46_(Mammoth Lakes-04)_RSN240\RSN240_MAMMOTH.AH_B-CVK090_V.txt', 
    'Earthquake_46_(Mammoth Lakes-04)_RSN240\RSN240_MAMMOTH.AH_B-CVK180_V.txt', 
    'Earthquake_46_(Mammoth Lakes-04)_RSN240\RSN240_MAMMOTH.AH_B-CVK-UP_V.txt'
]

displacementFilePaths_quake46 = [
    'Earthquake_46_(Mammoth Lakes-04)_RSN240\RSN240_MAMMOTH.AH_B-CVK090_D.txt', 
    'Earthquake_46_(Mammoth Lakes-04)_RSN240\RSN240_MAMMOTH.AH_B-CVK180_D.txt', 
    'Earthquake_46_(Mammoth Lakes-04)_RSN240\RSN240_MAMMOTH.AH_B-CVK-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake46[i], velocityFilePaths_quake46[i], displacementFilePaths_quake46[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 46'
name = 'Mammoth Lakes-04'
record_sequence_number = 240
earthquake_station = 'Convict Creek'

# Function to print the results in the desired format
def print_earthquake46_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake46_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 47 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake47
accelerationFilePaths_quake47 = [
    'Earthquake_47_(Mammoth Lakes-05)_RSN244\RSN244_MAMMOTH.K_K-CVK090_A.txt', 
    'Earthquake_47_(Mammoth Lakes-05)_RSN244\RSN244_MAMMOTH.K_K-CVK180_A.txt', 
    'Earthquake_47_(Mammoth Lakes-05)_RSN244\RSN244_MAMMOTH.K_K-CVK-UP_A.txt'
]

velocityFilePaths_quake47 = [
    'Earthquake_47_(Mammoth Lakes-05)_RSN244\RSN244_MAMMOTH.K_K-CVK090_V.txt', 
    'Earthquake_47_(Mammoth Lakes-05)_RSN244\RSN244_MAMMOTH.K_K-CVK180_V.txt', 
    'Earthquake_47_(Mammoth Lakes-05)_RSN244\RSN244_MAMMOTH.K_K-CVK-UP_V.txt'
]

displacementFilePaths_quake47 = [
    'Earthquake_47_(Mammoth Lakes-05)_RSN244\RSN244_MAMMOTH.K_K-CVK090_D.txt', 
    'Earthquake_47_(Mammoth Lakes-05)_RSN244\RSN244_MAMMOTH.K_K-CVK180_D.txt', 
    'Earthquake_47_(Mammoth Lakes-05)_RSN244\RSN244_MAMMOTH.K_K-CVK-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake47[i], velocityFilePaths_quake47[i], displacementFilePaths_quake47[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 47'
name = 'Mammoth Lakes-05'
record_sequence_number = 244
earthquake_station = 'Convict Creek	'

# Function to print the results in the desired format
def print_earthquake47_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake47_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 48 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake48
accelerationFilePaths_quake48 = [
    'Earthquake_48_(Mammoth Lakes-06)_RSN246\RSN246_MAMMOTH.L_L-BEN270_A.txt', 
    'Earthquake_48_(Mammoth Lakes-06)_RSN246\RSN246_MAMMOTH.L_L-BEN360_A.txt', 
    'Earthquake_48_(Mammoth Lakes-06)_RSN246\RSN246_MAMMOTH.L_L-BEN-UP_A.txt'
]

velocityFilePaths_quake48 = [
    'Earthquake_48_(Mammoth Lakes-06)_RSN246\RSN246_MAMMOTH.L_L-BEN270_V.txt', 
    'Earthquake_48_(Mammoth Lakes-06)_RSN246\RSN246_MAMMOTH.L_L-BEN360_V.txt', 
    'Earthquake_48_(Mammoth Lakes-06)_RSN246\RSN246_MAMMOTH.L_L-BEN-UP_V.txt'
]

displacementFilePaths_quake48 = [
    'Earthquake_48_(Mammoth Lakes-06)_RSN246\RSN246_MAMMOTH.L_L-BEN270_D.txt', 
    'Earthquake_48_(Mammoth Lakes-06)_RSN246\RSN246_MAMMOTH.L_L-BEN360_D.txt', 
    'Earthquake_48_(Mammoth Lakes-06)_RSN246\RSN246_MAMMOTH.L_L-BEN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake48[i], velocityFilePaths_quake48[i], displacementFilePaths_quake48[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 48'
name = 'Mammoth Lakes-06'
record_sequence_number = 246
earthquake_station = 'Benton'

# Function to print the results in the desired format
def print_earthquake48_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake48_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 49 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake49
accelerationFilePaths_quake49 = [
    'Earthquake_49_(Mammoth Lakes-07)_RSN251\RSN251_MAMMOTH.AH_C-FIS000_A.txt', 
    'Earthquake_49_(Mammoth Lakes-07)_RSN251\RSN251_MAMMOTH.AH_C-FIS090_A.txt', 
    'Earthquake_49_(Mammoth Lakes-07)_RSN251\RSN251_MAMMOTH.AH_C-FIS-UP_A.txt'
]

velocityFilePaths_quake49 = [
    'Earthquake_49_(Mammoth Lakes-07)_RSN251\RSN251_MAMMOTH.AH_C-FIS000_V.txt', 
    'Earthquake_49_(Mammoth Lakes-07)_RSN251\RSN251_MAMMOTH.AH_C-FIS090_V.txt', 
    'Earthquake_49_(Mammoth Lakes-07)_RSN251\RSN251_MAMMOTH.AH_C-FIS-UP_V.txt'
]

displacementFilePaths_quake49 = [
    'Earthquake_49_(Mammoth Lakes-07)_RSN251\RSN251_MAMMOTH.AH_C-FIS000_D.txt', 
    'Earthquake_49_(Mammoth Lakes-07)_RSN251\RSN251_MAMMOTH.AH_C-FIS090_D.txt', 
    'Earthquake_49_(Mammoth Lakes-07)_RSN251\RSN251_MAMMOTH.AH_C-FIS-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake49[i], velocityFilePaths_quake49[i], displacementFilePaths_quake49[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 49'
name = 'Northwest Calif-01'
record_sequence_number = 5
earthquake_station = 'Ferndale City Hall'

# Function to print the results in the desired format
def print_earthquake49_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake49_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 50 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake50
accelerationFilePaths_quake50 = [
    'Earthquake_50_(Mammoth Lakes-08)_RSN257\RSN257_MAMMOTH.AH_D-CBR000_A.txt', 
    'Earthquake_50_(Mammoth Lakes-08)_RSN257\RSN257_MAMMOTH.AH_D-CBR090_A.txt', 
    'Earthquake_50_(Mammoth Lakes-08)_RSN257\RSN257_MAMMOTH.AH_D-CBR-UP_A.txt'
]

velocityFilePaths_quake50 = [
    'Earthquake_50_(Mammoth Lakes-08)_RSN257\RSN257_MAMMOTH.AH_D-CBR000_V.txt', 
    'Earthquake_50_(Mammoth Lakes-08)_RSN257\RSN257_MAMMOTH.AH_D-CBR090_V.txt', 
    'Earthquake_50_(Mammoth Lakes-08)_RSN257\RSN257_MAMMOTH.AH_D-CBR-UP_V.txt'
]

displacementFilePaths_quake50 = [
    'Earthquake_50_(Mammoth Lakes-08)_RSN257\RSN257_MAMMOTH.AH_D-CBR000_D.txt', 
    'Earthquake_50_(Mammoth Lakes-08)_RSN257\RSN257_MAMMOTH.AH_D-CBR090_D.txt', 
    'Earthquake_50_(Mammoth Lakes-08)_RSN257\RSN257_MAMMOTH.AH_D-CBR-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

for i in range(len(components)):
    component_results = process_component(accelerationFilePaths_quake50[i], velocityFilePaths_quake50[i], displacementFilePaths_quake50[i], dt)
    results.append((components[i], component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 50'
name = 'Mammoth Lakes-08'
record_sequence_number = 257
earthquake_station = 'Cashbaugh (CBR)'

# Function to print the results in the desired format
def print_earthquake50_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake50_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 41 to Earthquake 50 --------------------------------

# ------------------------------------- Beginning of Earthquake51 to Earthqauke100 --------------------------------
# ------------------------------------- Earthquake 51 --------------------------------------------------
accelerationFilePaths_quake51 = [
    'Earthquake_51_(Mammoth Lakes-09)_RSN270\RSN270_MAMMOTH.AH_H-CON180_A.txt',
    'Earthquake_51_(Mammoth Lakes-09)_RSN270\RSN270_MAMMOTH.AH_H-CON270_A.txt',
    'Earthquake_51_(Mammoth Lakes-09)_RSN270\RSN270_MAMMOTH.AH_H-CONDWN_A.txt',
]

velocityFilePaths_quake51 = [
    'Earthquake_51_(Mammoth Lakes-09)_RSN270\RSN270_MAMMOTH.AH_H-CON180_V.txt',
    'Earthquake_51_(Mammoth Lakes-09)_RSN270\RSN270_MAMMOTH.AH_H-CON270_V.txt',
    'Earthquake_51_(Mammoth Lakes-09)_RSN270\RSN270_MAMMOTH.AH_H-CONDWN_V.txt',
]

displacementFilePaths_quake51 = [
    'Earthquake_51_(Mammoth Lakes-09)_RSN270\RSN270_MAMMOTH.AH_H-CON180_D.txt',
    'Earthquake_51_(Mammoth Lakes-09)_RSN270\RSN270_MAMMOTH.AH_H-CON270_D.txt',
    'Earthquake_51_(Mammoth Lakes-09)_RSN270\RSN270_MAMMOTH.AH_H-CONDWN_D.txt',
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake51)):
    component_results = process_component(accelerationFilePaths_quake51[i], velocityFilePaths_quake51[i], displacementFilePaths_quake51[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 51'
name = 'Mammoth Lakes-09'
record_sequence_number = 270
earthquake_station = 'Convict Lakes (CON)'

# Function to print the results in the desired format
def print_earthquake51_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake51_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 52 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake52
accelerationFilePaths_quake52 = [
    'Earthquake_52_(Westmorland)_RSN314\RSN314_WESMORL_BRA225_A.txt', 
    'Earthquake_52_(Westmorland)_RSN314\RSN314_WESMORL_BRA315_A.txt', 
    'Earthquake_52_(Westmorland)_RSN314\/RSN314_WESMORL_BRA-UP_A.txt'
]

velocityFilePaths_quake52 = [
    'Earthquake_52_(Westmorland)_RSN314\RSN314_WESMORL_BRA225_V.txt', 
    'Earthquake_52_(Westmorland)_RSN314\RSN314_WESMORL_BRA315_V.txt', 
    'Earthquake_52_(Westmorland)_RSN314\RSN314_WESMORL_BRA-UP_V.txt'
]

displacementFilePaths_quake52 = [
    'Earthquake_52_(Westmorland)_RSN314\RSN314_WESMORL_BRA225_D.txt', 
    'Earthquake_52_(Westmorland)_RSN314\RSN314_WESMORL_BRA315_D.txt', 
    'Earthquake_52_(Westmorland)_RSN314\RSN314_WESMORL_BRA-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake52)):
    component_results = process_component(accelerationFilePaths_quake52[i], velocityFilePaths_quake52[i], displacementFilePaths_quake52[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 52'
name = 'Westmorland'
record_sequence_number = 314
earthquake_station = 'Brawley Airport'

# Function to print the results in the desired format
def print_earthquake52_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake52_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 53 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake53
accelerationFilePaths_quake53 = [
    'Earthquake_53_(Mammoth Lakes-10)_RSN320\RSN320_MAMMOTH.AH_F-CVK090_A.txt',
    'Earthquake_53_(Mammoth Lakes-10)_RSN320\RSN320_MAMMOTH.AH_F-CVK180_A.txt',
    'Earthquake_53_(Mammoth Lakes-10)_RSN320\RSN320_MAMMOTH.AH_F-CVK-UP_A.txt'
]

velocityFilePaths_quake53 = [
    'Earthquake_53_(Mammoth Lakes-10)_RSN320\RSN320_MAMMOTH.AH_F-CVK090_V.txt',
    'Earthquake_53_(Mammoth Lakes-10)_RSN320\RSN320_MAMMOTH.AH_F-CVK180_V.txt',
    'Earthquake_53_(Mammoth Lakes-10)_RSN320\RSN320_MAMMOTH.AH_F-CVK-UP_V.txt'
]

displacementFilePaths_quake53 = [
    'Earthquake_53_(Mammoth Lakes-10)_RSN320\RSN320_MAMMOTH.AH_F-CVK090_D.txt',
    'Earthquake_53_(Mammoth Lakes-10)_RSN320\RSN320_MAMMOTH.AH_F-CVK180_D.txt',
    'Earthquake_53_(Mammoth Lakes-10)_RSN320\RSN320_MAMMOTH.AH_F-CVK-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake53)):
    component_results = process_component(accelerationFilePaths_quake53[i], velocityFilePaths_quake53[i], displacementFilePaths_quake53[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 53'
name = 'Mammoth Lakes-10'
record_sequence_number = 320
earthquake_station = 'Convict Creek'

# Function to print the results in the desired format
def print_earthquake53_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake53_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 54 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake54
accelerationFilePaths_quake54 = [
    r'Earthquake_54_(Mammoth Lakes-11)_RSN321\RSN321_MAMMOTH.AH_G-CVK090_A.txt',
    r'Earthquake_54_(Mammoth Lakes-11)_RSN321\RSN321_MAMMOTH.AH_G-CVK180_A.txt',
    r'Earthquake_54_(Mammoth Lakes-11)_RSN321\RSN321_MAMMOTH.AH_G-CVK-UP_A.txt'
]

velocityFilePaths_quake54 = [
    r'Earthquake_54_(Mammoth Lakes-11)_RSN321\RSN321_MAMMOTH.AH_G-CVK090_V.txt',
    r'Earthquake_54_(Mammoth Lakes-11)_RSN321\RSN321_MAMMOTH.AH_G-CVK180_V.txt',
    r'Earthquake_54_(Mammoth Lakes-11)_RSN321\RSN321_MAMMOTH.AH_G-CVK-UP_V.txt'
]

displacementFilePaths_quake54 = [
    r'Earthquake_54_(Mammoth Lakes-11)_RSN321\RSN321_MAMMOTH.AH_G-CVK090_D.txt',
    r'Earthquake_54_(Mammoth Lakes-11)_RSN321\RSN321_MAMMOTH.AH_G-CVK180_D.txt',
    r'Earthquake_54_(Mammoth Lakes-11)_RSN321\RSN321_MAMMOTH.AH_G-CVK-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake54)):
    component_results = process_component(accelerationFilePaths_quake54[i], velocityFilePaths_quake54[i], displacementFilePaths_quake54[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 54'
name = 'Mammoth Lakes-11'
record_sequence_number = 321
earthquake_station = 'Convict Creek'

# Function to print the results in the desired format
def print_earthquake54_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake54_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 55 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake55
accelerationFilePaths_quake55 = [
    'Earthquake_55_(Coalinga-01)_RSN322\RSN322_COALINGA.H_H-CAK270_A.txt',
    'Earthquake_55_(Coalinga-01)_RSN322\RSN322_COALINGA.H_H-CAK360_A.txt',
    'Earthquake_55_(Coalinga-01)_RSN322\RSN322_COALINGA.H_H-CAK-UP_A.txt'
]

velocityFilePaths_quake55 = [
    'Earthquake_55_(Coalinga-01)_RSN322\RSN322_COALINGA.H_H-CAK270_V.txt',
    'Earthquake_55_(Coalinga-01)_RSN322\RSN322_COALINGA.H_H-CAK360_V.txt',
    'Earthquake_55_(Coalinga-01)_RSN322\RSN322_COALINGA.H_H-CAK-UP_V.txt'
]

displacementFilePaths_quake55 = [
    'Earthquake_55_(Coalinga-01)_RSN322\RSN322_COALINGA.H_H-CAK270_D.txt',
    'Earthquake_55_(Coalinga-01)_RSN322\RSN322_COALINGA.H_H-CAK360_D.txt',
    'Earthquake_55_(Coalinga-01)_RSN322\RSN322_COALINGA.H_H-CAK-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake55)):
    component_results = process_component(accelerationFilePaths_quake55[i], velocityFilePaths_quake55[i], displacementFilePaths_quake55[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 55'
name = 'Coalinga-01'
record_sequence_number = 322
earthquake_station = 'Cantua Creek School'

# Function to print the results in the desired format
def print_earthquake55_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake55_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 56 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake56
accelerationFilePaths_quake56 = [
    'Earthquake_56_(Coalinga-02)_RSN370\RSN370_COALINGA_A-ALP085_A.txt',
    'Earthquake_56_(Coalinga-02)_RSN370\RSN370_COALINGA_A-ALP355_A.txt',
    'Earthquake_56_(Coalinga-02)_RSN370\RSN370_COALINGA_A-ALP-UP_A.txt'
]

velocityFilePaths_quake56 = [
    'Earthquake_56_(Coalinga-02)_RSN370\RSN370_COALINGA_A-ALP085_V.txt',
    'Earthquake_56_(Coalinga-02)_RSN370\RSN370_COALINGA_A-ALP355_V.txt',
    'Earthquake_56_(Coalinga-02)_RSN370\RSN370_COALINGA_A-ALP-UP_V.txt'
]

displacementFilePaths_quake56 = [
    'Earthquake_56_(Coalinga-02)_RSN370\RSN370_COALINGA_A-ALP085_D.txt',
    'Earthquake_56_(Coalinga-02)_RSN370\RSN370_COALINGA_A-ALP355_D.txt',
    'Earthquake_56_(Coalinga-02)_RSN370\RSN370_COALINGA_A-ALP-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake56)):
    component_results = process_component(accelerationFilePaths_quake56[i], velocityFilePaths_quake56[i], displacementFilePaths_quake56[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 56'
name = 'Coalinga-02'
record_sequence_number = 370
earthquake_station = 'ALP (temp)'

# Function to print the results in the desired format
def print_earthquake56_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake56_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 57 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake57
accelerationFilePaths_quake57 = [
    'Earthquake_57_(Coalinga-03)_RSN391\RSN391_COALINGA_B-BNT270_A.txt',
    'Earthquake_57_(Coalinga-03)_RSN391\RSN391_COALINGA_B-BNT360_A.txt',
    'Earthquake_57_(Coalinga-03)_RSN391\RSN391_COALINGA_B-BNT-UP_A.txt'
]

velocityFilePaths_quake57 = [
    'Earthquake_57_(Coalinga-03)_RSN391\RSN391_COALINGA_B-BNT270_V.txt',
    'Earthquake_57_(Coalinga-03)_RSN391\RSN391_COALINGA_B-BNT360_V.txt',
    'Earthquake_57_(Coalinga-03)_RSN391\RSN391_COALINGA_B-BNT-UP_V.txt'
]

displacementFilePaths_quake57 = [
    'Earthquake_57_(Coalinga-03)_RSN391\RSN391_COALINGA_B-BNT270_D.txt',
    'Earthquake_57_(Coalinga-03)_RSN391\RSN391_COALINGA_B-BNT360_D.txt',
    'Earthquake_57_(Coalinga-03)_RSN391\RSN391_COALINGA_B-BNT-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake57)):
    component_results = process_component(accelerationFilePaths_quake57[i], velocityFilePaths_quake57[i], displacementFilePaths_quake57[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 57'
name = 'Coalinga-03'
record_sequence_number = 391
earthquake_station = 'Burnett Construction'

# Function to print the results in the desired format
def print_earthquake57_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake57_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 58 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake58
accelerationFilePaths_quake58 = [
    'Earthquake_58_(Coalinga-04)_RSN394\RSN394_COALINGA_C-ATC270_A.txt',
    'Earthquake_58_(Coalinga-04)_RSN394\RSN394_COALINGA_C-ATC360_A.txt',
    'Earthquake_58_(Coalinga-04)_RSN394\RSN394_COALINGA_C-ATC-UP_A.txt'
]

velocityFilePaths_quake58 = [
    'Earthquake_58_(Coalinga-04)_RSN394\RSN394_COALINGA_C-ATC270_V.txt',
    'Earthquake_58_(Coalinga-04)_RSN394\RSN394_COALINGA_C-ATC360_V.txt',
    'Earthquake_58_(Coalinga-04)_RSN394\RSN394_COALINGA_C-ATC-UP_V.txt'
]

displacementFilePaths_quake58 = [
    'Earthquake_58_(Coalinga-04)_RSN394\RSN394_COALINGA_C-ATC270_D.txt',
    'Earthquake_58_(Coalinga-04)_RSN394\RSN394_COALINGA_C-ATC360_D.txt',
    'Earthquake_58_(Coalinga-04)_RSN394\RSN394_COALINGA_C-ATC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake58)):
    component_results = process_component(accelerationFilePaths_quake58[i], velocityFilePaths_quake58[i], displacementFilePaths_quake58[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 58'
name = 'Coalinga-04'
record_sequence_number = 394
earthquake_station = 'Anticline Ridge Free-Field'

# Function to print the results in the desired format
def print_earthquake58_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake58_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 59 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake59
accelerationFilePaths_quake59 = [
    'Earthquake_59_(Coalinga-05)_RSN405\RSN405_COALINGA_D-BNT270_A.txt',
    'Earthquake_59_(Coalinga-05)_RSN405\RSN405_COALINGA_D-BNT360_A.txt',
    'Earthquake_59_(Coalinga-05)_RSN405\RSN405_COALINGA_D-BNT-UP_A.txt'
]

velocityFilePaths_quake59 = [
    'Earthquake_59_(Coalinga-05)_RSN405\RSN405_COALINGA_D-BNT270_V.txt',
    'Earthquake_59_(Coalinga-05)_RSN405\RSN405_COALINGA_D-BNT360_V.txt',
    'Earthquake_59_(Coalinga-05)_RSN405\RSN405_COALINGA_D-BNT-UP_V.txt'
]

displacementFilePaths_quake59 = [
    'Earthquake_59_(Coalinga-05)_RSN405\RSN405_COALINGA_D-BNT270_D.txt',
    'Earthquake_59_(Coalinga-05)_RSN405\RSN405_COALINGA_D-BNT360_D.txt',
    'Earthquake_59_(Coalinga-05)_RSN405\RSN405_COALINGA_D-BNT-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake59)):
    component_results = process_component(accelerationFilePaths_quake59[i], velocityFilePaths_quake59[i], displacementFilePaths_quake59[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 59'
name = 'Coalinga-05'
record_sequence_number = 405
earthquake_station = 'Burnett Construction'

# Function to print the results in the desired format
def print_earthquake59_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake59_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 60 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake60
accelerationFilePaths_quake60 = [
    'Earthquake_60_(Coalinga-06)_RSN416\RSN416_COALINGA_E-CHP000_A.txt',
    'Earthquake_60_(Coalinga-06)_RSN416\RSN416_COALINGA_E-CHP090_A.txt',
    'Earthquake_60_(Coalinga-06)_RSN416\RSN416_COALINGA_E-CHP-UP_A.txt'
]

velocityFilePaths_quake60 = [
    'Earthquake_60_(Coalinga-06)_RSN416\RSN416_COALINGA_E-CHP000_V.txt',
    'Earthquake_60_(Coalinga-06)_RSN416\RSN416_COALINGA_E-CHP090_V.txt',
    'Earthquake_60_(Coalinga-06)_RSN416\RSN416_COALINGA_E-CHP-UP_V.txt'
]

displacementFilePaths_quake60 = [
    'Earthquake_60_(Coalinga-06)_RSN416\RSN416_COALINGA_E-CHP000_D.txt',
    'Earthquake_60_(Coalinga-06)_RSN416\RSN416_COALINGA_E-CHP090_D.txt',
    'Earthquake_60_(Coalinga-06)_RSN416\RSN416_COALINGA_E-CHP-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake60)):
    component_results = process_component(accelerationFilePaths_quake60[i], velocityFilePaths_quake60[i], displacementFilePaths_quake60[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 60'
name = 'Coalinga-06'
record_sequence_number = 416
earthquake_station = 'Coalinga-14th & Elm (Old CHP)'

# Function to print the results in the desired format
def print_earthquake60_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake60_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 1 to Earthquake 10 --------------------------------

# ------------------------------------- Beginning of Earthquake11 to Earthqauke70 --------------------------------
# ------------------------------------- Earthquake 61 --------------------------------------------------
accelerationFilePaths_quake61 = [
    'Earthquake_61_(Coalinga-07)_RSN418\RSN418_COALINGA_F-CHP000_A.txt',
    'Earthquake_61_(Coalinga-07)_RSN418\RSN418_COALINGA_F-CHP090_A.txt',
    'Earthquake_61_(Coalinga-07)_RSN418\RSN418_COALINGA_F-CHP-UP_A.txt'
]

velocityFilePaths_quake61 = [
    'Earthquake_61_(Coalinga-07)_RSN418\RSN418_COALINGA_F-CHP000_V.txt',
    'Earthquake_61_(Coalinga-07)_RSN418\RSN418_COALINGA_F-CHP090_V.txt',
    'Earthquake_61_(Coalinga-07)_RSN418\RSN418_COALINGA_F-CHP-UP_V.txt'
]

displacementFilePaths_quake61 = [
    'Earthquake_61_(Coalinga-07)_RSN418\RSN418_COALINGA_F-CHP000_D.txt',
    'Earthquake_61_(Coalinga-07)_RSN418\RSN418_COALINGA_F-CHP090_D.txt',
    'Earthquake_61_(Coalinga-07)_RSN418\RSN418_COALINGA_F-CHP-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake61)):
    component_results = process_component(accelerationFilePaths_quake61[i], velocityFilePaths_quake61[i], displacementFilePaths_quake61[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 61'
name = 'Coalinga-07'
record_sequence_number = 418
earthquake_station = 'Coalinga-14th & Elm (Old CHP)'

# Function to print the results in the desired format
def print_earthquake61_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake61_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 62 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake62
accelerationFilePaths_quake62 = [
    'Earthquake_62_(Coalinga-08)_RSN423\RSN423_COALINGA_G-CHP000_A.txt',
    'Earthquake_62_(Coalinga-08)_RSN423\RSN423_COALINGA_G-CHP090_A.txt',
    'Earthquake_62_(Coalinga-08)_RSN423\RSN423_COALINGA_G-CHP-UP_A.txt'
]

velocityFilePaths_quake62 = [
    'Earthquake_62_(Coalinga-08)_RSN423\RSN423_COALINGA_G-CHP000_V.txt',
    'Earthquake_62_(Coalinga-08)_RSN423\RSN423_COALINGA_G-CHP090_V.txt',
    'Earthquake_62_(Coalinga-08)_RSN423\RSN423_COALINGA_G-CHP-UP_V.txt'
]

displacementFilePaths_quake62 = [
    'Earthquake_62_(Coalinga-08)_RSN423\RSN423_COALINGA_G-CHP000_D.txt',
    'Earthquake_62_(Coalinga-08)_RSN423\RSN423_COALINGA_G-CHP090_D.txt',
    'Earthquake_62_(Coalinga-08)_RSN423\RSN423_COALINGA_G-CHP-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake62)):
    component_results = process_component(accelerationFilePaths_quake62[i], velocityFilePaths_quake62[i], displacementFilePaths_quake62[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 62'
name = 'Coalinga-08'
record_sequence_number = 423
earthquake_station = 'Coalinga-14th & Elm (Old CHP)'

# Function to print the results in the desired format
def print_earthquake62_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake62_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 63 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake63
accelerationFilePaths_quake63 = [
    'Earthquake_63_(Morgan Hill)_RSN446\RSN446_MORGAN_A1E000_A.txt',
    'Earthquake_63_(Morgan Hill)_RSN446\RSN446_MORGAN_A1E090_A.txt'
]

velocityFilePaths_quake63 = [
    'Earthquake_63_(Morgan Hill)_RSN446\RSN446_MORGAN_A1E000_V.txt',
    'Earthquake_63_(Morgan Hill)_RSN446\RSN446_MORGAN_A1E090_V.txt'
]

displacementFilePaths_quake63 = [
    'Earthquake_63_(Morgan Hill)_RSN446\RSN446_MORGAN_A1E000_D.txt',
    'Earthquake_63_(Morgan Hill)_RSN446\RSN446_MORGAN_A1E090_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake63)):
    component_results = process_component(accelerationFilePaths_quake63[i], velocityFilePaths_quake63[i], displacementFilePaths_quake63[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 63'
name = 'Morgan Hill'
record_sequence_number = 446
earthquake_station = 'APEEL 1E - Hayward'

# Function to print the results in the desired format
def print_earthquake63_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake63_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 64 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake64
accelerationFilePaths_quake64 = [
    'Earthquake_64_(Bishop (Rnd Val))_RSN485\RSN485_ROUNDVAL_MCG270_A.txt',
    'Earthquake_64_(Bishop (Rnd Val))_RSN485\RSN485_ROUNDVAL_MCG360_A.txt',
    'Earthquake_64_(Bishop (Rnd Val))_RSN485\RSN485_ROUNDVAL_MCG-UP_A.txt'
]

velocityFilePaths_quake64 = [
    'Earthquake_64_(Bishop (Rnd Val))_RSN485\RSN485_ROUNDVAL_MCG270_V.txt',
    'Earthquake_64_(Bishop (Rnd Val))_RSN485\RSN485_ROUNDVAL_MCG360_V.txt',
    'Earthquake_64_(Bishop (Rnd Val))_RSN485\RSN485_ROUNDVAL_MCG-UP_V.txt'
]

displacementFilePaths_quake64 = [
    'Earthquake_64_(Bishop (Rnd Val))_RSN485\RSN485_ROUNDVAL_MCG270_D.txt',
    'Earthquake_64_(Bishop (Rnd Val))_RSN485\RSN485_ROUNDVAL_MCG360_D.txt',
    'Earthquake_64_(Bishop (Rnd Val))_RSN485\RSN485_ROUNDVAL_MCG-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake64)):
    component_results = process_component(accelerationFilePaths_quake64[i], velocityFilePaths_quake64[i], displacementFilePaths_quake64[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 64'
name = 'Bishop (Rnd Val)'
record_sequence_number = 485
earthquake_station = 'McGee Creek - Surface'

# Function to print the results in the desired format
def print_earthquake64_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake64_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 65 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake65
accelerationFilePaths_quake65 = [
    'Earthquake_65_(Hollister-04)_RSN499\RSN499_HOLLISTR_D-HD3255_A.txt',
    'Earthquake_65_(Hollister-04)_RSN499\RSN499_HOLLISTR_D-HD3345_A.txt',
    'Earthquake_65_(Hollister-04)_RSN499\RSN499_HOLLISTR_D-HD3-UP_A.txt'
]

velocityFilePaths_quake65 = [
    'Earthquake_65_(Hollister-04)_RSN499\RSN499_HOLLISTR_D-HD3255_V.txt',
    'Earthquake_65_(Hollister-04)_RSN499\RSN499_HOLLISTR_D-HD3345_V.txt',
    'Earthquake_65_(Hollister-04)_RSN499\RSN499_HOLLISTR_D-HD3-UP_V.txt'
]

displacementFilePaths_quake65 = [
    'Earthquake_65_(Hollister-04)_RSN499\RSN499_HOLLISTR_D-HD3255_D.txt',
    'Earthquake_65_(Hollister-04)_RSN499\RSN499_HOLLISTR_D-HD3345_D.txt',
    'Earthquake_65_(Hollister-04)_RSN499\RSN499_HOLLISTR_D-HD3-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake65)):
    component_results = process_component(accelerationFilePaths_quake65[i], velocityFilePaths_quake65[i], displacementFilePaths_quake65[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 65'
name = 'Hollister-04'
record_sequence_number = 499
earthquake_station = 'Hollister Differential Array #3'

# Function to print the results in the desired format
def print_earthquake65_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake65_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 66 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake66
accelerationFilePaths_quake66 = [
    'Earthquake_66_(Mt. Lewis)_RSN502\RSN502_MTLEWIS_HVR000_A.txt',
    'Earthquake_66_(Mt. Lewis)_RSN502\RSN502_MTLEWIS_HVR090_A.txt',
    'Earthquake_66_(Mt. Lewis)_RSN502\RSN502_MTLEWIS_HVR-UP_A.txt'
]

velocityFilePaths_quake66 = [
    'Earthquake_66_(Mt. Lewis)_RSN502\RSN502_MTLEWIS_HVR000_V.txt',
    'Earthquake_66_(Mt. Lewis)_RSN502\RSN502_MTLEWIS_HVR090_V.txt',
    'Earthquake_66_(Mt. Lewis)_RSN502\RSN502_MTLEWIS_HVR-UP_V.txt'
]

displacementFilePaths_quake66 = [
    'Earthquake_66_(Mt. Lewis)_RSN502\RSN502_MTLEWIS_HVR000_D.txt',
    'Earthquake_66_(Mt. Lewis)_RSN502\RSN502_MTLEWIS_HVR090_D.txt',
    'Earthquake_66_(Mt. Lewis)_RSN502\RSN502_MTLEWIS_HVR-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake66)):
    component_results = process_component(accelerationFilePaths_quake66[i], velocityFilePaths_quake66[i], displacementFilePaths_quake66[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 66'
name = 'Mt. Lewis'
record_sequence_number = 502
earthquake_station = 'Halls Valley'

# Function to print the results in the desired format
def print_earthquake66_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake66_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 67 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake67
accelerationFilePaths_quake67 = [
    'Earthquake_67_(N. Palm Springs)_RSN511\RSN511_PALMSPR_ARM270_A.txt',
    'Earthquake_67_(N. Palm Springs)_RSN511\RSN511_PALMSPR_ARM360_A.txt',
    'Earthquake_67_(N. Palm Springs)_RSN511\RSN511_PALMSPR_ARM-UP_A.txt'
]

velocityFilePaths_quake67 = [
    'Earthquake_67_(N. Palm Springs)_RSN511\RSN511_PALMSPR_ARM270_V.txt',
    'Earthquake_67_(N. Palm Springs)_RSN511\RSN511_PALMSPR_ARM360_V.txt',
    'Earthquake_67_(N. Palm Springs)_RSN511\RSN511_PALMSPR_ARM-UP_V.txt'
]

displacementFilePaths_quake67 = [
    'Earthquake_67_(N. Palm Springs)_RSN511\RSN511_PALMSPR_ARM270_D.txt',
    'Earthquake_67_(N. Palm Springs)_RSN511\RSN511_PALMSPR_ARM360_D.txt',
    'Earthquake_67_(N. Palm Springs)_RSN511\RSN511_PALMSPR_ARM-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake67)):
    component_results = process_component(accelerationFilePaths_quake67[i], velocityFilePaths_quake67[i], displacementFilePaths_quake67[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 67'
name = 'N. Palm Springs'
record_sequence_number = 511
earthquake_station = 'Anza - Red Mountain'

# Function to print the results in the desired format
def print_earthquake67_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake67_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 68 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake68
accelerationFilePaths_quake68 = [
    'Earthquake_68_(Chalfant Valley-01)_RSN543\RSN543_CHALFANT.B_B-BEN270_A.txt',
    'Earthquake_68_(Chalfant Valley-01)_RSN543\RSN543_CHALFANT.B_B-BEN360_A.txt',
    'Earthquake_68_(Chalfant Valley-01)_RSN543\RSN543_CHALFANT.B_B-BEN-UP_A.txt'
]

velocityFilePaths_quake68 = [
    'Earthquake_68_(Chalfant Valley-01)_RSN543\RSN543_CHALFANT.B_B-BEN270_V.txt',
    'Earthquake_68_(Chalfant Valley-01)_RSN543\RSN543_CHALFANT.B_B-BEN360_V.txt',
    'Earthquake_68_(Chalfant Valley-01)_RSN543\RSN543_CHALFANT.B_B-BEN-UP_V.txt'
]

displacementFilePaths_quake68 = [
    'Earthquake_68_(Chalfant Valley-01)_RSN543\RSN543_CHALFANT.B_B-BEN270_D.txt',
    'Earthquake_68_(Chalfant Valley-01)_RSN543\RSN543_CHALFANT.B_B-BEN360_D.txt',
    'Earthquake_68_(Chalfant Valley-01)_RSN543\RSN543_CHALFANT.B_B-BEN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake68)):
    component_results = process_component(accelerationFilePaths_quake68[i], velocityFilePaths_quake68[i], displacementFilePaths_quake68[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 68'
name = 'Chalfant Valley-01'
record_sequence_number = 543
earthquake_station = 'Benton'

# Function to print the results in the desired format
def print_earthquake68_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake68_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 69 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake69
def make_motion_earthquake69(filepath_a, filepath_v, filepath_d, t_step):
    t, t_series_a = make_t_series(filepath_a, t_step)
    _, t_series_v = make_t_series(filepath_v, t_step)
    _, t_series_d = make_t_series(filepath_d, t_step)
    
    # Debug: Print lengths for diagnosis
    print(f"Lengths - Acceleration: {len(t_series_a)}, Velocity: {len(t_series_v)}, Displacement: {len(t_series_d)}")
    
    # Ensure all series have the same length (choose your method here, e.g., truncating to shortest series)
    min_length = min(len(t_series_a), len(t_series_v), len(t_series_d))
    t = t[:min_length]
    t_series_a = t_series_a[:min_length]
    t_series_v = t_series_v[:min_length]
    t_series_d = t_series_d[:min_length]

    data = np.column_stack((t, t_series_a, t_series_v, t_series_d))
    return data


def process_component_earthquake69(filepath_a, filepath_v, filepath_d, dt):
    data = make_motion_earthquake69(filepath_a, filepath_v, filepath_d, dt)
    return {
        'PGA': np.max(np.abs(data[:, 1])),
        'PGV': np.max(np.abs(data[:, 2])),
        'PGD': np.max(np.abs(data[:, 3]))
    }


# Earthquake69
accelerationFilePaths_quake69 = [
    'Earthquake_69_(Chalfant Valley-02)_RSN548\RSN548_CHALFANT.A_A-BEN270_A.txt',
    'Earthquake_69_(Chalfant Valley-02)_RSN548\RSN548_CHALFANT.A_A-BEN360_A.txt',
    'Earthquake_69_(Chalfant Valley-02)_RSN548\RSN548_CHALFANT.A_A-BEN-UP_A.txt'
]

velocityFilePaths_quake69 = [
    'Earthquake_69_(Chalfant Valley-02)_RSN548\RSN548_CHALFANT.A_A-BEN270_V.txt',
    'Earthquake_69_(Chalfant Valley-02)_RSN548\RSN548_CHALFANT.A_A-BEN360_V.txt',
    'Earthquake_69_(Chalfant Valley-02)_RSN548\RSN548_CHALFANT.A_A-BEN-UP_V.txt'
]

displacementFilePaths_quake69 = [
    'Earthquake_69_(Chalfant Valley-02)_RSN548\RSN548_CHALFANT.A_A-BEN270_D.txt',
    'Earthquake_69_(Chalfant Valley-02)_RSN548\RSN548_CHALFANT.A_A-BEN360_D.txt',
    'Earthquake_69_(Chalfant Valley-02)_RSN548\RSN548_CHALFANT.A_A-BEN-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake69)):
    component_results = process_component(accelerationFilePaths_quake69[i], velocityFilePaths_quake69[i], displacementFilePaths_quake69[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 69'
name = 'Chalfant Valley-02'
record_sequence_number = 548
earthquake_station = 'Benton'

# Function to print the results in the desired format
def print_earthquake69_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake69_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 70 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake70
accelerationFilePaths_quake70= [
    'Earthquake_70_(Chalfant Valley-03)_RSN559\RSN559_CHALFANT.B_C-LAD180_A.txt',
    'Earthquake_70_(Chalfant Valley-03)_RSN559\RSN559_CHALFANT.B_C-LAD270_A.txt',
    'Earthquake_70_(Chalfant Valley-03)_RSN559\RSN559_CHALFANT.B_C-LAD-UP_A.txt'
]

velocityFilePaths_quake70 = [
    'Earthquake_70_(Chalfant Valley-03)_RSN559\RSN559_CHALFANT.B_C-LAD180_V.txt',
    'Earthquake_70_(Chalfant Valley-03)_RSN559\RSN559_CHALFANT.B_C-LAD270_V.txt',
    'Earthquake_70_(Chalfant Valley-03)_RSN559\RSN559_CHALFANT.B_C-LAD-UP_V.txt'
]

displacementFilePaths_quake70 = [
    'Earthquake_70_(Chalfant Valley-03)_RSN559\RSN559_CHALFANT.B_C-LAD180_D.txt',
    'Earthquake_70_(Chalfant Valley-03)_RSN559\RSN559_CHALFANT.B_C-LAD270_D.txt',
    'Earthquake_70_(Chalfant Valley-03)_RSN559\RSN559_CHALFANT.B_C-LAD-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake70)):
    component_results = process_component(accelerationFilePaths_quake70[i], velocityFilePaths_quake70[i], displacementFilePaths_quake70[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 70'
name = 'Chalfant Valley-03'
record_sequence_number = 559
earthquake_station = 'Bishop - LADWP South St'

# Function to print the results in the desired format
def print_earthquake70_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake70_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 11 to Earthquake 70 --------------------------------

# ------------------------------------- Beginning of Earthquake71 to Earthqauke80 --------------------------------
# ------------------------------------- Earthquake 71 --------------------------------------------------
accelerationFilePaths_quake71 = [
    'Earthquake_71_(Chalfant Valley-04)_RSN562\RSN562_CHALFANT.B_D-LAD180_A.txt',
    'Earthquake_71_(Chalfant Valley-04)_RSN562\RSN562_CHALFANT.B_D-LAD270_A.txt',
    'Earthquake_71_(Chalfant Valley-04)_RSN562\RSN562_CHALFANT.B_D-LAD-UP_A.txt'
]

velocityFilePaths_quake71 = [
    'Earthquake_71_(Chalfant Valley-04)_RSN562\RSN562_CHALFANT.B_D-LAD180_V.txt',
    'Earthquake_71_(Chalfant Valley-04)_RSN562\RSN562_CHALFANT.B_D-LAD270_V.txt',
    'Earthquake_71_(Chalfant Valley-04)_RSN562\RSN562_CHALFANT.B_D-LAD-UP_V.txt'
]

displacementFilePaths_quake71 = [
    'Earthquake_71_(Chalfant Valley-04)_RSN562\RSN562_CHALFANT.B_D-LAD180_D.txt',
    'Earthquake_71_(Chalfant Valley-04)_RSN562\RSN562_CHALFANT.B_D-LAD270_D.txt',
    'Earthquake_71_(Chalfant Valley-04)_RSN562\RSN562_CHALFANT.B_D-LAD-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake71)):
    component_results = process_component(accelerationFilePaths_quake71[i], velocityFilePaths_quake71[i], displacementFilePaths_quake71[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 71'
name = 'Chalfant Valley-04'
record_sequence_number = 562
earthquake_station = 'Bishop - LADWP South St'

# Function to print the results in the desired format
def print_earthquake71_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake71_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 72 --------------------------------------------------
def make_motion_earthquake72(filepath_a, filepath_v, filepath_d, t_step):
    # Extract time series data from the files
    t, t_series_a = make_t_series(filepath_a, t_step)
    _, t_series_v = make_t_series(filepath_v, t_step)
    _, t_series_d = make_t_series(filepath_d, t_step)
    
    # Find the shortest length among the arrays
    min_length = min(len(t_series_a), len(t_series_v), len(t_series_d))
    
    # Truncate the arrays to the shortest length
    t_series_a = t_series_a[:min_length]
    t_series_v = t_series_v[:min_length]
    t_series_d = t_series_d[:min_length]
    t = t[:min_length]  # Also truncate the time array to match the data arrays
    
    # Concatenate the truncated arrays
    data = np.column_stack((t, t_series_a, t_series_v, t_series_d))
    return data


def process_component_earthquake72(filepath_a, filepath_v, filepath_d, dt):
    data = make_motion_earthquake72(filepath_a, filepath_v, filepath_d, dt)
    return {
        'PGA': np.max(np.abs(data[:, 1])),
        'PGV': np.max(np.abs(data[:, 2])),
        'PGD': np.max(np.abs(data[:, 3]))
    }
    

accelerationFilePaths_quake72 = [
    'Earthquake_72_(Baja California)_RSN585\RSN585_BAJA_CPE161_A.txt',
    'Earthquake_72_(Baja California)_RSN585\RSN585_BAJA_CPE251_A.txt',
    'Earthquake_72_(Baja California)_RSN585\RSN585_BAJA_CPE-UP_A.txt'
]

velocityFilePaths_quake72 = [
    'Earthquake_72_(Baja California)_RSN585\RSN585_BAJA_CPE161_V.txt',
    'Earthquake_72_(Baja California)_RSN585\RSN585_BAJA_CPE251_V.txt',
    'Earthquake_72_(Baja California)_RSN585\RSN585_BAJA_CPE-UP_V.txt'
]

displacementFilePaths_quake72 = [
    'Earthquake_72_(Baja California)_RSN585\RSN585_BAJA_CPE161_D.txt',
    'Earthquake_72_(Baja California)_RSN585\RSN585_BAJA_CPE251_D.txt',
    'Earthquake_72_(Baja California)_RSN585\RSN585_BAJA_CPE-UP_D.txt'
]
dt = 0.005




# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake72)):
    component_results = process_component(accelerationFilePaths_quake72[i], velocityFilePaths_quake72[i], displacementFilePaths_quake72[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 72'
name = 'Baja California'
record_sequence_number = 585
earthquake_station = 'Cerro Prieto'

# Function to print the results in the desired format
def print_earthquake72_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake72_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 73 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake73
accelerationFilePaths_quake73 = [
    'Earthquake_73_(Whittier Narrows-01)_RSN589\RSN589_WHITTIER.A_A-ALH180_A.txt',
    'Earthquake_73_(Whittier Narrows-01)_RSN589\RSN589_WHITTIER.A_A-ALH270_A.txt',
    'Earthquake_73_(Whittier Narrows-01)_RSN589\RSN589_WHITTIER.A_A-ALH-UP_A.txt'
]

velocityFilePaths_quake73 = [
    'Earthquake_73_(Whittier Narrows-01)_RSN589\RSN589_WHITTIER.A_A-ALH180_V.txt',
    'Earthquake_73_(Whittier Narrows-01)_RSN589\RSN589_WHITTIER.A_A-ALH270_V.txt',
    'Earthquake_73_(Whittier Narrows-01)_RSN589\RSN589_WHITTIER.A_A-ALH-UP_V.txt'
]

displacementFilePaths_quake73 = [
    'Earthquake_73_(Whittier Narrows-01)_RSN589\RSN589_WHITTIER.A_A-ALH180_D.txt',
    'Earthquake_73_(Whittier Narrows-01)_RSN589\RSN589_WHITTIER.A_A-ALH270_D.txt',
    'Earthquake_73_(Whittier Narrows-01)_RSN589\RSN589_WHITTIER.A_A-ALH-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake73)):
    component_results = process_component(accelerationFilePaths_quake73[i], velocityFilePaths_quake73[i], displacementFilePaths_quake73[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 73'
name = 'Whittier Narrows-01'
record_sequence_number = 589
earthquake_station = 'Alhambra - Fremont School'

# Function to print the results in the desired format
def print_earthquake73_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake73_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 74 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake74
accelerationFilePaths_quake74 = [
    'Earthquake_74_(Whittier Narrows-02)_RSN707\RSN707_WHITTIER.B_B-ALH180_A.txt',
    'Earthquake_74_(Whittier Narrows-02)_RSN707\RSN707_WHITTIER.B_B-ALH270_A.txt',
    'Earthquake_74_(Whittier Narrows-02)_RSN707\RSN707_WHITTIER.B_B-ALH-UP_A.txt'
]

velocityFilePaths_quake74 = [
    'Earthquake_74_(Whittier Narrows-02)_RSN707\RSN707_WHITTIER.B_B-ALH180_V.txt',
    'Earthquake_74_(Whittier Narrows-02)_RSN707\RSN707_WHITTIER.B_B-ALH270_V.txt',
    'Earthquake_74_(Whittier Narrows-02)_RSN707\RSN707_WHITTIER.B_B-ALH-UP_V.txt'
]

displacementFilePaths_quake74 = [
    'Earthquake_74_(Whittier Narrows-02)_RSN707\RSN707_WHITTIER.B_B-ALH180_D.txt',
    'Earthquake_74_(Whittier Narrows-02)_RSN707\RSN707_WHITTIER.B_B-ALH270_D.txt',
    'Earthquake_74_(Whittier Narrows-02)_RSN707\RSN707_WHITTIER.B_B-ALH-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake74)):
    component_results = process_component(accelerationFilePaths_quake74[i], velocityFilePaths_quake74[i], displacementFilePaths_quake74[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 74'
name = 'Whittier Narrows-02'
record_sequence_number = 707
earthquake_station = 'Alhambra - Fremont School'

# Function to print the results in the desired format
def print_earthquake74_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake74_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 75 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake75
accelerationFilePaths_quake75 = [
    'Earthquake_75_(Superstition Hills-01)_RSN718\RSN718_SUPER.A_A-IVW090_A.txt',
    'Earthquake_75_(Superstition Hills-01)_RSN718\RSN718_SUPER.A_A-IVW360_A.txt',
    'Earthquake_75_(Superstition Hills-01)_RSN718\RSN718_SUPER.A_A-IVW-UP_A.txt'
]

velocityFilePaths_quake75 = [
    'Earthquake_75_(Superstition Hills-01)_RSN718\RSN718_SUPER.A_A-IVW090_V.txt',
    'Earthquake_75_(Superstition Hills-01)_RSN718\RSN718_SUPER.A_A-IVW360_V.txt',
    'Earthquake_75_(Superstition Hills-01)_RSN718\RSN718_SUPER.A_A-IVW-UP_V.txt'
]

displacementFilePaths_quake75 = [
    'Earthquake_75_(Superstition Hills-01)_RSN718\RSN718_SUPER.A_A-IVW090_D.txt',
    'Earthquake_75_(Superstition Hills-01)_RSN718\RSN718_SUPER.A_A-IVW360_D.txt',
    'Earthquake_75_(Superstition Hills-01)_RSN718\RSN718_SUPER.A_A-IVW-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake75)):
    component_results = process_component(accelerationFilePaths_quake75[i], velocityFilePaths_quake75[i], displacementFilePaths_quake75[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 75'
name = 'Superstition Hills-01'
record_sequence_number = 718
earthquake_station = 'Imperial Valley Wildlife Liquefaction Array'

# Function to print the results in the desired format
def print_earthquake75_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake75_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 76 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake76
accelerationFilePaths_quake76 = [
    'Earthquake_76_(Superstition Hills-02)_RSN719\RSN719_SUPER.B_B-BRA225_A.txt',
    'Earthquake_76_(Superstition Hills-02)_RSN719\RSN719_SUPER.B_B-BRA315_A.txt'
]

velocityFilePaths_quake76 = [
    'Earthquake_76_(Superstition Hills-02)_RSN719\RSN719_SUPER.B_B-BRA225_V.txt',
    'Earthquake_76_(Superstition Hills-02)_RSN719\RSN719_SUPER.B_B-BRA315_V.txt'
]

displacementFilePaths_quake76 = [
    'Earthquake_76_(Superstition Hills-02)_RSN719\RSN719_SUPER.B_B-BRA225_D.txt',
    'Earthquake_76_(Superstition Hills-02)_RSN719\RSN719_SUPER.B_B-BRA315_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake76)):
    component_results = process_component(accelerationFilePaths_quake76[i], velocityFilePaths_quake76[i], displacementFilePaths_quake76[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 76'
name = 'Superstition Hills-02'
record_sequence_number = 719
earthquake_station = 'Brawley Airport'

# Function to print the results in the desired format
def print_earthquake76_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake76_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 77 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake77
accelerationFilePaths_quake77 = [
    'Earthquake_77_(Loma Prieta)_RSN731\RSN731_LOMAP_A10000_A.txt',
    'Earthquake_77_(Loma Prieta)_RSN731\RSN731_LOMAP_A10090_A.txt',
    'Earthquake_77_(Loma Prieta)_RSN731\RSN731_LOMAP_A10-UP_A.txt'
]

velocityFilePaths_quake77 = [
    'Earthquake_77_(Loma Prieta)_RSN731\RSN731_LOMAP_A10000_V.txt',
    'Earthquake_77_(Loma Prieta)_RSN731\RSN731_LOMAP_A10090_V.txt',
    'Earthquake_77_(Loma Prieta)_RSN731\RSN731_LOMAP_A10-UP_V.txt'
]

displacementFilePaths_quake77 = [
    'Earthquake_77_(Loma Prieta)_RSN731\RSN731_LOMAP_A10000_D.txt',
    'Earthquake_77_(Loma Prieta)_RSN731\RSN731_LOMAP_A10090_D.txt',
    'Earthquake_77_(Loma Prieta)_RSN731\RSN731_LOMAP_A10-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake77)):
    component_results = process_component(accelerationFilePaths_quake77[i], velocityFilePaths_quake77[i], displacementFilePaths_quake77[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 77'
name = 'Loma Prieta'
record_sequence_number = 731
earthquake_station = 'APEEL 10 - Skyline'

# Function to print the results in the desired format
def print_earthquake77_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake77_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 78 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake78
accelerationFilePaths_quake78 = [
    'Earthquake_78_(Cape Mendocino)_RSN825\RSN825_CAPEMEND_CPM000_A.txt',
    'Earthquake_78_(Cape Mendocino)_RSN825\RSN825_CAPEMEND_CPM090_A.txt',
    'Earthquake_78_(Cape Mendocino)_RSN825\RSN825_CAPEMEND_CPM-UP_A.txt'
]

velocityFilePaths_quake78 = [
    'Earthquake_78_(Cape Mendocino)_RSN825\RSN825_CAPEMEND_CPM000_V.txt',
    'Earthquake_78_(Cape Mendocino)_RSN825\RSN825_CAPEMEND_CPM090_V.txt',
    'Earthquake_78_(Cape Mendocino)_RSN825\RSN825_CAPEMEND_CPM-UP_V.txt'
]

displacementFilePaths_quake78 = [
    'Earthquake_78_(Cape Mendocino)_RSN825\RSN825_CAPEMEND_CPM000_D.txt',
    'Earthquake_78_(Cape Mendocino)_RSN825\RSN825_CAPEMEND_CPM090_D.txt',
    'Earthquake_78_(Cape Mendocino)_RSN825\RSN825_CAPEMEND_CPM-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake78)):
    component_results = process_component(accelerationFilePaths_quake78[i], velocityFilePaths_quake78[i], displacementFilePaths_quake78[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 78'
name = 'Cape Mendocino'
record_sequence_number = 825		
earthquake_station = 'Cape Mendocino'

# Function to print the results in the desired format
def print_earthquake78_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake78_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 79 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake79
accelerationFilePaths_quake79 = [
    'Earthquake_79_(Landers)_RSN832\RSN832_LANDERS_ABY000_A.txt',
    'Earthquake_79_(Landers)_RSN832\RSN832_LANDERS_ABY090_A.txt',
    'Earthquake_79_(Landers)_RSN832\RSN832_LANDERS_ABY-UP_A.txt'
]

velocityFilePaths_quake79 = [
    'Earthquake_79_(Landers)_RSN832\RSN832_LANDERS_ABY000_V.txt',
    'Earthquake_79_(Landers)_RSN832\RSN832_LANDERS_ABY090_V.txt',
    'Earthquake_79_(Landers)_RSN832\RSN832_LANDERS_ABY-UP_V.txt'
]

displacementFilePaths_quake79 = [
    'Earthquake_79_(Landers)_RSN832\RSN832_LANDERS_ABY000_D.txt',
    'Earthquake_79_(Landers)_RSN832\RSN832_LANDERS_ABY090_D.txt',
    'Earthquake_79_(Landers)_RSN832\RSN832_LANDERS_ABY-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Use the length of one of the file path lists assuming all have the same number of elements
for i in range(len(accelerationFilePaths_quake79)):
    component_results = process_component(accelerationFilePaths_quake79[i], velocityFilePaths_quake79[i], displacementFilePaths_quake79[i], dt)
    # Append a descriptive component name if needed, or adjust as necessary
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 79'
name = 'Landers'
record_sequence_number = 832
earthquake_station = 'Amboy'

# Function to print the results in the desired format
def print_earthquake79_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake79_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 80 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake80
accelerationFilePaths_quake80 = [
    'Earthquake_80_(Big Bear-01)_RSN901\RSN901_BIGBEAR_BLC270_A.txt',
    'Earthquake_80_(Big Bear-01)_RSN901\RSN901_BIGBEAR_BLC360_A.txt',
    'Earthquake_80_(Big Bear-01)_RSN901\RSN901_BIGBEAR_BLC-UP_A.txt'
]

velocityFilePaths_quake80 = [
    'Earthquake_80_(Big Bear-01)_RSN901\RSN901_BIGBEAR_BLC270_V.txt',
    'Earthquake_80_(Big Bear-01)_RSN901\RSN901_BIGBEAR_BLC360_V.txt',
    'Earthquake_80_(Big Bear-01)_RSN901\RSN901_BIGBEAR_BLC-UP_V.txt'
]

displacementFilePaths_quake80 = [
    'Earthquake_80_(Big Bear-01)_RSN901\RSN901_BIGBEAR_BLC270_D.txt',
    'Earthquake_80_(Big Bear-01)_RSN901\RSN901_BIGBEAR_BLC360_D.txt',
    'Earthquake_80_(Big Bear-01)_RSN901\RSN901_BIGBEAR_BLC-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake80)):
    component_results = process_component(accelerationFilePaths_quake80[i], velocityFilePaths_quake80[i], displacementFilePaths_quake80[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 80'
name = 'Big Bear-01'
record_sequence_number = 901		
earthquake_station = 'Big Bear Lake - Civic Center'

# Function to print the results in the desired format
def print_earthquake80_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake80_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 71 to Earthquake 80 --------------------------------

# ------------------------------------- Earthquake 81 --------------------------------------------------
accelerationFilePaths_quake81 = [
    'Earthquake_81_(Northridge-01)_RSN942\RSN942_NORTHR_ALH090_A.txt',
    'Earthquake_81_(Northridge-01)_RSN942\RSN942_NORTHR_ALH360_A.txt',
    'Earthquake_81_(Northridge-01)_RSN942\RSN942_NORTHR_ALH-UP_A.txt'
]

velocityFilePaths_quake81 = [
    'Earthquake_81_(Northridge-01)_RSN942\RSN942_NORTHR_ALH090_V.txt',
    'Earthquake_81_(Northridge-01)_RSN942\RSN942_NORTHR_ALH360_V.txt',
    'Earthquake_81_(Northridge-01)_RSN942\RSN942_NORTHR_ALH-UP_V.txt'
]

displacementFilePaths_quake81 = [
    'Earthquake_81_(Northridge-01)_RSN942\RSN942_NORTHR_ALH090_D.txt',
    'Earthquake_81_(Northridge-01)_RSN942\RSN942_NORTHR_ALH360_D.txt',
    'Earthquake_81_(Northridge-01)_RSN942\RSN942_NORTHR_ALH-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake81)):
    component_results = process_component(accelerationFilePaths_quake81[i], velocityFilePaths_quake81[i], displacementFilePaths_quake81[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))

    
# Given metadata for the earthquake
title = 'Earthquake 81'
name = 'Northridge-01'
record_sequence_number = 942
earthquake_station = 'Alhambra - Fremont School'

# Function to print the results in the desired format
def print_earthquake81_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake81_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 82 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake82
accelerationFilePaths_quake82 = [
    'Earthquake_82_(Upland)_RSN1630\RSN1630_UPLAND_UP90S-H1_A.txt',
    'Earthquake_82_(Upland)_RSN1630\RSN1630_UPLAND_UP90S-H2_A.txt',
    'Earthquake_82_(Upland)_RSN1630\RSN1630_UPLAND_UP90S-UP_A.txt'
]

velocityFilePaths_quake82 = [
    'Earthquake_82_(Upland)_RSN1630\RSN1630_UPLAND_UP90S-H1_V.txt',
    'Earthquake_82_(Upland)_RSN1630\RSN1630_UPLAND_UP90S-H2_V.txt',
    'Earthquake_82_(Upland)_RSN1630\RSN1630_UPLAND_UP90S-UP_V.txt'
]

displacementFilePaths_quake82 = [
    'Earthquake_82_(Upland)_RSN1630\RSN1630_UPLAND_UP90S-H1_D.txt',
    'Earthquake_82_(Upland)_RSN1630\RSN1630_UPLAND_UP90S-H2_D.txt',
    'Earthquake_82_(Upland)_RSN1630\RSN1630_UPLAND_UP90S-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake82)):
    component_results = process_component(accelerationFilePaths_quake82[i], velocityFilePaths_quake82[i], displacementFilePaths_quake82[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 82'
name = 'Upland'
record_sequence_number = 1630
earthquake_station = 'Ocean Floor SEMS III'

# Function to print the results in the desired format
def print_earthquake82_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake82_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 83 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake83
accelerationFilePaths_quake83 = [
    'Earthquake_83_(Sierra Madre)_RSN1641\RSN1641_SMADRE_ALT000_A.txt',
    'Earthquake_83_(Sierra Madre)_RSN1641\RSN1641_SMADRE_ALT090_A.txt',
    'Earthquake_83_(Sierra Madre)_RSN1641\RSN1641_SMADRE_ALT-UP_A.txt'
]

velocityFilePaths_quake83 = [
    'Earthquake_83_(Sierra Madre)_RSN1641\RSN1641_SMADRE_ALT000_V.txt',
    'Earthquake_83_(Sierra Madre)_RSN1641\RSN1641_SMADRE_ALT090_V.txt',
    'Earthquake_83_(Sierra Madre)_RSN1641\RSN1641_SMADRE_ALT-UP_V.txt'
]

displacementFilePaths_quake83 = [
    'Earthquake_83_(Sierra Madre)_RSN1641\RSN1641_SMADRE_ALT000_D.txt',
    'Earthquake_83_(Sierra Madre)_RSN1641\RSN1641_SMADRE_ALT090_D.txt',
    'Earthquake_83_(Sierra Madre)_RSN1641\RSN1641_SMADRE_ALT-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake83)):
    component_results = process_component(accelerationFilePaths_quake83[i], velocityFilePaths_quake83[i], displacementFilePaths_quake83[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 83'
name = 'Sierra Madre'
record_sequence_number = 1641
earthquake_station = 'Altadena - Eaton Canyon'

# Function to print the results in the desired format
def print_earthquake83_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake83_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 84 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake84
accelerationFilePaths_quake84 = [
    'Earthquake_84_(Northridge-02)_RSN1650\RSN1650_NORTH001_ANA090_A.txt',
    'Earthquake_84_(Northridge-02)_RSN1650\RSN1650_NORTH001_ANA180_A.txt',
    'Earthquake_84_(Northridge-02)_RSN1650\RSN1650_NORTH001_ANA-UP_A.txt'
]

velocityFilePaths_quake84 = [
    'Earthquake_84_(Northridge-02)_RSN1650\RSN1650_NORTH001_ANA090_V.txt',
    'Earthquake_84_(Northridge-02)_RSN1650\RSN1650_NORTH001_ANA180_V.txt',
    'Earthquake_84_(Northridge-02)_RSN1650\RSN1650_NORTH001_ANA-UP_V.txt'
]

displacementFilePaths_quake84 = [
    'Earthquake_84_(Northridge-02)_RSN1650\RSN1650_NORTH001_ANA090_D.txt',
    'Earthquake_84_(Northridge-02)_RSN1650\RSN1650_NORTH001_ANA180_D.txt',
    'Earthquake_84_(Northridge-02)_RSN1650\RSN1650_NORTH001_ANA-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake84)):
    component_results = process_component(accelerationFilePaths_quake84[i], velocityFilePaths_quake84[i], displacementFilePaths_quake84[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 84'
name = 'Northridge-02'
record_sequence_number = 1650
earthquake_station = 'Anaverde Valley - City R'

# Function to print the results in the desired format
def print_earthquake84_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake84_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 85 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake85
accelerationFilePaths_quake85 = [
    'Earthquake_85_(Northridge-03)_RSN1668\RSN1668_NORTH009_ORR090_A.txt',
    'Earthquake_85_(Northridge-03)_RSN1668\RSN1668_NORTH009_ORR360_A.txt',
    'Earthquake_85_(Northridge-03)_RSN1668\RSN1668_NORTH009_ORR-UP_A.txt'
]

velocityFilePaths_quake85 = [
    'Earthquake_85_(Northridge-03)_RSN1668\RSN1668_NORTH009_ORR090_V.txt',
    'Earthquake_85_(Northridge-03)_RSN1668\RSN1668_NORTH009_ORR360_V.txt',
    'Earthquake_85_(Northridge-03)_RSN1668\RSN1668_NORTH009_ORR-UP_V.txt'
]

displacementFilePaths_quake85 = [
    'Earthquake_85_(Northridge-03)_RSN1668\RSN1668_NORTH009_ORR090_D.txt',
    'Earthquake_85_(Northridge-03)_RSN1668\RSN1668_NORTH009_ORR360_D.txt',
    'Earthquake_85_(Northridge-03)_RSN1668\RSN1668_NORTH009_ORR-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake85)):
    component_results = process_component(accelerationFilePaths_quake85[i], velocityFilePaths_quake85[i], displacementFilePaths_quake85[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 85'
name = 'Northridge-03'
record_sequence_number = 1668
earthquake_station = 'Castaic - Old Ridge Route'

# Function to print the results in the desired format
def print_earthquake85_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake85_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 86 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake86
accelerationFilePaths_quake86 = [
    'Earthquake_86_(Northridge-04)_RSN1675\RSN1675_NORTH142_ANA090_A.txt',
    'Earthquake_86_(Northridge-04)_RSN1675\RSN1675_NORTH142_ANA180_A.txt',
    'Earthquake_86_(Northridge-04)_RSN1675\RSN1675_NORTH142_ANA-UP_A.txt'
]

velocityFilePaths_quake86 = [
    'Earthquake_86_(Northridge-04)_RSN1675\RSN1675_NORTH142_ANA090_V.txt',
    'Earthquake_86_(Northridge-04)_RSN1675\RSN1675_NORTH142_ANA180_V.txt',
    'Earthquake_86_(Northridge-04)_RSN1675\RSN1675_NORTH142_ANA-UP_V.txt'
]

displacementFilePaths_quake86 = [
    'Earthquake_86_(Northridge-04)_RSN1675\RSN1675_NORTH142_ANA090_D.txt',
    'Earthquake_86_(Northridge-04)_RSN1675\RSN1675_NORTH142_ANA180_D.txt',
    'Earthquake_86_(Northridge-04)_RSN1675\RSN1675_NORTH142_ANA-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake86)):
    component_results = process_component(accelerationFilePaths_quake86[i], velocityFilePaths_quake86[i], displacementFilePaths_quake86[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 86'
name = 'Northridge-04'    
record_sequence_number = 1675
earthquake_station = 'Anaverde Valley - City R'

# Function to print the results in the desired format
def print_earthquake86_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake86_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 87 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake87
accelerationFilePaths_quake87 = [
    'Earthquake_87_(Northridge-05)_RSN1682\RSN1682_NORTH151_ANA090_A.txt',
    'Earthquake_87_(Northridge-05)_RSN1682\RSN1682_NORTH151_ANA180_A.txt',
    'Earthquake_87_(Northridge-05)_RSN1682\RSN1682_NORTH151_ANA-UP_A.txt'
]

velocityFilePaths_quake87 = [
    'Earthquake_87_(Northridge-05)_RSN1682\RSN1682_NORTH151_ANA090_V.txt',
    'Earthquake_87_(Northridge-05)_RSN1682\RSN1682_NORTH151_ANA180_V.txt',
    'Earthquake_87_(Northridge-05)_RSN1682\RSN1682_NORTH151_ANA-UP_V.txt'
]

displacementFilePaths_quake87 = [
    'Earthquake_87_(Northridge-05)_RSN1682\RSN1682_NORTH151_ANA090_D.txt',
    'Earthquake_87_(Northridge-05)_RSN1682\RSN1682_NORTH151_ANA180_D.txt',
    'Earthquake_87_(Northridge-05)_RSN1682\RSN1682_NORTH151_ANA-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake87)):
    component_results = process_component(accelerationFilePaths_quake87[i], velocityFilePaths_quake87[i], displacementFilePaths_quake87[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 87'
name = 'Northridge-05'
record_sequence_number = 1682
earthquake_station = 'Anaverde Valley - City R'

# Function to print the results in the desired format
def print_earthquake87_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake87_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 88 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake88
accelerationFilePaths_quake88 = [
    'Earthquake_88_(Northridge-06)_RSN1691\RSN1691_NORTH392_ACI000_A.txt',
    'Earthquake_88_(Northridge-06)_RSN1691\RSN1691_NORTH392_ACI270_A.txt'
]

velocityFilePaths_quake88 = [
    'Earthquake_88_(Northridge-06)_RSN1691\RSN1691_NORTH392_ACI000_V.txt',
    'Earthquake_88_(Northridge-06)_RSN1691\RSN1691_NORTH392_ACI270_V.txt'
]

displacementFilePaths_quake88 = [
    'Earthquake_88_(Northridge-06)_RSN1691\RSN1691_NORTH392_ACI000_D.txt',
    'Earthquake_88_(Northridge-06)_RSN1691\RSN1691_NORTH392_ACI270_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake88)):
    component_results = process_component(accelerationFilePaths_quake88[i], velocityFilePaths_quake88[i], displacementFilePaths_quake88[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 88'
name = 'Northridge-06'
record_sequence_number = 1691
earthquake_station = 'Anacapa Island'

# Function to print the results in the desired format
def print_earthquake88_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake88_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 89 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake89
accelerationFilePaths_quake89 = [
    'Earthquake_89_(San Juan Bautista)_RSN1756\RSN1756_SANJUAN_CHA090_A.txt',
    'Earthquake_89_(San Juan Bautista)_RSN1756\RSN1756_SANJUAN_CHA180_A.txt',
    'Earthquake_89_(San Juan Bautista)_RSN1756\RSN1756_SANJUAN_CHA-UP_A.txt'
]

velocityFilePaths_quake89 = [
    'Earthquake_89_(San Juan Bautista)_RSN1756\RSN1756_SANJUAN_CHA090_V.txt',
    'Earthquake_89_(San Juan Bautista)_RSN1756\RSN1756_SANJUAN_CHA180_V.txt',
    'Earthquake_89_(San Juan Bautista)_RSN1756\RSN1756_SANJUAN_CHA-UP_V.txt'
]

displacementFilePaths_quake89 = [
    'Earthquake_89_(San Juan Bautista)_RSN1756\RSN1756_SANJUAN_CHA090_D.txt',
    'Earthquake_89_(San Juan Bautista)_RSN1756\RSN1756_SANJUAN_CHA180_D.txt',
    'Earthquake_89_(San Juan Bautista)_RSN1756\RSN1756_SANJUAN_CHA-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake89)):
    component_results = process_component(accelerationFilePaths_quake89[i], velocityFilePaths_quake89[i], displacementFilePaths_quake89[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 89'
name = 'San Juan Bautista'
record_sequence_number = 1756
earthquake_station = 'Hollister - City Hall Annex'

# Function to print the results in the desired format
def print_earthquake89_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake89_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 90 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake90
accelerationFilePaths_quake90 = [
    'Earthquake_90_(Hector Mine)_RSN1759\RSN1759_HECTOR_IMH090_A.txt',
    'Earthquake_90_(Hector Mine)_RSN1759\RSN1759_HECTOR_IMH180_A.txt',
    'Earthquake_90_(Hector Mine)_RSN1759\RSN1759_HECTOR_IMH-UP_A.txt'
]

velocityFilePaths_quake90 = [
    'Earthquake_90_(Hector Mine)_RSN1759\RSN1759_HECTOR_IMH090_V.txt',
    'Earthquake_90_(Hector Mine)_RSN1759\RSN1759_HECTOR_IMH180_V.txt',
    'Earthquake_90_(Hector Mine)_RSN1759\RSN1759_HECTOR_IMH-UP_V.txt'
]

displacementFilePaths_quake90 = [
    'Earthquake_90_(Hector Mine)_RSN1759\RSN1759_HECTOR_IMH090_D.txt',
    'Earthquake_90_(Hector Mine)_RSN1759\RSN1759_HECTOR_IMH180_D.txt',
    'Earthquake_90_(Hector Mine)_RSN1759\RSN1759_HECTOR_IMH-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake90)):
    component_results = process_component(accelerationFilePaths_quake90[i], velocityFilePaths_quake90[i], displacementFilePaths_quake90[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 90'
name = 'Hector Mine'
record_sequence_number = 1759
earthquake_station = '12440 Imperial Hwy, North Grn'

# Function to print the results in the desired format
def print_earthquake90_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake90_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 65 to Earthquake 90 --------------------------------

# ------------------------------------- Beginning of Earthquake91 to Earthqauke100 --------------------------------
# ------------------------------------- Earthquake 91 --------------------------------------------------
accelerationFilePaths_quake91 = [
    'Earthquake_91_(Yountville)_RSN1843\RSN1843_YOUNTVL_A02090_A.txt',
    'Earthquake_91_(Yountville)_RSN1843\RSN1843_YOUNTVL_A02360_A.txt',
    'Earthquake_91_(Yountville)_RSN1843\RSN1843_YOUNTVL_A02-UP_A.txt'
]

velocityFilePaths_quake91 = [
    'Earthquake_91_(Yountville)_RSN1843\RSN1843_YOUNTVL_A02090_V.txt',
    'Earthquake_91_(Yountville)_RSN1843\RSN1843_YOUNTVL_A02360_V.txt',
    'Earthquake_91_(Yountville)_RSN1843\RSN1843_YOUNTVL_A02-UP_V.txt'
]

displacementFilePaths_quake91 = [
    'Earthquake_91_(Yountville)_RSN1843\RSN1843_YOUNTVL_A02090_D.txt',
    'Earthquake_91_(Yountville)_RSN1843\RSN1843_YOUNTVL_A02360_D.txt',
    'Earthquake_91_(Yountville)_RSN1843\RSN1843_YOUNTVL_A02-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake91)):
    component_results = process_component(accelerationFilePaths_quake91[i], velocityFilePaths_quake91[i], displacementFilePaths_quake91[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 91'
name = 'Yountville'
record_sequence_number = 1843
earthquake_station = 'APEEL 2 - Redwood City'

# Function to print the results in the desired format
def print_earthquake91_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 


# Assuming results are stored in 'results' list as before
print_earthquake91_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 92 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake92
accelerationFilePaths_quake92 = [
    'Earthquake_92_(Big Bear-02)_RSN1868\RSN1868_BEARAFT_788BY090_A.txt',
    'Earthquake_92_(Big Bear-02)_RSN1868\RSN1868_BEARAFT_788BY360_A.txt',
    'Earthquake_92_(Big Bear-02)_RSN1868\RSN1868_BEARAFT_788BY-UP_A.txt'
]

velocityFilePaths_quake92 = [
    'Earthquake_92_(Big Bear-02)_RSN1868\RSN1868_BEARAFT_788BY090_V.txt',
    'Earthquake_92_(Big Bear-02)_RSN1868\RSN1868_BEARAFT_788BY360_V.txt',
    'Earthquake_92_(Big Bear-02)_RSN1868\RSN1868_BEARAFT_788BY-UP_V.txt'
]

displacementFilePaths_quake92 = [
    'Earthquake_92_(Big Bear-02)_RSN1868\RSN1868_BEARAFT_788BY090_D.txt',
    'Earthquake_92_(Big Bear-02)_RSN1868\RSN1868_BEARAFT_788BY360_D.txt',
    'Earthquake_92_(Big Bear-02)_RSN1868\RSN1868_BEARAFT_788BY-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake92)):
    component_results = process_component(accelerationFilePaths_quake92[i], velocityFilePaths_quake92[i], displacementFilePaths_quake92[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 92'
name = 'Big Bear-02'
record_sequence_number = 1868
earthquake_station = 'Colton - Hospital Complex FF'

# Function to print the results in the desired format
def print_earthquake92_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake92_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 93 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake93
accelerationFilePaths_quake93 = [
    'Earthquake_93_(Anza-02)_RSN1917\RSN1917_ANZA1_02467090_A.txt',
    'Earthquake_93_(Anza-02)_RSN1917\RSN1917_ANZA1_02467360_A.txt',
    'Earthquake_93_(Anza-02)_RSN1917\RSN1917_ANZA1_02467-UP_A.txt'
]

velocityFilePaths_quake93 = [
    'Earthquake_93_(Anza-02)_RSN1917\RSN1917_ANZA1_02467090_V.txt',
    'Earthquake_93_(Anza-02)_RSN1917\RSN1917_ANZA1_02467360_V.txt',
    'Earthquake_93_(Anza-02)_RSN1917\RSN1917_ANZA1_02467-UP_V.txt'
]

displacementFilePaths_quake93 = [
    'Earthquake_93_(Anza-02)_RSN1917\RSN1917_ANZA1_02467090_D.txt',
    'Earthquake_93_(Anza-02)_RSN1917\RSN1917_ANZA1_02467360_D.txt',
    'Earthquake_93_(Anza-02)_RSN1917\RSN1917_ANZA1_02467-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake93)):
    component_results = process_component(accelerationFilePaths_quake93[i], velocityFilePaths_quake93[i], displacementFilePaths_quake93[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 93'
name = 'Anza-02'
record_sequence_number = 1917
earthquake_station = 'Alpine Fire Station'

# Function to print the results in the desired format
def print_earthquake93_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake93_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 94 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake94
accelerationFilePaths_quake94 = [
    'Earthquake_94_(Gulf of California)_RSN1990\RSN1990_GULFCA_BCR090_A.txt',
    'Earthquake_94_(Gulf of California)_RSN1990\RSN1990_GULFCA_BCR360_A.txt',
    'Earthquake_94_(Gulf of California)_RSN1990\RSN1990_GULFCA_BCR-UP_A.txt'
]

velocityFilePaths_quake94 = [
    'Earthquake_94_(Gulf of California)_RSN1990\RSN1990_GULFCA_BCR090_V.txt',
    'Earthquake_94_(Gulf of California)_RSN1990\RSN1990_GULFCA_BCR360_V.txt',
    'Earthquake_94_(Gulf of California)_RSN1990\RSN1990_GULFCA_BCR-UP_V.txt'
]

displacementFilePaths_quake94 = [
    'Earthquake_94_(Gulf of California)_RSN1990\RSN1990_GULFCA_BCR090_D.txt',
    'Earthquake_94_(Gulf of California)_RSN1990\RSN1990_GULFCA_BCR360_D.txt',
    'Earthquake_94_(Gulf of California)_RSN1990\RSN1990_GULFCA_BCR-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake94)):
    component_results = process_component(accelerationFilePaths_quake94[i], velocityFilePaths_quake94[i], displacementFilePaths_quake94[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 94'
name = 'Gulf of California'
record_sequence_number = 1990
earthquake_station = 'Bonds Corner'

# Function to print the results in the desired format
def print_earthquake94_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake94_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 95 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake95
accelerationFilePaths_quake95 = [
    'Earthquake_95_(CABaja Border Area)_RSN2002\RSN2002_CABAJA_BRA090_A.txt',
    'Earthquake_95_(CABaja Border Area)_RSN2002\RSN2002_CABAJA_BRA360_A.txt',
    'Earthquake_95_(CABaja Border Area)_RSN2002\RSN2002_CABAJA_BRA-UP_A.txt'
]

velocityFilePaths_quake95 = [
    'Earthquake_95_(CABaja Border Area)_RSN2002\RSN2002_CABAJA_BRA090_V.txt',
    'Earthquake_95_(CABaja Border Area)_RSN2002\RSN2002_CABAJA_BRA360_V.txt',
    'Earthquake_95_(CABaja Border Area)_RSN2002\RSN2002_CABAJA_BRA-UP_V.txt'
]

displacementFilePaths_quake95 = [
    'Earthquake_95_(CABaja Border Area)_RSN2002\RSN2002_CABAJA_BRA090_D.txt',
    'Earthquake_95_(CABaja Border Area)_RSN2002\RSN2002_CABAJA_BRA360_D.txt',
    'Earthquake_95_(CABaja Border Area)_RSN2002\RSN2002_CABAJA_BRA-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake95)):
    component_results = process_component(accelerationFilePaths_quake95[i], velocityFilePaths_quake95[i], displacementFilePaths_quake95[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 95'
name = 'CA/Baja Border Area'
record_sequence_number = 2002
earthquake_station = 'Brawley Airport'

# Function to print the results in the desired format
def print_earthquake95_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake95_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 96 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake96
accelerationFilePaths_quake96 = [
    'Earthquake_96_(Gilroy)_RSN2011\RSN2011_GILROY2_OFS180_A.txt',
    'Earthquake_96_(Gilroy)_RSN2011\RSN2011_GILROY2_OFS270_A.txt',
    'Earthquake_96_(Gilroy)_RSN2011\RSN2011_GILROY2_OFS-UP_A.txt'
]

velocityFilePaths_quake96 = [
    'Earthquake_96_(Gilroy)_RSN2011\RSN2011_GILROY2_OFS180_V.txt',
    'Earthquake_96_(Gilroy)_RSN2011\RSN2011_GILROY2_OFS270_V.txt',
    'Earthquake_96_(Gilroy)_RSN2011\RSN2011_GILROY2_OFS-UP_V.txt'
]

displacementFilePaths_quake96 = [
    'Earthquake_96_(Gilroy)_RSN2011\RSN2011_GILROY2_OFS180_D.txt',
    'Earthquake_96_(Gilroy)_RSN2011\RSN2011_GILROY2_OFS270_D.txt',
    'Earthquake_96_(Gilroy)_RSN2011\RSN2011_GILROY2_OFS-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake96)):
    component_results = process_component(accelerationFilePaths_quake96[i], velocityFilePaths_quake96[i], displacementFilePaths_quake96[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 96'
name = 'Gilroy'
record_sequence_number = 2011
earthquake_station = 'Alameda - Oakland Airport FS #4'

# Function to print the results in the desired format
def print_earthquake96_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake96_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 97 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake97
accelerationFilePaths_quake97 = [
    'Earthquake_97_(Yorba Linda)_RSN2047\RSN2047_YLINDA_13066025_A.txt', 
    'Earthquake_97_(Yorba Linda)_RSN2047\RSN2047_YLINDA_13066115_A.txt', 
    'Earthquake_97_(Yorba Linda)_RSN2047\RSN2047_YLINDA_13066-UP_A.txt'
]

velocityFilePaths_quake97 = [
    'Earthquake_97_(Yorba Linda)_RSN2047\RSN2047_YLINDA_13066025_V.txt', 
    'Earthquake_97_(Yorba Linda)_RSN2047\RSN2047_YLINDA_13066115_V.txt', 
    'Earthquake_97_(Yorba Linda)_RSN2047\RSN2047_YLINDA_13066-UP_V.txt'
]

displacementFilePaths_quake97 = [
    'Earthquake_97_(Yorba Linda)_RSN2047\RSN2047_YLINDA_13066025_D.txt', 
    'Earthquake_97_(Yorba Linda)_RSN2047\RSN2047_YLINDA_13066115_D.txt', 
    'Earthquake_97_(Yorba Linda)_RSN2047\RSN2047_YLINDA_13066-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake97)):
    component_results = process_component(accelerationFilePaths_quake97[i], velocityFilePaths_quake97[i], displacementFilePaths_quake97[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 97'
name = 'Yorba Linda'
record_sequence_number = 2047
earthquake_station = 'Anaheim - Brookhurst & Crescent'

# Function to print the results in the desired format
def print_earthquake97_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake97_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 98 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake98
accelerationFilePaths_quake98 = [
    'Earthquake_98_(Big Bear City)_RSN2119\RSN2119_BEARCTY_TRF090_A.txt',
    'Earthquake_98_(Big Bear City)_RSN2119\RSN2119_BEARCTY_TRF360_A.txt',
    'Earthquake_98_(Big Bear City)_RSN2119\RSN2119_BEARCTY_TRF-UP_A.txt'
]

velocityFilePaths_quake98 = [
    'Earthquake_98_(Big Bear City)_RSN2119\RSN2119_BEARCTY_TRF090_V.txt',
    'Earthquake_98_(Big Bear City)_RSN2119\RSN2119_BEARCTY_TRF360_V.txt',
    'Earthquake_98_(Big Bear City)_RSN2119\RSN2119_BEARCTY_TRF-UP_V.txt'
]

displacementFilePaths_quake98 = [
    'Earthquake_98_(Big Bear City)_RSN2119\RSN2119_BEARCTY_TRF090_D.txt',
    'Earthquake_98_(Big Bear City)_RSN2119\RSN2119_BEARCTY_TRF360_D.txt',
    'Earthquake_98_(Big Bear City)_RSN2119\RSN2119_BEARCTY_TRF-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake98)):
    component_results = process_component(accelerationFilePaths_quake98[i], velocityFilePaths_quake98[i], displacementFilePaths_quake98[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 98'
name = 'Big Bear City'
record_sequence_number = 2119
earthquake_station = 'Anza - Tripp Flats Training'

# Function to print the results in the desired format
def print_earthquake98_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake98_info(title, name, record_sequence_number, earthquake_station, results)
# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 99 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake99
accelerationFilePaths_quake99 = [
    'Earthquake_99_(Whittier Narrows-02)_RSN3684\RSN3684_WHITTIER.B_B-WBA000_A.txt',
    'Earthquake_99_(Whittier Narrows-02)_RSN3684\RSN3684_WHITTIER.B_B-WBA090_A.txt',
    'Earthquake_99_(Whittier Narrows-02)_RSN3684\RSN3684_WHITTIER.B_B-WBA-UP_A.txt'
]

velocityFilePaths_quake99 = [
    'Earthquake_99_(Whittier Narrows-02)_RSN3684\RSN3684_WHITTIER.B_B-WBA000_V.txt',
    'Earthquake_99_(Whittier Narrows-02)_RSN3684\RSN3684_WHITTIER.B_B-WBA090_V.txt',
    'Earthquake_99_(Whittier Narrows-02)_RSN3684\RSN3684_WHITTIER.B_B-WBA-UP_V.txt'
]

displacementFilePaths_quake99 = [
    'Earthquake_99_(Whittier Narrows-02)_RSN3684\RSN3684_WHITTIER.B_B-WBA000_D.txt',
    'Earthquake_99_(Whittier Narrows-02)_RSN3684\RSN3684_WHITTIER.B_B-WBA090_D.txt',
    'Earthquake_99_(Whittier Narrows-02)_RSN3684\RSN3684_WHITTIER.B_B-WBA-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake99)):
    component_results = process_component(accelerationFilePaths_quake99[i], velocityFilePaths_quake99[i], displacementFilePaths_quake99[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))
    
# Given metadata for the earthquake
title = 'Earthquake 99'
name = 'Whittier Narrows-02'
record_sequence_number = 3684
earthquake_station = 'Anaheim - W Ball Rd'

# Function to print the results in the desired format
def print_earthquake99_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake99_info(title, name, record_sequence_number, earthquake_station, results)

# -----------------------------------------------------------------------------------------------------

# ------------------------------------- Earthquake 100 --------------------------------------------------
# Assuming file paths are given and exist
# Earthquake100
accelerationFilePaths_quake100 = [
    'Earthquake_100_(Cape Mendocino)_RSN3744\RSN3744_CAPEMEND_BNH270_A.txt',
    'Earthquake_100_(Cape Mendocino)_RSN3744\RSN3744_CAPEMEND_BNH360_A.txt',
    'Earthquake_100_(Cape Mendocino)_RSN3744\RSN3744_CAPEMEND_BNH-UP_A.txt'
]

velocityFilePaths_quake100 = [
    'Earthquake_100_(Cape Mendocino)_RSN3744\RSN3744_CAPEMEND_BNH270_V.txt',
    'Earthquake_100_(Cape Mendocino)_RSN3744\RSN3744_CAPEMEND_BNH360_V.txt',
    'Earthquake_100_(Cape Mendocino)_RSN3744\RSN3744_CAPEMEND_BNH-UP_V.txt'
]

displacementFilePaths_quake100 = [
    'Earthquake_100_(Cape Mendocino)_RSN3744\RSN3744_CAPEMEND_BNH270_D.txt',
    'Earthquake_100_(Cape Mendocino)_RSN3744\RSN3744_CAPEMEND_BNH360_D.txt',
    'Earthquake_100_(Cape Mendocino)_RSN3744\RSN3744_CAPEMEND_BNH-UP_D.txt'
]
dt = 0.005

# Process each component
components = ["First Horizontal Component", "Second Horizontal Component", "Vertical Component"]
results = []

# Adjust the loop to iterate based on the length of one of the file path lists
for i in range(len(accelerationFilePaths_quake100)):
    component_results = process_component(accelerationFilePaths_quake100[i], velocityFilePaths_quake100[i], displacementFilePaths_quake100[i], dt)
    # Dynamically create a component name if needed or use a placeholder
    component_name = components[i] if i < len(components) else f"Component {i+1}"
    results.append((component_name, component_results))

    
# Given metadata for the earthquake
title = 'Earthquake 100'
name = 'Cape Mendocino'
record_sequence_number = 3744
earthquake_station = 'Bunker Hill FAA'

# Function to print the results in the desired format
def print_earthquake100_info(title, name, record_sequence_number, earthquake_station, results):
    print(f"Title: '{title}'")
    print(f"Earthquake Name: '{name}'")
    print(f"Record Sequence Number: {record_sequence_number}")
    print(f"Earthquake Station: '{earthquake_station}'")
    for component, res in results:
        print(f"{component}: PGA = {res['PGA']:.8f}, PGV = {res['PGV']:.6f}, PGD = {res['PGD']:.7f}")
    print('-' * 80) 

# Assuming results are stored in 'results' list as before
print_earthquake100_info(title, name, record_sequence_number, earthquake_station, results)
# ----------------------------------- End of Earthquake 91 to Earthquake 100 --------------------------------