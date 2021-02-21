"""
This module tracks in real time the ISS and shows the position.

Author: Ziliotto Filippo 
GitHub: ZiliottoFilippoDev
"""

__author__ = "Ziliotto Filippo"
__email__ = "filippo.ziliotto1996@gmail.com"
__status__ = "planning"


import urllib.request 
import json
import pandas as pd 
import plotly.express as px
from time import gmtime, strftime

def track_iss():
    global time, location

    #import current time
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    time

    #request API of the ISS and create a smallDataframe
    req = urllib.request.Request('http://api.open-notify.org/iss-now.json')
    with urllib.request.urlopen(req) as response:
        iss_loc = response.read()
    
    location = pd.read_json(iss_loc).transpose()
    return location.transpose()


def view_iss(projection):
    #suggested projections : 'ortographic', 'natural earth'  

    #define the coordinates
    track_iss()

    #use plotly to plot the interactive earth map
    fig = px.scatter_geo(
    location, 
    lat='latitude',
    lon='longitude',
    projection=projection,
    fitbounds=False
                    )

    #update layout of the image for a better view
    fig.update_layout(geo = dict(
        countrycolor = 'rebeccapurple',
        showcountries = True),
        title = 'ISS location: {}'.format(time),
        height=700)

    fig.update_traces(
    marker=dict(size=17,color="red",symbol='128'),
    name='ISS',
    textfont=dict(color='black',size=18,family='Times New Roman'))

    fig.update_geos(
    showcoastlines=True, coastlinecolor="RebeccaPurple",
    showland=True, landcolor="lawngreen",
    showocean=True, oceancolor="Blue",
    showlakes=True, lakecolor="Blue",
    showrivers=True, rivercolor="Blue",
    lataxis_showgrid=True, lonaxis_showgrid=True,
    bgcolor='black'
    )
    fig.show()
    return