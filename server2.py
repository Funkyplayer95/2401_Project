from flask import Flask


app = Flask(__name__)

topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

def template(contents,content):
    return f''' <!doctype html>
    <html>
        <body>
            <h1> <a href="/">Web</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
        </body>
    </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        # 끝마무리 / 잘해놓자. 마무리애매하면 오류찾기 힘듬.
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/">{topic["title"]}</a></li>'
    return liTags

@app.route('/')  # 기본으로 접속했을 시 (flask 는 5000번대로 접속) 서버에 나오게 할 문구 작성.
def index():
    return template(getContents(),'<h2>Welcome</h2>hello,web')


@app.route('/read/<int:id>/')  # <int :id> 할 경우 안에 들어가는 type을 정해줄 수 있다.
def read(id):  # 인자로 id를 받게하면
    title = ''
    body = ''
    for topic in topics:
        if id==topic["id"]:
            title = topic['title']
            body = topic['body']
            break
    return template(getContents(),f'<h2>{title}</h2>{body}') # {} 쓸꺼면 f 잘 붙이자. 한순간의 실수로 멘붕올 수 있다.


@app.route('/create')
def create():
    return 'Create'


# port= ???? 할 경우 해당 포트번호로 이동 가능, debug=True는 실시간으로 코드를 고칠 경우 서버를 재실행 안하고 리로드가능하게.
app.run(debug=True)
