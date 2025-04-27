import streamlit as st
import duckdb as db
import pandas as pd
import plotly.express as px
st.write("### Count Starbucks Stores each Continent :house_with_garden::coffee::mermaid:")
#st.sidebar.success("Select a demo above.")

df = pd.read_csv("Starbucks.csv")
#st.write(df)
    #x = 'Bangkok'
x = st.sidebar.selectbox('Choose continent',['Asia','America','Europe','Atlantic','Africa','Australia','Pacific','Etc'])
#results = db.sql(f"SELECT "Ownership Type", count(*) as cnt FROM df where City='{x}' group by "Ownership Type" asc").df()
results = db.sql(f"""
    SELECT "Country", count(*) as cnt 
    FROM df 
    --WHERE City='{x}' 
    where Timezone like '%{x}%'
    GROUP BY "Country"
    ORDER BY cnt ASC
""").df()
#st.write(results)

fig = px.bar(results, x="Country", y="cnt"
             #, title="Count Starbucks Store each Continent"
             )
st.plotly_chart(fig)