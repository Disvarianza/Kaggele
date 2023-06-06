# Your first BigQuery commands
# To use BigQuery, we'll import the Python package below:

from google.cloud import bigquery

# The first step in the workflow is to create a Client object. As you'll soon see, 
# this Client object will play a central role in retrieving information from BigQuery datasets.
# # Create a "Client" object
client = bigquery.Client()

# We'll work with a dataset of posts on Hacker News, a website focusing on computer science and cybersecurity news.

# In BigQuery, each dataset is contained in a corresponding project. In this case, our hacker_news dataset is contained in the bigquery-public-data project. To access the dataset,

# We begin by constructing a reference to the dataset with the dataset() method.
# Next, we use the get_dataset() method, along with the reference we just constructed, to fetch the dataset.
#--------------------------------------------------------------------------------------------------------------

# Construct a reference to the "hacker_news" dataset
dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")

# API request - fetch the dataset
dataset = client.get_dataset(dataset_ref)

