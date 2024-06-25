import dash
from dash import html

import feffery_antd_components as fac

from components.quiz import quiz


dash.register_page(
    __name__,
    path='/quiz',
    title='Quiz',
    name='Quiz'
)

layout = html.Div(
    [

        html.Div(
            html.Div(
                html.Div(
                    [
                        html.Div([html.Div([html.Div("QUIZ"), html.Div("Quiz Overview")], className="generator-title"), fac.AntdButton("New quiz", href="/generator", icon=fac.AntdIcon(icon="antd-plus"))], className="quiz-overview-header"),
                        html.Div(id="quiz-collection", className="quiz-overview-list"),
                        quiz({"title": "", "quiz": [{"question": "", "options": [""], "answer": ""}]}, hide=True),
                    ],
                    className="quiz-overview-content"
                ),
                className="quiz-overview"
            ),
            id="active_quiz",
            className="quiz-content-container"
        )
    ],
    className="quiz-container"
)