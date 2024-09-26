from django.shortcuts import render
from .models import Document

# View for Index Page Documents
def index(request):
    documents = Document.objects.filter(page='index')
    return render(request, 'index.html', {'documents': documents})

# View for About Page Documents
def about(request):
    documents = Document.objects.filter(page='about')
    return render(request, 'about.html', {'documents': documents})

# View for Services Page Documents
def services(request):
    documents = Document.objects.filter(page='services')
    return render(request, 'services.html', {'documents': documents})

# View for Register Page Documents
def register(request):
    documents = Document.objects.filter(page='register')
    return render(request, 'register.html', {'documents': documents})

# View for Reports Page Documents
def reports(request):
    documents = Document.objects.filter(page='reports')
    return render(request, 'reports.html', {'documents': documents})

# View for CS Page Documents
def cs(request):
    documents = Document.objects.filter(page='cs')
    return render(request, 'cs.html', {'documents': documents})

# View for ML Page Documents
def ml(request):
    documents = Document.objects.filter(page='ml')
    return render(request, 'ml.html', {'documents': documents})

# View for Economics Page Documents
def economics(request):
    documents = Document.objects.filter(page='economics')
    return render(request, 'economics.html', {'documents': documents})

# View for Data Analysis Page Documents
def data_analysis(request):
    documents = Document.objects.filter(page='data_analysis')
    return render(request, 'data_analysis.html', {'documents': documents})

# View for Data Mining Page Documents
def data_mining(request):
    documents = Document.objects.filter(page='data_mining')
    return render(request, 'data_mining.html', {'documents': documents})

# View for Finance Page Documents
def finance(request):
    documents = Document.objects.filter(page='finance')
    return render(request, 'finance.html', {'documents': documents})

# View for Business Analytics Page Documents
def business_analytics(request):
    documents = Document.objects.filter(page='business_analytics')
    return render(request, 'business_analytics.html', {'documents': documents})

# View for Case Studies Page Documents
def case_studies(request):
    documents = Document.objects.filter(page='case_studies')
    return render(request, 'case_studies.html', {'documents': documents})

# View for Business Page Documents
def business(request):
    documents = Document.objects.filter(page='business')
    return render(request, 'business.html', {'documents': documents})

# View for Marketing Page Documents
def marketing(request):
    documents = Document.objects.filter(page='marketing')
    return render(request, 'marketing.html', {'documents': documents})

# View for Research Page Documents
def research(request):
    documents = Document.objects.filter(page='research')
    return render(request, 'research.html', {'documents': documents})
