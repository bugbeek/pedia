from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import Personforms
from django.contrib import messages
from allauth.account.decorators import login_required
from .models import Person
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#piyush unwanted
@login_required
def profiledetail(request):
    if request.method == 'POST':
        form = Personforms(request.POST or None)
        if form.is_valid():
            n = form.cleaned_data['name']
            el = form.cleaned_data['Earlylife']
            ed = form.cleaned_data['Eduction'] 
            st = form.cleaned_data['Intrest'] 
            fv = form.cleaned_data['Favorates']
            dt = Person(name=n, Earlylife=el, Eduction=ed, Intrest=st, Favorates=fv)
            dt.save()
    else:
        form = Personforms()

    return render(request, 'profiledetail.html', {'form': form})

def index(request):
    return render(request, 'index.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        user=Person.objects.none()
    else:    
        # user = Person.objects.filter(name__icontains = query)
        formname = Person.objects.filter(name__icontains = query)
        formear = Person.objects.filter(Earlylife__icontains = query)
        formitr = Person.objects.filter(Intrest__icontains = query)
        user=  formname.union(formear, formitr)
    

    params = {'allusers': user, 'query': query}
    return render(request, 'search.html', params)

@login_required
def userbio(request):
    logged_in_user = request.user
    logged_in_user_bio = Person.objects.filter(author=logged_in_user)
    params = {'bio': logged_in_user_bio}
    return render(request, 'userbio.html', params)