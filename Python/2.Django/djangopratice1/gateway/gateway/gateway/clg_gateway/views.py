import logging
import requests
import json
import base64
from requests.auth import HTTPBasicAuth

from django.http import JsonResponse

from rest_framework.decorators import APIView
from rest_framework import status

from gateway.settings import API_URL
from . import globalparamers
logger = logging.getLogger('django')


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            auth_header = request.META['HTTP_AUTHORIZATION']
            encoded_credentials = auth_header.split(' ')[1]
            print("encoded: ", encoded_credentials)

            decoded_credentials = base64.b64decode(
                encoded_credentials).decode("utf-8").split(':')
            email = decoded_credentials[0]
            password = decoded_credentials[1]
            url = "".join([API_URL, '/login'])
            print(url)
            response = requests.post(
                url=url, headers=request.headers, auth=HTTPBasicAuth(email, password))
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VendorSignupView(APIView):
    def post(self, request):
        try:
            url = "".join([API_URL, '/vendor/register'])
            response = requests.post(
                url=url, headers=request.headers, data=request.body)
            print(response.text)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductCreateView(APIView):
    def post(self, request):
        try:
            url = "".join([API_URL, '/product/create'])
            response = requests.post(
                url=url, headers=request.headers, data=request.body)
            print(response.text)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
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
        try:
            url = "".join([API_URL, '/product/list'])
            response = requests.get(url=url, headers=request.headers)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
            url = "".join([API_URL, '/province/list'])
            response = requests.get(url=url, headers=request.headers)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DistrictListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            url = "".join([API_URL, '/district/list'])
            data = request.GET.get("data", None)
            print("data", data)
            response = requests.get(
                url=url, headers=request.headers, params=request.query_params)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MunicipalityListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            url = "".join([API_URL, '/municipality/list'])
            response = requests.get(
                url=url, headers=request.headers, params=request.query_params)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
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
            url = "".join([API_URL, '/category/list'])
            response = requests.get(url=url, headers=request.headers)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserCategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            url = "".join([API_URL, '/user/category/list'])
            response = requests.get(url=url, headers=request.headers)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubProductListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            url = "".join([API_URL, '/sub/product/list'])
            data = request.GET.get("data", None)
            print("data", data)
            response = requests.get(
                url=url, headers=request.headers, params=request.query_params)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VendorProductListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            url = "".join([API_URL, '/vendor/product/list'])
            response = requests.get(url=url, headers=request.headers)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OrderCreateView(APIView):
    def post(self, request):
        try:
            url = "".join([API_URL, '/order/create'])
            response = requests.post(
                url=url, headers=request.headers, data=request.body)
            print(response.text)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserRegisterView(APIView):
    def post(self, request):
        try:
            url = "".join([API_URL, '/user/register'])
            response = requests.post(
                url=url, headers=request.headers, data=request.body)
            print(response.text)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OtpGenerateView(APIView):
    def post(self, request):
        try:
            url = "".join([API_URL, '/otp/generate'])
            response = requests.post(
                url=url, headers=request.headers, data=request.body)
            print(response.text)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EachVendorListView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            url = "".join([API_URL, '/each/vendor/list'])
            response = requests.get(url=url, headers=request.headers)
            return JsonResponse(response.json(), status=response.status_code)
        except requests.ConnectionError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except requests.HTTPError:
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.CONNECTION_ERROR
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            logger.error(str(e), exc_info=True)
            message = {
                globalparamers.RESULT_CODE: globalparamers.UNSUCESS_CODE,
                globalparamers.RESULT_DESCRIPTION: globalparamers.ERROR_MESSAGE
            }
            return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
