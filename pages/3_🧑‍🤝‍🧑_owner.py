import streamlit as st
import duckdb as db
import pandas as pd
import plotly.express as px
st.write("### Ownership Type of Starbucks Stores each Continent :people_holding_hands::coffee:")
#st.sidebar.success("Select a demo above.")

df = pd.read_csv("Starbucks.csv")
#st.write(df)
    #x = 'Bangkok'
x = st.sidebar.selectbox('Choose continent',['Asia','America','Europe','Atlantic','Africa','Australia','Pacific','Etc', 'All'])
#results = db.sql(f"SELECT "Ownership Type", count(*) as cnt FROM df where City='{x}' group by "Ownership Type" asc").df()

results = db.sql(f"""
    SELECT "Ownership Type", count(*) as cnt 
    FROM df 
    --WHERE City='{x}' 
    where Timezone like '%{x}%'
    GROUP BY "Ownership Type"
    ORDER BY cnt ASC
""").df()

results1 = db.sql(f"""
    SELECT "Ownership Type", count(*) as cnt 
    FROM df 
    GROUP BY "Ownership Type"
    ORDER BY cnt ASC
""").df()


fig = px.bar(results1, x="Ownership Type", y="cnt"
             , title="Count Starbucks Store" , color= "Ownership Type"
             )
st.plotly_chart(fig)

fig = px.bar(results, x="Ownership Type", y="cnt"
             , title="Count Starbucks Store each Continent" , color= "Ownership Type"
             )
st.plotly_chart(fig)

