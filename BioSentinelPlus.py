import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="BioSentinel+", layout="wide")

hide_streamlit_style = """ 
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Home", "See a Doc", "Quick Tips", "Comprehensive Education"],
    icons=["house", "person-lines-fill", "lightbulb", "book"],
    orientation="horizontal",
)

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

if selected == "Home":

    # LOGO.

    logo = current_dir / "assets" / "logo.png"
    logo = Image.open(logo)

    st.image(logo, use_container_width=True)
            
    # Metrics row
    st.title("🧬 Vital Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Name", "Juma Anderson")
    col2.metric("Age", "29")
    col3.metric("Gender", "Male")

    col4, col5, col6 = st.columns(3)
    col4.metric("ID", "BSN-2045")
    col5.metric("Blood Type", "O+")
    col6.metric("Iris Type", "Type B")

    col7, col8, col9 = st.columns(3)
    col7.metric("Weight", "65kg")
    col8.metric("Height", "170cm")
    col9.metric("BMI", "22.5")

    col10, col11 = st.columns(2)
    col10.metric("Points Earned", "3,200 🏆")
    col11.metric("Next Checkup", "20 July 2025 @ 10:00AM")

    st.success("🩺 Health Overview: You're doing great! Keep tracking your vitals and earning points.")

    st.title("📊 Interactive & Gamified Health Graphs")
    colA, colB = st.columns(2)
    with colA:
        fig1 = px.line(
            x=["Mon", "Tue", "Wed", "Thu", "Fri"],
            y=[72, 76, 75, 78, 77],
            markers=True,
            title="❤️ Heart Rate (bpm)"
        )
        fig1.update_traces(line=dict(width=4), marker=dict(size=10))
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = px.bar(
            x=["Mon", "Tue", "Wed", "Thu", "Fri"],
            y=[120, 118, 119, 117, 121],
            title="🩸 Blood Pressure (mmHg)",
            color=[120, 118, 119, 117, 121],
            color_continuous_scale='reds'
        )
        st.plotly_chart(fig2, use_container_width=True)

    with colB:
        fig3 = px.area(
            x=["Mon", "Tue", "Wed", "Thu", "Fri"],
            y=[5, 6, 7, 6, 8],
            title="😊 Mood Tracker",
            markers=True
        )
        st.plotly_chart(fig3, use_container_width=True)

        fig4 = px.line(
            x=["Mon", "Tue", "Wed", "Thu", "Fri"],
            y=[36.5, 36.7, 36.6, 36.8, 36.7],
            markers=True,
            title="🌡️ Body Temperature (°C)"
        )
        st.plotly_chart(fig4, use_container_width=True)

        fig5 = px.bar_polar(
            r=[60, 62, 61, 63, 65],
            theta=["Mon", "Tue", "Wed", "Thu", "Fri"],
            title="💧 Hydration (%)",
            color=[60, 62, 61, 63, 65],
            color_continuous_scale="Blues"
        )
        st.plotly_chart(fig5, use_container_width=True)

elif selected == "See a Doc":

    st.subheader("Book an Appointment")
    st.date_input("Choose a Date")
    st.time_input("Choose a Time")
    st.selectbox("Select a Specialist", ["General Physician", "Cardiologist", "Nutritionist", "Psychologist"])
    st.button("Book Appointment")

    st.subheader("Can't Wait for an Appointment? Get a Live Consultation")
    st.markdown("[🔗Dr. Achieng's Meeting](https://meet.google.com/abc-defg-hij)")
    st.markdown("[🔗Dr. Kamau's Meeting](https://meet.google.com/xyz-wxyz-mno)")

    st.subheader("Cost Evaluation Calculator")
    budget = st.slider("Select Your Budget (Kshs)", 1000, 10000, 3000)
    urgency = st.selectbox("Urgency Level", ["Low", "Moderate", "High"])
    insurance = st.radio("Do you have insurance?", ["Yes", "No"])

    st.write("**Suggested Specialists Based on Budget & Preferences:**")
    if budget < 2500:
        st.warning("Limited to general care and checkups.")
        st.write("- General Physician")
    elif budget < 5000:
        st.info("Good options for most outpatient services.")
        st.write("- Nutritionist\n- Psychologist")
    else:
        st.success("All services available.")
        st.write("- Cardiologist\n- All Specialists")

elif selected == "Quick Tips":
    st.title("⚕️ Quick Health Tips")
    gender = st.radio("Select Gender", ["Male", "Female"])

    if gender == "Male":
        st.info("**Tips for Men:**\n- Regular prostate checks.\n- Monitor blood pressure.\n- Exercise regularly.\n- Limit alcohol and tobacco use.")
        st.warning("⚠️ Avoid self-medication. Always consult a qualified practitioner.")
    else:
        st.info("**Tips for Women:**\n- Regular breast exams.\n- Maintain bone density.\n- Balanced diet rich in iron.\n- Routine pap smears.")
        st.warning("⚠️ Early detection saves lives. Don't skip annual checkups.")

elif selected == "Comprehensive Education":
    st.title("🎓 Comprehensive Education")

    st.subheader("📽️ Watch & Learn")
    st.video("https://www.youtube.com/watch?v=dBnniua6-oM")
    st.video("https://www.youtube.com/watch?v=30gEiweaAVQ")

    st.subheader("🕹️ Interactive Modules")
    module = st.selectbox("Choose a Module", ["Nutrition Basics", "Mental Health", "Exercise Essentials"])

    if module == "Nutrition Basics":
        st.markdown("**What is a balanced diet?**")
        st.radio("Pick the correct definition:", [
            "Only fruits and water",
            "A mix of proteins, carbs, fats, vitamins, and minerals",
            "Fasting every other day"
        ])

        st.markdown("**What are healthy fats?**")
        st.checkbox("Avocados")
        st.checkbox("Fried chicken")
        st.checkbox("Olive oil")

    elif module == "Mental Health":
        st.markdown("**How often should you check in on your mental health?**")
        st.slider("Rate your mental wellness today (1 = low, 10 = excellent)", 1, 10, 5)

        st.markdown("**Choose stress-relieving activities:**")
        st.checkbox("Meditation")
        st.checkbox("Screaming")
        st.checkbox("Deep breathing")
        st.checkbox("Punching walls")

    elif module == "Exercise Essentials":
        st.markdown("**How many minutes of moderate exercise is recommended weekly?**")
        st.radio("Choose one:", ["60 minutes", "150 minutes", "300 minutes"])

        st.markdown("**Which of these are cardio exercises?**")
        st.checkbox("Jogging")
        st.checkbox("Weight lifting")
        st.checkbox("Swimming")
        st.checkbox("Bench press")

    st.subheader("📊 Progress Tracker")
    st.progress(0.6)
    st.info("You've completed 60% of the education journey!")
