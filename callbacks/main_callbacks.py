from dash import Input, Output

from app import app


@app.callback(
    Output('nav-drawer', 'visible'),
    Input('hamburger-menu', 'nClicks'),
    prevent_initial_call=True
)
def open_navigation_drawer(n_clicks: int) -> bool:
    """
    Opens the navigation drawer when the hamburger menu is clicked.

    Args:
        n_clicks (int): The number of clicks on the hamburger menu.

    Returns:
        bool: True to set the navigation drawer to visible.
    """

    return True


@app.callback(
    Output('menu-horizontal', 'currentKey'),
    Output('menu-inline', 'currentKey'),
    Input('_pages_location', 'pathname')
)
def sync_navigation_bar_with_active_page(page: str) -> tuple[str, str]:
    """
    Synchronizes the current page path with the active keys of the horizontal and inline menus.

    Args:
        page (str): The current page name.

    Returns:
        tuple[str, str]: A tuple with the page for both the horizontal and inline menu current keys.
    """

    return page, page
    


