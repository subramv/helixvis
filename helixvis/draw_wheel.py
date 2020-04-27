import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as pltcol
import matplotlib.patches as mpatches
from matplotlib.patches import Arc
import math
pd.options.mode.chained_assignment = None

def draw_wheel(sequence, colors = ["gray", "yellow", "blue", "red"], labels = False, labelcolor = "black", legend = False):
    "draw helix"
    min_num = 2
    max_num = 18
    num_colors = 4
    num_resid = len(sequence)
    # 0 = hydrophobic, 1 = polar, 2 = basic, 3 = acidic
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
        'y': y_center[0:num_resid], 'color': range(num_resid), 'type': range(num_resid)})
    for i in range(num_resid):
        if sequence[i] not in residues:
            return "ERROR: " + sequence[i] + " is not a valid one-letter code for an amino acid."
        circle_data['color'][i] = colors[residues[sequence[i]]]
        circle_data['type'][i] = residues[sequence[i]]
        
    segment_data = pd.DataFrame(data={'xstart': x_center[0:num_resid - 1], 
        'ystart': y_center[0:num_resid - 1], 'xend': x_center[1:num_resid], 
        'yend': y_center[1:num_resid]})
    fig, ax = plt.subplots()
    for i in range(num_resid - 1):
        plt.plot([segment_data['xstart'][i], segment_data['xend'][i]], [segment_data['ystart'][i], segment_data['yend'][i]], 'ro-', color = 'black')
        
    for i in range(num_resid):
        circle = plt.Circle((circle_data['x'][i], circle_data['y'][i]), circle_radius, clip_on = False, zorder = 10, facecolor=circle_data['color'][i], edgecolor = 'black')
        ax.add_artist(circle)
        if labels:
            ax.annotate(sequence[i], xy=(circle_data['x'][i], circle_data['y'][i]), zorder = 15, fontsize=10, ha="center", va = "center", color = labelcolor)
        
        
    if legend:
        restypes = set(circle_data['type'])
        handleid = []
        nonpolar = mpatches.Patch(color = colors[0], label = 'hydrophobic')
        polar = mpatches.Patch(color = colors[1], label = 'polar')
        basic = mpatches.Patch(color = colors[2], label = 'basic')
        acidic = mpatches.Patch(color = colors[3], label = 'acidic')
        if 0 in restypes:
            handleid = [nonpolar]
            
        if 1 in restypes:
            if bool(handleid):
                handleid.append(polar)
            else:
                handleid = [polar]
                
        if 2 in restypes:
            if bool(handleid):
                handleid.append(basic)
            else:
                handleid = [basic]
        
        if 3 in restypes:
            if bool(handleid):
                handleid.append(acidic)
            else:
                handleid = [acidic]
                
        plt.legend(handles = handleid, loc='center left', bbox_to_anchor=(1.04, 0.5))
        
    plt.axis('off')
    ax.set_aspect('equal')
    return fig, ax