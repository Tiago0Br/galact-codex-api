import functions_framework
from app.main import app as flask_app

@functions_framework.http
def app(request):
  """
  Esta função age como um 'Proxy'.
  Ela recebe a request do Google Cloud Functions, cria um contexto Flask e processa a rota correta.
  """
  with flask_app.request_context(request.environ):
    try:
      rv = flask_app.preprocess_request()
      if rv is None:
        rv = flask_app.dispatch_request()
    except Exception as e:
      rv = flask_app.handle_user_exception(e)

    response = flask_app.make_response(rv)
    return response.get_data(), response.status_code, response.headers