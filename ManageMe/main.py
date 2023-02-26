from website import create_app

app = create_app()
""""""
@app.route('/')
def start():
    return app

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)