from application import app 
from flask import render_template, url_for 
import pandas as pd 
import json 
import plotly 
import plotly.express as px

@app.route("/")
def index():
    
    #Graph One 
    import plotly.graph_objects as go
    import pandas as pd

    # Human Capital Index Interactive Choropleth Map
    df = pd.read_csv('/Users/johnle/Downloads/hci_code.csv')

    fig1 = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        z = df['HUMAN CAPITAL INDEX 2020'],
        text = df['COUNTRY'],
        colorscale = 'agsunset',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title = 'HCI Score (0-1)',
    ))

    fig1.update_layout(
        title_text='Human Capital Index (HCI) 2020 Across the World', 
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
    )
    
    graph1JSON = json.dumps(fig1, cls =plotly.utils.PlotlyJSONEncoder)
    
    #Graph Two 
    
    import plotly.graph_objects as go
    import pandas as pd

    df = pd.read_csv('/Users/johnle/Downloads/gdp_code.csv')

    fig2 = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        z = df['GDP PER CAPITA 2020'],
        text = df['COUNTRY'],
        colorscale = 'electric',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_tickprefix = '$',
        colorbar_title = 'GDP Per Capita',
    ))

    fig2.update_layout(
        title_text='Gross Domestic Product (GDP) Per Capita 2020 Across the World', 
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
    )
    
    graph2JSON = json.dumps(fig2, cls =plotly.utils.PlotlyJSONEncoder)
    
    # Graph Three
    import plotly.graph_objects as go
    import pandas as pd

    # GDP Predicted Interactive Choropleth Map
    df= pd.read_csv('/Users/johnle/Downloads/gdp_predicted.csv')

    fig3 = go.Figure(data=go.Choropleth(
        locations = df['CODE'],
        z = df['PERCENTAGE ERROR'],
        text = df['COUNTRY'],
        colorscale = [[0, 'green'], [0.1, 'yellow'], [1, 'red']],
        autocolorscale=False,
        reversescale=False,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title = 'GDP Per Capita Percentage Error',
        zmin = 0,
        zmax = 10
    ))
    fig3.update_layout(
        title_text='Predicted GDP Per Capita 2020 Percentage Error Across the World', 
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
    )
    
    graph3JSON = json.dumps(fig3, cls =plotly.utils.PlotlyJSONEncoder)
    
    # Graph Four
    df = pd.read_csv('/Users/johnle/Desktop/School/Projects/DS4002/final_df_country.csv')
    fig4 = px.scatter_3d(df, x ="Harmonized Test Scores", y = "HUMAN CAPITAL INDEX 2020", z ="2020", 
                         color = "Region_encoded", hover_name = "Country Name", title="3D Scatterplot")
    
    
    
    graph4JSON = json.dumps(fig4, cls =plotly.utils.PlotlyJSONEncoder)
    
    
    
    #Rendering
    return render_template("index.html", title = "Home", graph1JSON = graph1JSON, graph2JSON = graph2JSON, graph3JSON = graph3JSON, graph4JSON = graph4JSON)