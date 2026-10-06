import streamlit as st
import joblib
import pandas as pd


# ---------------------------------------------------------
# Load trained model
# ---------------------------------------------------------
model = joblib.load("loan_model.pkl")


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Loan Approval Prediction")
st.write("Enter all customer details below to predict loan approval.")


# ---------------------------------------------------------
# Helper functions for validation
# ---------------------------------------------------------
def get_required_int(value, field_name, min_value=None, max_value=None):
    value = value.strip()

    if value == "":
        st.error(f"Please enter {field_name}.")
        return None

    try:
        number = int(value)
    except ValueError:
        st.error(f"{field_name} must be a whole number.")
        return None

    if min_value is not None and number < min_value:
        st.error(f"{field_name} must be at least {min_value}.")
        return None

    if max_value is not None and number > max_value:
        st.error(f"{field_name} must not be greater than {max_value}.")
        return None

    return number


def get_required_float(value, field_name, min_value=None, max_value=None):
    value = value.strip()

    if value == "":
        st.error(f"Please enter {field_name}.")
        return None

    try:
        number = float(value)
    except ValueError:
        st.error(f"{field_name} must be a number.")
        return None

    if min_value is not None and number < min_value:
        st.error(f"{field_name} must be at least {min_value}.")
        return None

    if max_value is not None and number > max_value:
        st.error(f"{field_name} must not be greater than {max_value}.")
        return None

    return number


# ---------------------------------------------------------
# Input Form
# ---------------------------------------------------------
with st.form("loan_prediction_form"):

    st.subheader("Customer Details")

    # 1. Age
    person_age_input = st.text_input(
        "Age",
        placeholder="Enter your age"
    )

    # 2. Gender
    person_gender = st.selectbox(
        "Gender",
        ["male", "female"],
        index=None,
        placeholder="Choose your gender"
    )

    # 3. Education
    person_education = st.selectbox(
        "Education",
        [
            "High School",
            "Associate",
            "Bachelor",
            "Master",
            "Doctorate"
        ],
        index=None,
        placeholder="Choose your education"
    )

    # 4. Annual Income
    person_income_input = st.text_input(
        "Annual Income",
        placeholder="Enter your annual income"
    )

    # 5. Employment Experience
    person_emp_exp_input = st.text_input(
        "Employment Experience (Years)",
        placeholder="Enter employment experience in years"
    )

    # 6. Home Ownership
    person_home_ownership = st.selectbox(
        "Home Ownership",
        [
            "RENT",
            "OWN",
            "MORTGAGE",
            "OTHER"
        ],
        index=None,
        placeholder="Choose your home ownership"
    )

    # 7. Loan Amount
    loan_amnt_input = st.text_input(
        "Loan Amount",
        placeholder="Enter the loan amount"
    )

    # 8. Loan Intent
    loan_intent = st.selectbox(
        "Loan Intent",
        [
            "PERSONAL",
            "EDUCATION",
            "MEDICAL",
            "VENTURE",
            "HOMEIMPROVEMENT",
            "DEBTCONSOLIDATION"
        ],
        index=None,
        placeholder="Choose the loan purpose"
    )

    # 9. Loan Interest Rate
    loan_int_rate_input = st.text_input(
        "Loan Interest Rate (%)",
        placeholder="Enter interest rate (example: 10.5)"
    )

    # 10. Loan Percent of Income
    loan_percent_income_input = st.text_input(
        "Loan Percent of Income",
        placeholder="Enter value between 0 and 1 (example: If 20 percent, enter 0.20)"
    )

    # 11. Credit History Length
    cb_person_cred_hist_length_input = st.text_input(
        "Credit History Length (Years)",
        placeholder="Enter credit history length"
    )

    # 12. Credit Score
    credit_score_input = st.text_input(
        "Credit Score",
        placeholder="Enter credit score (300 - 850)"
    )

    # 13. Previous Loan Default
    previous_loan_defaults_on_file = st.selectbox(
        "Previous Loan Default",
        ["Yes", "No"],
        index=None,
        placeholder="Choose previous loan default status"
    )

    st.write("")

    predict_button = st.form_submit_button(
        "🔍 Predict Loan Status",
        use_container_width=True
    )


# ---------------------------------------------------------
# Prediction
# ---------------------------------------------------------
if predict_button:

    # -----------------------------------------------------
    # Validate numeric inputs
    # -----------------------------------------------------

    person_age = get_required_int(
        person_age_input,
        "Age",
        min_value=18,
        max_value=100
    )

    person_income = get_required_int(
        person_income_input,
        "Annual Income",
        min_value=0
    )

    person_emp_exp = get_required_int(
        person_emp_exp_input,
        "Employment Experience",
        min_value=0,
        max_value=50
    )

    loan_amnt = get_required_float(
        loan_amnt_input,
        "Loan Amount",
        min_value=0
    )

    loan_int_rate = get_required_float(
        loan_int_rate_input,
        "Loan Interest Rate",
        min_value=0,
        max_value=50
    )

    loan_percent_income = get_required_float(
        loan_percent_income_input,
        "Loan Percent of Income",
        min_value=0,
        max_value=1
    )

    cb_person_cred_hist_length = get_required_float(
        cb_person_cred_hist_length_input,
        "Credit History Length",
        min_value=0,
        max_value=50
    )

    credit_score = get_required_int(
        credit_score_input,
        "Credit Score",
        min_value=300,
        max_value=850
    )

    # -----------------------------------------------------
    # Validate dropdown inputs
    # -----------------------------------------------------

    valid_inputs = True

    if person_gender is None:
        st.error("Please choose your gender.")
        valid_inputs = False

    if person_education is None:
        st.error("Please choose your education.")
        valid_inputs = False

    if person_home_ownership is None:
        st.error("Please choose your home ownership.")
        valid_inputs = False

    if loan_intent is None:
        st.error("Please choose the loan purpose.")
        valid_inputs = False

    if previous_loan_defaults_on_file is None:
        st.error("Please choose your previous loan default status.")
        valid_inputs = False

    # -----------------------------------------------------
    # Check numeric validation
    # -----------------------------------------------------

    numeric_inputs_valid = all(
        value is not None
        for value in [
            person_age,
            person_income,
            person_emp_exp,
            loan_amnt,
            loan_int_rate,
            loan_percent_income,
            cb_person_cred_hist_length,
            credit_score
        ]
    )

    # -----------------------------------------------------
    # Only predict if everything is valid
    # -----------------------------------------------------

    if numeric_inputs_valid and valid_inputs:

        # Create DataFrame with exactly the same
        # column names used during model training
        input_data = pd.DataFrame([{
            "person_age": person_age,
            "person_gender": person_gender,
            "person_education": person_education,
            "person_income": person_income,
            "person_emp_exp": person_emp_exp,
            "person_home_ownership": person_home_ownership,
            "loan_amnt": loan_amnt,
            "loan_intent": loan_intent,
            "loan_int_rate": loan_int_rate,
            "loan_percent_income": loan_percent_income,
            "cb_person_cred_hist_length": cb_person_cred_hist_length,
            "credit_score": credit_score,
            "previous_loan_defaults_on_file":
                previous_loan_defaults_on_file
        }])

        # -------------------------------------------------
        # Prediction
        # -------------------------------------------------
        prediction = model.predict(input_data)

        # -------------------------------------------------
        # Display result
        # -------------------------------------------------
        if prediction[0] == 1:
            st.success("✅ Loan Approved")

            # Show probability if model supports it
            if hasattr(model, "predict_proba"):
                probability = model.predict_proba(input_data)[0][1]
                st.info(
                    f"Approval Probability: "
                    f"{probability * 100:.2f}%"
                )

        else:
            st.error("❌ Loan Not Approved")

            # Show probability if model supports it
            if hasattr(model, "predict_proba"):
                probability = model.predict_proba(input_data)[0][1]
                st.info(
                    f"Approval Probability: "
                    f"{probability * 100:.2f}%"
                )