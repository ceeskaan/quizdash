from dash import html, dcc

import feffery_antd_components as fac


def quiz(data: dict, hide: bool = False) -> fac.AntdTabs:
    """
    Generates a quiz interface with questions, options, and navigation.

    Args:
        data (dict): A dictionary containing the quiz title and a list of questions.
        hide (bool, optional): Whether to hide the quiz initially. Defaults to False.

    Returns:
        fac.AntdTabs: A Tabs component with each question as a tab and a results tab.
    """
    
    return fac.AntdTabs(
        [
            fac.AntdTabPane(
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.Div(data["title"], className="quiz-title"),
                                        html.Div(f"{len(data['quiz'])} Questions")
                                    ], 
                                    className="quiz-header-title"
                                ),
                                fac.AntdProgress(
                                    percent=(index / len(data["quiz"]))*100,
                                    className="quiz-progress",
                                    showInfo=False
                                ),
                            ],
                            className="quiz-header"
                        ),

                        html.Div(
                            [
                                html.Div(question["question"], className="quiz-question"),

                                fac.AntdCheckCardGroup(
                                    [
                                        fac.AntdCheckCard(
                                            i,
                                            value=i,
                                            className="correct" if i == question["answer"] else "incorrect"
                                        )
                                        for i in question["options"]
                                    ],
                                    id={"index": index, "type": "option-cards"},
                                    className="answer-options",
                                    multiple=True,
                                ),


                            ],
                            className="quiz-content"
                        ),

                        html.Div(
                            [
                                fac.AntdAlert(
                                    message=html.Div(
                                        [
                                            html.Div(id={"index": index, "type": "feedback"}, className="quiz-answer-feedback"),
                                            html.Div(f"The right answer was: {question['answer']}", className="quiz-answer-correct"),
                                            html.Div(id={"index": index, "type": "answer-explanation"}, className="quiz-answer-explanation")
                                        ]
                                    ),
                                    showIcon=True,
                                    id={"index": index, "type": "answer-status"}
                                )
                            ],
                            id={"index": index, "type": "answer"},
                            style={"display": "none"},
                            className="quiz-answer"
                        ),
                        
                        html.Div(
                            [
                                fac.AntdButton("View results" if index == (len(data["quiz"]) - 1) else "Next Question", type="primary", id={"index": index, "type": "next-question-button"}),
                                fac.AntdButton("Need help?", id={"index": index, "type": "tutor-button"})
                            ],
                            className="quiz-footer"
                        ),
                    ],
                    className="question-container"
                ),
                key=str(index),
                tab=str(index)
            )
            for index, question in enumerate(data["quiz"])
        ] + [fac.AntdTabPane(html.Div(id="results"), key=str(len(data["quiz"])), tab="results")],
        id="question-tabs",
        centered=True,
        persistence=True,
        persistence_type="session",
        style={"display": "none"} if hide else {"display": "block"}
    )


def quiz_list(data: list[dict]) -> list[html.Div]:
    """
    Generates a list of quizzes with their details and links to start each quiz.

    Args:
        data (list[dict]): A list of dictionaries containing quiz details.

    Returns:
        list[html.Div]: A list of Divs, each containing information about a quiz and a link to start it.
    """

    if len(data) == 0:
        return html.Div("You have not generated any quizzes yet!", className="quiz-link-container")
        
    return [
        html.Div(
            [
                html.Div([data[i]["title"], dcc.Link(fac.AntdButton("Start quiz", type="primary"), href=f"/quiz?quiz_id={i}")], className="quiz-link-header"),
                html.Div(
                    [
                        html.Div(["Questions: ", html.Div(data[i]["n_questions"])], className="quiz-link-setting"),
                        html.Div(["Options per question: ", html.Div(data[i]["n_options"])], className="quiz-link-setting"),
                        html.Div(["Difficulty: ", html.Div(data[i]["difficulty"])], className="quiz-link-setting")
                    ],
                    className="quiz-link-content"
                )
            ], 
            className="quiz-link-container"
        )
        for i in range(len(data))
    ]


def quiz_results(quiz_id: str, feedback: list[str]) -> html.Div:
    """
    Generates the quiz results summary with a score and feedback.

    Args:
        quiz_id (str): The ID of the quiz.
        feedback (list[str]): List of feedback messages for each quiz question.

    Returns:
        html.Div: A Div containing the quiz results, including score and feedback.
    """

    correct = feedback.count("Awesome, Great Job!")
    incorrect = feedback.count("Woops, that's not correct!")
    total = len(feedback)

    score_circle = fac.AntdProgress(
        percent=(correct/total)*100,
        type='circle'
    )

    return html.Div(
        html.Div(
            [
                html.Div("Your score is:"),
                score_circle, 
                html.Div(f"You made {incorrect} mistake(s)"),
                fac.AntdSpace([fac.AntdButton("Try again", href=f"/quiz?quiz_id={quiz_id}"), fac.AntdButton("Practice other quiz", href="/quiz")])
            ],
            className="quiz-results"
        ),
        className="quiz-results-container"
    )   
