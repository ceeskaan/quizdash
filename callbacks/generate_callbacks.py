import base64
import fitz
import dash
from dash import html, Input, Output, State

import feffery_antd_components as fac

from app import app
from components.quiz_generator import LLM_generate_quiz


@app.callback(
    Output("quiz-storage", "data"),
    Output('generate-quiz-button', 'loading'),
    Output("generate-modal", "visible"),
    Output("generate-modal", "children"),
    Output("topic-input", "status"),
    Output("text-input", "status"),
    Output("pdf-input", "status"),
    Input("quiz-input-type", "activeKey"),
    Input("generate-quiz-button", "nClicks"),
    State("topic-input", "value"),
    State("text-input", "value"),
    State("pdf-input", "value"),
    State("n-questions-input", "value"),
    State("n-options-input", "value"),
    State("difficulty-input", "value"),
    State("quiz-storage", "data"),
)
def generate_quiz(
    active_tab: str,
    n_clicks: int,
    topic: str,
    text: str,
    pdf: str,
    n_questions: int,
    n_options: int,
    difficulty: str,
    data: list[dict]
    ) -> tuple[list[dict], bool, bool, html.Div, str, str, str]:
    """
    Generate a quiz based on the input type (Topic or Text) and provided parameters.

    Args:
        active_tab (str): The active tab key indicating input type ("Topic" or "Text").
        n_clicks (int): The number of clicks on the generate button.
        topic (str): The topic for the quiz.
        text (str): The text for the quiz (used if active tab is "Text").
        n_questions (int): The number of questions for the quiz.
        n_options (int): The number of options for each question.
        difficulty (str): The difficulty level of the quiz.
        data (list[dict]): The current quiz data stored.

    Returns:
        Tuple containing:
            - Updated quiz data
            - Loading state of the generate button
            - Visibility state of the generate modal
            - Content of the generate modal
            - Status of the topic input
            - Status of the text input
    """

    if n_clicks:
        if not topic and active_tab == "Topic":
            return dash.no_update, False, False, dash.no_update, "error", dash.no_update, dash.no_update
        
        if not text and active_tab == "Text":
            return dash.no_update, False, False, dash.no_update, dash.no_update, "error", dash.no_update
        
        if not pdf and active_tab == "Upload":
            return dash.no_update, False, False, dash.no_update, dash.no_update, dash.no_update, "error"
        
        else:
            final_topic = f"The following text: '{text}'" if active_tab == "Text" or active_tab == "Upload" else topic

            try:
                quiz_dict = LLM_generate_quiz(final_topic, n_questions, n_options, difficulty)
            except:
                return dash.no_update, False, True, "AI features are disabled, as there are no valid DBRX credentials. Clone go to the github and follow the instructions to get the full Quizdash experience!", dash.no_update, dash.no_update, dash.no_update
            
            data.append(quiz_dict)

            modal_content = html.Div(
                [
                    fac.AntdButton("Generate more", href="/generator"),
                    fac.AntdButton("View all", href="/quiz"),
                    fac.AntdButton("Start Quiz", type="primary", href=f"/quiz?quiz_id={len(data)-1}")
                ],
                className="generator-modal-buttons"
            )

            status = fac.AntdResult(
                title='Success!',
                subTitle='Ready to practice your knowledge?',
                status="success"
            )
        
            return data, False, True, html.Div([status, modal_content]), dash.no_update, dash.no_update, dash.no_update
    
    else:
        return dash.no_update, dash.no_update, False, dash.no_update, dash.no_update, dash.no_update, dash.no_update
    

@app.callback(
    Output("home-input-storage", "data"),
    Input("home-quiz-button", "nClicks"),
    Input("home-input", "nSubmit"),
    State("home-input", "value"),
    prevent_initial_call=True
)
def save_home_topic(n_clicks: int, n_submit: int, topic: str) -> str:
    """
    Store the topic input from the home page when the quiz button is clicked or the input is submitted.

    Args:
        n_clicks (int): The number of clicks on the home quiz button.
        n_submit (int): The number of times the home input is submitted.
        topic (str): The topic input value from the home input.

    Returns:
        str: The topic input value if either the button is clicked or the input is submitted; otherwise, no update.
    """

    if n_clicks or n_submit:
        return topic
    else:
        return dash.no_update
    
    
@app.callback(
    Output("topic-input", "value"),
    Input("home-input-storage", "data"),
)
def store_topic_to_generator(topic: str) -> str:
    """
    Update the value of the topic input based on the stored topic data.

    Args:
        topic (str): The topic data stored in home-input-storage.

    Returns:
        str: The topic data to be set as the value of the topic input.
    """

    return topic


def extract_text_from_pdf(pdf_content):
    # Decode the base64 PDF content
    decoded = base64.b64decode(pdf_content)
    # Save the PDF to a file
    with open('uploaded.pdf', 'wb') as f:
        f.write(decoded)
    
    # Use PyMuPDF to extract text
    doc = fitz.open('uploaded.pdf')
    text = ''
    for page in doc:
        text += page.get_text()
    
    return text


@app.callback(
    Output('pdf-input', 'value'),
    Output('pdf-input', 'disabled'),
    Input('upload-pdf', 'contents'),
    State('upload-pdf', 'filename'),
    prevent_initial_call=True
)
def update_output(contents, filename):
    if contents is not None:
        content_type, content_string = contents.split(',')
        if 'pdf' in content_type:
            text = extract_text_from_pdf(content_string)
            return text, False
    return html.Div([
        html.H5("No PDF uploaded or invalid file type.")
    ], True
)