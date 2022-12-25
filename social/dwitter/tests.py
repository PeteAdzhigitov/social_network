import pytest
from django.contrib.auth.models import User
from django.test import Client

from .forms import DweetForm
from .views import DashboardList
#
# import sys
# # sys.path.append(r'C:\Users\79851\Desktop\social_network\social')
# from social.users import forms

# Create your tests here.





    # @pytest.mark.django_db(databases=['default'])
    # def test_user_in_db(self):
    #     # all_users = User.objects.all()
    #     # print(all_users)
    #     me = User.objects.get(username='socialadmin3')
    #     assert me.is_superuser

# @pytest.mark.django_db(databases=['default'])
# def test_with_authenticated_client(client, django_user_model):
#     # username = "user1"
#     # password = "bar"
#     # user = djangodjango.core.exceptions.ImproperlyConfigured: URL route 'profile/<iwnt:pk>' uses invalid converter 'iwnt'._user_model.objects.create_user(username=username, password=password)
#     # client = Client()
#     # Use this:
#     # client.login(username='socialadmin3', password='Testing321')
#     # Or this:
#     # client.login(username=username, password=password)
#     response = client.get('/')
#     assert response.url == '/login/?next=/'
    # @pytest.mark.django_db
    # def test_correctness_of_view_url(self):
    #     client = Client()
    #     response = client.get('/')
    #     assert response.status_code == 200
from .models import Dweet


# @pytest.mark.django_db(databases=['default'])
# def test_user_cannot_change_not_his_own_dweets(client, django_user_model):
#
#     client = Client()
#     client.login(username='socialadmin3', password='Testing321')
#     dweets = Dweet.objects.exclude(user=User.objects.get(username='socialadmin3'))
#     b = dweets[2].id
#     response = client.get('/dweet_update/{0}'.format(b))

    # assert response.status_code == 403
# @pytest.mark.django_db(databases=['default'])
# def test_login(client, django_user_model):
#     client = Client()
#     client.login(username='socialadmin3', password='Testing321')
#     current_user = User.objects.get(username='socialadmin3')
#     response = client.get('/')
#     # assert response.resolver_match.func.view_class == DashboardList
#     # assert response.content
#     text = b'Here will be displayed your or your followers'
#     assert text in response.content


#
# def test_form_validation(client, django_user_model):
#     from social.users.forms import CustomRegistrationForm
#     form = CustomRegistrationForm(data={'username':'Petyan33','email':'aaa@aa.ru','password1':'Testing123', 'password2':'Testing123'})
#
#     assert form.is_valid()



# def is_palindrome(text):
#     a = text[:]
#     b= text[-1:]
#     if a == b:
#         return True
#     return False
#
# text = 'abba'
# print(is_palindrome(text))



# class Singleton:
#     __instance = None
#     def __new__(cls):
#         if (cls.__instance is None):
#             cls.__instance = super(Singleton, cls).__new__(cls)
#         return cls.__instance
#
#
# s1 = Singleton()
# print(s1)
# s2 = Singleton()
# print(s2)




