from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from django.http import HttpResponseRedirect, JsonResponse
from datetime import date
from Life.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
# from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login

def index(request):
    today = date.today()
    return render(request, "donate/index.html",{
        "camps": DonationCamp.objects.filter(end_date__gt=today),
        "banks": BloodBank.objects.all(),
        "hospitals": User.objects.filter(is_hospital=True),
        "today": today
    })

def filter(request, city):
    today = date.today()
    if city == 'Select Your City':
        dp_city = DonationPlace.objects.all()
        hospitals = User.objects.filter(is_hospital=True)
    else:
        dp_city = DonationPlace.objects.filter(city=city)
        hospitals = User.objects.filter(is_hospital=True, city=city)
    return JsonResponse({"camps": [camp.serialize() for camp in DonationCamp.objects.filter(dp_no__in=dp_city, end_date__gt=today)],
        "banks": [bank.serialize() for bank in BloodBank.objects.filter(dp_no__in=dp_city)],
        "hospitals": [hospital.serialize() for hospital in hospitals]}, safe=False)


@login_required(login_url="login")
def getunits(request, btype):
    rows = BloodUnit.objects.filter(blood_group=btype)
    return JsonResponse({"rows": [row.serialize() for row in rows]}, safe=False)

@login_required(login_url="login")
def bank(request, bank_name):
    if request.user.is_hospital == True:
        no = DonationPlace.objects.get(name=bank_name)
        blood_bank = BloodBank.objects.get(dp_no=no)
        blood_units = BloodUnit.objects.filter(blood_bank=blood_bank)
        return render(request, "donate/bank.html", {
            "bank": blood_bank,
            "units": blood_units
        })
    else:
        return HttpResponseRedirect(reverse(index))

def profile(request, name):
    user = User.objects.get(username=name)
    donations = user.donations.all()
    today = date.today()
    age = 0
    if user.is_hospital == False:
        age = today.year - user.dob.year - ((today.month, today.day) < (user.dob.month, user.dob.day))
    return render(request, "donate/profile.html", {
        "donations": donations,
        "user1": user,
        "age": age
    })

@login_required(login_url="login")
def requests(request):
    if request.method == 'POST':
        city = request.user.city
        req_type = request.POST["blood_req_type"]
        subject = 'Blood Donation Request'
        message = f'''You have got a blood donation request from {request.user}. A patient urgently needs blood of type {req_type}, if you can come and save a life. Please respond ASAP on the website.
        \n{request.user}'s Address : {request.user.street}, {request.user.city}, {request.user.state}'''

        recepient = ['darpansudan99@gmail.com']
        for donor in User.objects.filter(blood_type=req_type, city=city):
            BloodRequest.objects.create(hospital=request.user,donor=donor)
            recepient.append(f'{donor.email}')

        send_mail(subject, message, EMAIL_HOST_USER, recepient, fail_silently=False)
    
    if request.user.is_hospital == True:
        reqs = BloodRequest.objects.filter(hospital=request.user)
    else:
        reqs = BloodRequest.objects.filter(donor=request.user)

    return render(request, "donate/requests.html", {
            "reqs": reqs.order_by('date').reverse(),
            "today": date.today()
        })


@login_required(login_url="login")
def response(request, id):
    if request.method =='POST':
        req = BloodRequest.objects.get(id=id)
        
        if 'accept' in request.POST:
            req.status = 'A'
        elif 'deny' in request.POST:
            req.status = 'D'
        req.save()
        
        if request.user.is_hospital == True:
            reqs = BloodRequest.objects.filter(hospital=request.user)
        else:
            reqs = BloodRequest.objects.filter(donor=request.user)

        return render(request, "donate/requests.html", {
            "reqs": reqs.order_by('date').reverse(),
            "today": date.today()
        })
    else:
        return HttpResponseRedirect(reverse('requests'))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "donate/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "donate/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    return render(request, "donate/register.html")

def registerOption(request, option):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        phone_no = request.POST["phone_no"]
        street = request.POST["street"]
        city = request.POST["city"]
        state = request.POST["state"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            if option == "hospital":
                return render(request, "donate/register_hospital.html", {
                    "message": "Passwords must match."
                })
            elif option == "donor":
                return render(request, "donate/register_donor.html", {
                    "message": "Passwords must match."
                })

        if option == "donor":
            blood_type = request.POST["blood_type"]
            first_name = request.POST["firstname"]
            last_name = request.POST["lastname"]
            dob = request.POST["dob"]
            gender = request.POST["gender"]

           # Check if the username already exists
        user_exists = User.objects.filter(username=username).exists()
        if user_exists:
            if option == "hospital":
                return render(request, "donate/register_hospital.html", {
                    "message": "Username already taken."
                })
            elif option == "donor":
                return render(request, "donate/register_donor.html", {
                    "message": "Username already taken."
                })

         # Create a new user
        user = User.objects.create_user(username,email, password)
        user.street = street
        user.city = city
        user.state = state
        user.phone_no = phone_no
        if option == "donor":
            user.first_name = first_name
            user.last_name = last_name
            user.blood_type = blood_type
            user.dob = dob
            user.gender = gender
            user.is_hospital = False
        elif option == "hospital":
            user.is_hospital = True
        user.save()

        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        if option == "hospital":
            return render(request, "donate/register_hospital.html")
        elif option == "donor":
            return render(request, "donate/register_donor.html")
        else:
            return HttpResponseRedirect(reverse("register"))
        
