from dash import Input, Output, State

from app import app
from components.tutor import render_textbox, chain_with_message_history


# Much of this code is borrowed from: https://github.com/plotly/dash-sample-apps/blob/main/apps/dash-gpt3-chatbot/app.py


@app.callback(
    Output("display-conversation", "children"), 
    Input("store-conversation", "data")
)
def update_display(chat_history):
    return [render_textbox("Welcome! I'm your personal tutor, I can help you to learn any subject!", box="AI")] + [
        render_textbox(x, box="human") if i % 2 == 0 else render_textbox(x, box="AI")
        for i, x in enumerate(chat_history.split("<split>")[:-1])
    ]


@app.callback(
    Output("user-input", "value"),
    Input("submit", "nClicks"), 
    Input("user-input", "nSubmit"),
)
def clear_input(n_clicks, n_submit):
    return ""


@app.callback(
    Output("submit", "loading", allow_duplicate=True), 
    Input("user-input", "nSubmit"),
    prevent_initial_call=True
)
def spinner_when_nsubmit(n_submit):
    return True


@app.callback(
    Output("store-conversation", "data"), 
    Output('submit', 'loading'),
    Input("submit", "nClicks"), 
    Input("user-input", "nSubmit"),
    State("user-input", "value"), 
    State("store-conversation", "data"),
    prevent_initial_call=True
)
def run_chatbot(n_clicks, n_submit, user_input, chat_history):
    if n_clicks == 0 and n_submit is None:
        return "", False

    if user_input is None or user_input == "" or len(user_input) == 1:
        return chat_history, False
    
    chat_history += f"Human: {user_input}<split>ChatBot: "

    result_ai = chain_with_message_history.invoke(
        {"input": user_input},
        {"configurable": {"session_id": "unused"}},
    )

    model_output = result_ai.content
    chat_history += f"{model_output}<split>"
    
    return chat_history, False