from django.urls import path
from . import views


urlpatterns = [
    #sets the url path to home page index.html
    path('', views.home, name='index'),
    # sets the url path to create new account page createnewaccount.html
    path('create/', views.create_account, name='create'),
    # sets the url path to balance sheet page balancesheet.html
    path('<int:pk>/balance/', views.balance, name='balance'),
    # sets the url path to add new transaction page addnewtransaction.html
    path('transaction/', views.transaction, name='transaction')

]
