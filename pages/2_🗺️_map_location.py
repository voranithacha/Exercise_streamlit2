import streamlit as st
import duckdb as db
import pandas as pd
import plotly.express as px
st.write("### Mapping of Starbucks Stores :world_map::coffee:")
#st.sidebar.success("Select a demo above.")

df = pd.read_csv("Starbucks.csv")
#st.write(df)
    #x = 'Bangkok'
x = st.sidebar.selectbox('Choose continent',['Asia','America','Europe','Atlantic','Africa','Australia','Pacific','Etc'])
#results = db.sql(f"SELECT "Ownership Type", count(*) as cnt FROM df where City='{x}' group by "Ownership Type" asc").df()
results = db.sql(f"""
    SELECT Latitude, Longitude,City
    FROM df 
    --WHERE City='{x}' 
    where Timezone like '%{x}%'
""").df()
#st.write(results)

fig = px.scatter_mapbox(
    results,
    lat="Latitude",
    lon="Longitude",
    hover_name="City",  # optional, if you have this column
    zoom=3,
    height=600
)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#fig.show()
st.plotly_chart(fig)