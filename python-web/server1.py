from flask import Flask
import random

app = Flask(__name__) 

topics = [
    {'id': 1, 'title':'html', 'body':'html is ...'},
    {'id': 2, 'title':'css', 'body':'css is ...'},
    {'id': 3, 'title':'javascript', 'body':'javascript is ...'}
]

@app.route('/') # 기본으로 접속했을 시 (flask 는 5000번대로 접속) 서버에 나오게 할 문구 작성.
def index():
    liTags = ''
    for topic in topics:
        liTags= liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>' # 끝마무리 / 잘해놓자. 마무리애매하면 오류찾기 힘듬.
    return f''' <!doctype html>
    <html>
        <body>
            <h1> <a href="/">Web</a></h1>
            <ol>
                {liTags}
            </ol>
            <h2>Welcome</h2>
            Hello,Web
        </body>
    </html>
    '''

@app.route('/read/<id>/') #< ?? > 안에 들어오는 값이 함수의 인자값(파라미터)로 받아서 들어와진다
def read(id): # 인자로 id를 받게하면
    print(id) # 로그에 뜨는 값은 id값으로 들어간다
    return 'Read ' + id # id값으로 들어가는 값으로 내용이 나온다

@app.route('/create')
def create():
    return 'Create'






app.run(debug=True) # port= ???? 할 경우 해당 포트번호로 이동 가능, debug=True는 실시간으로 코드를 고칠 경우 서버를 재실행 안하고 리로드가능하게.