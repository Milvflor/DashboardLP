#!/usr/bin/env python

"""
app.py

Booking App dashboard
"""
from dash import Dash, html, dcc, Input, Output
from plotly.subplots import make_subplots
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

f_dic = {}

"""
Fills the dictionary with files ended in '.csv' inside the content folder
"""


def fill_dic(folder_name="Data"):
    files_paths = (
        Path.cwd()
        .joinpath(folder_name)
        .glob(
            "*.csv",
        )
    )

    for file_path in files_paths:
        if file_path.is_file:
            file_name = str(file_path)
            dic_entry = file_name[
                file_name.find(f"/{folder_name}/") + len(f"/{folder_name}/") :
            ]
            f_dic[dic_entry] = file_name


fill_dic()

# Creating data_frames from the csv files using pandas
df_hotels = pd.read_csv(f_dic["hotels.csv"])
df_hotels = df_hotels.sort_values("score", ascending=False)
df_categories = pd.read_csv(f_dic["categories.csv"], low_memory=False)
df_surroundings = pd.read_csv(f_dic["surroundings.csv"], low_memory=False)

# Setting default fields
default_province = df_hotels.province.unique()[0]
default_category = df_categories[df_categories.province == default_province]['category'].unique()
default_hotel = df_categories[df_categories.province == default_province]['hotel'].unique()[:8]

app = Dash(
    __name__,
    external_stylesheets=[
        str(Path.cwd().joinpath("Visualization").joinpath("style.css"))
    ],
)

app.layout = html.Div(
    className="body",
    children=[
        html.Div(
            className="base",
            children=[
                html.Div(
                    className="controllers",
                    children=[
                        html.H1(
                            children="Hoteles en Ecuador",
                            style={"padding-top": "10px", "color": "#1fccff"},
                        ),
                        html.H3(
                            children="Bienvenido al Dashboard de los Hoteles de Ecuador",
                            style={"padding-top": "20px", "color": "##444444"},
                        ),
                        html.H4(
                            children="Conoce los hoteles con las mejores puntuaciones y precios que tienen algunos cantones del Ecuador, según los datos de la plataforma Booking.",
                            style={"padding-top": "20px", "color": "#424343"},
                        ),
                        html.P(
                            "Seleccione Localidad: ",
                            style={"text-align": "left", "padding-top": "20px"},
                        ),
                        dcc.Dropdown(
                            df_hotels["province"].unique(),
                            default_province,
                            id="dropdown-province",
                            className="drop-1",
                        ),
                        html.P(
                            "Seleccione Categoría: ",
                            style={"text-align": "left", "padding-top": "20px"},
                        ),
                        dcc.Dropdown(
                            options=default_category,
                            id="multidrop-category",
                            className="multidrop-category",
                            multi=True,
                        ),
                        html.P(
                            "Seleccione Hoteles: ",
                            style={"text-align": "left", "padding-top": "20px"},
                        ),
                        dcc.Dropdown(
                            options=default_hotel,
                            id="multidrop-hotel",
                            className="multidrop-hotel",
                            multi=True,
                        ),
                        html.P(
                            "Distancia de lugares más cercanos (km): ",
                            style={"text-align": "left", "padding-top": "20px"},
                        ),
                        dcc.Slider(
                            2,
                            100,
                            step=25,
                            value=0,
                            id="distance-slider",
                        ),
                    ],
                ),
                html.Div(
                    className="content",
                    children=[
                        dcc.Graph(id="price_score_graph", className="graph-1"),
                        dcc.Graph(id="categories_graph", className="graph-2"),
                        dcc.Graph(id="distance_graph", className="graph-3"),
                    ],
                ),
            ],
        ),
        html.Div(
            className="foot",
            children=[
                html.P("Autor: Milca Valdez Flores."),
                html.P("Materia: Lenguajes de Programación. Término: 2022-II"),
            ],
        ),
    ],
)


@app.callback(
    Output("price_score_graph", "figure"),
    Output("multidrop-category", "options"),
    Output("multidrop-hotel", "options"),
    Output("multidrop-category", "value"),
    Output("multidrop-hotel", "value"),
    Input("dropdown-province", "value"),
)
def update_graph(province_value):
    dff = df_hotels[df_hotels["province"] == province_value]
    categories = df_categories[df_categories["province"] == province_value][
        "category"
    ].unique()
    hotels = df_categories[df_categories["province"] == province_value][
        "hotel"
    ].unique()

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=dff["hotel"], y=dff["price"], name="Price"), secondary_y=False
    )

    fig.add_trace(
        go.Scatter(x=dff["hotel"], y=dff["score"], name="Score"),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(title_text=f"Hoteles en {province_value}")

    # Set x-axis title
    fig.update_xaxes(title_text=f"hotels")
    fig.layout.template = "plotly_dark"

    # Set y-axes titles
    fig.update_yaxes(title_text="<b>price</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>score</b>", secondary_y=True)

    return fig, categories, hotels, categories, hotels
    # hotels[0],hotels


@app.callback(
    Output("categories_graph", "figure"),
    Output("distance-slider", "min"),
    Output("distance-slider", "max"),
    Output("distance-slider", "value"),
    Output("distance-slider", "step"),
    Input("dropdown-province", "value"),
    Input("multidrop-category", "value"),
    Input("multidrop-hotel", "value"),
)
def update_graph2(province_value, categories_values, hotel_values):
    dff = df_categories[df_categories["province"] == province_value]
    dff = dff.sort_values("score_category", ascending=False)

    dff_t = df_surroundings[df_surroundings["hotel"].isin(hotel_values)]
    distance_surr = dff_t["distance"].unique()

    fig = go.Figure()

    for hotel in hotel_values:
        dff_h = dff[dff["hotel"] == hotel]
        df_categories_temp = dff_h[dff_h["category"].isin(categories_values)].sort_values(
            "category", ascending=True
        )
        categorias = df_categories_temp["category"]
        values = df_categories_temp["score_category"]

        fig.add_trace(
            go.Scatterpolar(
                r=values, theta=categorias, fill="toself", name=hotel.upper()
            )
        )

        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 10])), showlegend=True
        )

        fig.layout.template = "seaborn"
        fig.update_layout(title_text=f"Categorías")

    if hotel_values:
        return (
            fig,
            distance_surr.min(),
            distance_surr.max(),
            distance_surr.max(),
            distance_surr.max() / 5,
        )
    return fig, 0, 100, 100, 100


# , {str(dis): str(dis) for dis in distance_surr}


@app.callback(
    Output("distance_graph", "figure"),
    Input("multidrop-hotel", "value"),
    Input("distance-slider", "value"),
)
def update_graph3(hotel_values, distance_value):
    dff = df_surroundings[df_surroundings["hotel"].isin(hotel_values)]
    dff = dff[dff["distance"] <= distance_value]
    dff = dff.sort_values("score", ascending=False)

    fig = px.scatter(dff, y="distance", x="places", color="hotel")
    fig.update_traces(marker_size=10)
    fig.update_layout(scattermode="group", scattergap=0.75)

    fig.update_layout(title_text=f"Parques, Restaurantes, y demás lugares más cercanos")
    fig.update_yaxes(title_text="<b>distancia (km)</b>")

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
