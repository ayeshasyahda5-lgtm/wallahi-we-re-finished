import streamlit as st

pages = [
    st.Page(page="pages/Pendahuluan.py", title="Pendahuluan┈•✦", icon="🌼"),
    st.Page(page="pages/Visualisasi.py", title="Visualisasi Data┈•✦", icon="🌸"),
    st.Page(page="pages/Analisis.py", title="Analisis┈•✦", icon="🌻"),
    st.Page(page="pages/Kesimpulan.py", title="Kesimpulan┈•✦", icon="🎀"),
    st.Page(page="pages/.Data.py", title="Data┈•✦", icon="📟")
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()