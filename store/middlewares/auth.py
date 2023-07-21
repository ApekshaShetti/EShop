from django.shortcuts import redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # to go from login page directly to orders page as middleware is applied so i cannot go to order page without login
        returnURL = request.META['PATH_INFO']
        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnURL}')
        response = get_response(request)
        return response
    return middleware