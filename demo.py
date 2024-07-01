import streamlit as st
import time
st.write("Hello world!")
st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
st.balloons
multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)
import streamlit as st

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
with st.form(key='my_form'):
    # 入力フィールドを追加
    user_input = st.text_input("Enter some text")
    
    # フォーム送信ボタン
    submit_button = st.form_submit_button(label="Submit")

# ボタンが押されたときの処理
if submit_button:
    st.write(f"You entered: {user_input}")

with st.spinner('Wait for it...'):
    time.sleep(1)
st.success('Done!')
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
st.toast('Your edited image was saved!', icon='😍')
st.button("Rerun")
