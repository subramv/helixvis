import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as pltcol

def draw_wheel(sequence, colors = ["gray", "yellow", "blue", "red"]):
    "draw helix"
    min_num = 2
    max_num = 18
    num_colors = 4
    num_resid = len(sequence)
    # 0 = nonpolar, 1 = polar, 2 = basic, 3 = acidic
    residues = {"A":0, "R":2, "N":1, "D":3, "C":1,
                  "Q":1, "E":3, "G":0, "H":2, "I":0,
                  "L":0, "K":2, "M":0, "F":0, "P":0,
                  "S":1, "T":1, "W":0, "Y":0, "V":0}
        
    if num_resid not in range(min_num, max_num + 1):
        return "ERROR: sequence must have between 2 and 18 (inclusive) characters."
    if len(colors) != 4:
        return "ERROR: parameter `colors` has missing or too many colors."
    for i in range(len(colors)):
        if colors[i] not in pltcol.cnames:
            return "ERROR: parameter `colors` has invalid colors." 

    x_center = np.array([0, 0.8371, -0.2907, -0.7361, 0.5464, 0.5464, 
        -0.7361, -0.2907, 0.8371, 0, -0.8371, 0.2907, 0.7361, 
        -0.5464, -0.5464, 0.7361, 0.2907, -0.8371], dtype = 'f')
    y_center = np.array([0.85, -0.1476, -0.7987, 0.425, 0.6511, -0.6511, 
        -0.425, 0.7987, 0.1476, -0.85, 0.1476, 0.7987, -0.425, 
        -0.6511, 0.6511, 0.425, -0.7987, -0.1476], dtype = 'f')
    x_center = x_center/2 + 0.5
    y_center = y_center/2 + 0.5
    circle_radius = 0.0725
    circle_data = pd.DataFrame(data={'x': x_center[0:num_resid], 
        'y': y_center[0:num_resid], 'color': range(num_resid)})
    for i in range(num_resid):
        if sequence[i] not in residues:
            return "ERROR: " + sequence[i] + " is not a valid one-letter code for an amino acid."
        circle_data['color'][i] = colors[residues[sequence[i]]]
        
    segment_data = pd.DataFrame(data={'xstart': x_center[0:num_resid - 1], 
        'ystart': y_center[0:num_resid - 1], 'xend': x_center[1:num_resid], 
        'yend': y_center[1:num_resid]})
    fig, ax = plt.subplots()
    for i in range(num_resid - 1):
        plt.plot([segment_data['xstart'][i], segment_data['xend'][i]], [segment_data['ystart'][i], segment_data['yend'][i]], 'ro-', color = 'black')
        
    for i in range(num_resid):
        circle = plt.Circle((circle_data['x'][i], circle_data['y'][i]), circle_radius, clip_on = False, zorder = 10, facecolor=circle_data['color'][i], edgecolor = 'black')
        ax.add_artist(circle)
        
    plt.axis('off')
    plt.show()
    
    return fig, ax
    