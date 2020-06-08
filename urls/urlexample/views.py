from django.http import HttpResponse
def profile(request, username='Default User'):
    return HttpResponse('<h1>This is the profile page! The user is {}</h1>'.format(username))

def article(request, article_value):
    return HttpResponse('<h1>The article name is {}'.format(article_value))
