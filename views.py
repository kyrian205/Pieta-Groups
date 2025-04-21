from django.shortcuts import render
from django.http import HttpResponse
from .models import Complaint, Admission, Result

# Home view
def home(request):
    return render(request, 'home.html')

# Gallery view
def gallery(request):
    return render(request, 'gallery.html')

# News view
def news(request):
    return render(request, 'news.html')

# Complaint submission view
def complaint_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Complaint.objects.create(name=name, email=email, message=message)
        return HttpResponse("Thank you for your complaint. We will review it shortly.")
    return render(request, 'complaint.html')

# Admission submission view
def admission_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        parent_name = request.POST.get('parent_name')
        parent_contact = request.POST.get('parent_contact')
        email = request.POST.get('email')
        Admission.objects.create(name=name, dob=dob, gender=gender, address=address, parent_name=parent_name, parent_contact=parent_contact, email=email)
        return HttpResponse("Your admission application has been submitted.")
    return render(request, 'admission.html')

# Result Checker view
def result_checker(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            result = Result.objects.get(student_id=student_id)
            return render(request, 'result_checker.html', {'result': result})
        except Result.DoesNotExist:
            return HttpResponse("Result not found for this student ID.")
    return render(request, 'result_checker.html')

# Admin Dashboard
def admin_dashboard(request):
    complaints = Complaint.objects.all()
    admissions = Admission.objects.all()
    results = Result.objects.all()
    return render(request, 'admin.html', {'complaints': complaints, 'admissions': admissions, 'results': results})