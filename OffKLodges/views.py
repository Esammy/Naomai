from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PaymentForm, FindRoomMateForm
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import LodgeProperties, Lodge, Payment, FindRoomMates
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.paginator import Paginator#, zEmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

def index(request):
    form = FindRoomMateForm()
    if request.method == 'POST':
        form = FindRoomMateForm(request.POST)
        

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('fname')
            messages.success(request, f' {username} request has been submitted')
            return redirect('index')
    context = {
        'lodges': Lodge.objects.all(),
        'form': form,
        }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=request.user)
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created! Your are now able to log in')
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



def initiate_payment(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment = payment_form.save()
            return render(request, 'make_payment.html', {'payment':payment, 'paystack_public_key': settings.PAYSTACK_PUBLIC_KEY})#
    else:
        payment_form = PaymentForm()     
        return render(request, 'initiate_payment.html', {'payment_form':payment_form})   

def verify_payment(request: HttpRequest, ref:str) -> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "Verification Successfull.")
    else:
        messages.error(request, "Verification Failed.")    
    return redirect('initiate-payment')



def booked(request):
    context = {'lodges': Lodge.objects.all()}
    
    return render(request, 'booked.html', context)

def search(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        results = Lodge.objects.filter(name__contains=searched)
        lodges = Lodge.objects.all()
        return render(request, 'booked.html', {'searched':searched, 'results':results, 'lodges':lodges})
    else:
        return render(request, 'booked.html',)    

'''
def allLodges(request):
    lodge_list = Lodge.objects.all()
    page = object.GET.get('page', 1)
    paginator = Paginator(lodge_list, 2)

    try:
        lodges = paginator.page(page)
    except PageNotAnInteger:
        lodges = paginator.page(1)
    except zEmptyPage:
        lodges = paginator.page(paginator.num_pages)

    context = {
        'lodges': lodges,
    }

    #context = {'lodges': Lodge.objects.all()}
    return render(request, 'all_lodges.html', context)
 '''

class LodgeDetailView(DetailView):
    model = LodgeProperties
    template_name = 'lodge_detail.html'
    #ordering = ['-date-poste']

 
class ConfPayment(DetailView):
    model = LodgeProperties
    template_name = 'confirm_payment.html'

'''
class KeywordListView(ListView):
    paginate_by = 2
    model = Lodge
    template_name = "all_lodges.html"
'''

def listing(request):
    lodges = Lodge.objects.all().order_by("name")
    paginator = Paginator(lodges, per_page=2)
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
        form = FindRoomMateForm(request.POST)

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