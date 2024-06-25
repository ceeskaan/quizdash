from dash import Dash

app = Dash(
    __name__,
    use_pages=True,
    meta_tags=[{'name': 'viewport', 'content': 'width=device-width, ''initial-scale=1'}],
)

app.title = "Quizdash"
