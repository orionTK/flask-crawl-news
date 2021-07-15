from flask import Flask, jsonify, request
import utils

app = Flask(__name__)

@app.route("/categories", methods=['GET'])
def get_categories():
    querry = "SELECT * FROM categories"
    rows = utils.get_all(querry)
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "name": r[1],
            "urls": r[2]
        })
    return jsonify({"categories": data})

@app.route("/news", methods=['GET'])
def get_news():
    querry = "SELECT * FROM news"
    rows = utils.get_all(querry)
    data = []
    for r in rows:
        data.append({
            "id": r[0],
            "subject": r[1],
            "description": r[2],
            "image": r[3],
            "orginal_url": r[4]
        })
    return jsonify({"news": data})
# chu y: phai de method trong dau ' '
@app.route("/news/<int:news_id>", methods=['GET'])
def get_news_by_id(news_id):
    r = utils.get_news_by_id(news_id)
    # print(2)
    d = {
        "subject": r[0],
            "description": r[1],
            "image": r[2],
            "orginal_url": r[3],
        "category_name": r[4],
        "category_url": r[5]

    }
    return jsonify({"product": d})

@app.route("/news/add", methods=['POST'])
def insert_news():
    pass

@app.route("/news/<int:news_id>", methods=['POST'])
def insert_commnets(news_id):
    # import pdb
    # pdb.set_trace()
    if request.form.get("content"):
        utils.add_comments(news_id, request.form["content"])
        return jsonify({"status": 1, "message": "Successful"})
    return jsonify({"status ":-1, "message": "Need News ID"})


if __name__ == "__main__":
    app.run()