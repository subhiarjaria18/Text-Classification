# Text-Classification
Use of HuggingFace and Streamlit

# Text Sentiment Classifier with Hugging Face and Streamlit

This project demonstrates a simple web application for text sentiment classification using Hugging Face's DistilBERT model and Streamlit. The application allows users to input text, which is then classified into either positive or negative sentiment.

## Features

- **Text Sentiment Classification:** Uses the pre-trained DistilBERT model from Hugging Face for sentiment analysis.
- **Web Application:** Built with Streamlit for a user-friendly web interface.
- **Binary Classification:** Predicts sentiment as either positive (1) or negative (0) based on input text.

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
