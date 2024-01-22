from flask import Flask, request, redirect


app = Flask(__name__)

nextId= 4
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

def template(contents,content,id=None):
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li><a href="/update/{id}/">update</a></li>
        '''
    return f''' <!doctype html>
    <html>
        <body>
            <h1> <a href="/">Web</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
                {contextUI}
            </ul>
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
    return template(getContents(),f'<h2>{title}</h2>{body}', id) # {} 쓸꺼면 f 잘 붙이자. 한순간의 실수로 멘붕올 수 있다.


@app.route('/create/', methods=['GET','POST']) # 메소드스를 지정해야 get, post를 받을 수 있음. post는 네트워크안에 숨겨짐
def create():
    if request.method == 'GET':
        content = '''
            <form action="/create/" method="POST">
                <p><input type="text" name="title" placeholder="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p>
                <p><input type="submit" value="create"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method=='POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        url = '/read/'+str(nextId) + '/' # url속성상 nextId가 int이기에 str로 바꿔서 진행해줘야한다. 모를때는 f12눌러서 network찾아보자
        nextId = nextId + 1
        return redirect(url)


@app.route('/update/<int:id>/', methods=['GET','POST'])
def update(id):
    if request.method == 'GET':
        title = ''
        body = ''
        for topic in topics:
            if id==topic["id"]:
                title = topic['title']
                body = topic['body']
                break
        content = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" name="title" placeholder="title" value="{title}"></p>
                <p><textarea name="body" placeholder="body">{body}</textarea></p>
                <p><input type="submit" value="update"></p>
            </form>
        '''
        return template(getContents(), content)
    elif request.method=='POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        for topic in topics:
            if id == topic['id']:
                topic['title'] = title
                topic['body'] = body
                break
        url = '/read/'+str(id) + '/' 
        return redirect(url)





# port= ???? 할 경우 해당 포트번호로 이동 가능, debug=True는 실시간으로 코드를 고칠 경우 서버를 재실행 안하고 리로드가능하게.
app.run(debug=True)
