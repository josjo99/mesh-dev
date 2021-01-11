from django.urls import path
from registeration.views import(

	registration_view,

)

app_name = 'registeration'

urlpatterns = [
	path('register', registration_view, name="register"),
]

