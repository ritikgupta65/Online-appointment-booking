import streamlit as st
with st.sidebar:
    st.title("your current health status")
    st.checkbox("import your health parameters")

st.markdown("""
<style>
    .stApp {
        # background-color: #2D2D2D;
        color: white;
    }
    .stTextInput > div > div > input {
        background-color: #4A4A4A;
        color: white;
            border: 2px solid white;
            border-radius: 3px;
    }
    .stHeader {
        background-color: transparent;
    }
    .main > div {
        padding: 2rem;
    }
    h1 {
        text-align: center;
        padding-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("Current Body Health Parameters")

col1, col2 = st.columns(2)

with col1:
    heart_rate = st.text_input("Heart Rate :")
    respiratory_rate = st.text_input("Respiratory Rate :")
    systolic_bp = st.text_input("Systomin B.P. :")
    diastolic_bp = st.text_input("Diagstotic B.P. :")

with col2:
    oxygen_level = st.text_input("Oxygen Level :")
    derived_pulse = st.text_input("Derived Pulse Pressure :")

    body_temp = st.text_input("Body Temp :")
    

health_risk = st.slider("Health Risk Percentage :", 
                           min_value=0, 
                           max_value=100, 
                           value=0)
                           
st.markdown("""
<style>
    .stSelectbox >div{
            border: 1px solid white;}

    [data-baseweb="textarea"] {
        border: 1px solid white;
    }
            </style>
            """, unsafe_allow_html=True)

risk_category = st.selectbox("Risk Category :", 
                                ["Low", "Medium", "High"],
                             index=0)
st.text_area("Nessecary Precautions :", height=100)