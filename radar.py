import pyart

# Load NEXRAD data using Py-ART
radar = pyart.io.read_nexrad_archive('path/to/file.gz')

# Access radar metadata
print(radar.metadata)

# Access radar fields
print(radar.fields.keys())

# Plot a PPI (Plan Position Indicator) of reflectivity data
display = pyart.graph.RadarDisplay(radar)
fig = plt.figure(figsize=[10, 8])
ax = fig.add_subplot(111)
display.plot('reflectivity', 0, vmin=-32, vmax=64, colorbar_label='Reflectivity (dBZ)')
display.set_limits(ylim=[-120, 120], xlim=[-120, 120])
plt.show()