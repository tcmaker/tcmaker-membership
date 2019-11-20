from django.urls import path
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.index, name='index'),
    path('signout', views.signout, name='signout'),
    # path('account', views.AccountView.as_view(), name='account'),
    # path('contact', views.ContactView.as_view(), name='contact'),
    #
    # # New Signups
    # path('dues', views.DuesView.as_view(), name='dues'),
    # path('dues/card', views.CardView.as_view(), name='card'),
    # path('dues/paypal', views.BraintreeView.as_view(), name='paypal'),
    # path('legal', views.LiabilityWaiverView.as_view(), name='legal'),
    # path('final', views.final, name="final"),
    #
    # # Invitation to join existing membership
    # path('invite/accept/<code>', views.accept_invite, name='invite_accept'),
    # path('invite/account', views.InviteAccountView.as_view(), name='invite_account'),
    # path('invite/contact', views.InviteContactView.as_view(), name='invite_contact'),
    # path('invite/legal', views.InviteLegalView.as_view(), name='invite_legal'),
    # path('invite/final', views.invite_final, name='invite_final'),
]
