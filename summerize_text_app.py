import streamlit as st
from transformers import pipeline


def askGpt(prompt):
    messages=[{"role": "user", "content": prompt}]    
    # pipe = pipeline("text-generation", model="Saxo/Linkbricks-Horizon-AI-Korean-Gemma-2-sft-dpo-27B")
    pipe = pipeline("summarization")
    gptResponse = pipe(prompt)
    return gptResponse[0]['summary_text']
    
def main():
    st.set_page_config(page_title="요약 프로그램")
    
    with st.sidebar:
        st.text_input(label="선택")
        
        st.markdown('---')
    st.header("요약 프로그램")
    st.markdown('---')
    
    text = st.text_area("요약할 글을 입력하세요")
    if st.button("요약"):
        prompt = f'''{text}'''
        st.info(askGpt(prompt))

if __name__=="__main__":
    main()