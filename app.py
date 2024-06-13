import torch
import streamlit as st
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

# Load tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)

# Save the model and tokenizer
model.save_pretrained('./small_model')
tokenizer.save_pretrained('./small_model')



# Load the tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained('./small_model')
model = DistilBertForSequenceClassification.from_pretrained('./small_model')

# Streamlit UI
st.title('Simple Text Classification')

input_text = st.text_area("Enter text for classification", "Type Here")

if st.button("Classify"):
    # Tokenize input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Perform inference
    outputs = model(**inputs)
    logits = outputs.logits

    # Determine prediction
    predicted_class = torch.argmax(logits, dim=1).item()
    st.write(f"Predicted Class: {predicted_class}")
