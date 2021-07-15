from newspaper import Article
import sqlite3
import newspaper
def get_all(querry):
    conn = sqlite3.connect("data/newsdb.db")
    data = conn.execute(querry).fetchall()
    conn.close()
    return data

def get_news_by_id(news_id):
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
    SELECT N.subject, N.description, N.image, N.orginal_url, C.name, C.urls
    FROM news N INNER JOIN categories C on N.category_id = C.id
    WHERE N.id=?
    '''
    news = conn.execute(sql, (news_id, )).fetchone()
    conn.close()
    return news
def add_news(conn, url, category_id):
    sql = '''
    INSERT INTO news( subject,
                     description,
                     image,
                     orginal_url,
                     category_id)
    VALUES(?,?,?,?,?)
    '''
    article = Article(url)
    article.download()
    article.parse()

    conn.execute(sql, (article.title, article.text, article.top_image, article.url, category_id))
    conn.commit()

def get_news_url():
    categories = get_all("Select * from categories")
    conn = sqlite3.connect('data/newsdb.db')
    for cat in categories:
        cat_id = cat[0]
        url = cat[2]
        cat_paper = newspaper.build(url)
        for articel in cat_paper.articles:
            try:
                print("===", articel.url)
                add_news(conn, articel.url, cat_id)
            except Exception as ex:
                print("Error: " + str(ex))
                pass
    conn.close()

def add_comments(news_id, comment):
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
        INSERT INTO comments(content,news_id)
        VALUES(?,?)
    '''
    conn.execute(sql, (comment, news_id ))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    get_news_url()