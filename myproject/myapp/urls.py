from django.urls import path
from .views import home,user,micart,kidscart,mainpage,mobile,women,onepluscart,fash,lapcart,mencart
from .views import buy,usercart_details,offr,cartdet,samscart,oppocart,sareecart,kurticart,westcart
from .views import watchcart,hdcart,earcart,tvcart,accart,rfcart,head,add,add2,buy2
urlpatterns = [
    path('',home,name='home'),
    path('user/',user,name='user'),
    path('main/',mainpage,name='main'),
    path('mobile/',mobile,name='mobile'),
    path('fash/', fash, name='fash'),
    path('lap/', lapcart, name='lap'),
    path('hd/', hdcart, name='hd'),
    path('buy/', buy, name='buy'),
    path('cart/', usercart_details, name='cart'),
    path('ofr/', offr, name='ofr'),
    path('iphn/',cartdet, name='iphn'),
    path('one/', onepluscart, name='one'),
    path('oppo/', oppocart, name='oppo'),
    path('sam/', samscart, name='sam'),
    path('mi/', micart, name='mi'),
    path('women/', women, name='women'),
    path('saree/', sareecart, name='saree'),
    path('kurt/', kurticart, name='kurt'),
    path('west/', westcart, name='west'),
    path('men/', mencart, name='men'),
    path('kids/', kidscart, name='kids'),
    path('wat/', watchcart, name='wat'),
    path('ear/', earcart, name='ear'),
    path('tv/', tvcart, name='tv'),
    path('ac/', accart, name='ac'),
    path('rf/', rfcart, name='rf'),
    path('head/', head, name='head'),
    path('add/', add, name='add'),
    path('add2/', add2, name='add2'),
    path('buy2/', buy2, name='buy2'),



]
