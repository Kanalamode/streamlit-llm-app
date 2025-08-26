import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

#OpenAIのAPIキーを環境変数から読み込む
from dotenv import load_dotenv
load_dotenv()

input_message = st.text_input(label="質問を入力してください。")

#回答者の立場を選択するラジオボタン
selected_item = st.radio(
    "回答者の立場を選択してください。",
    ["楽観主義", "悲観主義"]
)

st.divider()

#質問を受け付けて回答を返す関数
def get_answer(input_message, selected_item):
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    if selected_item == "楽観主義":
        messages = [
            SystemMessage(content="You are a optimism helpful assistant."),
            HumanMessage(content=input_message),
        ]

    elif selected_item == "悲観主義":
        messages = [
            SystemMessage(content="You are a pessimism helpful assistant."),
            HumanMessage(content=input_message),
        ]

    result = llm(messages)

    return result.content


if st.button("実行"):
    if input_message:
        result = get_answer(input_message, selected_item)
        st.write(f"回答: **{result}**")
    else:
        st.error("質問を入力してから「実行」ボタンを押してください。")