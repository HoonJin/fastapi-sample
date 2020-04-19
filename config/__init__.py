from starlette.config import Config

# 앱 실행시 uvicorn main:app --reload --env-file resources/.env
# 식으로 파일을 지정할 수 있다.
# 지정시에는 파라미터로 지정한 파일이 더 우선순위가 높다.
# 환경변수로 선언되어있는 경우에는 환경변수의 우선순위가 더 높다.
# 패키지의 순환 구조를 막기 위해서 config package 를 따로 만들고 여기에서 import 해 사용하도록 함.

conf = Config('resources/.env')

SECRET_KEY = conf.get('SECRET_KEY', str)
