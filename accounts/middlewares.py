import jwt
from django.http import JsonResponse
from django.conf import settings

class TokenValidationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request path is excluded from token validation
        excluded_prefixes = ['/']
        for prefix in excluded_prefixes:
            if request.path_info.startswith(prefix):
                return self.get_response(request)

        # Check if the Authorization header is present
        authorization_header = request.headers.get('Authorization', None)
        if not authorization_header:
            return JsonResponse({'error': 'Authorization header missing'}, status=401)

        # Check if the Authorization header has the correct format (Bearer <token>)
        parts = authorization_header.split()
        if len(parts) != 2 or parts[0] != 'Bearer':
            return JsonResponse({'error': 'Invalid Authorization header format'}, status=401)

        # Extract the token from the Authorization header
        token = parts[1]

        try:
            # Verify the token using the SECRET_KEY
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            # Optionally, you can perform additional checks here, such as checking token expiration, user permissions, etc.

            # Attach the decoded token data to the request for later use if needed
            request.decoded_token = decoded_token

        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        # Pass the request through if the token is valid
        return self.get_response(request)
