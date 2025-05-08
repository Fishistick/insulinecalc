import streamlit as st

st.title("💉 Insuline Calculator")

# Maaltijd keuze
maaltijd = st.selectbox(
    "Welke maaltijd wordt er gegeten?",
    options=[("Ontbijt", 1), ("Middagmaal", 2), ("Avondeten", 3)],
    format_func=lambda x: x[0]
)

# Bepaal factor op basis van maaltijd
if maaltijd[1] == 1:
    factor = 5
elif maaltijd[1] == 2:
    factor = 8
elif maaltijd[1] == 3:
    factor = 7

# Koolhydraten input
kh = st.number_input("Hoeveel koolhydraten worden er gegeten?", min_value=0, step=1)

# Basis berekenen
basis = kh / factor
st.write(f"Uw basis is: **{basis:.2f}E**")

# Glucosewaarde input
glu = st.number_input("Op hoeveel staat de glucose op het moment?", min_value=0, step=1)

# Aanpassing op basis van glucose
if glu <= 59:
    basis -= 2
elif glu <= 79:
    basis -= 1
elif glu <= 149:
    pass  # Geen aanpassing
elif glu <= 199:
    basis += 1
elif glu <= 299:
    basis += 2
elif glu <= 399:
    basis += 3
elif glu <= 500:
    basis += 4

# Resultaat tonen
st.success(f"Neem **{basis:.2f}E** insuline!")
