import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as pltcol
from matplotlib.patches import Arc
import math
pd.options.mode.chained_assignment = None

def draw_wheel(sequence, colors = ["gray", "yellow", "blue", "red"], showplot = False):
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
    if showplot:
        plt.show()
    
    return fig, ax

def draw_wenxiang(sequence, colors = ["gray", "yellow", "blue", "red"], showplot = False):
    "draw wenxiang"
    min_num = 2
    max_num = 18
    num_colors = 4
    circle_radius = 0.04
    num_resid = len(sequence)
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
            
    between_distance = 0.042
    start_radius = 0.0625
    CENTER_Y = 0.5
    CENTER_X = 0.52
    df_spiral = pd.DataFrame(data={'end_angle': [90, 270] * 5, 'start_angle': [270, 90] * 5, 
        'center_y': [CENTER_Y, CENTER_Y + between_distance] * 5, 'center_x': [CENTER_X]* 10, 'radius': start_radius}) 
    df_spiral['start_angle'][9] = 190
    for i in range(10):
        df_spiral['radius'][i] = start_radius + i* between_distance
        
    #df_resid = pd.DataFrame(data={'y': df_spiral['center_y'] + df_spiral['radius'] * math.sin(100*math.pi/180), 'x': df_spiral['center_x'] + df_spiral['radius'] * math.cos(100*math.pi/180), 'color': 'blue', 'lettername': 'a'})  
    df_resid = pd.DataFrame(data ={'y': np.array([0.5625, 0.4891, 0.4438, 
        0.5943, 0.6122, 0.3878, 0.4478, 0.7191, 0.54, 0.2695, 
        0.5893, 0.7955, 0.3428, 0.2689, 0.8151, 0.6993, 0.1255, 
        0.4655]), 'x': np.array([0.52, 0.5816, 0.4843, 0.4295, 0.6142, 
        0.6142, 0.3568, 0.4555, 0.747, 0.52, 0.2516, 0.6276, 
        0.7924, 0.2908, 0.2908, 0.8651, 0.6563, 0.0862]), 'color': 'blue', 'lettername': 'a'})
    df_resid = df_resid.iloc[range(num_resid)]
    resid_spiral = np.array([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 10])    
    df_spiral = df_spiral.iloc[range(resid_spiral[num_resid-1])]
    df_spiral['start_angle'][len(df_spiral)-1] = (df_spiral['end_angle'][len(df_spiral)-1] - (num_resid-1) * 100 + 180 * (resid_spiral[num_resid-1]-1))% 360        
    for i in range(num_resid):
        if sequence[i] not in residues:
            return "ERROR: " + sequence[i] + " is not a valid one-letter code for an amino acid."
        df_resid['color'][i] = colors[residues[sequence[i]]]
        df_resid['lettername'][i] = sequence[i]
    
    fig, ax = plt.subplots()
    for i in range(resid_spiral[num_resid-1]):
        ax.add_patch(Arc((df_spiral['center_x'][i], df_spiral['center_y'][i]), 2*df_spiral['radius'][i], 2*df_spiral['radius'][i], theta1 = df_spiral['start_angle'][i], theta2 = df_spiral['end_angle'][i]))     

    for i in range(num_resid):
        circle = plt.Circle((df_resid['x'][i], df_resid['y'][i]), circle_radius, clip_on = False, zorder = 10, facecolor=df_resid['color'][i], edgecolor = 'black')
        ax.add_artist(circle)
    
    plt.axis('off')
    if showplot:
        plt.show()
    
    return fig, ax
    