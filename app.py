import streamlit as st
import joblib
import pandas as pd


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("models/logistic_regression.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    .main {
        padding-top: 1rem;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    .result-box {
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        margin-top: 25px;
    }

    .result-title {
        font-size: 28px;
        font-weight: 700;
    }

    .probability {
        font-size: 22px;
        margin-top: 10px;
    }

    div.stButton > button {
        width: 100%;
        height: 50px;
        font-size: 18px;
        font-weight: 600;
        border-radius: 10px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="title">📊 Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict whether a customer is likely to churn using machine learning.'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# CUSTOMER INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">👤 Customer Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col2:
    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

with col3:
    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )


col1, col2, col3 = st.columns(3)

with col1:
    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

with col2:
    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=12
    )

with col3:
    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )


# =========================================================
# PHONE SERVICES
# =========================================================

if phone_service == "Yes":

    col1, col2, col3 = st.columns(3)

    with col1:
        multiple_lines = st.selectbox(
            "Multiple Lines",
            ["Yes", "No"]
        )

else:
    multiple_lines = "No phone service"


# =========================================================
# INTERNET SERVICES
# =========================================================

st.markdown(
    '<div class="section-title">🌐 Internet Services</div>',
    unsafe_allow_html=True
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)


if internet_service == "No":

    online_security = "No internet service"
    online_backup = "No internet service"
    device_protection = "No internet service"
    tech_support = "No internet service"
    streaming_tv = "No internet service"
    streaming_movies = "No internet service"

    st.info("Internet-related services are automatically set to 'No internet service'.")

else:

    col1, col2, col3 = st.columns(3)

    with col1:
        online_security = st.selectbox(
            "Online Security",
            ["Yes", "No"]
        )

    with col2:
        online_backup = st.selectbox(
            "Online Backup",
            ["Yes", "No"]
        )

    with col3:
        device_protection = st.selectbox(
            "Device Protection",
            ["Yes", "No"]
        )


    col1, col2, col3 = st.columns(3)

    with col1:
        tech_support = st.selectbox(
            "Tech Support",
            ["Yes", "No"]
        )

    with col2:
        streaming_tv = st.selectbox(
            "Streaming TV",
            ["Yes", "No"]
        )

    with col3:
        streaming_movies = st.selectbox(
            "Streaming Movies",
            ["Yes", "No"]
        )


# =========================================================
# CONTRACT & BILLING
# =========================================================

st.markdown(
    '<div class="section-title">💳 Contract & Billing</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

with col2:
    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

with col3:
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


col1, col2 = st.columns(2)

with col1:
    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=70.0,
        step=1.0
    )

with col2:
    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=840.0,
        step=10.0
    )


# =========================================================
# PREDICTION
# =========================================================

st.markdown("---")

predict_button = st.button(
    "🔍 Predict Customer Churn"
)


if predict_button:

    # Create customer dataframe

    new_customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }])


    # Preprocess

    customer_processed = preprocessor.transform(
        new_customer
    )


    # Prediction

    prediction = model.predict(
        customer_processed
    )[0]

    probability = model.predict_proba(
        customer_processed
    )[0][1]


    # =====================================================
    # RESULT
    # =====================================================

    st.markdown("---")

    if prediction == 1:

        st.error(
            f"⚠️ Customer is likely to Churn"
        )

    else:

        st.success(
            f"✅ Customer is likely to Stay"
        )


    # Probability

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Churn Probability",
            f"{probability:.2%}"
        )

    with col2:
        st.metric(
            "Stay Probability",
            f"{1 - probability:.2%}"
        )


    # Progress bar

    st.write("### Churn Risk")

    st.progress(
        probability
    )