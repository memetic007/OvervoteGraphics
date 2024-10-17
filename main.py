import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import Utils
import os


Utils.clear_terminal()

# Sample data: list of tuples (string, number between -100.0 and 100.0)
# Define the directory and filename
default_directory = r"c:\OverVoteData"

# Prompt the user for the filename
filename = input("Please enter the filename (e.g., ByOvervote.csv): ")

# Prompt the user for the header
header = input("Please enter the title for the plot: ")

full_path = os.path.join(default_directory, filename)

# Combine directory and filename


data = Utils.read_data_from_csv(full_path)

# Extract labels and values from data
labels = [item[0] for item in data]
values = [item[1] for item in data]

# Positions for the bars on the y-axis 
y_positions = np.arange(len(labels))

# Determine colors based on positive or negative values
colors = ['blue' if value <= 0 else 'red' for value in values]

# Create the plot
plt.figure(figsize=(6, len(labels) * 0.3))
plt.barh(y_positions, values, align='center', color=colors)

# Set labels and ticks
plt.yticks(y_positions, labels)
plt.xlim(-6000000, 6000000)
plt.xticks(np.arange(-6000000, 6000001, 1000000))

# Custom formatter to display absolute value of ticks in millions
def millions(x, pos):
    return f'{abs(int(x / 1_000_000))}'

formatter = mticker.FuncFormatter(millions)
plt.gca().xaxis.set_major_formatter(formatter)

plt.grid(axis='x', linestyle='--', color='gray', alpha=0.7)

# Invert y-axis to have the first item on top
plt.gca().invert_yaxis()

# Labels and title
plt.xlabel('In Millions', labelpad=10)
plt.title(header, pad=20)  # Set the plot title to the user-provided header

# Adjust layout to prevent clipping
plt.tight_layout()

# Save the plot as a PNG file
rootname, _ = os.path.splitext(filename)  # Extract the root name from the filename
png_filename = f"{rootname}.png"  # Create the PNG filename
png_full_path = os.path.join(default_directory, png_filename)  # Full path for the PNG file
plt.savefig(png_full_path)  # Save the plot

print(f"Plot saved as {png_full_path}")

# Show the plot
plt.show()

print ("ending program")
