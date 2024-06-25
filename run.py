import dash
from dash import html, dcc

import feffery_antd_components as fac

from app import *
import callbacks.chat_callbacks
import callbacks.generate_callbacks
import callbacks.main_callbacks
import callbacks.quiz_callbacks
from components.nav_bar import nav_bar, nav_items
from components.input import render_chat_input

import feffery_utils_components as fuc

example_quiz = {
    "title": "Example Quiz",
    "n_questions": 5,
    "n_options": 4,
    "difficulty": "Medium",
    "quiz": [
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "answer": "William Shakespeare",
            "explanation": "William Shakespeare was an English playwright and poet who is widely regarded as the greatest writer in the English language. He is often called England's national poet and the 'Bard of Avon'. 'Romeo and Juliet' is one of his most famous plays.",
            "options": [
                "William Shakespeare",
                "Charles Dickens",
                "Jane Austen",
                "George Orwell"
            ]
        },
        {
            "question": "What is the capital city of Australia?",
            "answer": "Canberra",
            "explanation": "Canberra is the capital city of Australia. It is located in the Australian Capital Territory (ACT) and was purpose-built as the capital following a compromise between the two largest cities, Sydney and Melbourne.",
            "options": [
                "Sydney",
                "Melbourne",
                "Canberra",
                "Brisbane"
            ]
        },
        {
            "question": "Who painted the Mona Lisa?",
            "answer": "Leonardo da Vinci",
            "explanation": "Leonardo da Vinci was an Italian polymath of the High Renaissance who is widely considered one of the greatest painters of all time. The Mona Lisa is one of his most famous works and is considered a masterpiece of the Italian Renaissance.",
            "options": [
                "Michelangelo",
                "Raphael",
                "Leonardo da Vinci",
                "Donatello"
            ]
        },
        {
            "question": "What is the largest planet in our solar system?",
            "answer": "Jupiter",
            "explanation": "Jupiter is the largest planet in our solar system. It is a gas giant and is known for its Great Red Spot, a storm that has been raging on the planet for at least 300 years.",
            "options": [
                "Saturn",
                "Jupiter",
                "Mars",
                "Earth"
            ]
        },
        {
            "question": "Who discovered penicillin?",
            "answer": "Alexander Fleming",
            "explanation": "Alexander Fleming was a Scottish physician and microbiologist who is best known for discovering penicillin. He won the Nobel Prize in Physiology or Medicine in 1945 for his discovery.",
            "options": [
                "Louis Pasteur",
                "Edward Jenner",
                "Alexander Fleming",
                "Robert Koch"
            ]
        }
    ]
}

app.layout = html.Div(
    [
        dcc.Location(id="url"),

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
    ]
)


if __name__ == '__main__':
    app.run(debug=False)