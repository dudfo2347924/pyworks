from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # 루트경로
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return "<h1>회원가입 페이지 입니다.</h1>"

@app.route('/board')
def board():
    return "게시판 목록입니다."

if __name__ == "__main__" :
    app.run()