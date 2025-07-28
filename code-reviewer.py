import openai
import streamlit as st
import json
import os

# Configure OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

def review_code(code, language):
    prompt = f"""
    Review this {language} code for:
    1. Potential bugs or errors
    2. Performance improvements
    3. Code style and best practices
    4. Security issues
    
    Code:
    ```{language}
    {code}
    ```
    
    Provide your review in JSON format:
    {{
        "bugs": ["list of potential bugs"],
        "performance": ["performance suggestions"],
        "style": ["style improvements"],
        "security": ["security concerns"],
        "overall_score": "score out of 10",
        "summary": "brief overall assessment"
    }}
    """
    
    try:
        # Check if API key is set
        if not openai.api_key:
            return {"error": "OpenAI API key not found. Please set OPENAI_API_KEY environment variable."}
        
        response = openai.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            stream=True  # Enable streaming
        )
        
        return response
    
    except Exception as e:
        return {"error": f"Review failed: {str(e)}"}

def main():
    st.title("AI Code Reviewer")
    
    language = st.selectbox("Language", ["python", "javascript", "java", "go", "rust"])
    code = st.text_area("Paste your code here:", height=300)
    
    if st.button("Review Code"):
        if code:
            # Create a placeholder for streaming content
            review_placeholder = st.empty()
            full_response = ""
            
            with st.spinner("Reviewing..."):
                response = review_code(code, language)
                
                if isinstance(response, dict) and "error" in response:
                    st.error(response["error"])
                else:
                    # Stream the response
                    for chunk in response:
                        if chunk.choices[0].delta.content is not None:
                            content = chunk.choices[0].delta.content
                            full_response += content
                            # Update the placeholder with the accumulated response
                            review_placeholder.markdown(full_response)

if __name__ == "__main__":
    main()
