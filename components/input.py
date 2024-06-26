from dash import html

import feffery_antd_components as fac


def render_chat_input() -> html.Div:
    """
    Renders a chat input interface with a text area and a submit button.

    Returns:
        html.Div: A Div containing an AntdInput text area and an AntdButton 
        for submitting messages, styled and arranged within the div.
    """
    
    return html.Div(
        [
            fac.AntdInput(
                id="user-input",
                mode='text-area',
                autoSize={
                    'minRows': 1,
                    'maxRows': 10
                },
                placeholder='Send a message...',
                style={
                    'width': 150
                }
            ),
            html.Div(
                fac.AntdButton(
                    fac.AntdIcon(icon="antd-arrow-up"),
                    id="submit",
                    shape="circle",
                    type="primary",
                    loadingChildren=html.Div(),
                    autoSpin=True
                ),
                className="tutor-submit-container"
            )
        ],
        className="tutor-input-container"
    )

