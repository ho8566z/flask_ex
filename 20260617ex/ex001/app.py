from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')     # @app.route('/mail') = mail 서비스로 전환
def home():
    return "<h1>Hello, Flask</h1>"

# http://127.0.0.1:5000/hello
@app.route('/hello')
def hello():
    return "Hello, WWW"

# http://127.0.0.1:5000/me
@app.route('/me')
def me():
    return "It's me, flask engineer"

# http://127.0.0.1:5000/about
@app.route('/about')
def about():
    return 'First List Page'

# http://127.0.0.1:5000/users
# @app.route('/users')
# def get_user():
#     return 'user search'

# http://127.0.0.1:5000/users/10
# 동적 URL 처리(Path Parameter)
# int : 정수
@app.route('/users/<int:user_id>')
def get_user(user_id):
    if user_id == 1:
        # print(f'user_id: {user_id}st')
        return f'{user_id}st : user search'

    elif user_id == 2:
        return f'{user_id}nd : user search'

    elif user_id == 3:
        return f'{user_id}rd : user search'

    else:
        return f'{user_id}th : user search'

# http://127.0.0.1:5000/users/gildong
# 동적 URL 처리(Path Parameter)
# string : 문자열
@app.route('/users/<string:name>')
def get_name(name):
    return f'{name}님의 요청'

# http://127.0.0.1:5000/pi/3.14
# 동적 URL 처리(Path Parameter)
# float : 실수
@app.route('/pi/<float:pi>')
def get_pi(pi):
    return f'pi : {pi}'

# http://127.0.0.1:5000/files/res/imges/cat.jpg
# 동적 URL 처리(Path Parameter)
# path : 전체 경로를 지정(중간에 /가 있어도 문자열 끝까지 받는다)
@app.route('/files/<path:filepath>')
def files(filepath):
    return f'filepath : {filepath}'

##================================================================================#
##================================================================================#

# HTTP Method(요청 방식)

# GET 방식
 
# # 경로 변수 (path variable)
# # http://127.0.0.1:5000/search/weather
# @app.route('/search/<string:keyword>')
# def search(keyword):
#     return f'keyword : {keyword}'

# # http://127.0.0.1:5000/search/10
# @app.route('/search/<int:no>', methods=['GET'])
# def search(no):
#     return f'{no} 사용자'

# 쿼리 스트링 (query string)
# http://127.0.0.1:5000/search?keyword=weather&datetime=2026
@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    datetime = request.args.get('datetime')
    return f'keyword? : {keyword}, datetime : {datetime}'

# # http://127.0.0.1:5000/search?uNo=10
# @app.route('/search', methods=['GET'])
# def search():
#     uNo = request.args.get('uNo')
#     return f'{uNo} 번째 사용자'

##================================================================================#

# POST 
# http://127.0.0.1:5000/login_form
@app.route("/login_form")
def login_form():
    # str = ''
    # str += '<form action="/login_confirm" method="post">'
    # str += '    <input type="text" name="u_id" placeholder="Input user ID">'
    # str += '<br>'
    # str += '    <input type="password" name="u_pw" placeholder="Input user PW">'
    # str += '<br>'
    # str += '    <input type="submit" value="LOG_IN">'
    # str += '</form>'

    # return str

    return'''
    <form action="/login_confirm" method="post">
        <input type="text" name="u_id" placeholder="Input user ID">
    <br>
        <input type="password" name="u_pw" placeholder="Input user PW">
    <br>
        <input type="submit" value="LOG_IN">
    </form>
    '''

@app.route('/login_confirm', methods=["POST"])      # methods=["POST", "PUT", "DELETE", "GET"]
def login_confirm():

    u_id = request.form.get('u_id')
    u_pw = request.form.get('u_pw')

    if u_id == 'gildong' and u_pw == '1234':
        return f"Good <br> {u_id} - LOG_IN : COMPLETE"
    else:
        return f"{u_id} : It's Bad, because ... "



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
