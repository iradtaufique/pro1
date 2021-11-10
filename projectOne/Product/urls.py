from django.urls import path
from Product.views import home_view, empDetails, contact, about


urlpatterns = [
    path('', home_view, name='home'),
    path('employee/<int:id>', empDetails, name='employee_details'),
    path('contact/', contact, name='contact_page'),
    path('about/', about, name='about_page'),
]
