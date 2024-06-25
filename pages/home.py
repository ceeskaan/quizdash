import dash
from dash import html

import feffery_antd_components as fac


dash.register_page(
    __name__,
    path='/',
    title='Quizdash',
    name='Home'
)


layout = html.Div(
    [
        html.Div(
            [
                html.Div("Study better using AI", className="home-title"),
                html.Div("Enhance your active learning experience with LLM generated quizzes and your personal AI tutor", className="home-subtitle"),
                html.Div(
                    [
                        fac.AntdInput(placeholder="Choose any topic... e.g. neural networks", id="home-input"),
                        fac.AntdButton("Quiz me!", type="primary", className="home-quiz-button", id="home-quiz-button", href="/generator", size="large")
                    ],
                    className="home-input-container"
                )
            ],
            className="home-content-container"
        )
    ],
    className="home-container"
)