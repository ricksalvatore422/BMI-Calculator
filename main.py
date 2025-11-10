import streamlit as st

# Page configuration
st.set_page_config(
      page_title="BMI Calculator",
      page_icon="🏥",
      layout="centered"
)

# Custom CSS for professional medical look
st.markdown("""
    <style>
        .main-title {
                text-align: center;
                        color: #1E4D8B;
                                font-size: 2.5em;
                                        font-weight: bold;
                                                margin-bottom: 10px;
                                                    }
                                                        .subtitle {
                                                                text-align: center;
                                                                        color: #5A5A5A;
                                                                                font-size: 1.1em;
                                                                                        margin-bottom: 30px;
                                                                                            }
                                                                                                .bmi-result {
                                                                                                        text-align: center;
                                                                                                                font-size: 3em;
                                                                                                                        font-weight: bold;
                                                                                                                                padding: 20px;
                                                                                                                                        border-radius: 10px;
                                                                                                                                                margin: 20px 0;
                                                                                                                                                    }
                                                                                                                                                        .category-box {
                                                                                                                                                                text-align: center;
                                                                                                                                                                        font-size: 1.5em;
                                                                                                                                                                                font-weight: bold;
                                                                                                                                                                                        padding: 15px;
                                                                                                                                                                                                border-radius: 10px;
                                                                                                                                                                                                        margin: 15px 0;
                                                                                                                                                                                                            }
                                                                                                                                                                                                                .disclaimer {
                                                                                                                                                                                                                        background-color: #FFF3CD;
                                                                                                                                                                                                                                border-left: 4px solid #FFC107;
                                                                                                                                                                                                                                        padding: 15px;
                                                                                                                                                                                                                                                margin-top: 30px;
                                                                                                                                                                                                                                                        border-radius: 5px;
                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                .recommendation {
                                                                                                                                                                                                                                                                        background-color: #E8F4F8;
                                                                                                                                                                                                                                                                                border-left: 4px solid #1E4D8B;
                                                                                                                                                                                                                                                                                        padding: 15px;
                                                                                                                                                                                                                                                                                                margin: 15px 0;
                                                                                                                                                                                                                                                                                                        border-radius: 5px;
                                                                                                                                                                                                                                                                                                            }
                                                                                                                                                                                                                                                                                                                </style>
                                                                                                                                                                                                                                                                                                                    """, unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="main-title">🏥 BMI Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Body Mass Index Assessment Tool</div>', unsafe_allow_html=True)

st.markdown("---")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
      st.subheader("📏 Height")
      height_unit = st.radio("Unit", ["cm", "inches"], key="height_unit", horizontal=True)

    if height_unit == "cm":
              height = st.number_input("Enter height (cm)", min_value=50.0, max_value=250.0, value=170.0, step=0.1)
              height_m = height / 100  # Convert to meters
else:
          height = st.number_input("Enter height (inches)", min_value=20.0, max_value=100.0, value=67.0, step=0.1)
          height_m = height * 0.0254  # Convert to meters

with col2:
      st.subheader("⚖️ Weight")
      weight_unit = st.radio("Unit", ["kg", "lbs"], key="weight_unit", horizontal=True)

    if weight_unit == "kg":
              weight = st.number_input("Enter weight (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
              weight_kg = weight
else:
          weight = st.number_input("Enter weight (lbs)", min_value=40.0, max_value=660.0, value=154.0, step=0.1)
          weight_kg = weight * 0.453592  # Convert to kg

st.markdown("---")

# Calculate BMI button
if st.button("Calculate BMI", type="primary", use_container_width=True):
      # Calculate BMI
      bmi = weight_kg / (height_m ** 2)

    # Determine category and color
      if bmi < 18.5:
                category = "Underweight"
                color = "#3498DB"  # Blue
        recommendation = """
                **Health Recommendations:**
                        - Consult with a healthcare provider to identify underlying causes
                                - Consider a balanced, nutrient-rich diet to reach a healthy weight
                                        - Include strength training exercises to build muscle mass
                                                - Monitor for nutritional deficiencies
                                                        - Seek guidance from a registered dietitian
                                                                """
elif 18.5 <= bmi < 25:
        category = "Normal Weight"
        color = "#27AE60"  # Green
        recommendation = """
                **Health Recommendations:**
                        - Maintain your current healthy weight through balanced nutrition
                                - Continue regular physical activity (150 minutes/week moderate exercise)
                                        - Stay hydrated and get adequate sleep
                                                - Schedule regular health check-ups
                                                        - Practice stress management techniques
                                                                """
elif 25 <= bmi < 30:
        category = "Overweight"
        color = "#F39C12"  # Orange
        recommendation = """
                **Health Recommendations:**
                        - Consider gradual weight loss through diet and exercise
                                - Aim for 150-300 minutes of moderate physical activity per week
                                        - Focus on whole foods, fruits, vegetables, and lean proteins
                                                - Monitor portion sizes and reduce processed foods
                                                        - Consult with a healthcare provider for personalized guidance
                                                                - Consider working with a registered dietitian
                                                                        """
else:
        category = "Obese"
          color = "#E74C3C"  # Red
        recommendation = """
                **Health Recommendations:**
                        - Consult with a healthcare provider for a comprehensive health assessment
                                - Consider referral to weight management specialist or program
                                        - Work with a registered dietitian for personalized meal planning
                                                - Start with gradual increases in physical activity as tolerated
                                                        - Screen for obesity-related conditions (diabetes, hypertension, sleep apnea)
                                                                - Explore evidence-based treatment options
                                                                        - Consider behavioral health support
                                                                                """

    # Display BMI result with color coding
    st.markdown(f'<div class="bmi-result" style="background-color: {color}20; color: {color}; border: 2px solid {color};">{bmi:.1f}</div>', unsafe_allow_html=True)

    # Display category
    st.markdown(f'<div class="category-box" style="background-color: {color}20; color: {color}; border: 2px solid {color};">{category}</div>', unsafe_allow_html=True)

    # BMI ranges reference
    st.markdown("### 📊 BMI Categories")
    st.markdown("""
        - **Underweight:** BMI < 18.5
            - **Normal Weight:** BMI 18.5 - 24.9
                - **Overweight:** BMI 25.0 - 29.9
                    - **Obese:** BMI ≥ 30.0
                        """)

    # Display recommendations
    st.markdown('<div class="recommendation">', unsafe_allow_html=True)
    st.markdown(recommendation)
    st.markdown('</div>', unsafe_allow_html=True)

# Disclaimer
st.markdown('<div class="disclaimer">', unsafe_allow_html=True)
st.markdown("""
**⚠️ Disclaimer:**

This BMI calculator is provided for **educational purposes only** and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

BMI is a screening tool and has limitations:
- It does not directly measure body fat percentage
- It may not accurately reflect health status for athletes, elderly individuals, pregnant women, or children
- It does not account for muscle mass, bone density, or body composition
- Individual health status varies based on many factors beyond BMI

**Always consult with a qualified healthcare provider** for personalized medical advice and before making any decisions related to your health or weight management.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
      '<div style="text-align: center; color: #888; font-size: 0.9em;">Developed for educational purposes | Not a substitute for medical care</div>',
      unsafe_allow_html=True
)
