import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_pie_and_barplot(data):
    f, ax = plt.subplots(1, 2, figsize=(30, 10))
    labels = "Didn't Make Subscriptions", "Made Subscriptions"
    data["y"].value_counts().plot.pie(explode=[0, 0.25], autopct='%1.2f%%', ax=ax[0], shadow=True, startangle=25)
    ax[0].set_xlabel('Loan', fontsize=20)
    sns.barplot(x="education", y="balance", hue="y", data=data, estimator=lambda x: len(x) / len(data) * 100, ax=ax[1])
    ax[1].set(ylabel="(%)")
    ax[1].set_xticklabels(data["education"].unique(), rotation=0, rotation_mode="anchor")
    plt.show()

def plot_contact_and_subscriptions(data):
    dt = pd.DataFrame()
    dt['yes'] = data[data['y'] == 'yes']['contact'].value_counts()
    dt['no'] = data[data['y'] == 'no']['contact'].value_counts()
    plt.figure(figsize=(12, 8))
    dt.plot.bar()
    plt.title('Type of Contact and Subscriptions')
    plt.xlabel('Number of Contact')
    plt.ylabel('Count')
    plt.legend(title='Subscriptions', loc='upper right', labels=['Yes', 'No'])
    plt.xticks(rotation=0, ha='right')
    plt.tight_layout()
    plt.show()

def plot_job_and_subscriptions(data):
    dt = pd.DataFrame()
    dt['yes'] = data[data['y'] == 'yes']['job'].value_counts()
    dt['no'] = data[data['y'] == 'no']['job'].value_counts()
    plt.figure(figsize=(12, 8))
    dt.plot.bar()
    plt.title('Type of Job and Subscriptions')
    plt.xlabel('Number of Campaigns')
    plt.ylabel('Count')
    plt.legend(title='Subscriptions', loc='upper right', labels=['Yes', 'No'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_campaign_and_subscriptions(data):
    dt = pd.DataFrame()
    dt['Yes'] = data[data['y'] == 'yes']['campaign'].value_counts().sort_index()
    dt['No'] = data[data['y'] == 'no']['campaign'].value_counts().sort_index()
    plt.figure(figsize=(12, 8))
    dt.plot.bar()
    plt.title('Type of Campaign and Subscriptions')
    plt.xlabel('Number of Campaigns')
    plt.ylabel('Count')
    plt.legend(title='Subscriptions', loc='upper right', labels=['Yes', 'No'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_month_and_subscriptions(data):
    dt = pd.DataFrame()
    dt['Yes'] = data[data['y'] == 'yes']['month'].value_counts().sort_index()
    dt['No'] = data[data['y'] == 'no']['month'].value_counts().sort_index()
    dt.index = dt.index.str.capitalize()
    dt = dt.reindex(index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.figure(figsize=(12, 8))
    dt.plot.bar()
    plt.title('Type of Month and Subscriptions')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.legend(title='Subscriptions', loc='upper right', labels=['Yes', 'No'])
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# # Read the data
# df = pd.read_csv('bank-full.csv', delimiter=';')

# # Call the plot functions
# plot_pie_and_barplot(df)
# plot_contact_and_subscriptions(df)
# plot_job_and_subscriptions(df)
# plot_campaign_and_subscriptions(df)
# plot_month_and_subscriptions(df)
