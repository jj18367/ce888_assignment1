import numpy as np
#import panda as pd
import matplotlib.pyplot as plt

# Open the data file in reading mode
f = open("flags_dataset/flag.data", "r+")

# Save the information in the data variable
data = f.read()

# Show de data on the screen
print(data)

f.close # Close the data file