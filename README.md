# Sentiment Analysis with DistilBERT Transformer 🤖📝

Welcome to the sentiment analysis project powered by Hugging Face's DistilBERT model! This project demonstrates how to perform sentiment analysis on text using a pre-trained DistilBERT model for sequence classification.

## 🌟 Key Features

- **DistilBERT Transformer Model:** Utilizes the DistilBERT model from Hugging Face's Transformers library for efficient text classification.
- **DistilBERTTokenizer:** Tokenizes text input to prepare it for model inference.
- **DistilBertForSequenceClassification:** Fine-tuned model for sentiment analysis, predicting sentiment labels for input text.
- **Streamlit Web App:** Integrates the sentiment analysis model into a user-friendly web interface using Streamlit.
-  **Binary Classification:** Predicts sentiment as either positive (1) or negative (0) based on input text.

This tool provides users with a quick and accurate way to analyze the sentiment of text inputs, making it suitable for various applications, including customer feedback analysis and social media sentiment monitoring.

## 🔗 Check Out the App

Explore the sentiment analysis app here: [Sentiment Analysis with DistilBERT Web App](https://stock-forecast-app-twu5hak22gtlievyyoypof.streamlit.app/)

## 🛠️ Technologies Used

1. **Hugging Face Transformers:** For accessing the DistilBERT model and tokenizer.
2. **Streamlit:** To create an interactive web interface for the sentiment analysis.
3. **Python Libraries:** Transformers, Streamlit, Pandas, NumPy (used for data manipulation and application development).

## Getting Started

To run this application locally or deploy it to a server, follow these steps:

### Prerequisites

- Python 3.6 or later
- Pip package manager

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd text-sentiment-classifier

2. Run the app
   ```bash
   streamlit run app.py
   
**Model Details**

The sentiment classification is powered by the DistilBERT model, a smaller and faster version of BERT, fine-tuned for sequence classification tasks like sentiment analysis.
