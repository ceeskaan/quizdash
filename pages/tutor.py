import dash
from dash import html, dcc

from components.input import render_chat_input


dash.register_page(
    __name__,
    path='/tutor',
    title='Tutor',
    name='Tutor'
)


layout = html.Div(
    [
        dcc.Store(id="store-conversation", data=""),
        html.Div(id="display-conversation", className="tutor-conversation-container"),
        html.Div(render_chat_input(), className="tutor-message-container")
    ],
    className="tutor-container"
)
