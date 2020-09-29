from django.urls import path

from employee.views import main_page, empl, create_empl, create_acc
urlpatterns = [
    path('empl/', main_page),
    path('empl/<id>', empl, name='employee'),
    path('createempl/', create_empl),
    path('createacc/<id>', create_acc, name='createacc'),

]
