from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, FindRoomMateForm, AgentPersonalInfoForm, AgentPropertiesForm #, BookedLodgeForm, PaymentForm,
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import LodgeProperties, Lodge, NewPayment, FindRoomMate, AgentPersonalInfo #, Payment,
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator#, zEmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from datetime import datetime

from .models import User
from notifications.signals import notify

current_user_name = []
def index(request):

    if request.method == 'POST':
        form = FindRoomMateForm(request.POST)
        
        if form.is_valid():
            form.save()
            fname = form.cleaned_data.get('fname')
            current_user_name.append(fname)
            messages.success(request, f' {fname} request has been submitted')

            return redirect('findroomateconfirm')
            #return redirect('login')
    else:
        context = {
            'lodges': Lodge.objects.all()[:4],
            'form': FindRoomMateForm(),
            }
    return render(request, 'index.html', context)

def last_score():
    scores = FindRoomMate.objects.order_by('date_created')
    score_list = []
    for i in scores:
        score_list.append(i)
    if score_list:
        return score_list[-1]
    else:
        return None
    

def roommateResult(request):
    persons = FindRoomMate.objects.order_by('date_created')
    #u_form = UserUpdateForm(instance=request.user)
    l_score = last_score()
    thresh_h = 10
    print('This is the last person to submit form: ', l_score.fname, 'socre:', l_score.match_score)
    this_info = []
    person_matched = []
    
    new_person = []
    for person in persons:
        new_person.append(person)
    this_person = []
    l_scores_value = [l_score.sex, l_score.state, l_score.earlywake, 
                        l_score.noise, l_score.grocries, l_score.personalSpace,
                        l_score.organizedSpace, l_score.disabilites, l_score.level
    ]


    for i in new_person[1:-1]:
        if i.sex == l_score.sex:
            if i.state == l_score.state:
                if i.earlywake == l_score.earlywake:
                    if i.noise == l_score.noise:
                        if i.organizedSpace == l_score.organizedSpace:
                            if i.grocries == l_score.grocries:
                                if i.personalSpace == l_score.personalSpace:
                                    if i.disabilites == l_score.disabilites:
                                        if i.level == l_score.level:
                                            this_person.append(i)
        
        
    context = {
        'this_info': this_info,
        'person_matched': person_matched,
        'this_person': this_person,
        'l_score': l_score
        #'[u_form':u_form
        }
    
    return render(request, 'findroomatesresult.html', context)



def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_email = form.cleaned_data.get('email') 
            messages.success(request, f'Account for {username} has been created!')

            # subject = 'welcome to Naomi Acc Sys'
            # message = (f"Hi {username}, thank you for registering in Naomi's third party lodge acc system.")
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user_email, ]
            # print('from: ', email_from)
            # print('to:', recipient_list)
            # send_mail( subject, message, email_from, recipient_list )

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'l_score': last_score(),
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)

def deposit(request):
    lodge = Lodge.objects.all()
    email = request.user.email
    context = {
        'lodges': lodge, 
        'email': email,
        'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY
    }
    return render(request, 'confirm_payment.html', context)

def ini_pay(request, id):
    lodge = LodgeProperties()
    lodge_id = get_object_or_404(LodgeProperties, id=id)
    user = User.objects.get(username=request.user)
    lodge_name = lodge_id
    email = request.user.email
    amount = lodge_id.lodge.price
    payment = NewPayment.objects.create(user=user, lodge_name=lodge_name, email=email, amount=amount)
    # if request.method == 'POST':
    #     user = User.objects.get(username=request.user)
    #     lodge_name = request.POST['name']
    #     email = request.POST['email']
    #     amount = request.POST['price']
        
    #     print(lodge_id.id)

    #     payment = NewPayment.objects.create(user=user, lodge_name=lodge_name, email=email, amount=amount)
    return render(request, 'confirm_payment.html', {'lodge_id':lodge_id, 'lodge':lodge })
        #return redirect('confirm_payment', id)


# def initiate_payment(request: HttpRequest, id:int) -> HttpResponse:
#     if request.method == "POST":
#         lodge = LodgeProperties
#         lodge_id = get_object_or_404(lodge, id=id)

#         payment_form = PaymentForm(request.POST)
#         if payment_form.is_valid():
#             payment = payment_form.save()
#             return render(request, 'make_payment.html', {'lodge_id':lodge_id ,'payment':payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})#
#     else:
#         payment_form = PaymentForm()
#         return render(request, 'initiate_payment.html', {'payment_form':payment_form})   

# def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
#     payment = get_object_or_404(Payment, ref=ref)
#     verified = payment.verify_payment()
#     if verified:
#         messages.success(request, "Verification Successfull.")
#     else:
#         messages.error(request, "Verification Failed.")    
#     return redirect('initiate-payment')


def lodgeview(request, id):
    try:
        lodge = LodgeProperties
        lodge_id = get_object_or_404(lodge, id=id)
        users = User.objects.all()
        print(request.user)
        user = User.objects.get(username=request.user)

        return render(request, 'lodge_detail.html', 
                    {'users': users, 'user': user, 'lodge':lodge, 'lodge_id':lodge_id})
    except Exception as e:
        print(e)
        return HttpResponse("Something is wrong at the moment.")

class LodgeDetailView(DetailView):
    model = LodgeProperties
    template_name = 'lodge_detail.html'
    #ordering = ['-date-poste']

class ConfPayment(DetailView):
    model = LodgeProperties
    template_name = 'confirm_payment.html'

# class Lodge_booking(DetailView):
#     model = LodgeProperties
#     #user = User.objects.get(username=request.user)
#     template_name = 'lodge_booking.html'


def listing(request):
    lodges = Lodge.objects.all().order_by("name")
    paginator = Paginator(lodges, per_page=6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj, "lodges":lodges}
    return render(request, "list.html", context)

def listing_api(request):
    page_number = request.GET.get("page", 1)
    per_page = request.GET.get("per_page", 2)
    startswith = request.GET.get("startswith", "")
    keywords = Lodge.objects.filter(
        name__startswith=startswith
    )
    paginator = Paginator(keywords, per_page)
    page_obj = paginator.get_page(page_number)
    data = [{"name": kw.name} for kw in page_obj.object_list]

    payload = {
        "page": {
            "current": page_obj.number,
            "has_next": page_obj.has_next(),
            "has_previous": page_obj.has_previous(),
        },
        "data": data
    }
    return JsonResponse(payload)

#@login_required
def findRoomie(request):
    if request.method == 'POST':
        form = FindRoomMateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('fname')
            messages.success(request, f' {username} request has been submitted')
            return redirect('index')
    else:
        form = FindRoomMateForm()
        return render(request, 'index.html', {'form': form})
            
def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        results = Lodge.objects.filter(name__contains=searched)
        lodges = Lodge.objects.all()
        return render(request, 'list.html', {'searched':searched, 'results':results, 'lodges':lodges})
    else:
        return render(request, 'list.html',)

def filter(request):
    if request.method == "POST":
        minimum = request.POST.get('minimum')
        maximum = request.POST.get('maximum')
        lodges = Lodge.objects.all()
        price_query = []
        for i in lodges:
            if i.price >= int(minimum) and i.price <= int(maximum):
                #print(i.price)
                price_query.append(i)
        return render(request, 'list.html', {'price_query': price_query})
    else:
        return render(request, 'list.html',)
    

def bookings(request, id):
    try:
        lodge = LodgeProperties
        lodge_id = get_object_or_404(lodge, id=id)
        users = User.objects.all()
        print(request.user)
        user = User.objects.get(username=request.user)
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y %H:%M:%S")

        return render(request, 'lodge_booking.html', 
                    {'users': users, 'date_str':date_str, 'user': user, 'lodge':lodge, 'lodge_id':lodge_id})
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages.")

def message(request):
    try:
        if request.method == 'POST':
            #sender = User.objects.get(username=request.user)
            sender = User.objects.get(username=request.user)
            receiver = User.objects.get(id=request.POST.get('user_id'))
            notify.send(sender, recipient=receiver, verb='Message', description=request.POST.get('message'))
            return redirect('index')
        else:
            return HttpResponse("Invalid request")
    except Exception as e:
        print(e)
        return HttpResponse("Please login from admin site for sending messages")


def agentPersonalInfo(request):
    try:
        if request.method == 'POST':
            form = AgentPersonalInfoForm(request.POST)
            
            if form.is_valid():
                agent = form.save(commit=False)
                agent.user = request.user
                agent.save()
                agent_fname = form.cleaned_data.get('agent_fname')
                messages.success(request, f' {agent_fname} request has been submitted')

                #return HttpResponse("Your response has been submitted successfully. The admin will contact you in two days time")
                return redirect('agentProperties')
        else:
            form = AgentPersonalInfoForm()
        return render(request, 'agentpersonalinfo.html', {'form': form})
    except Exception as e:
        print(e)
        #return HttpResponse("Account has been created for this user proceed to properties upload by typing this ")
        return render(request, 'agenterrorpage.html')


def agentProperties(request):
    try:
        if request.method == 'POST':
            form = AgentPropertiesForm(request.POST, request.FILES)
            
            if form.is_valid():
                # agent = form.save(commit=False)
                # agent.agent_ersonal_info = request.user.agentproperties
                form.save()
                messages.success(request, f' request to upload properties has been submitted')

                return HttpResponse("Your response has been submitted successfully. The admin will contact you in two days time")
        else:
            form = AgentPropertiesForm()
        return render(request, 'agentproperties.html', {'form': form})
    except Exception as e:
        print(e)
        return render(request, 'propertyerrorpage.html')
