import streamlit as st

st.set_page_config(page_icon="assets\favicon.ico", layout='wide')
st.title('Privacy Checklist')

url = st.text('Start: you operate a website or app')

applicability = st.radio(
    "The website or app is operated in the EU or UK (1), targets (2) or creates profiles (3) of visitors/users in the EU or UK",
    ('Yes', 'No'))

if applicability == 'Yes':
    method_1 = st.radio(
        "Do you use any kind of 'cookies' when operating your website or app?",
        ('Yes', 'No'))
    if method_1 == "No":
        method_2 = st.radio(
        "Do you collect information that is already stored on user's device?",
        ('Yes', 'No'))
    elif method_1 == 'Yes':
        necessity = st.radio(
            "Is the activity necessary for the proper operation of the website or app?",
            ('Yes', 'No'))
        if necessity == 'Yes':
            information = st.radio(
            "Do you properly inform users about the tracking and transfer, if any (and if third parties are involved also about them)?",
            ('Yes', 'No'))
        elif necessity == 'No':
            consent_1 = st.radio(
            "Do you obtain consent before starting the activity?",
            ('Yes', 'No'))
            if consent_1 == 'Yes':
                 consent_2 = st.radio(
                 "Is the consent statement pre-selected or pre-clcicked?",
                 ('Yes', 'No'))
            elif consent_1 == 'No':
                st.error("Not compliant, do not do this until adjusted appropiately or a specialist has approved this")

elif applicability == 'No':
    local_law = st.radio(
        "Have you checked whether the applicable local law has stricter or additional requirements?",
        ('Yes', 'No'))
