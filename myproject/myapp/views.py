from django.shortcuts import render, redirect
from .form import UserForm, cartForm
from django.contrib.auth.hashers import check_password
from django.db.models import Sum
from .models import Regi, productlist, cartlist
from django.core.mail import send_mail
from myproject.settings import EMAIL_HOST_USER


def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        customer = Regi.get_user_by_username(username)
        print(customer)
        print(username, password)
        error_message = None
        if customer:
            f = check_password(password,  customer.password)
            print(customer.password)
            if password == customer.password:
                return redirect('main')
            else:
                error_message = 'User Name Or Password Invalid !!'
        else:
            error_message = 'User Name Or Password Invalid !!'
        return render(request, 'home.html', {'error': error_message})


def user(request):
    s = UserForm()

    if request.method == 'POST':

        if s == " ":
            text = {'form': s}
            return render(request, 'newuser.html', text)
        else:
            s = UserForm(request.POST)
            subject = "Greetings"
            msg = "Hello we welcome you here in our Tierra Eshop!!!"
            recepient = str(s['Email_Id'].value())
            send_mail(subject, msg, EMAIL_HOST_USER, [recepient], fail_silently=False)
            if s.is_valid():
                s.save()
            st = Regi.objects.all()
            t = {'recepient': recepient, 'form': s, 'stu': st}
            return render(request, 'reciuser.html', t)
    text = {'form': s}
    return render(request, 'newuser.html', text)


def mainpage(request):
    return render(request, 'main.html')


def head(request):
    return render(request, 'head.html')


def buy(request):
    return render(request, 'buy.html')

def buy2(request):
    return render(request, 'buy2.html')


def cartdet(request):
    c = cartForm()
    w = request.POST.get('iphone')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('iphone', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["AppleiPhone12ProMax", "AppleiPhoneX", "AppleiPhone11", "AppleiPhone8", "AppleiPhone12Mini",
                            "AppleiPhone7", "AppleiPhoneSE", "AppleiPhoneXRs", "AppleiPhoneXSMax", "AppleiPhone7Plus",
                            "AppleiPhone11Pro", "AppleiPhone6sPlus"]:
                    if item == "AppleiPhone12ProMax":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "AppleiPhoneX":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "AppleiPhone11":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "AppleiPhone8":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "AppleiPhone12Mini":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "AppleiPhone7":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "AppleiPhoneSE":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "AppleiPhoneXRs":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "AppleiPhoneXSMax":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "AppleiPhone7Plus":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "AppleiPhone11Pro":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "AppleiPhone6sPlus":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'iphone.html', text)
    return render(request, 'iphone.html')


def usercart_details(request):
    user_cart = cartForm()
    total_price = cartlist.objects.aggregate(Sum('price'))
    print(total_price)
    if request.method == 'POST':
        object = request.POST.get('item',None)
        cartlist.objects.filter(item=object).delete()
        return redirect('cart')
    all_items = cartlist.objects.all()
    total_price = sum(all_items.values_list('price', flat=True))
    text = {'form': user_cart, 'total_price': total_price, 'all_items': all_items}
    return render(request, 'cart.html', text)


def onepluscart(request):
    c = cartForm()
    w = request.POST.get('oneplus')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('oneplus', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["OnePlusSNord", "OnePlus8T", "OnePlus9R", "OnePlus9", "OnePlus9Pro", "OnePlus8Pro",
                            "OnePlus5", "OnePlus6T", "OnePlus7T", "OnePlus7TPro", "OnePlus6", "OnePlus7Pro"]:

                    if item == "OnePlusSNord":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "OnePlus8T":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "OnePlus9R":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "OnePlus9":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "OnePlus9Pro":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "OnePlus8Pro":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "OnePlus5":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "OnePlus6T":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "OnePlus7T":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "OnePlus7TPro":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "OnePlus6":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "OnePlus7Pro":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == ' ':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'Oneplus.html', text)
    return render(request, 'Oneplus.html')


def oppocart(request):
    c = cartForm()
    w = request.POST.get('oppo')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('oppo', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["OPPORenoPro", "OPPOFindX", "OPPOReno4Pro", "OPPOReno2Z", "OPPOReno2", "OPPOReno3Pro",
                            "OPPOF19Pro", "OPPOA12", "OPPOA31", "OPPOA53", "OPPOA1K", "OPPOA9"]:

                    if item == "OPPORenoPro":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "OPPOFindX":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "OPPOReno4Pro":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "OPPOReno2Z":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "OPPOReno2":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "OPPOReno3Pro":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "OPPOF19Pro":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "OPPOA12":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "OPPOA31":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "OPPOA53":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "OPPOA1K":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "OPPOA9":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == ' ':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)

        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'oppo.html', text)
    return render(request, 'oppo.html')


def samscart(request):
    c = cartForm()
    w = request.POST.get('sams')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('sams', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["SAMSUNGGalaxyF41", "SAMSUNGGalaxyNote20Ultra", "SAMSUNGGalaxyNote10Lite",
                            "SAMSUNGGalaxyM31", "SAMSUNGGalaxyF62", "SAMSUNGGalaxyA12", "SAMSUNGGalaxyA12s",
                            "SAMSUNGGalaxyA72", "SAMSUNGGalaxyA32", "SAMSUNGGalaxyM01", "SAMSUNGGalaxyM21",
                            "SAMSUNGGalaxyM11"]:

                    if item == "SAMSUNGGalaxyF41":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "SAMSUNGGalaxyNote20Ultra":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "SAMSUNGGalaxyNote10Lite":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "SAMSUNGGalaxyM31":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "SAMSUNGGalaxyF62":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "SAMSUNGGalaxyA12":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "SAMSUNGGalaxyA12s":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "SAMSUNGGalaxyA72":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "SAMSUNGGalaxyA32":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "SAMSUNGGalaxyM01":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "SAMSUNGGalaxyM21":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "SAMSUNGGalaxyM11":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price,image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'sams.html', text)
    return render(request, 'sams.html')


def micart(request):
    c = cartForm()
    w = request.POST.get('mi')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('mi', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["RedmiNote10ProMax", "Mi10T", "RedmiNote9ProMax", "RedmiNote9", "RedmiNote8", "Redmi9i",
                            "Redmi9Power", "Redmi8", "Redmi8ADual", "Redmi8A", "Redmi9Prime", "Redmi9"]:

                    if item == "RedmiNote10ProMax":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "Mi10T":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "RedmiNote9ProMax":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "RedmiNote9":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "RedmiNote8":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "Redmi9i":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "Redmi9Power":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "Redmi8":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "Redmi8ADual":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "Redmi8A":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "Redmi9Prime":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "Redmi9":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'mi.html', text)
    return render(request, 'mi.html')


def sareecart(request):
    c = cartForm()
    w = request.POST.get('saree')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('saree', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == "cart":
                if item in ["PartyWearHalfSaree", "Georgette", "CottonLinenBlendSaree", "LinenPrintedSaree",
                            "ArtSilkSaree", "GeorgetteSaree", "FloralPrintedSaree", "ANNIDESIGNERSAREE",
                            "BanarasiCottonSilkSaree", "BangloriMalaiSaree", "PureCottonSaree",
                            "PureCottonPrintedSaree"]:

                    if item == "PartyWearHalfSaree":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "Georgette":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "CottonLinenBlendSaree":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "LinenPrintedSaree":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "ArtSilkSaree":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "GeorgetteSaree":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "FloralPrintedSaree":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "ANNIDESIGNERSAREE":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "BanarasiCottonSilkSaree":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "BangloriMalaiSaree":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "PureCottonSaree":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "PureCottonPrintedSaree":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'saree.html', text)
    return render(request, 'saree.html')


def kurticart(request):
    c = cartForm()
    w = request.POST.get('kurti')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('kurti', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["RayonPrintedKurti", "KhadireadymadeKurti", "RayonA-LineKurta", "SoftRayonKurta",
                            "CrepeStraightKurti", "NAINVISHCrepeKurti", "PureCottonStraightKurta",
                            "kalpitcreationsRayonKurta", "AnarkaliKurti", "CottonAnarkaliKurtI", "silkstraightKurti",
                            "EliteEthnicSolidKurta"]:

                    if item == "RayonPrintedKurti":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "KhadireadymadeKurti":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "RayonA-LineKurta":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "SoftRayonKurta":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "CrepeStraightKurti":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "NAINVISHCrepeKurti":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "PureCottonStraightKurta":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "kalpitcreationsRayonKurta":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "AnarkaliKurti":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "CottonAnarkaliKurtI":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "silkstraightKurti":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "EliteEthnicSolidKurta":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == ' ':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'kurt.html', text)
    return render(request, 'kurt.html')


def westcart(request):
    c = cartForm()
    w = request.POST.get('west')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('west', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["JayshreeFashionWesternDress", "MitahaWomen'sTops", "ILLILONDONDress",
                            "SkaterKneeLengthDress", "DenimJacket", "LONDONWomen'sTOP", "RetrobellaPartyBalloonTop",
                            "HarpaWomen'sTop", "MitahaCasualWesternTop", "VEROMODACasualDress", "VEROMODABodyconDress",
                            "SkaterCasualDress"]:

                    if item == "JayshreeFashionWesternDress":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "MitahaWomen'sTops":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "ILLILONDONDress":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "SkaterKneeLengthDress":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "DenimJacket":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "LONDONWomen'sTOP":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "RetrobellaPartyBalloonTop":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "HarpaWomen'sTop":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "MitahaCasualWesternTop":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "VEROMODACasualDress":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "VEROMODABodyconDress":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "SkaterCasualDress":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'west.html', text)
    return render(request, 'west.html')


def mencart(request):
    c = cartForm()
    w = request.POST.get('men')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('men', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["RegularFitCasualShirt", "EYEBOGLERMen'sSolidTshirt", "A-lineKurta", "BREGEOMen'sBlazer",
                            "HoodedHoodies", "DenimJacketForMen", "Cardigan'sforMen", "FormalShirt",
                            "CasualSolidShirts", "LEVIZORegularShirt", "DennisLingoShirt", "DennisLingo"]:
                    if item == "RegularFitCasualShirt":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "EYEBOGLERMen'sSolidTshirt":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "A-lineKurta":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "BREGEOMen'sBlazer":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "HoodedHoodies":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "DenimJacketForMen":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "Cardigan'sforMen":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "FormalShirt":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "CasualSolidShirts":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "LEVIZORegularShirt":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "DennisLingoShirt":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "DennisLingo":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'men.html', text)
    return render(request, 'men.html')


def kidscart(request):
    c = cartForm()
    w = request.POST.get('kids')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('kids', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["TwillDungareeforBoys", "FashionKidsShirt", "DIGIMARTGirl'sKurta", "WingsGirl'sSkirt",
                            "ManaitriGirlsSkirt", "CamouflageT-Shirt", "ClassicFitDenim", "WaistcoatShirt",
                            "T-ShirtsforGirls", "Jumpsuit", "PrintedTshirt", "MidiDress"]:
                    if item == "TwillDungareeforBoys":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "FashionKidsShirt":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "DIGIMARTGirl'sKurta":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "WingsGirl'sSkirt":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "ManaitriGirlsSkirt":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "CamouflageT-Shirt":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "ClassicFitDenim":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "WaistcoatShirt":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "T-ShirtsforGirls":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "Jumpsuit":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "PrintedTshirt":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "MidiDress":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items' : item, 'quantity': quantity, 'image': image, 'price':price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'kids.html', text)
    return render(request, 'kids.html')


def lapcart(request):
    c = cartForm()
    w = request.POST.get('lap')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('lap', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["MicrosoftSurface", "LenovoIdeaPad", "AVITAEssential", "HP15", "ASUSVivoBook14",
                            "HPChromebook14a", "AcerSwift5", "DellVostro3401", "AppleMacBookPro", "AppleMacBookAir",
                            "HPSpectre", "LenovoYoga"]:
                    if item == "MicrosoftSurface":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "LenovoIdeaPad":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "AVITAEssential":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "HP15":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "ASUSVivoBook14":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "HPChromebook14a":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "AcerSwift5":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "DellVostro3401":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "AppleMacBookPro":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "AppleMacBookAir":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "HPSpectre":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "LenovoYoga":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
            total_price = cartlist.objects.aggregate(Sum('price'))
            print(total_price)
            text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                    't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                    'total_price': total_price}
        return render(request, 'elec.html', text)
    return render(request, 'elec.html')


def watchcart(request):
    c = cartForm()
    w = request.POST.get('wat')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('wat', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["SamsungGalaxyActive2", "GOQiiSmart", "MiSmartBand4", "G-ShockCarbon", "DecodeAnalogue",
                            "RelishAnalogueWatch", "FastrackTrendiesWatch", "FastrackWomen'sWatch", "FastrackSunburn",
                            "AppleWatchSeries6", "AppleWatchSE", "PumaWatch"]:
                    if item == "SamsungGalaxyActive2":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "GOQiiSmart":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "MiSmartBand4":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "G-ShockCarbon":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "DecodeAnalogue":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "RelishAnalogueWatch":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "FastrackTrendiesWatch":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "FastrackWomen'sWatch":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "FastrackSunburn":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "AppleWatchSeries6":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "AppleWatchSE":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "PumaWatch":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'watch.html', text)
    return render(request, 'watch.html')


def hdcart(request):
    c = cartForm()
    w = request.POST.get('hd')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('hd', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["MytrackMTJP10", "RedmiHi", "ShopMagicsWireless", "JBLC100SI", "JBLEndurance",
                            "boAtBassheads", "boAtRockerz", "7PlusSports", "Shopbug", "Infinity", "Brandshub",
                            "TEVOTALK"]:
                    if item == "MytrackMTJP10":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "RedmiHi":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "ShopMagicsWireless":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "JBLC100SI":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "JBLEndurance":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "boAtBassheads":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "boAtRockerz":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "7PlusSports":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "Shopbug":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "Infinity":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "Brandshub":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "TEVOTALK":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'hd.html', text)
    return render(request, 'hd.html')


def earcart(request):
    c = cartForm()
    w = request.POST.get('ear')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('ear', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["AppleAirPods", "pTronBassbuds", "WeCool", "boAtAirdopes", "JBLC115TWS", "NoiseBuds",
                            "realmeBuds", "OPPOENCO", "RedmiEarbudsS", "XiaomiAirdots", "HammerKO", "BoultAirBass"]:
                    if item == "AppleAirPods":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "pTronBassbuds":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "WeCool":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "boAtAirdopes":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "JBLC115TWS":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "NoiseBuds":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "realmeBuds":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "OPPOENCO":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "RedmiEarbudsS":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "XiaomiAirdots":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "HammerKO":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "BoultAirBass":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'earbud.html', text)
    return render(request, 'earbud.html')


def tvcart(request):
    c = cartForm()
    w = request.POST.get('tv')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('tv', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["Panasonic", "AmazonBasics", "MiTV4APRO", "OnePlusYSeries", "eAirtec", "Samsung",
                            "RedmiTVX50", "LG", "RedmiTVX55", "TCL", "Kevin", "VW"]:

                    if item == "Panasonic":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "AmazonBasics":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "MiTV4APRO":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "OnePlusYSeries":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "eAirtec":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "Samsung":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "RedmiTVX50":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "LG":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "RedmiTVX55":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "TCL":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "Kevin":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "VW":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""

                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity':  quantity, 'image':  image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'tv.html', text)
    return render(request, 'tv.html')


def accart(request):
    c = cartForm()
    w = request.POST.get('ac')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('ac', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["Sanyo1Ton", "Whirlpool1.5Ton", "Daikin0.8Ton", "BlueStar0.8Ton", "LG1.5Ton",
                            "Godrej1.25Ton", "AmazonBasics1Ton", "Midea1Ton", "Voltas1Ton", "Samsung1.5Ton", "TCLElite",
                            "Samsung1Ton"]:
                    if item == "Sanyo1Ton":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "Whirlpool1.5Ton":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "Daikin0.8Ton":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "BlueStar0.8Ton":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "LG1.5Ton":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "Godrej1.25Ton":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "AmazonBasics1Ton":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "Midea1Ton":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "Voltas1Ton":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "Samsung1.5Ton":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "TCLElite":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "Samsung1Ton":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""

                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'ac.html', text)
    return render(request, 'ac.html')


def rfcart(request):
    c = cartForm()
    w = request.POST.get('rf')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        item = request.POST.get('rf', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["AmazonBasicsRefrigerator", "Samsung198L", "Whirlpool200L", "LG260L", "Haier181L",
                            "Haier192L", "Haier258L", "Samsung314L", "Whirlpool190L", "Samsungs315L", "Whirlpool245L",
                            "Samsung244L"]:

                    if item == "AmazonBasicsRefrigerator":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "Samsung198L":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "Whirlpool200L":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "LG260L":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "Haier181L":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "Haier192L":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "Haier258L":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "Samsung314L":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "Whirlpool190L":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "Samsungs315L":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "Whirlpool245L":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "Samsung244L":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""
                price = float(q)*selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                'total_price': total_price}
        return render(request, 'rf.html', text)
    return render(request, 'rf.html')


def offr(request):
    c = cartForm()
    w = request.POST.get('ofr')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        t9 = ' '
        t10 = ' '
        t11 = ' '
        t12 = ' '
        t13 = ' '
        t14 = ' '
        t15 = ' '
        t16 = ' '
        item = request.POST.get('ofr', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["Redmi9Prime1", "lenovoYoga11", "AppleiPhoneX(256GB)", "SKYHEIGHTSPartyDress", "LOISCARON",
                            "LIMESTONE", "pTronnTangent", "BoAtAirdopes381", "Samsung198", "BASE41T-Shirt",
                            "DennisoLingoShirt", "Panasonicc", "BoAtBassheadss242", "OnePluss7T", "GlorySarees",
                            "OPPOoA9"]:

                    if item == "Redmi9Prime1":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "lenovoYoga11":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "AppleiPhoneX(256GB)":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "SKYHEIGHTSPartyDress":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "LOISCARON":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "LIMESTONE":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "pTronnTangent":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "BoAtAirdopes381":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""

                    if item == "Samsung198":
                        t9 = "Added to cart!!"
                    else:
                        t9 = ""

                    if item == "BASE41T-Shirt":
                        t10 = "Added to cart!!"
                    else:
                        t10 = ""

                    if item == "DennisoLingoShirt":
                        t11 = "Added to cart!!"
                    else:
                        t11 = ""

                    if item == "Panasonicc":
                        t12 = "Added to cart!!"
                    else:
                        t12 = ""

                    if item == "BoAtBassheadss242":
                        t13 = "Added to cart!!"
                    else:
                        t13 = ""

                    if item == "OnePluss7T":
                        t14 = "Added to cart!!"
                    else:
                        t14 = ""

                    if item == "GlorySarees":
                        t15 = "Added to cart!!"
                    else:
                        t15 = ""

                    if item == "OPPOoA9":
                        t16 = "Added to cart!!"
                    else:
                        t16 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 't9': t9, 't10': t10, 't11': t11, 't12': t12,
                't13': t13, 't14': t14, 't15': t15, 't16': t16, 'total_price': total_price}
        return render(request, 'ofr.html', text)
    return render(request, 'ofr.html')


def mobile(request):
    c = cartForm()
    w = request.POST.get('mob')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        item = request.POST.get('mob', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["AppleiPhone11ProMaxx", "POCOM3", "OPPOF19Pro+", "Mi10T5G"]:

                    if item == "AppleiPhone11ProMaxx":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "POCOM3":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "OPPOF19Pro+":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "Mi10T5G":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item . price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)

        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 'total_price': total_price}
        return render(request, 'Mobile.html', text)
    return render(request, 'Mobile.html')


def add(request):
    item_all = cartlist.objects.all()
    total_price = sum(item_all.values_list('price', flat=True))
    print(total_price)
    if request.method == 'POST':
        text = {'total_price': total_price}
        return render(request, 'buy.html', text)
    text = {'total_price': total_price}
    return render(request, 'add.html', text)


def add2(request):

    return render(request, 'address.html')


def fash(request):
    c = cartForm()
    w = request.POST.get('dress')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '

        item = request.POST.get('dress', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["Levi'sMen'sCasualShirt", "MaxcottonnKurta", "ClobayDungaree", "AJDEZINES",
                            "BLIVEKid'sHenleyT-Shirt", "Levi'sWomen'sShirt", "DennisLingoMenn'sShirt",
                            "CUPIDVIBEGirlsDress"]:

                    if item == "Levi'sMen'sCasualShirt":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "MaxcottonnKurta":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "ClobayDungaree":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "AJDEZINES":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "BLIVEKid'sHenleyT-Shirt":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "Levi'sWomen'sShirt":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "DennisLingoMenn'sShirt":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "CUPIDVIBEGirlsDress":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 'total_price': total_price}
        return render(request, 'fashion.html', text)
    return render(request, 'fashion.html')


def women(request):
    c = cartForm()
    w = request.POST.get('cloth')
    if request.method == 'POST':
        t1 = ' '
        t2 = ' '
        t3 = ' '
        t4 = ' '
        t5 = ' '
        t6 = ' '
        t7 = ' '
        t8 = ' '
        item = request.POST.get('cloth', None)
        q = request.POST.get('quantity')
        btn = request.POST.get('b')
        selected_item = productlist.get_item_by_name(item)
        if selected_item:
            item = item
            quantity = q
            image = selected_item.image
            if btn == 'cart':
                if item in ["ZONOKAStylishHoodies", "ElyraaWesternPolka", "SilkTraditionalSaree", "LehengaCholi",
                            "WomenSalwar", "RegularFitTop", "Women'sNetLehenga", "Women'sMiniDress"]:
                    if item == "ZONOKAStylishHoodies":
                        t1 = "Added to cart!!"
                    else:
                        t1 = ""

                    if item == "ElyraaWesternPolka":
                        t2 = "Added to cart!!"
                    else:
                        t2 = ""

                    if item == "SilkTraditionalSaree":
                        t3 = "Added to cart!!"
                    else:
                        t3 = ""

                    if item == "LehengaCholi":
                        t4 = "Added to cart!!"
                    else:
                        t4 = ""

                    if item == "WomenSalwar":
                        t5 = "Added to cart!!"
                    else:
                        t5 = ""

                    if item == "RegularFitTop":
                        t6 = "Added to cart!!"
                    else:
                        t6 = ""

                    if item == "Women'sNetLehenga":
                        t7 = "Added to cart!!"
                    else:
                        t7 = ""

                    if item == "Women'sMiniDress":
                        t8 = "Added to cart!!"
                    else:
                        t8 = ""
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                cart = cartlist(item=item, image=image, quantity=quantity, price=price)
                cart.save()
            elif btn == '':
                pass
            else:
                price = float(q) * selected_item.price
                print(item, quantity, price, image)
                total_price = price
                text = {'total_price': total_price}
                return render(request, 'address.html', text)
        total_price = cartlist.objects.aggregate(Sum('price'))
        print(total_price)
        text = {'items': item, 'quantity': quantity, 'image': image, 'price': price, 't1': t1, 't2': t2, 't3': t3,
                't4': t4, 't5': t5, 't6': t6, 't7': t7, 't8': t8, 'total_price': total_price}
        return render(request, 'women.html', text)
    return render(request, 'women.html')
