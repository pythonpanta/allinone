import email
import random
import smtplib
from . import custom_exception
from . models import Product, Order, Customer, Province, District, Municipality, Category, SubCategory
from . import login_auth
from . import validations
from user.models import Role, User
from rest_framework.decorators import APIView, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import exceptions, status
from django.db import transaction
from django.contrib.auth import authenticate
from django.http import JsonResponse
import base64
from datetime import datetime
from requests import JSONDecodeError, request

from .import globalparamers
import json
import logging
import uuid


logger = logging.getLogger('django')
# Create your views here.


class LoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        try:
            json_error, email, password = login_auth.login_validation(
                request, None)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    'error': json_error
                }
                return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
            user = authenticate(request, email=email, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                message = {
                    "username": user.username,
                    "email": user.email,
                    "mobileNumber": user.phone,
                    "token": token.key
                }
                return JsonResponse(message, status=status.HTTP_200_OK)
            else:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: "No such user."
                }
                return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
        except ValueError as e:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductListView(APIView):
    def get(self, request, *args, **kwargs):
        permission_classes = []
        try:
            product_list = []
            products = Product.objects.filter(is_void=False)
            for product in products:
                product_list.append({
                    "name": product.name,
                    "price": product.price,
                    "photo": base64.b64encode(product.photo).decode("utf-8") if product.photo else None,
                    "description": product.description,
                    "date_created": product.manufactured_date,
                    "status": product.status
                })

            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": product_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ForgorPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        if not request.body:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.NO_REQUEST_BODY
            }
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        try:
            json_error, email, password = login_auth.forgot_password_validation(
                request, None)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.filter(email=email, is_active=True)
            if user.exists():
                try:
                    user = User.objects.get(email=email, is_active=True)
                    user.set_password(password)
                    user.save()
                    message = {
                        "resut_code": "password successfully changed."
                    }
                    return JsonResponse(message, status=status.HTTP_200_OK)
                except User.DoesNotExist as e:
                    logger.error(str(e), exc_info=True)
                    message = {
                        globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                        globalparamers.RESULT_DESCRIPTION: globalparamers.ID_DOES_NOT_EXIT,
                    }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            else:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(APIView):
    def post(self, request, *args, **kwargs):
        if not request.body:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.NO_REQUEST_BODY
            }
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        try:
            json_error, email, password, first_name, last_name, phone = validations.user_create_register_validation(
                request, None)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    print("ssssssssss")
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print("user", request.user)
        if not request.body:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.NO_REQUEST_BODY
            }
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        try:
            json_error, user = login_auth.auth_validation(request)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
            (json_error, product_name, product, sub_product, description, product_prize,
             manufactured_date, image) = validations.product_validation(request, None)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_404_NOT_FOUND)
            print(user)
            created_by = User.objects.get(id=user)
            print("ddd", created_by)
            with transaction.atomic():
                category = Category.objects.get(id=product)
                sub_category = SubCategory.objects.get(id=sub_product)
                Product.objects.create(name=product_name,
                                       price=product_prize,
                                       description=description,
                                       category=category,
                                       sub_category=sub_category,
                                       photo=image,
                                       manufactured_date=manufactured_date,
                                       created_by_id=created_by
                                       )
                message = {
                    globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.DATA_CREATE
                }
                return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VendorRegister(APIView):
    def post(self, request, *args, **kwargs):
        try:
            if not request.body:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.INVALID_REQUEST_BODY,
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            (json_error, first_name, last_name, username, password, email, date_of_birth,
             gender, phone, toll, address, pan, products) = validations.vendor_register(
                request)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            with transaction.atomic():
                role = Role.objects.get(role='VENDOR')
                user = User.objects.create_user(email=email,
                                                username=username,
                                                phone=phone,
                                                date_of_birth=date_of_birth,
                                                gender=gender,
                                                first_name=first_name,
                                                last_name=last_name,
                                                address=address,
                                                location=toll,
                                                pan_number=pan,
                                                role=role
                                                )
                for product in products:
                    category = Category.objects.get(id=product)
                    user.category.add(category)
                user.set_password(password)
                user.save()
                message = {
                    globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.DATA_CREATE
                }
                return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)


class UserRecommendationView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        try:
            json_error, user = login_auth.auth_validation(request)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
            product_list = []
            products = Product.objects.filter(is_void=False)
            for product in products:
                product_list.append({
                    "name": product.name,
                    "price": product.price,
                    "photo": base64.b64encode(product.photo).decode("utf-8") if product.photo else None,
                    "description": product.description,
                    "date_created": product.date_created.date()
                })
            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": product_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProvinceListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            provinces = Province.objects.all()
            province_list = []
            for province in provinces:
                province_list.append({
                    "id": province.id,
                    "name": province.name
                })
            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": province_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)


class DistrictListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            province_id = request.query_params.get("data", None)
            districts = District.objects.filter(province_id=province_id)
            district_list = []
            for district in districts:
                district_list.append({
                    "id": district.id,
                    "name": district.name
                })
            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": district_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)


class MunicipalityListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            province_id = request.query_params.get("data", None)
            district_id = request.query_params.get("data1", None)
            municipalitys = Municipality.objects.filter(
                province_id=province_id, district_id=district_id)
            municipality_list = []
            for municipality in municipalitys:
                municipality_list.append({
                    "id": municipality.id,
                    "name": municipality.name
                })
            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": municipality_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)


class VendorSignupView(APIView):
    def post(self, request, *args, **kwargs):
        if not request.body:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.NO_REQUEST_BODY
            }
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        try:
            (json_error, name, description,
             product_prize, manufactured_date, image) = validations.product_validation(request, None)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_404_NOT_FOUND)
            import datetime
            created_by = User.objects.get(
                id='ba7d387f38964f1fb62e1e5c5b3b3b6b')
            Product.objects.create(name=name,
                                   price=product_prize,
                                   description=description,
                                   photo=image,
                                   date_created=datetime.datetime.now(),
                                   created_by=created_by
                                   )
            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.DATA_CREATE
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            categorys = Category.objects.all()
            category_list = []
            for category in categorys:
                category_list.append({
                    "id": category.id,
                    "name": category.name
                })
            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": category_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)


class UserCategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', None)
            token = Token.objects.get(key=token)
            user = token.user_id
            categorys = User.objects.filter(
                id=user).values('category')
            category_list = []
            for category in categorys:
                user_category = Category.objects.get(id=category['category'])
                category_list.append({
                    "id": category['category'],
                    "name": user_category.name
                })
            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": category_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = custom_exception.custom_exception(request, e)
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)


class SubProductListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            category_id = request.query_params.get("data", None)
            categorys = SubCategory.objects.filter(category=category_id)
            sub_category_list = []
            for category in categorys:
                sub_category_list.append({
                    "id": category.id,
                    "name": category.name
                })
            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": sub_category_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)


class VendorProductListView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        try:
            json_error, user = login_auth.auth_validation(request)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
            if not user:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
            product_list = []
            products = Product.objects.filter(
                is_void=False, created_by=request.user)

            for product in products:
                product_list.append({
                    "name": product.name,
                    "price": product.price,
                    "photo": base64.b64encode(product.photo).decode("utf-8") if product.photo else None,
                    "description": product.description,
                    "date_created": product.manufactured_date,
                    "status": product.status
                })

            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": product_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        if not request.body:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.NO_REQUEST_BODY
            }
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
        try:
            (json_error, product_name, product, sub_product, description, product_prize,
             manufactured_date, image) = validations.order_validation(request, None)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_404_NOT_FOUND)
            created_by = User.objects.get(
                id='ba7d387f38964f1fb62e1e5c5b3b3b6b')
            with transaction.atomic():
                category = Category.objects.get(id=product)
                sub_category = SubCategory.objects.get(id=sub_product)
                Product.objects.create(name=product_name,
                                       price=product_prize,
                                       description=description,
                                       category=category,
                                       sub_category=sub_category,
                                       photo=image,
                                       manufactured_date=manufactured_date,
                                       created_by=created_by
                                       )
                message = {
                    globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.DATA_CREATE
                }
                return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserRegister(APIView):
    def post(self, request, *args, **kwargs):
        try:
            if not request.body:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.INVALID_REQUEST_BODY,
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            (json_error, username, password, email, date_of_birth, gender) = validations.user_register(
                request)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            with transaction.atomic():
                role = Role.objects.get(role='USER')
                user = User.objects.create_user(email=email,
                                                username=username,
                                                date_of_birth=date_of_birth,
                                                gender=gender,
                                                role=role
                                                )
                user.set_password(password)
                user.save()
                message = {
                    globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.DATA_CREATE
                }
                return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)


class OtpGenerateListView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            json_error = []
            data = json.loads(request.body)
            print(data)
            confirm_email = str(data['confirmEmail']).strip(
            ) if 'confirmEmail' in data else ''
            if not confirm_email:
                json_error.append('Email can not be blank')
            else:
                if User.objects.filter(email=confirm_email).exists():
                    pass
                else:
                    json_error.append("Please send correct email.")
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            with transaction.atomic():
                user = User.objects.get(email=confirm_email)
                globalparamers.CONFIRM_EMAIL.clear()
                globalparamers.CONFIRM_EMAIL.append(user)
                otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('anishbista2056@gmail.com', 'lrekhlrgnapjwjkz')
                msg = f"hello{confirm_email} your otp code is {str(otp)}"
                server.sendmail("anishbista2056@gmail.com", confirm_email, msg)
                server.quit()
                user.otp = otp
                user.save()
                message = {
                    globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                    "data": user
                }
                return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)


class OtpConfirmView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            json_error = []
            data = json.loads(request.body)
            print(data)
            confirm_email = str(data['confirmEmail']).strip(
            ) if 'confirmEmail' in data else ''
            if not confirm_email:
                json_error.append('Email can not be blank')
            else:
                if User.objects.filter(email=confirm_email).exists():
                    pass
                else:
                    json_error.append("Please send correct email.")
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            with transaction.atomic():
                user = User.objects.get(email=confirm_email)
                globalparamers.CONFIRM_EMAIL = user
                otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('anishbista2056@gmail.com', 'lrekhlrgnapjwjkz')
                msg = f"hello{confirm_email} your otp code is {str(otp)}"
                server.sendmail("anishbista2056@gmail.com", confirm_email, msg)
                server.quit()
                user.otp = otp
                user.save()
                message = {
                    globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                }
                return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            json_error = []
            data = json.loads(request.body)
            print(data)
            confirm_email = str(data['confirmpassword']).strip(
            ) if 'confirmEmail' in data else ''
            if not confirm_email:
                json_error.append('Email can not be blank')
            else:
                if User.objects.filter(email=confirm_email).exists():
                    pass
                else:
                    json_error.append("Please send correct email.")
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            with transaction.atomic():
                user = User.objects.get(email=confirm_email)
                globalparamers.CONFIRM_EMAIL = user
                otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('anishbista2056@gmail.com', 'lrekhlrgnapjwjkz')
                msg = f"hello{confirm_email} your otp code is {str(otp)}"
                server.sendmail("anishbista2056@gmail.com", confirm_email, msg)
                server.quit()
                user.otp = otp
                user.save()
                message = {
                    globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                }
                return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            message = custom_exception.custom_exception(request, e)
            return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)


class EachVendorListView(APIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        try:
            json_error, user = login_auth.auth_validation(request)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_401_UNAUTHORIZED)
            product_list = []
            products = Product.objects.filter(
                is_void=False, created_by_id=user)
            for product in products:
                product_list.append({
                    "name": product.name,
                    "price": product.price,
                    "description": product.description,
                    "manufactured_date": product.manufactured_date,
                    "status": product.status,
                    "category": product.category.name if product.category else None,
                    "subcategory": product.sub_category.name if product.sub_category else None
                })

            message = {
                globalparamers.RESULT_CODE: globalparamers.SUCCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.SUCCESS_RESULT_DESCRIPTION,
                "data": product_list
            }
            return JsonResponse(message, status=status.HTTP_200_OK)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
