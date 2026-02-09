import streamlit as st


st.title("CAH Veterinary Drug Dosage Calculator")

# Definitions, Inputs, and Values
p_name = st.sidebar.text_input("Enter patient's name:")
p_weight_lbs = st.sidebar.number_input("Enter patient's weight in pounds:", min_value=0.0, step=0.1)
p_age = st.sidebar.number_input("Enter patient's age in years:", min_value=0.0, step=0.5)

if p_name == "JG" and p_weight_lbs == 999.0 and p_age == 99.0:
    st.balloons()
    st.image("JG and Ethan.jpg", caption="Made by JG :)", width=300)


# Drug List
complete_drug_list = [
    "Adequan", "Alprazolam", "Aluminum Hydroxide", "Apoquel", "Atropine", "Amoxi/Clav (tablets)", "Amoxi/Clav (suspension)",
    "Amoxicillin", "Baytril (oral)", "Baytril (injection)", "Benazepril", "Buprenorphine", "Buspar (felines)",
    "Butorphanol", "Carprofen", "Cefpodoxime", "Cephalexin", "Cerenia (injection)", "Cerenia (tablets)",
    "Clavamox", "Clindamycin (capsules)", "Clindamycin (liquid)", "Convenia", "Cortrosyn (injection)",
    "Cough Tablets", "Dexamethasone-SP", "Diazepam", "Diphenhydramine (injection)", "Diphenhydramine (oral liquid)",
    "Doxycycline", "Enalapril", "Furosemide (oral)", "Gabapentin (capsules)", "Gabapentin (liquid)", "Galliprant", "Hydroxyzine (canine)", "Hydroxyzine (feline)",
    "Immiticide (injection)", "Meloxicam (tablets)", "Meloxicam (injection)", "Meloxicam (liquid)", "Methocarbamol",
    "Metronidazole", "Panacur (suspension)", "Percorten (injection)", "Prednisone", "Proin", "Propofol",
    "Strongid", "Telazol", "Trazadone", "Vetmedin", "Proheart 6", "Proheart 12"
]

selected_drugs = st.multiselect(
    "Select specific drugs to calculate:",
    options=sorted(complete_drug_list),
    placeholder="Choose medications..."
)

# Session States
if "mode" not in st.session_state:
    st.session_state.mode = None

col1, col2 = st.columns(2)

with col1:
    if st.button("Calculate Surgical Protocol"):
        st.session_state.mode = "Surgical Protocol"

with col2:
    if st.button("Calculate Selected Drugs"):
        st.session_state.mode = "Selected Drugs"

# Logic
if st.session_state.mode:

    # Basic Weight Calculations and Conversions
    p_weight_float = p_weight_lbs
    p_age_int = int(p_age)
    p_weight_kg = p_weight_float / 2.2

    # Drug Calculations

    # PreMed / Surgery
    atropine_dose = p_weight_float / 40
    butorphanol_dose = p_weight_float / 100
    diazepam_dose = p_weight_float * 0.1 / 5
    propofol_dose = p_weight_float * 2 / 10
    telazol_dose = p_weight_float / 100
    meloxicam_dose = p_weight_kg * 0.2 / 5
    buprenorphine_low = p_weight_kg * 0.005 / 0.3
    buprenorphine_high = p_weight_kg * 0.02 / 0.3
    cerenia_dose = p_weight_float / 22

    # Extended List Formulas
    adequan_dose = p_weight_kg * 4.4 / 100
    alprazolam_dose = p_weight_kg * 0.01
    aluminum_hydroxide_low = p_weight_kg * 5
    aluminum_hydroxide_high = p_weight_kg * 10
    amoxiclav_tablet_low = p_weight_kg * 15
    amoxiclav_tablet_high = p_weight_kg * 20
    amoxiclav_liquid_low = p_weight_kg * 15 / 91
    amoxiclav_liquid_high = p_weight_kg * 20 / 91
    amoxicillin_dose = p_weight_kg * 10
    apoquel_low = p_weight_kg * 0.4
    apoquel_high = p_weight_kg * 0.6
    baytril_oral_low = p_weight_kg * 5
    baytril_oral_high = p_weight_kg * 10
    baytril_injection_low = p_weight_kg * 2.5
    baytril_injection_high = p_weight_kg * 5
    benazepril_dose = p_weight_kg * 0.50
    buspar_low = p_weight_kg * 0.50
    buspar_high = p_weight_kg * 1.0
    carprofen_dose = p_weight_float
    cefpodoxime_low = p_weight_kg * 5
    cefpodoxime_high = p_weight_kg * 10
    cephalexin_dose = p_weight_kg * 20
    cerenia_tablet_dose = p_weight_kg
    clavamox_low = p_weight_kg * 15
    clavamox_high = p_weight_kg * 20
    clindamycin_capsule_low = p_weight_kg * 5
    clindamycin_capsule_high = p_weight_kg * 11
    clindamycin_liquid_low = p_weight_kg * 5 / 25
    clindamycin_liquid_high = p_weight_kg * 11 / 25
    convenia_dose = p_weight_float / 22
    cortrosyn_dose = p_weight_kg * 5 / 250
    cough_tablet_small = "1/2 tablet q4h or as directed by DVM"
    cough_tablet_large = "1 tablet q4h or as directed by DVM"
    dexamethasonesp_dose = p_weight_kg * 0.50 / 4
    diphenhydramine_injection_dose = p_weight_float / 50
    diphenhydramine_liquid_dose = p_weight_float / 2.5
    doxycycline_low = p_weight_kg * 5
    doxycycline_high = p_weight_kg * 10
    enalapril_dose = p_weight_kg * 0.50
    furosemide_dose = p_weight_kg * 2
    gabapentin_low = p_weight_kg * 5
    gabapentin_high = p_weight_kg * 10
    gabapentin_liquid_low = p_weight_kg * 5 / 50
    gabapentin_liquid_high = p_weight_kg * 10 / 50
    galliprant_dose = p_weight_kg * 2
    hydroxyzine_canine = p_weight_kg * 2
    hydroxyzine_feline_low = p_weight_kg * 5
    hydroxyzine_feline_high = p_weight_kg * 10
    immiticide_dose = p_weight_kg * 0.10 / 25
    meloxicam_tablets = p_weight_kg * 0.10
    meloxicam_liquid = "See package insert"
    methocarbomol_low = p_weight_kg * 15
    methocarbomol_high = p_weight_kg * 20
    metronidazole_low = p_weight_kg * 10
    metronidazole_high = p_weight_kg * 15
    panacur_liquid_dose = p_weight_float / 5
    percorten_dose = p_weight_float
    prednisone_low = p_weight_kg * 0.25
    prednisone_high = p_weight_kg * 0.50
    proin_dose = p_weight_float * 0.90
    strongid_dose = p_weight_float / 10
    trazadone_dose = p_weight_kg * 7
    vetmedin_dose = p_weight_kg * 0.50
    proheart_6_dose = p_weight_kg * 0.05
    proheart_12_dose = p_weight_kg * 0.05

    # Output
    st.divider()

    # Surgery Mode
    if st.session_state.mode == "Surgical Protocol":
        st.subheader(f"Surgical Protocol for {p_name or 'Patient'}")

        if p_age_int < 8:
            st.write(f"**Atropine:** {atropine_dose:.2f} mL")
            st.write(f"**Butorphanol:** {butorphanol_dose:.2f} mL")
            st.write(f"**Telazol:** {telazol_dose:.2f} mL")
            st.write(f"**Meloxicam:** {meloxicam_dose:.2f} mL")
            st.write(f"**Buprenorphine:** {buprenorphine_low:.2f} mL (low) - {buprenorphine_high:.2f} mL (high)")
            st.write(f"**Cerenia:** {cerenia_dose:.2f} mL")
        else:
            st.write(f"**Atropine:** {atropine_dose:.2f} mL")
            st.write(f"**Butorphanol:** {butorphanol_dose:.2f} mL")
            st.write(f"**Diazepam:** {diazepam_dose:.2f} mL")
            st.write(f"**Propofol:** {propofol_dose:.2f} mL")
            st.write(f"**Meloxicam:** {meloxicam_dose:.2f} mL")
            st.write(f"**Buprenorphine:** {buprenorphine_low:.2f} mL (low) - {buprenorphine_high:.2f} mL (high)")
            st.write(f"**Cerenia:** {cerenia_dose:.2f} mL")

    # Selected Drugs Mode
    elif st.session_state.mode == "Selected Drugs":
        st.subheader(f"Drug Dosages for {p_name or 'Patient'}")

        if not selected_drugs:
            st.warning("Please select at least one drug from the dropdown above.")

        if "Adequan" in selected_drugs:
            st.write(f"**Adequan:** {adequan_dose:.2f} mL")
        if "Alprazolam" in selected_drugs:
            st.write(f"**Alprazolam:** {alprazolam_dose:.2f} mg BID")
        if "Aluminum Hydroxide" in selected_drugs:
            st.write(f"**Aluminum Hydroxide:** {aluminum_hydroxide_low:.2f} - {aluminum_hydroxide_high:.2f} mg")
        if "Amoxi/Clav (tablets)" in selected_drugs:
            st.write(f"**Amoxi/Clav (tablets):** {amoxiclav_tablet_low:.2f} - {amoxiclav_tablet_high:.2f} mg BID")
        if "Amoxi/Clav (suspension)" in selected_drugs:
            st.write(f"**Amoxi/Clav (suspension):** {amoxiclav_liquid_low:.2f} - {amoxiclav_liquid_high:.2f} mL BID")
        if "Amoxicillin" in selected_drugs:
            st.write(f"**Amoxicillin:** {amoxicillin_dose:.2f} mg BID")
        if "Apoquel" in selected_drugs:
            st.write(f"**Apoquel:** {apoquel_low:.2f} - {apoquel_high:.2f} mg SID or as directed by DVM")     
        if "Atropine" in selected_drugs:
            st.write(f"**Atropine:** {atropine_dose:.2f} mL")
        if "Baytril (oral)" in selected_drugs:
            st.write(f"**Baytril (oral):** {baytril_oral_low:.2f} - {baytril_oral_high:.2f} mL SID")
        if "Baytril (injection)" in selected_drugs:
            st.write(f"**Baytril (injection):** {baytril_injection_low:.2f} - {baytril_injection_high:.2f} mg")
        if "Benazepril" in selected_drugs:
            st.write(f"**Benazepril:** {benazepril_dose:.2f} mg as directed by DVM")
        if "Buprenorphine" in selected_drugs:
            st.write(f"**Buprenorphine:** {buprenorphine_low:.2f} mL (low) - {buprenorphine_high:.2f} mL (high)")
        if "Buspar (felines)" in selected_drugs:
            st.write(f"**Buspar (felines):** {buspar_low:.2f} - {buspar_high:.2f} mg PO BID")
        if "Butorphanol" in selected_drugs:
            st.write(f"**Butorphanol:** {butorphanol_dose:.2f} mL")
        if "Carprofen" in selected_drugs:
            st.write(f"**Carprofen:** {carprofen_dose:.2f} mg BID")
        if "Cefpodoxime" in selected_drugs:
            st.write(f"**Cefpodoxime:** {cefpodoxime_low:.2f} - {cefpodoxime_high:.2f} mg SID")
        if "Cephalexin" in selected_drugs:
            st.write(f"**Cephalexin:** {cephalexin_dose:.2f} mg BID")
        if "Cerenia (injection)" in selected_drugs:
            st.write(f"**Cerenia (injection):** {cerenia_dose:.2f} mL")
        if "Cerenia (tablets)" in selected_drugs:
            st.write(f"**Cerenia (tablets):** {cerenia_tablet_dose:.2f} mg SID")
        if "Clavamox" in selected_drugs:
            st.write(f"**Clavamox:** {clavamox_low:.2f} - {clavamox_high:.2f} mg BID")
        if "Clindamycin (capsules)" in selected_drugs:
            st.write(f"**Clindamycin (capsules):** {clindamycin_capsule_low:.2f} - {clindamycin_capsule_high:.2f} mg BID")
        if "Clindamycin (liquid)" in selected_drugs:
            st.write(f"**Clindamycin (liquid):** {clindamycin_liquid_low:.2f} - {clindamycin_liquid_high:.2f} mL")
        if "Convenia" in selected_drugs:
            st.write(f"**Convenia:** {convenia_dose:.2f} mL")
        if "Cortrosyn (injection)" in selected_drugs:
            st.write(f"**Cortrosyn (injection):** {cortrosyn_dose:.2f} mL (freeze after opening bottle)")
        if "Cough Tablets" in selected_drugs:

            if p_weight_lbs < 20:
                 st.write(f"**Cough Tablets:** {cough_tablet_small}")
            else:
                 st.write(f"**Cough Tablets:** {cough_tablet_large}")
        if "Dexamethasone-SP" in selected_drugs:
            st.write(f"**Dexamethasone-SP:** {dexamethasonesp_dose:.2f} mL")
        if "Diazepam" in selected_drugs:
            st.write(f"**Diazepam:** {diazepam_dose:.2f} mL")
        if "Diphenhydramine (injection)" in selected_drugs:
            st.write(f"**Diphenhydramine (injection):** {diphenhydramine_injection_dose:.2f} mL")
        if "Diphenhydramine (oral liquid)" in selected_drugs:
            st.write(f"**Diphenhydramine (oral liquid):** {diphenhydramine_liquid_dose:.2f} mL")
        if "Doxycycline" in selected_drugs:
            st.write(f"**Doxycycline:** {doxycycline_low:.2f} - {doxycycline_high:.2f} mg BID")
        if "Enalapril" in selected_drugs:
            st.write(f"**Enalapril:** {enalapril_dose:.2f} mg as directed by DVM")
        if "Furosemide (oral)" in selected_drugs:
            st.write(f"**Furosemide (oral):** {furosemide_dose:.2f} mL as directed by DVM")
        if "Gabapentin (capsules)" in selected_drugs:
            st.write(f"**Gabapentin (capsules):** {gabapentin_low:.2f} mg (low) - {gabapentin_high:.2f} mg (high) BID")
        if "Gabapentin (liquid)" in selected_drugs:
            st.write(f"**Gabapentin (liquid):** {gabapentin_liquid_low:.2f} mL (low) - {gabapentin_liquid_high:.2f} mL (high) BID")
        if "Galliprant" in selected_drugs:
            st.write(f"**Galliprant:** {galliprant_dose:.2f} mg")
        if "Hydroxyzine (canine)" in selected_drugs:
            st.write(f"**Hydroxyzine (canine):** {hydroxyzine_canine:.2f} mg")
        if "Hydroxyzine (feline)" in selected_drugs:
            st.write(f"**Hydroxyzine (feline):** {hydroxyzine_feline_low:.2f} - {hydroxyzine_feline_high:.2f} mg")
        if "Immiticide (injection)" in selected_drugs:
            st.write(f"**Immiticide (injection):** {immiticide_dose:.2f} mL")
        if "Meloxicam (tablets)" in selected_drugs:
            st.write(f"**Meloxicam (tablets):** {meloxicam_tablets:.2f} mg SID")
        if "Meloxicam (injection)" in selected_drugs:
            st.write(f"**Meloxicam (injection):** {meloxicam_dose:.2f} mL")
        if "Meloxicam (liquid)" in selected_drugs:
            st.write(f"**Meloxicam (liquid):** {meloxicam_liquid}")
        if "Methocarbamol" in selected_drugs:
            st.write(f"**Methocarbamol:** {methocarbomol_low:.2f} - {methocarbomol_high:.2f} mg BID")
        if "Metronidazole" in selected_drugs:
            st.write(f"**Metronidazole:** {metronidazole_low:.2f} - {metronidazole_high:.2f} mg BID")
        if "Panacur (suspension)" in selected_drugs:
            st.write(f"**Panacur (suspension):** {panacur_liquid_dose:.2f} mL SID for 3 days (patient < 6 months)")
        if "Percorten (injection)" in selected_drugs:
            st.write(f"**Percorten (injection):** {percorten_dose:.2f} mL IM")
        if "Prednisone" in selected_drugs:
            st.write(f"**Prednisone:** {prednisone_low:.2f} - {prednisone_high:.2f} mg as directed by DVM")
        if "Proin" in selected_drugs:
            st.write(f"**Proin:** {proin_dose:.2f} mg BID")
        if "Propofol" in selected_drugs:
            st.write(f"**Propofol:** {propofol_dose:.2f} mL")
        if "Strongid" in selected_drugs:
            st.write(f"**Strongid:** {strongid_dose:.2f} mL")
        if "Telazol" in selected_drugs:
            st.write(f"**Telazol:** {telazol_dose:.2f} mL")
        if "Trazadone" in selected_drugs:
            st.write(f"**Trazadone:** {trazadone_dose:.2f} mg BID")
        if "Vetmedin" in selected_drugs:
            st.write(f"**Vetmedin:** {vetmedin_dose:.2f} mg as directed by DVM")
        if "Proheart 6" in selected_drugs:
            st.write(f"**Proheart 6:** {proheart_6_dose:.2f} mL")
        if "Proheart 12" in selected_drugs:
            st.write(f"**Proheart 12:** {proheart_12_dose:.2f} mL")

st.divider()

st.warning("⚠️ DISCLAIMER: For reference only. Always get DVM approval before administration.")






