from random import sample

import matplotlib.pyplot as plt
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

st.title(title)

radio = st.radio("Choose your planner mode", ["Day", "Week"])

if st.button("Create"):
    if radio == "Day":
        # Create a combination of breakfast and dinner and markdown table
        col1, col2 = st.columns(2)

        with col1:
            st.write("### Breakfast\n\n", sample(breakfast_list, 1)[0])

        with col2:
            st.write("### Dinner\n\n", sample(dinner_list, 1)[0])

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
                "Breakfast": sample(breakfast_list, len(days)),
                "Dinner": sample(dinner_list, len(days)),
            },
        )
        st.dataframe(df, use_container_width=True)

        # hide axes
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        
        ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
        
        fig.tight_layout()
        
        # Save to file first or an image file has already existed.
        fn = 'weekly.png'
        plt.savefig(fn)
        with open(fn, "rb") as img:
            btn = st.download_button(
                label="Download",
                data=img,
                file_name=fn,
                mime="image/png"
            )
