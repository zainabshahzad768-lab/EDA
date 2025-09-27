
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------
# Streamlit App
# --------------------------

st.title("E-Commerce Data Analysis")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read file
    df_new = pd.read_csv(uploaded_file)

    # Show preview
    st.subheader("Dataset Preview")
    st.write(df_new.head())

    # Define color palette
    color = sns.color_palette("Set2")

    # --------------------------
    # Plot 1: Orders per Hour
    # --------------------------
    st.subheader("📊 Number of Orders for Different Hours")

    fig, ax = plt.subplots(figsize=(15,6))
    (df_new.groupby('invoice_num')['hour']
          .unique()
          .value_counts()
          .iloc[:-1]
          .sort_index()
          .plot(kind='bar', color=color[0], ax=ax))

    ax.set_xlabel('Hour', fontsize=15)
    ax.set_ylabel('Number of Orders', fontsize=15)
    ax.set_title('Number of Orders for Different Hours', fontsize=15)
    ax.set_xticklabels(range(6,21), rotation='horizontal', fontsize=12)

    st.pyplot(fig)

    # --------------------------
    # Plot 2: Orders per Customer
    # --------------------------
    st.subheader("📊 Number of Orders for Different Customers")

    orders = df_new.groupby(by=['cust_id','country'], as_index=False)['invoice_num'].count()

    fig, ax = plt.subplots(figsize=(15,6))
    ax.plot(orders.cust_id, orders.invoice_num, marker='o', linestyle='-')
    ax.set_xlabel('Customer ID')
    ax.set_ylabel('Number of Orders')
    ax.set_title('Number of Orders for Different Customers')

    st.pyplot(fig)

    # --------------------------
    # Plot 3: Orders by Country
    # --------------------------
    st.subheader("📊 Number of Orders for Different Countries")

    group_country_orders = df_new.groupby('country')['invoice_num'].count().sort_values()

    fig, ax = plt.subplots(figsize=(15,8))
    group_country_orders.plot(kind='barh', fontsize=12, color=color[0], ax=ax)

    ax.set_xlabel('Number of Orders', fontsize=12)
    ax.set_ylabel('Country', fontsize=12)
    ax.set_title('Number of Orders for Different Countries', fontsize=12)

    st.pyplot(fig)

