from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import RegistrationForm

# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, 'services.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user information to the database
            return redirect('index')  # Redirect to the home page
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def reports(request):
    return render(request, 'reports.html')


def cs(request):
    return render(request, 'cs.html')



def ml(request):
    return render(request, 'ml.html')


def data_analysis(request):
    return render(request, 'data_analysis.html')


def economics(request):
    return render(request, 'economics.html')

def data_mining(request):
    return render(request, 'data_mining.html')


def finance(request):
    return render(request, 'finance.html')

def business_analytics(request):
    return render(request, 'business_analytics.html')

def case_studies(request):
    return render(request, 'case_studies.html')

def business(request):
    return render(request, 'business.html')

def marketing(request):
    return render(request, 'marketing.html')

def research(request):
    return render(request, 'research.html')