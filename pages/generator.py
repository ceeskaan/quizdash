import dash
from dash import html, dcc

import feffery_antd_components as fac


dash.register_page(
    __name__,
    path='/generator',
    title='Generator',
    name='Generator'
)


layout = html.Div(
    [
        html.Div(
            [
                
                # Input type selector
                fac.AntdTabs(
                    [
                        fac.AntdTabPane(
                            html.Div(
                                [
                                    fac.AntdInput(
                                        id="topic-input",
                                        placeholder="What topic do you want to generate a quiz about?",
                                        maxLength=100,
                                    ),
                                ],
                                className="generator-topic-container"
                            ),
                            key="Topic",
                            tab="Topic"
                        ),

                        fac.AntdTabPane(
                            fac.AntdInput(
                                id="text-input",
                                placeholder="Paste your own text",
                                mode="text-area",
                                maxLength=1200,
                            ),
                            key="Text",
                            tab="Text"
                        ),

                        fac.AntdTabPane(
                            [
                                dcc.Upload(html.Div(['Drag and Drop or ', html.A('Select a PDF File')]), id="upload-pdf"),
                                fac.AntdInput(
                                    id="pdf-input",
                                    placeholder="Your uploaded text will appear here!",
                                    mode="text-area",
                                    maxLength=1200,
                                    disabled=True
                                ),
                            ],
                            key="Upload",
                            tab="Upload"
                        )
                    ],
                    id="quiz-input-type",
                    className="quiz-content-input",
                    centered=True,
                    tabBarLeftExtraContent=html.Div([html.Div("GENERATOR"), html.Div("Generate a quiz")], className="generator-title"),
                    defaultActiveKey="Topic"
                ),
                
                # Quiz settings
                html.Div(
                    [
                        html.Div(
                            [
                                "Number of questions",
                                fac.AntdInputNumber(id="n-questions-input", defaultValue=5, min=1, max=10)
                            ],
                            className="settings-input"
                        ),

                        html.Div(
                            [
                                "Options per question",
                                fac.AntdInputNumber(id="n-options-input", defaultValue=4, min=2, max=6)
                            ],
                            className="settings-input"
                        ),

                        html.Div(
                            [
                                "Difficulty",
                                fac.AntdSelect(id="difficulty-input", defaultValue="Normal", options=[{'label': i,'value': i} for i in ["Easy", "Normal", "Hard"]], allowClear=False)
                            ], 
                            className="settings-input"
                        )
                    ],
                    id="quiz-settings",
                    className="quiz-settings"

                ),

                # Generate button
                fac.AntdButton("Generate quiz", id="generate-quiz-button", type="primary", autoSpin=True),

            ],
            className="generator-content-container"
        )
    ],
    className="generator-container"
)