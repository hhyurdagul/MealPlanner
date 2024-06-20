from random import choice

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


def get_breakfast() -> str:
    return choice(breakfast_list)


def get_dinner() -> str:
    return choice(dinner_list)

def append_with_spacing(lst, item):
    if item in lst:
        # Find the index of the last occurrence of the item
        last_index = len(lst) - 1 - lst[::-1].index(item)
        # Check if there are at least three different items in between
        if len(lst) - last_index == 4:
            lst.append(item)
            return True
        else:
            return False  # Not enough space to append the item
    else:
        lst.append(item)
        return True


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
        selected_breakfasts: list[str] = []
        selected_dinners: list[str] = []

        while len(selected_breakfasts) < 7:
            append_with_spacing(selected_breakfasts, get_breakfast())
        while len(selected_dinners) < 7:
            append_with_spacing(selected_dinners, get_dinner())

        df = pd.DataFrame(
            index=days,
            data={
                "Breakfast": selected_breakfasts,
                "Dinner": selected_dinners,
            },
        )
        st.dataframe(df, use_container_width=True)

        # hide axes
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        
        ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='left')
        
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
