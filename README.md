# BazaarWise India: Indian Customer Segmentation Interface
## Overview

BazaarWise India is a customer segmentation interface designed to help businesses understand and categorize their customers based on their annual income and spending habits. This tool uses a pre-trained machine learning model to predict customer segments and provides tailored recommendations to engage each segment effectively.

## Features

- **Customer Segmentation**: Classify customers into different segments based on their annual income and spending score.
- **Tailored Recommendations**: Get personalized recommendations for each customer segment to improve engagement and spending behavior.
- **User-Friendly Interface**: Easy-to-use interface built with Streamlit for seamless interaction.

## Segments

The model classifies customers into the following segments:

1. **Regular Shoppers**: Balanced profile with moderate income and spending habits.
2. **Price Sensitive Shoppers**: High income but cautious with spending.
3. **Budget Conscious**: Lower income and mindful of spending.
4. **Impulsive Buyers**: Lower income but tend to spend significantly when attracted by a good deal.
5. **Premium Shoppers**: High income paired with high spending, seeking premium experiences.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/customer_segmentation.git
    cd customer_segmentation
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

## Usage

1. Open the Streamlit app in your browser.
2. Enter the customer's details, including annual income and spending score.
3. Select the unit for annual income (Lakhs INR or Thousands USD).
4. Click the "Get Segment" button to see the customer's segment and tailored recommendations.

![Interface](/images/Screenshot%202025-03-06%20232925.png)

## Example

![Example](/images/Screenshot%202025-03-06%20232941.png)
![Example](/images/Screenshot%202025-03-06%20233202.png)

## Real-Time Usage

You can also access the real-time version of the application hosted online:

[![BazaarWise India](images/real-time.png)](https://bazaarwise.onrender.com/)

Visit the [BazaarWise India](https://bazaarwise.onrender.com/) application to try it out in real-time.

## Contributing

We welcome contributions to improve this project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Create a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [scikit-learn](https://scikit-learn.org/)
- [Matplotlib](https://matplotlib.org/)
- [Pandas](https://pandas.pydata.org/)

