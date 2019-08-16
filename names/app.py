import dash
import dash_core_components as dcc
import dash_html_components as html

# import plotly.plotly as py
import pandas as pd
import plotly.graph_objects as go




app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

server = app.server
app.config.suppress_callback_exceptions = True



df = pd.read_csv("data/names.txt",header = None)
df.columns = ['year','name','gender','count']
df['decade'] = (df['year'] // 10)*10
df = df[['decade','name','count']]





df_total = df.groupby(['name'])['count'].sum()
df_total = df_total.reset_index()
# df_total = df_total.transpose()




df = df.groupby(['decade','name'])['count'].sum()
df = df.reset_index()



df_min = df.groupby(['name'])['count'].min()
df_min = df_min.reset_index()

df_max = df.groupby(['name'])['count'].max()
df_max = df_max.reset_index()

decade = df.groupby(['decade'])['count'].sum()
decade = decade.reset_index()
decade = decade['decade']
decade = decade.values.tolist()


df = pd.merge(df, df_min, how = 'left', on = ['name'])
df = pd.merge(df, df_max, how = 'left', on = ['name'])

df.columns = ['decade','name','cnt','min','max']

df['nrml'] = (df['cnt'] - df['min']) / (df['max'] - df['min'])




df = df.pivot_table(index = 'name', columns = 'decade')['nrml']

# print( df[(df['name'] == 'Mary')])




df = df.dropna()

df = df.reset_index()

df = df[(df[1920] >= .8) & (df[1980] >= .8)]


x = df.columns[1:].tolist()
y = df['name'].tolist()

z = df[decade]
z = z.values
# print(z)

# print(df[df['name'] == 'Lula'].transpose())


# fig = go.Figure(data=go.Heatmap(
#                    z=z,
#                    x=x,
#                    y=y))

# fig.show()







app.layout = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            # children=[html.Img(src=app.get_asset_url("https://dunhamweb.com/wp-content/uploads/banner-sample.png"))],
            children=[html.Img(src="https://dunhamweb.com/wp-content/uploads/banner-sample.png")],
        ),
        # Left column
        html.Div(
            id="left-column",
            className="four columns",
            children="Hello"
            # children=[description_card(), generate_control_card()]
            # + [
            #     html.Div(
            #         ["initial child"], id="output-clientside", style={"display": "none"}
            #     )
            # ],
        ),
        # Right column
        html.Div(
            id="right-column",
            className="eight columns",
            children=[
                # Patient Volume Heatmap
                html.Div(
                    id="patient_volume_card",
                    children=[
                        html.B("Patient Volume"),
                        html.Hr(),
                        dcc.Graph(id="patient_volume_hm"),
                    ],
                ),
                # Patient Wait time by Department
                html.Div(
                    id="wait_time_card",
                    children=[
                        html.B("Patient Wait Time and Satisfactory Scores"),
                        html.Hr(),
                        # html.Div(id="wait_time_table", children=initialize_table()),
                    ],
                ),
            ],
        ),
    ],
)









# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)