from django.contrib.auth import logout

class MyMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # other checks to make sure this middleware should run.
        # eg, this only happens on authenticated URLs

        login_timestamp_ago = timezone.now().timestamp() - request.session.get('login_timestamp', timezone.now().timestamp())

        if settings.RECEPTION_LOGIN_DURATION and <insert user checks here> and login_timestamp_ago >= settings.RECEPTION_LOGIN_DURATION:
            logout(request)  # nukes session
            messages.warning(request, "Your session has expired. We need you to log in again to confirm your identity.")
            return redirect(request.get_full_path())