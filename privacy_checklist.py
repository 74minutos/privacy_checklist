import streamlit as st

st.set_page_config(page_icon="assets\favicon.ico", layout='wide')
st.title('Starting point: you operate a website or app :computer:')

st.sidebar.title('Privacy Checklist')
st.sidebar.write("The main purpose of this app is to make it easier to obtain a result that clarifies whether our tracking and privacy policies are adequate within the frameworks of ePrivacy Directive and GDPR")

st.sidebar.write('This is based on the work of David Rosenthal, where he and his team developed a flow-chart and checklist, you can check it out [here](https://www.rosenthal.ch/downloads/VISCHER-Tracking-Checklist.pdf)')

st.sidebar.write("Nothing has been changed or updated from the original document. I decided to create this app just because I found the chart hard to follow sometimes, and this forced me to understand everything a little better")

def radio_streamlit_simplified(sentence):
    return st.radio(
        sentence,
        ('Yes', 'No'))

def streamlit_error():
    st.error("Not compliant, do not do this until adjusted appropiately or a specialist has approved this", icon="🚨")

def streamlit_success():
    st.success("If your data processing is otherwise compliant, your planned activity is probably, too", icon="✅")
    st.balloons()

def streamlit_warning():
    st.warning("The local law aspects need to be checked. Ask a specialist to do that", icon="⚠️")

sentences = {
'applicability': 'The website or app is operated in the EU or UK (1), targets (2) or creates profiles (3) of visitors/users in the EU or UK :person_in_tuxedo:',
'method_1': "Do you use any kind of 'cookies' when operating your website or app? :cookie:",
'method_2': "Do you collect information that is already stored on user's device? :diving_mask:",
'method_3': "Do you store any information on the device of the user? :iphone:",
'method_4': "Do you otherwise track individual users that use your website or app (e.g. using 'fingerprinting' or device id)? :jigsaw:",
'method_5': "Do you let any third party doing anything of the above (e.g. by integrating third party tools or cookies)? :toolbox:",
'necessity': 'Is the activity necessary for the proper operation of the website or app? :bricks:',
'information': "Do you properly inform users about the tracking and transfer, if any (and if third parties are involved also about them)? :newspaper:",
'retention': "Do you limit the retention of tracking and other personal data gathered to what is necessary? :closed_lock_with_key:",
'international_transfer_1': 'Will personal data be transferred to a third country without an adequate level of data protection? :earth_americas:',
'international_transfer_2': "Do you have sufficient safeguards for such transfer (EU SCC, TIA) or obtain valid explicit consent for the transfer? :earth_africa:",
'local_law_1': "Have you checked whether the applicable local law has stricter or additional requirements? :male-judge:",
'local_law_2': "Have you ensured to follow these stricter/additional requirements for such activities (if any)? :female-judge:",
'consent_1': "Do you obtain consent before starting the activity? :briefcase:",
'consent_2': "Is the consent statement pre-selected or pre-clcicked? :pushpin:",
'consent_3': "Is the user clearly and properly informed  about what the consent is about (including any follow-up data processing)? :books:",
'consent_4': "Is the consent obtained separately from other consent and any terms & conditions the user may have to accept? :mailbox_with_mail:",
'consent_5': "Is it equally easy to deny consent as to give it and is it presented inthe same manner (i.e. no nudging)? :red_circle:",
'consent_6': "Can the website or app (or services therein) be used without consenting (i.e.  no 'cookie-wall')? :crystal_ball:",
'consent_7': "Is it easily possible to withdraw the consent given and is the user informed about it and how? :lower_left_ballpoint_pen:",
'adequate_control_agreement': "Do you have an adequate agreement with the third party that allocates and governs controller responsibilities (for example, Facebook and LinkedIn offer a joint  controller agreement,  others such as Google rely  on controller-controller  agreements, always  assuming personal data is involved.) :file_folder:"}

def necessity_flow():
    if radio_streamlit_simplified(sentences["information"]) == 'Yes':
        if radio_streamlit_simplified(sentences["retention"]) == 'Yes':
            if radio_streamlit_simplified(sentences['international_transfer_1']) == 'Yes':
                if radio_streamlit_simplified(sentences['international_transfer_2']) == 'Yes':
                    if radio_streamlit_simplified(sentences['local_law_1']) == 'Yes':
                        if radio_streamlit_simplified(sentences['local_law_2']) == 'Yes':
                            streamlit_success()
                        else:
                            streamlit_warning()
                    else:
                        streamlit_warning()
                else:
                    streamlit_error()
            else:
                if radio_streamlit_simplified(sentences['local_law_1']) == 'Yes':
                    if radio_streamlit_simplified(sentences['local_law_2']) == 'Yes':
                        streamlit_success()
                    else:
                        streamlit_warning()
                else:
                    streamlit_warning()
        else:
            streamlit_error()
    else:
        streamlit_error()

def consent_flow():
    if radio_streamlit_simplified(sentences["consent_1"]) == 'Yes':
        if radio_streamlit_simplified(sentences["consent_2"]) == 'No':
            if radio_streamlit_simplified(sentences['consent_3']) == 'Yes':
                if radio_streamlit_simplified(sentences['consent_4']) == 'Yes':
                    if radio_streamlit_simplified(sentences['consent_5']) == 'Yes':
                        if radio_streamlit_simplified(sentences['consent_6']) == 'Yes':
                            if radio_streamlit_simplified(sentences['consent_7']) == 'Yes':
                                necessity_flow()
                            else:
                                streamlit_error()
                        else:
                            streamlit_error()
                    else:
                        streamlit_error()
                else:
                    streamlit_error()
            else:
                streamlit_error()
        else:
            streamlit_error()
    else:
        streamlit_error()

def necessity_or_consent():
    if radio_streamlit_simplified(sentences["necessity"]) == 'Yes':
        necessity_flow()
    else:
        consent_flow()


if radio_streamlit_simplified(sentences["applicability"]) == 'Yes':
    if radio_streamlit_simplified(sentences["method_1"]) == "No":
        if radio_streamlit_simplified(sentences["method_2"]) == 'No':
            if radio_streamlit_simplified(sentences["method_3"]) == 'No':
                if radio_streamlit_simplified(sentences["method_4"]) == 'No':
                    if radio_streamlit_simplified(sentences["method_5"]) == 'No':
                        streamlit_success()
                    else:
                        if radio_streamlit_simplified(sentences['adequate_control_agreement']) == 'Yes':
                            necessity_or_consent()
                        else:
                            streamlit_error()
                else:
                    necessity_or_consent()
            else:
                necessity_or_consent()
        else:
            necessity_or_consent()
    else:
        necessity_or_consent()
else:
    if radio_streamlit_simplified(sentences['local_law_1']) == 'Yes':
        if radio_streamlit_simplified(sentences['local_law_2']) == 'Yes':
            streamlit_success()
        else:
            streamlit_warning()
    else:
        streamlit_warning()
