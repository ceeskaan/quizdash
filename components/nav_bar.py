from dash import html, dcc

import feffery_antd_components as fac

from components.verification import verify_DBRX_credentials


# Items (links) in nav-bar, used for horizontal and vertical (small screen) nav bar
nav_items = [
    {
        'component': 'Item',
        'props': {
            'key': '/',
            'title': 'Home',
            "href": "/",
        }
    },
    {
        'component': 'Item',
        'props': {
            'key': '/generator',
            'title': 'Generator',
            "href": "/generator",
        }
    },
    {
        'component': 'Item',
        'props': {
            'key': '/quiz',
            'title': 'Quiz',
            "href": "/quiz",
        }
    },
    {
        'component': 'Item',
        'props': {
            'key': '/tutor',
            'title': 'Tutor',
            "href": "/tutor"
        }
    },
]


nav_bar = html.Div(
    [
        html.Div(
            [
                
                # Quizdash Logo
                dcc.Link(
                    [
                        html.Div(className="logo"),
                        html.Div([html.Div("quiz"), html.Div("dash")], className="nav-bar-title")
                    ],
                    href="/",
                    className="nav-bar-brand"
                ),

                # Horizontal links
                html.Div(
                    fac.AntdMenu(
                        id='menu-horizontal',
                        menuItems=nav_items,
                        mode='horizontal'
                    ),
                    className="nav-bar-links"
                ),

                # Info button
                fac.AntdTooltip(
                    fac.AntdButton(
                        fac.AntdIcon(icon="antd-info-circle"),
                        shape='circle',
                        type="text",
                        size="large"
                    ),
                    title="This app is a submission to the Databricks LLM (DBRX) Dash App Building Challenge"
                ),
                
                # Github button
                fac.AntdButton(
                    fac.AntdIcon(icon="antd-github"),
                    href="https://github.com/ceeskaan/quizdash",
                    shape='circle',
                    type="text",
                    size="large"
                ),

                # DBRX credentials verifier
                verify_DBRX_credentials(),
            
                # Hamburger menu (opens vertical nav-bar in drawer)
                fac.AntdButton(
                    fac.AntdIcon(icon="antd-menu"),
                    type="default",
                    id="hamburger-menu"
                ),

                # Vertical menu (only visible on small screens)
                fac.AntdDrawer(
                    fac.AntdMenu(
                        id='menu-inline',
                        menuItems=nav_items,
                        mode='inline'
                    ),
                    id='nav-drawer'
                )

            ],
            className="nav-bar-container"
        )
    ],
    className="nav-bar"
)