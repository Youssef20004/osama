from .forms import FormSumData
from .models import Services
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import FormSumData

# library_law
def library_law(request):
    return render(
        request,
        'pages/library_law.html'
    )

# lawyer_guide
def lawyer_guide(request):
    return render(
        request,
        'pages/lawyer_guide.html',
    )

# Contact Us
def contact(request):
    return render(
        request,
        'pages/contact_us.html',
    )

def conslut(request):
    if request.method == 'POST':
        form = FormSumData(request.POST)
        if form.is_valid():
          
            sum_data = form.save()

            # إرسال بيانات العميل إلى المحامي عبر البريد الإلكتروني
            send_mail(
                subject="طلب استشارة جديدة",
                message=f"اسم العميل: {sum_data.name}\n"
                        f"البريد الإلكتروني: {sum_data.email}\n"
                        f"رقم الهاتف: {sum_data.phone}\n"
                        f"سبب التواصل: {sum_data.reason_for_contact}\n"
                        f"الرسالة:\n{sum_data.message}",
                from_email="youssefabdelrhim57@gmail.com",
                recipient_list=["osamaabdelrhim@gmail.com"],  
                fail_silently=False,
            )

           
            send_mail(
                subject="شكراً لتواصلك معنا",
                message="تم استلام استفسارك، وسنقوم بالتواصل معك قريبًا. شكرًا لك!",
                from_email="youssefabdelrhim57@gmail.com",
                recipient_list=[sum_data.email],  
                fail_silently=False,
            )

            messages.success(request, "تم إرسال البيانات بنجاح، وسوف يتم التواصل معك قريبًا.")
            return redirect('conslut')  

    else:
        form = FormSumData()

    return render(request, 'pages/consult.html', {'form': form})

def index(request):
    return render(
        request,
        'pages/index.html'
    )

def services(request):
    texts = Services.objects.all()
    return render(
        request,
        'pages/services.html',
        {'texts' : texts}
    )
