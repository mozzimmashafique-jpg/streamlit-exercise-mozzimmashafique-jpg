import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Medals Visualaization", layout="wide")
st.title("Medals Visualaization")

#dropdown menu
medal = st.selectbox("medal type", ["Gold", "Silver", "Bronze"])

#checkboxes

show_bar = st.checkbox("show Bar Chart",value=true)

show_pie = st.checkbox("show Pie Chart",value=true)

# two-col structure

col1, col2 = st.columns(2)

# load the medal wide dataset
df = px.data.medals_wide()

# plot the bar chart 

if show_bar:
  fig = px.bar(
      df,
      x="nation",
      y=f"{medal}",
      title=f"medals count ({medal})",

  )

fig_bar.update_layout(
        title_x=0.5,
        xaxis_title="county",
        yaxis_title="count",
        height = 300
       
      )


coll.plotly_chart(fig_bar, use_container_width=True)

if show_pie:
  fig_pie = px.pie(
      df,
      names ="country",
      values=f"{medal}",
      title=f"medals count ({medal})",
      
  )

fig_pie.update_layout(
        title_x=0.5,
        height = 300
       
      )

fig.show ()
