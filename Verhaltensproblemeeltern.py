import streamlit as st
import pandas as pd
import altair as alt

st.header("Verhaltensprobleme (emotionale Probleme, Hyperaktivitätsprobleme o. ä.) von Kindern und Jugendlichen")
st.subheader("zwischen 11 und 17 Jahren nach Angaben ihrer Eltern")

source = pd.DataFrame({
        'Anteil(%)': [27.9, 17.5, 7.3, 2.5, 0.6],
        'Bereichen': ['Insgesamt auffälig', 'In einem Bereich', 'In zwei Bereichen', 'In drei Bereichen', 'In vier Bereichen']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Bereichen:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Deutschland; Eltern von 11 bis 17 Jährigen; Robert Koch-Institut
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: BMBF; BMG")