import streamlit as st

st.title("💉 Insuline Calculator")

# Maaltijdopties met standaardfactoren
maaltijden = [
    ("Ontbijt", 1, 5),
    ("Middagmaal", 2, 8),
    ("Avondeten", 3, 7)
]

# Maaltijdkeuze met zichtbare factor
maaltijd_keuze = st.selectbox(
    "Welke maaltijd wordt er gegeten?",
    options=maaltijden,
    format_func=lambda x: f"{x[0]} (factor: {x[2]})"
)

# Standaardfactor ophalen
standaard_factor = maaltijd_keuze[2]

# Checkbox om factor handmatig aan te passen
override = st.checkbox("Factor handmatig aanpassen?")
if override:
    factor = st.number_input(
        "Voer aangepaste factor in:",
        value=float(standaard_factor),
        step=1.0,
        min_value=1.0
    )
else:
    factor = standaard_factor

st.write(f"Gekozen factor: **{factor}**")

# Invoer koolhydraten
kh = st.number_input("Hoeveel koolhydraten worden er gegeten?", min_value=0, step=1)

# Basis berekenen
basis = kh / factor
st.write(f"Uw basis is: **{basis:.2f}E**")

# Glucosewaarden als keuzelijst (afgerond)
glucose_opties = {
    "0 - 59": -2,
    "60 - 79": -1,
    "80 - 149": 0,
    "150 - 199": 1,
    "200 - 299": 2,
    "300 - 399": 3,
    "400 - 500": 4
}

# Keuze van glucosebereik
glucose_keuze = st.selectbox("Op hoeveel staat de glucose op het moment?", options=list(glucose_opties.keys()))
correctie = glucose_opties[glucose_keuze]
basis += correctie

# Toon correctie
if correctie != 0:
    st.write(f"Correctie toegepast: {correctie:+}E")

# Resultaat
st.success(f"Neem **{basis:.2f}E** insuline!")
