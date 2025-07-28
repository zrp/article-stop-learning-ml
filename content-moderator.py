from transformers import pipeline
import streamlit as st
import pandas as pd

# Load a pre-trained model for toxicity detection
# Toxic-bert is available at: https://huggingface.co/unitary/toxic-bert
# Device -1 means use GPU if available, otherwise use CPU
toxicity_classifier = pipeline("text-classification", model="unitary/toxic-bert", device=-1)

def moderate_content(text):
    results = {}
    
    # Check toxicity
    toxicity = toxicity_classifier(text)
    results['toxic'] = toxicity[0]['label'] == 'TOXIC'
    results['toxicity_score'] = toxicity[0]['score']
    
    # Overall decision
    results['should_block'] = results['toxicity_score'] > 0.9
    
    return results

def main():
    st.title("AI Content Moderator")
    
    # Single text moderation
    st.subheader("Single Text Check")
    text = st.text_area("Enter text to moderate:")
    
    if st.button("Check Content"):
        if text:
            result = moderate_content(text)
            
            if result['should_block']:
                st.error("🚫 Content should be blocked")
            else:
                st.success("✅ Content looks good")
            
            st.metric("Toxicity Score", f"{result['toxicity_score']:.3f}")
    

if __name__ == "__main__":
    main()
