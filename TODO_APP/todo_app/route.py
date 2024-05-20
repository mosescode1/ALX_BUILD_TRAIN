from todo_app import app


@app.route('/')
def home():
    return "Todo APP"
