import json
from rest_framework.authtoken.models import Token
from user.models import User
import logging
import base64
from django.contrib.auth.hashers import check_password
def login_validation(request, pk):
    json_error = []
    try:
        auth_header = request.META['HTTP_AUTHORIZATION']
        print('one')
        print(auth_header)
        encoded_credentials = auth_header.split(' ')[1]
        print("encoded: ", encoded_credentials)
        decoded_credentials = base64.b64decode(
            encoded_credentials).decode("utf-8").split(':')
        print('decode:', decoded_credentials)
        email = decoded_credentials[0]
        print('email:', email)
        password = decoded_credentials[1]
        print('password:', password)
        try:
            user = User.objects.get(email=email, is_active=True)
            if User.objects.filter(email=email, is_active=True).exists():
                user_password = user.password
                match_password = check_password(password, user_password)
                if not match_password:
                    json_error.append("Invalid password.")
                else:
                    pass
            else:
                json_error.append("incorrect email.")

        except User.DoesNotExist as e:
            # logger.error(str(e), exc_info=True)
            json_error.append("No such user.")

    except Exception as e:
        # logger.error(str(e), exc_info=True)
        json_error.append("No such user.")
    return json_error, email, password