from random import choice

import pandas as pd
import streamlit as st

# Change title of the app from configs
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

try:
    title = st.secrets["title"]
except Exception:
    title = "Hello"


breakfast_list = [
    "Menemen",
    "Simit",
    "Gözleme",
    "Patatesli Börek",
    "Bal + Kaymak",
    "Sucuklu + Yumurta",
    "Peynir Tabağı + Zeytin",
    "Domates + Salatalık + Yumurta",
    "Ceviz + Taze meyve + Yulaf Ezmesi",
    "Taze meyve",
    "Yulaf ezmesi",
    "Pastırma",
    "Sigara böreği",
    "Kayısı reçeli + Kiraz reçeli + Beyaz peynir",
    "Patates kızartması",
]


dinner_list = [
    "Karnıyarık",
    "Mercimek Çorbası",
    "Biber Dolması",
    "Fasulye Pilaki",
    "Patatesli Börek",
    "Mücver",
    "Ali Nazik",
    "Ispanaklı Yumurta",
    "Kısır",
    "Pilav",
    "İmam Bayıldı",
    "Çiğ Köfte",
    "Etli Ekmek",
    "Tavuk Şiş",
    "Et Sote",
    "Yoğurtlu Kebap",
    "Zeytinyağlı Yaprak Sarma",
    "Güveç",
    "Balık Buğulama",
    "Bezelye Yemeği",
    "Menemen",
    "Şakşuka",
    "Taze Fasulye",
    "Hamsili Pilav",
    "Lahana Dolması",
    "Tavuklu Pilav",
    "Sucuklu Kuru Fasulye",
    "Nohut Yemeği",
    "Patlıcan Musakka",
    "Sebzeli Güveç",
    "Arnavut Ciğeri",
    "Çoban Kavurma",
]


def get_breakfast():
    return choice(breakfast_list)


def get_dinner():
    return choice(dinner_list)


st.title(title)

radio = st.radio("Choose your planner mode", ["Day", "Week"])

if st.button("Create"):
    if radio == "Day":
        # Create a combination of breakfast and dinner and markdown table
        col1, col2 = st.columns(2)

        with col1:
            st.write("### Breakfast\n\n", get_breakfast())

        with col2:
            st.write("### Dinner\n\n", get_dinner())

    else:
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        df = pd.DataFrame(
            index=days,
            data={
                "Breakfast": [get_breakfast() for _ in range(7)],
                "Dinner": [get_dinner() for _ in range(7)],
            },
        )
        st.dataframe(df, use_container_width=True)
