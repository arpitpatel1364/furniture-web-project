from django.shortcuts import render


def index(request):
    return render(request, 'index.html')  # Ensure this matches your template name
def shop(request):
    return render(request, 'shop.html')  # Ensure this matches your template name
def about(request):
    return render(request, 'about.html')  # Ensure this matches your template name
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request, 'contact.html')
def cart(request):
    return render(request, 'cart.html')
def checkout(request):
    return render(request, 'checkout.html')
def services(request):
    return render(request, 'services.html')
def thankyou(request):
    return render(request, 'thankyou.html')
def login(request):
    return render(request, 'login.html')
def data(request):
    us=""
    pas=""

    try:
        us=request.GET.get ('username')
        pas=request.GET.get('password')

        dict ={
            'username':us,
            'password':pas
            }
    except:
        pass
    
    return render(request, 'data.html',dict)
