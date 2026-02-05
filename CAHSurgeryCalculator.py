import streamlit as st


st.title("CAH Surgery Dosage Calculator")

 #Definitions and Input
p_name = st.sidebar.text_input("Enter patient's name:")
p_weight_lbs = st.sidebar.number_input("Enter patient's weight in pounds:", min_value=0.0, step=0.1)
p_age = st.sidebar.number_input("Enter patient's age in years:", min_value=0.0, step=0.5)

if st.button("Calculate Dosages"):


    #Logic and Calculations

    p_weight_float = p_weight_lbs
    p_age_int = int(p_age)
    p_weight_kg = p_weight_float / 2.2


    # PreMed Dosages
    atropine_dose = p_weight_float / 40
    butorphanol_dose = p_weight_float / 100
    diazepam_dose = p_weight_float * 0.1 / 5

    # Induction Dosages
    propofol_dose = p_weight_float * 2 / 10
    telazol_dose = p_weight_float / 100

    # Pain/Nausea Injection Dosages
    meloxicam_dose = p_weight_kg * 0.2 / 5
    buprenorphine_low = p_weight_kg * 0.005 / 0.3
    buprenorphine_high = p_weight_kg * 0.02 / 0.3
    cerenia_dose = p_weight_float / 22


 #Output
    st.divider()

    if p_name:
        st.header(f"Drug dosages for {p_name}")
    else:
        st.header("Drug dosages for Patient")


    if p_age_int < 8:
        st.write(f"**Atropine:** {atropine_dose:.2f} mL")
        st.write(f"**Butorphanol:** {butorphanol_dose:.2f} mL")
        st.write(f"**Telazol:** {telazol_dose:.2f} mL")
        st.write(f"**Meloxicam:** {meloxicam_dose:.2f} mL")
        st.write(f"**Buprenorphine:** {buprenorphine_low:.2f} mL (low) - {buprenorphine_high:.2f} mL (high)")
        st.write(f"**Cerenia:** {cerenia_dose:.2f} mL")

    if p_age_int >= 8:
        st.write(f"**Atropine:** {atropine_dose:.2f} mL")
        st.write(f"**Butorphanol:** {butorphanol_dose:.2f} mL")
        st.write(f"**Diazepam:** {diazepam_dose:.2f} mL")
        st.write(f"**Propofol:** {propofol_dose:.2f} mL")
        st.write(f"**Meloxicam:** {meloxicam_dose:.2f} mL")
        st.write(f"**Buprenorphine:** {buprenorphine_low:.2f} mL (low) - {buprenorphine_high:.2f} mL (high)")
        st.write(f"**Cerenia:** {cerenia_dose:.2f} mL")
