import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_pipeline():
    # pipe = pipeline("summarization")
    # pipe = pipeline("text-generation", model="Saxo/Linkbricks-Horizon-AI-Korean-Gemma-2-sft-dpo-27B")
    return pipeline("text-generation", model="openchat/openchat_3.5")


def askGpt(prompt, pipe):
    messages=[{"role": "user", "content": prompt}]    
    gptResponse = pipe(messages)
    # gptResponse = pipe(prompt)
    return gptResponse
    
def main():
    st.set_page_config(page_title="요약 프로그램")
    pipe = load_pipeline()
    
    with st.sidebar:
        st.text_input(label="선택")
        
        st.markdown('---')
    st.header("요약 프로그램")
    st.markdown('---')
    
    text = st.text_area("요약할 글을 입력하세요")
    if st.button("요약"):
        prompt = f'''
        **Instructions** :
    - You are an expert assistant that summarizes text into **Korean language**.
    - Your task is to summarize the **text** sentences in **Korean language**.
    - Your summaries should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text : {text}'''
        st.info(askGpt(prompt, pipe))

if __name__=="__main__":
    main()
