from django.conf import settings

def baseurl(request):
    """
    Return a BASE_URL template context for the current request.
    """
    return {'BASE_URL': settings.BASE_URL}
