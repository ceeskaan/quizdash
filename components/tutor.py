from dash import html, dcc
import feffery_antd_components as fac
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

from components.model import llm


def render_textbox(text:str, box:str = "AI") -> html.Div:
    """
    Renders a textbox for displaying messages from either a human or an AI.

    Args:
        text (str): The text to display in the textbox.
        box (str, optional): The type of textbox to render ("human" or "AI"). Defaults to "AI".

    Returns:
        html.Div: A Div containing the formatted text message.
    
    Raises:
        ValueError: If the `box` argument is not "human" or "AI".
    """
        
    text = text.replace(f"ChatBot:", "").replace("Human:", "")

    if box == "human":
        return html.Div(html.Div(text, className="textbox"), className="human textbox-container")
    
    elif box == "AI":
        return html.Div(
            [
                fac.AntdIcon(icon="antd-robot", className="ai-textbox-icon"),
                dcc.Markdown(text, className="textbox")
            ],
            className="ai textbox-container"
        )

    else:
        raise ValueError("Incorrect option for `box`.")
    


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability. Respond with some nice formatted markdown code",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

chain = prompt | llm

chat_history_for_chain = ChatMessageHistory()
chain_with_message_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: chat_history_for_chain,
    input_messages_key="input",
    history_messages_key="chat_history",
)