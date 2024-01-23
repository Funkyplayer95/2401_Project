from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt

#파이썬코드에 html이 있으면 가독성이 떨어진다.
#그러니 template engine 을 사용할 줄 알아야 한다.



nextId = 4
topics = [ # 앱이 재생할 때마다 나오는 데이터 이다. 그렇다면 DB를 사용할때엔 이 정보를 불러와야겠지..?
    {'id': 1, 'title': 'routing', 'body': 'routing is..'},
    {'id': 2, 'title': 'view', 'body': 'view is..'},
    {'id': 3, 'title': 'model', 'body': 'model is..'}
]


def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="POST">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="delete">
                </form>
            </li>
            <li><a href="/update/{id}">update</a></li>
        '''
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic['title']}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">django</h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
            
            {contextUI}
            
        </ul>
    </body>
    </html>
    '''


def index(request):
    article = '''
    <h2>welcome</h2>
        hello, django
    '''
    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic["id"] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'

    return HttpResponse(HTMLTemplate(article, id))


@csrf_exempt
def create(request):
    global nextId
    if request.method == "GET": #textarea에는 보안에 대한것도 생각해야한다. security
        article = ''' 
            <form action="/create/" method="POST">
                <p><input type="text" placeholder="title" name="title"></p>
                <p><textarea name="body" placeholder="body"></textarea></p> 
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        url = '/read/'+str(nextId)
        nextId += 1
        return redirect(url)
@csrf_exempt
def update(request,id):
    global topics
    if request.method =="GET":
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body']
                    }
        article = f'''
            <form action="/update/{id}/" method="POST">
                <p><input type="text" placeholder="title" name="title" value={selectedTopic["title"]}></p>
                <p><textarea name="body" placeholder="body" > {selectedTopic['body']} </textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article,id))
    elif request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}/') # / 언제나 잘 붙여야한다 꼭
    



@csrf_exempt
def delete(request):
    global topics
    if request.method == "POST":
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')