import streamlit as st
from joblib import load
import pandas as pd
import json
from eda import plot_pie_and_barplot, plot_contact_and_subscriptions, plot_job_and_subscriptions, plot_campaign_and_subscriptions, plot_month_and_subscriptions

# Load the dataset
df = pd.read_csv('bank-full.csv', delimiter=';')

# Load the model pipeline
pipeline = load('model_pipeline.pkl')

# Load the selected features
with open('selected_features.txt', 'r') as file_1:
    selected_columns = json.load(file_1)

st.set_option('deprecation.showPyplotGlobalUse', False)

# Set page config
st.set_page_config(
    page_icon=":chart_with_upwards_trend:",
    page_title="Prediction Model for Bank's Customer Deposit Subscription",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for selecting the page
page = st.sidebar.selectbox("Select a page", ["EDA", "Prediction"])

if page == "EDA":
    st.title(" Exploratory Data Analysis ")
    # Add your EDA code here
       
    # Custom CSS for the scroll bar
    st.markdown(
        """
        <style>
        ::-webkit-scrollbar {
            width: 12px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        ::-webkit-scrollbar-thumb {
            background: #888;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the DataFrame with a scroll bar and styled title
    st.write(
        "<div style='overflow-x: auto; text-align:center;'><span style='font-size:24px; color:#FF5733;'>The DataFrame</span></div>",
        unsafe_allow_html=True
    )
    
    st.write(df) 
    ## Bank's Customer Deposit Prediction
    # Display insight title
    st.write("<div style='text-align:center;'><h2 style='font-size:24px; color:#FF5733;'>Information on Term Subscriptions</h2></div>", unsafe_allow_html=True)


    # Display EDA visualizations
    plot_pie_and_barplot = plot_pie_and_barplot(df)
    st.pyplot(plot_pie_and_barplot)

    # Display insight paragraph
    st.write("The absence of overlap between 'yes' and 'no' responses in the provided data suggests a binary and decisive nature of the responses, indicating a clear-cut distinction between positive and negative outcomes. From a business perspective, this insight underscores the importance of understanding and targeting specific audience segments effectively. By recognizing this binary behavior, businesses can tailor their marketing strategies, products, or services to cater to the distinct preferences or needs of different customer segments. Additionally, it highlights the significance of clear and unambiguous communication or calls to action in marketing campaigns, ensuring that messages resonate clearly with the intended audience and elicit the desired responses. Furthermore, businesses can leverage this insight to refine their customer segmentation strategies, identify high-value customer segments, and personalize offerings to meet their unique preferences, ultimately driving customer engagement, loyalty, and business growth.")

    plot_contact_and_subscriptions = plot_contact_and_subscriptions(df)
    st.pyplot(plot_contact_and_subscriptions)
    
    st.write("The insight from the provided data suggests that the majority of contacts are made through cellular communication, with significantly higher counts compared to other methods such as unknown and telephone. This highlights the prevalence of mobile communication channels in the dataset. Additionally, it would be beneficial to analyze the response rates associated with each contact method to understand which method yields the most positive responses. This insight can guide marketing or communication strategies by emphasizing more effective channels to increase the likelihood of positive outcomes.")

    plot_job_and_subscriptions = plot_job_and_subscriptions(df)
    st.pyplot(plot_job_and_subscriptions)

    st.write("The provided data presents information on job categories and corresponding responses categorized as either positive (yes) or negative (no). Insight from this data reveals variations in response counts across different job categories. Specifically, the management and technician categories exhibit higher counts of negative responses compared to other professions such as blue-collar and administrative roles. On the other hand, job categories like retired, student, and unemployed display relatively lower counts of negative responses. This highlights potential disparities in the responses based on occupation type. Further analysis could involve examining the reasons behind these variations, identifying potential factors influencing responses within different job categories, and devising targeted strategies or interventions to address any observed disparities.")

    plot_campaign_and_subscriptions = plot_campaign_and_subscriptions(df)
    st.pyplot(plot_campaign_and_subscriptions)

    st.write("The provided data represents campaign types and their corresponding response outcomes categorized as either positive (yes) or negative (no). Insights from this data reveal variations in response counts across different campaign types. Campaign type 1 has the highest count of positive responses, followed by campaign type 2, indicating their effectiveness in eliciting positive outcomes. Conversely, campaign types 16, 32, 24, and others exhibit significantly lower counts of positive responses, suggesting lower effectiveness or limited engagement with these campaign types. This insight underscores the importance of understanding the impact of different campaign strategies and optimizing resources towards more successful approaches to maximize positive response rates.")

    plot_month_and_subscriptions = plot_month_and_subscriptions(df)
    st.pyplot(plot_month_and_subscriptions) 

    st.write("The provided data represents response outcomes categorized by months. Insights from this data indicate variations in response counts across different months. May exhibits the highest count of positive responses, followed by August and July, suggesting potential seasonal trends or campaign effectiveness during these months. Conversely, months such as December and January display relatively lower counts of positive responses, possibly due to factors like holiday seasons or lower campaign engagement. Understanding these patterns can inform strategic planning and resource allocation, allowing for more targeted and effective marketing efforts during periods of higher response rates.")

    # Display more EDA visualizations here...

elif page == "Prediction":
    st.title(" Prediction ")

    # Prediction bar for user input
    with st.expander("User Input", expanded=True):
        # Create placeholders for user input
        user_input = {}

        # Create input fields for each selected feature
        for feature in selected_columns:
            st.markdown(f"<div style='margin-bottom:10px'>{feature}</div>", unsafe_allow_html=True)
            user_input[feature] = st.text_input("", key=feature)

    # Convert user input to DataFrame
    input_df = pd.DataFrame([user_input])

    # Keep only selected features
    input_df = input_df[selected_columns]
    
    def decode_y(y):
        if y == 1:
            return "Yes"
        elif y == 0:
            return "No"
        else:
            return "Unknown"
        
        # Predict button
    if st.button('Predict'):
        prediction = pipeline.predict(input_df)
        st.write('Prediction:', decode_y(prediction))

 