import streamlit as st
from transformers import pipeline


@st.cache_resource
def load_pipeline():
    # pipe = pipeline("summarization")
    # pipe = pipeline("text-generation", model="Saxo/Linkbricks-Horizon-AI-Korean-Gemma-2-sft-dpo-27B")
    # return pipeline("text-generation", model="openchat/openchat_3.5")
    return pipeline("summarization", model="EleutherAI/gpt-neo-125M")# model="EleutherAI/gpt-neo-1.3B")


# def askGpt(prompt, pipe):
#     messages=[{"role": "user", "content": prompt}]    
#     gptResponse = pipe(messages)
#     # gptResponse = pipe(prompt)
#     return gptResponse

def askGpt(prompt, pipe):
    response = pipe(prompt, max_new_tokens=50, num_return_sequences=1, pad_token_id=50256)
    return response[0]['summary_text']  # 반환된 텍스트만 출력
    
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
        prompt = f'''{text}'''
        st.info(askGpt(prompt, pipe))

if __name__=="__main__":
    main()
