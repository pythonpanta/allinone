from django.shortcuts import render,HttpResponse
from rest_framework.decorators import APIView
from .models import District,Province,Municipality,Category,SubCategory,Product
from .import globalparamers
from rest_framework import status
from django.http import JsonResponse
import base64
from user.models import Role, User
from django.db import transaction
from . import validations
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from . import login_auth



# Create your views here.


class DistrictListView(APIView):
    # http://127.0.0.1:8000/district/list/?data=1
    def get(self, request, *args, **kwargs):
        try:
            province_id = request.query_params.get("data", None)
            # province_id = request.GET.get("data", None)
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
            # message = custom_exception.custom_exception(request, e)
            print('Error')
            print(e)

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
            # message = custom_exception.custom_exception(request, e)
            print('Error')
            print(e)

class MunicipalityListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            province_id = request.query_params.get("data", None)
            district_id = request.query_params.get("data1", None)
            print(province_id,district_id)
            municipalitys = Municipality.objects.filter(
                province_id=province_id, district_id=district_id)
            print(municipalitys)
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
            # message = custom_exception.custom_exception(request, e)
            print(e)

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
            # message = custom_exception.custom_exception(request, e)
            print(e)
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
            # message = custom_exception.custom_exception(request, e)
            return JsonResponse({'message':'error'}, status=status.HTTP_400_BAD_REQUEST)
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
            # logger.error(str(e), exc_info=True)
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
                    'message':'you need to have data for registration'
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            (json_error, username, password, email, date_of_birth, gender) = validations.user_register(
                request)
            # print(json_error, username, password, email, date_of_birth, gender)
            if json_error:
                message = {
                    globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                    globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION,
                    "error": json_error
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            with transaction.atomic():
                role = Role.objects.get(role='USER')
                # print(role)
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
            print(e)
            # message = custom_exception.custom_exception(request, e)
            return JsonResponse({'message':'error'}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        try:
            json_error, email, password = login_auth.login_validation(
                request, None)
            print(email)
            print(password)
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
            print(e)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.UNSUCCESS_RESULT_DESCRIPTION
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            # logger.error(str(e), exc_info=True)
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
                    'message':'data is needed for registration'
                }
                return JsonResponse(message, status=status.HTTP_400_BAD_REQUEST)
            (json_error, first_name, last_name, username, password, email, date_of_birth,
             gender, phone, toll, address, pan, products) = validations.vendor_register(
                request)
            print(json_error, first_name, last_name, username, password, email, date_of_birth,
             gender, phone, toll, address, pan, products)
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
            # message = custom_exception.custom_exception(request, e)
            return JsonResponse({'message':'error'}, status=status.HTTP_400_BAD_REQUEST)