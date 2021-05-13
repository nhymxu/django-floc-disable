class FLoCDisableMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        policy = 'interest-cohort=()'
        if response.get('Permissions-Policy', ''):
            policy = response['Permissions-Policy'] + ', ' + policy

        response['Permissions-Policy'] = policy

        return response
