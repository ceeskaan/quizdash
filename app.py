import json

import dash
from dash import html, dcc

import feffery_antd_components as fac
import feffery_utils_components as fuc

import callbacks.chat_callbacks
import callbacks.generate_callbacks
import callbacks.main_callbacks
import callbacks.quiz_callbacks
from components.nav_bar import nav_bar
from components.input import render_chat_input


app = dash.Dash(
    __name__,
    use_pages=True,
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, ''initial-scale=1'}],
)


with open('data/example_quiz.json') as file:
    example_quiz = json.load(file)


app.layout = html.Div(
    [
        nav_bar,

        fuc.FefferyTopProgress(dash.page_container, color="#1890ff"),

        fac.AntdModal(
            html.Div(
                [
                    dcc.Store(id="store-conversation", data="", storage_type="memory"),
                    html.Div(id="display-conversation", className="tutor-conversation-container"),
                    html.Div(render_chat_input(), className="tutor-message-container")
                ],
                className="tutor-modal"
            ),
            width='75vw',
            id='tutor-modal',
            title='Tutor',
            locale="en-us",
            transitionType='slide-up',
            bodyStyle= {"background": "#F6F8FB"},
            centered=True
        ),

        fac.AntdModal(
            id='generate-modal',
            title='Quiz generator',
            locale="en-us",
            centered=True,
        ),

        dcc.Store(id="quiz-storage", data=[example_quiz], storage_type="session"),
        dcc.Store(id="home-input-storage", storage_type="session"),
        dcc.Location(id="url"),
    ]
)


app.title = "Quizdash"
server = app.server


if __name__ == '__main__':
    app.run(debug=False)