from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application

# Configurações básicas do Django
settings.configure(
    DEBUG=False,                
    SECRET_KEY='CHAVE_SECRETA',  
    ALLOWED_HOSTS=['*'],        
    ROOT_URLCONF=__name__,      
    MIDDLEWARE_CLASSES=(),     
)

# View simples
def index(request):
    return HttpResponse("Hello world!")  # Retornar uma resposta HTTP simples

# Configuração de URL
urlpatterns = [
    path('', index),  # Mapear a URL raiz para a view index
]

# Aplicação WSGI
application = get_wsgi_application()

# Servidor WSGI
if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    httpd = make_server('', 80, application)  # Servir a aplicação usando o servidor WSGI na porta 80
    print("Servidor Django executando na porta 80...")
    httpd.serve_forever()  # Iniciar o servidor