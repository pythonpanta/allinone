from user.models import User
import json
from .models import Municipality,District,Province,Category
from . import globalparamers
def vendor_register(request):
    json_error = []
    try:
        data = json.loads(request.body)
        print('hello')
        print(data)
        first_name = str(data['firstname']).strip() if 'firstname' else ''
        if not first_name:
            json_error.append("First name can not be blank.")

        last_name = str(data['lastname']).strip() if 'lastname' in data else ''
        if not last_name:
            json_error.append("Last name can not be blank.")

        username = str(data['username']).strip() if 'username' in data else ''
        if not username:
            json_error.append("Username can not be blank.")

        password = data['password'] if 'password' in data else ''
        if not password:
            json_error.append("Password can ntot be blank.")

        email = str(data['email']).strip() if 'email' in data else ''
        if not email:
            json_error.append("Email can not be blank.")
        if User.objects.filter(email=email).exists():
            json_error.append('Email already exist.')

        date_of_birth = str(data['date_of_birth']).strip(
        ) if 'date_of_birth' in data else ''
        if not date_of_birth:
            json_error.append("Date of birth can ntot be blank.")

        gender = str(data['gender']).strip() if 'gender' in data else ''
        if not gender:
            json_error.append("Gender can ntot be blank.")

        phone = str(data['phone']).strip() if 'phone' in data else ''
        if User.objects.filter(phone=phone).exists():
            json_error.append("Phone number must be unique.")
        if not phone:
            json_error.append("Phone can ntot be blank.")
        toll = str(data['toll']).strip() if 'toll' in data else ''
        if not toll:
            json_error.append("Toll can not be blank.")
        pan = str(data['pan']).strip() if 'pan' in data else ''
        if not pan:
            json_error.append("Pan number can not be blank.")
        else:
            if User.objects.filter(pan_number=pan).exists():
                json_error.append("Pan number must be unique.")
            else:
                pass

        products = data['product'] if 'product' else ''
        print(products)
        if not products:
            print('not product')
            json_error.append("Product can not be blank.")
        else:
            for product in products:
                if Category.objects.filter(id=product).exists():
                    print('yes')
                    pass
                else:
                    json_error.append("Select valid product.")
                    break
        province = str(data['province']).strip() if 'province' in data else ''
        if province:
            if Province.objects.filter(id=province).exists():
                province = Province.objects.get(id=province)
                province = province.name
            else:
                json_error.append("Select valid Province.")
        else:
            province = ''
        district = str(data['district']).strip() if 'district' in data else ''
        if district:
            if District.objects.filter(id=district).exists():
                district = District.objects.get(id=district)
                district = district.name
            else:
                json_error.append("Select valid district.")
        else:
            district = ''
        municipality = str(data['municipality']).strip(
        ) if 'municipality' in data else ''
        if municipality:
            if Municipality.objects.filter(id=municipality).exists():
                municipality = Municipality.objects.get(id=municipality)
                municipality = municipality.name
            else:
                json_error.append('Select valid municipality.')
        else:
            municipality = ''
        address = province + ' ' + district + ' ' + municipality
        # address='banepa'

        return json_error, first_name, last_name, username, password, email, date_of_birth, gender, phone, toll, address, pan, products
    except Exception as e:
        # logger.error(str(e), exc_info=True)
        # logger.error(str(e), exc_info=True)
        print('error')
        json_error.append(globalparamers.ERROR_MESSAGE)
        return json_error, None, None, None, None, None, None, None, None, None, None, None, None



def user_register(request):
    json_error = []
    try:
        data = json.loads(request.body) #converting user data into python native data type
        username = str(data['username']).strip() if 'username' in data else ''
        if not username:
            json_error.append("Username can not be blank.")

        password = data['password'] if 'password' in data else ''
        if not password:
            json_error.append("Password can not be blank.")

        email = str(data['email']).strip() if 'email' in data else ''
        if not email:
            json_error.append("Email can not be blank.")
        if User.objects.filter(email=email).exists():
            json_error.append('Email already exist.')

        date_of_birth = str(data['date_of_birth']).strip() if 'date_of_birth' in data else ''
        if not date_of_birth:
            json_error.append("Date of birth can not be blank.")

        gender = str(data['gender']).strip() if 'gender' in data else ''
        if not gender:
            json_error.append("Gender can not be blank.")

        return json_error, username, password, email, date_of_birth, gender
    except Exception as e:
        # logger.error(str(e), exc_info=True)
        # logger.error(str(e), exc_info=True)
        json_error.append(globalparamers.ERROR_MESSAGE)
        return json_error, None, None, None, None, None