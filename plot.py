import plotly.graph_objects as go
import pandas as pd

def plot_choropleth(feature, text, colorbar_title, title, colorscale):
	'''
	plot choropleth map for given feature
	'''
	fig = go.Figure(data=go.Choropleth(
	    locations = pd.read_csv('topics.csv')['code'],
	    z = feature, # heat['total video'],
	    text = text, # topics['title'],
	    colorscale = colorscale, # 'Reds',
	    autocolorscale=False,
	    reversescale=False,
	    marker_line_color='black',
	    marker_line_width=0.5,
	    colorbar_tickprefix = '',
	    colorbar_title = colorbar_title, # 'Totoal Videos',
	))

	fig.update_layout(
	    title_text=title, #"2019 US Media's Attension",
	    geo=dict(
	        showframe=False,
	        showcoastlines=False,
	        projection_type='equirectangular'
	    ),
	)

	fig.show()