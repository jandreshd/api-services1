import connexion
app= connexion.App(__name__, specification_dir="./")

app.add_api("swagger.yaml")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=4000)