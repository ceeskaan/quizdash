from urllib.parse import parse_qs
import dash
from dash import ctx, Input, Output, ALL, MATCH, State, html

from components.quiz import quiz, quiz_list, quiz_results


@dash.callback(
    Output('quiz-collection', 'children'),
    Input("quiz-storage", "data"),
)
def show_quiz_overview(data: list[dict]) -> html.Div:
    """
    Update the quiz collection overview based on the stored quiz data.

    Args:
        data (list[dict]): The stored quiz data.

    Returns:
        html.Div: A Div containing the overview of quizzes.
    """

    return quiz_list(data)


@dash.callback(
    Output({"index": MATCH, "type": "feedback"}, "children"),
    Output({"index": MATCH, "type": "option-cards"}, "value"),
    Output({"index": MATCH, "type": "answer-status"}, "type"),
    Output({"index": MATCH, "type": "answer-explanation"}, "children"),
    Input({"index": MATCH, "type": "option-cards"}, "value"),
    State("quiz-storage", "data"),
    State('url', 'search'),
    prevent_initial_call=True
)
def answer_verification(answer: str, data: list[dict], url: str) -> tuple[str, list[str]]:
    """
    Verify the selected answer and provide feedback.

    Args:
        answer (str): The selected answer value.
        data (list[dict]): The stored quiz data.
        url (str): The current URL, used to extract the quiz ID.

    Returns:
        tuple[str, list[str]]: Feedback message and the updated option cards value.
    """
     
    quiz_id = parse_qs(url)["?quiz_id"][0]
    quiz = data[int(quiz_id)]

    question_id = ctx.triggered_id["index"]
    answer = ctx.triggered[0]["value"][0]
    correct_answer = quiz["quiz"][question_id]["answer"]
    explanation = quiz["quiz"][question_id]["explanation"]

    if answer == correct_answer:
        return "Awesome, Great Job!", dash.no_update, "success", explanation

    else:
        return "Woops, that's not correct!", [answer, correct_answer], "error", explanation
    

@dash.callback(
    Output({"index": MATCH, "type": "answer"}, "style"),    
    Output({"index": MATCH, "type": "next-question-button"}, "style"),    
    Output({"index": MATCH, "type": "tutor-button"}, "style"),    
    Output({"index": MATCH, "type": "option-cards"}, "readOnly"),
    Input({"index": MATCH, "type": "option-cards"}, "value")
)
def display_content_after_answer(value: str) -> list:
    """
    Display the correct answer, next question button, and tutor button when an option is selected,
    and make the option cards read-only.

    Args:
        value (str): The selected value from the option cards.

    Returns:
        list: Styles for the answer, next question button, and tutor button and readOnly status for the option cards.
    """

    if value:
        return [{"display": "flex"}, {"display": "block"}, {"display": "block"}] + [True]
    else:
        return [{"display": "none"}] * 3 + [False]
    

@dash.callback(
    Output('tutor-modal', 'visible'),
    Input({"index": ALL, "type": "tutor-button"}, "nClicks"),
    prevent_initial_call=True
)
def open_tutor_modal(n_clicks: str) -> bool:
    """
    Toggle the visibility of the tutor modal based on button clicks.

    Args:
        n_clicks (list[int]): List of click counts for all tutor buttons.

    Returns:
        bool: open tutor modal if any tutor button is clicked
    """

    if any(n_clicks):
        return True
    else:
        return False


@dash.callback(
    Output('question-tabs', 'activeKey'),
    Input({"index": ALL, "type": "next-question-button"}, "nClicks"),
    prevent_initial_call=True
)
def next_question(n_clicks: list[int]) -> str:
    """
    Advance to the next question tab based on the button click event.

    Args:
        n_clicks (list[int]): List of click counts for all next-question buttons.

    Returns:
        str: The key of the next question tab to be activated.
    """

    # Get the index of the button that triggered the callback
    triggered_index = int(ctx.triggered_id["index"])

    # Return the key for the next question tab
    return str(triggered_index + 1)
 

@dash.callback(
    Output("results", "children"),
    Input({"index": ALL, "type": "feedback"}, "children"),
    Input('url', 'search'),
    prevent_initial_call=True
)
def show_results(feedback: list[str], url: str) -> html.Div:
    """
    Display quiz results based on the provided feedback and quiz ID from the URL.

    Args:
        feedback (list[str]): List of feedback messages from each question.
        url (str): The current URL search parameters.

    Returns:
        html.Div: Quiz results component
    """

    if not url:
        return dash.no_update
    
    quiz_id = parse_qs(url)["?quiz_id"][0]

    return quiz_results(quiz_id, feedback)


@dash.callback(
    Output("active_quiz", "children"),
    Input('url', 'search'),
    Input("quiz-storage", "data")
)
def start_quiz(url: str, data: list[dict]) -> html.Div:
    """
    Start the quiz based on the provided quiz ID from the URL.

    Args:
        url (str): The current URL search parameters.
        data (list[dict]): The stored quiz data.

    Returns:
        html.Div: Quiz component
    """

    if url:
        quiz_id = parse_qs(url)["?quiz_id"][0]
    else:
        return dash.no_update
    
    return quiz(data[int(quiz_id)])

