from info import create_app

app = create_app("development")


if __name__ == '__main__':
    print(app.url_map)
    app.run()