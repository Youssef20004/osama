from .forms import FormSumData
from .models import Services
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.views.decorators.cache import cache_page

# إرسال الإيميلات للاستشارة
def send_consultation_email(sum_data):
    try:
        send_mail(
            subject="طلب استشارة جديدة",
            message=f"اسم العميل: {sum_data.name}\n"
                    f"البريد الإلكتروني: {sum_data.email}\n"
                    f"رقم الهاتف: {sum_data.phone}\n"
                    f"سبب التواصل: {sum_data.subject}\n"
                    f"الرسالة:\n{sum_data.message}",
            from_email="osamaabdelrhim@gmail.com",
            recipient_list=["osamaabdelrhim@gmail.com"],
            fail_silently=False,
        )

        send_mail(
            subject="شكراً لتواصلك معنا",
            message="تم استلام استفسارك، وسنقوم بالتواصل معك قريبًا. شكرًا لك!",
            from_email="osamaabdelrhim@gmail.com",
            recipient_list=[sum_data.email],
            fail_silently=False,
        )
        return True

    except Exception as e:
        return str(e)

# دالة مساعدة لمعالجة نماذج التواصل
def handle_consultation_form(request, template, redirect_url):
    if request.method == 'POST':
        form = FormSumData(request.POST)
        if form.is_valid():
            sum_data = form.save(commit=False)
            email_status = send_consultation_email(sum_data)
            if email_status is True:
                sum_data.save()
                messages.success(request, "تم إرسال البيانات بنجاح، وسوف يتم التواصل معك قريبًا.")
                return redirect(redirect_url)
            else:
                messages.error(request, f"حدث خطأ أثناء إرسال البريد: {email_status}")
    else:
        form = FormSumData()
    return render(request, template, {'form': form})

# الصفحات الثابتة مع الكاش
@cache_page(60 * 15)  # 15 دقيقة
def library_law(request):
    return render(request, 'pages/library_law.html')

@cache_page(60 * 15)  # 15 دقيقة
def lawyer_guide(request):
    return render(request, 'pages/lawyer_guide.html')

@cache_page(60 * 15)  # 15 دقيقة
def index(request):
    return render(request, 'pages/index.html')

# صفحة الخدمات مع كاش للبيانات
def services(request):
    cache_key = 'services_texts'
    texts = cache.get(cache_key)
    if not texts:
        texts = Services.objects.all()
        cache.set(cache_key, texts, 60 * 60)  # 1 ساعة
    return render(request, 'pages/services.html', {'texts': texts})

# صفحات التواصل
def contact(request):
    return handle_consultation_form(request, 'pages/contact_us.html', 'contact')

def conslut(request):
    return handle_consultation_form(request, 'pages/consult.html', 'conslut')
