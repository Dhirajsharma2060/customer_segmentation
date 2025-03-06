import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cache the model loading to improve performance
@st.cache_data
def load_model():
    return joblib.load("customer_segmentation_model.joblib")

# Load the trained segmentation model (trained on Mall_Customers.csv)
model = load_model()

# Updated mapping from cluster label to a descriptive segment for an Indian audience
@st.cache_data
def get_segment_mapping():
    return {
        0: {
            "name": "Regular Shoppers",
            "description": (
                "These customers have a balanced profile with moderate income and spending habits. "
                "They represent the average Indian shopper who shops regularly without extreme behaviors."
            ),
            "recommendation": (
                "Engage them with regular offers, loyalty rewards, and festive discounts during occasions like Diwali, Eid, or Holi. "
                "Check out platforms like [Flipkart Big Billion Days](https://www.flipkart.com/big-billion-days) and "
                "[Zomato Festive Offers](https://www.zomato.com) for exciting deals."
            )
        },
        1: {
            "name": "Price Sensitive Shoppers",
            "description": (
                "Customers in this group have relatively high incomes but are cautious with their spending. "
                "They are always on the lookout for the best deals and value for money."
            ),
            "recommendation": (
                "Offer them attractive cashback deals, EMI options, and exclusive discounts during sales events like the "
                "[Big Billion Days](https://www.flipkart.com/big-billion-days). Consider exploring financial products like "
                "[SBI Life Insurance](https://www.sbilife.co.in) for smart investments."
            )
        },
        2: {
            "name": "Budget Conscious",
            "description": (
                "These customers have lower incomes and are very mindful of their spending. "
                "They prioritize saving money and often hunt for the best bargains."
            ),
            "recommendation": (
                "Consider offering deep discount vouchers, limited-time deals, and value-for-money promotions that cater to tight budgets. "
                "Look out for daily deals on platforms like [Flipkart](https://www.flipkart.com) and "
                "[Amazon Great Indian Festival](https://www.amazon.in)."
            )
        },
        3: {
            "name": "Impulsive Buyers",
            "description": (
                "This segment, despite having lower incomes, tends to spend significantly when attracted by a good deal. "
                "They are quick to make spontaneous purchases when influenced by trends or flash sales."
            ),
            "recommendation": (
                "Introduce flash sales, one-day offers, and trend-based promotions—particularly during festive seasons—to capture their interest. "
                "Platforms like [Flipkart Big Billion Days](https://www.flipkart.com/big-billion-days) and [Zomato](https://www.zomato.com) offer timely deals."
            )
        },
        4: {
            "name": "Premium Shoppers",
            "description": (
                "These customers enjoy high incomes paired with high spending. "
                "They seek premium experiences and are willing to invest in quality and exclusivity."
            ),
            "recommendation": (
                "Provide them with exclusive pre-launch events, personalized services, and tailor-made loyalty programs that match their upscale lifestyle. "
                "Consider exploring premium financial products like [LIC](https://www.licindia.in) and premium credit cards for added benefits."
            )
        }
    }

segment_mapping = get_segment_mapping()

# Build the Streamlit user interface
st.title("BazaarWise India : Indian Customer Segmentation Interface")
st.write(
    "Enter the customer's details below. You can provide the Annual Income either in Lakhs (INR) or in Thousands (USD). "
    "If you select Lakhs (INR), it will be automatically converted to the required unit (thousands USD) for processing. "
    "For example, 1 Lakh INR is roughly equivalent to 1.33 Thousand USD (assuming an exchange rate of 1 USD ≈ 75 INR)."
)

# Let the user choose the unit for Annual Income
income_unit = st.radio("Select the unit for Annual Income", ("Lakhs (INR)", "Thousands (USD)"))

if income_unit == "Lakhs (INR)":
    annual_income_input = st.number_input("Annual Income (in Lakhs INR)", min_value=0.0, max_value=500.0, value=50.0, step=1.0)
    # Convert: 1 Lakh INR ~ 1.33 Thousand USD
    annual_income_converted = annual_income_input * 1.33  
else:
    annual_income_input = st.number_input("Annual Income (in Thousands USD)", min_value=0.0, max_value=500.0, value=50.0, step=1.0)
    annual_income_converted = annual_income_input

spending_score = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, value=50, step=1)

if st.button("Get Segment"):
    # Prepare the input as expected by the model (annual income in thousands USD and spending score)
    input_features = np.array([[annual_income_converted, spending_score]])
    cluster_label = model.predict(input_features)[0]
    
    # Get the descriptive segment from our mapping
    segment_info = segment_mapping.get(cluster_label, {
        "name": "Unknown Segment",
        "description": "The customer could not be mapped to a known segment.",
        "recommendation": "Try different inputs or check the model configuration."
    })
    
    st.subheader(f"Segment: {segment_info['name']}")
    st.write(segment_info['description'])
    st.markdown("**Recommendation:**")
    st.write(segment_info['recommendation'])
    
    # Hypothetical improvement chart (spending score before and after applying recommendations)
    st.markdown("### Hypothetical Impact of Recommendations on Spending Behavior")
    
    # For demonstration, assume a fixed improvement for each segment:
    # (These values are illustrative and can be adjusted based on market research)
    improvement_factors = {0: 5, 1: 7, 2: 10, 3: 8, 4: 3}
    
    before_score = spending_score
    after_score = spending_score + improvement_factors.get(cluster_label, 0)
    after_score = min(after_score, 100)  # cap the score at 100
    
    # Create a simple bar chart to show before and after spending score
    fig, ax = plt.subplots(figsize=(6, 4))
    categories = ['Before', 'After']
    scores = [before_score, after_score]
    colors = ['#1f77b4', '#2ca02c']
    
    ax.bar(categories, scores, color=colors)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Spending Score")
    ax.set_title("Spending Score Impact")
    for i, v in enumerate(scores):
        ax.text(i, v + 2, str(v), color='black', fontweight='bold', ha='center')
    
    st.pyplot(fig)
    
    st.write("The above chart is a hypothetical illustration of how effective recommendations might improve a customer's spending behavior over time.")
