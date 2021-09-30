from django.shortcuts import render
from .models import Products
from .forms import PropertyForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render,get_object_or_404

# Create your views here.
def Index(request):
    products = Products.objects.all()
    return render(request, 'Index.html', {"products":products})

def SavePropertyForm(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Products.objects.all()
            data['html_product_list'] = render_to_string('Index.html', {
                'products': products
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)

def AddProducts(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
    else:
        form = PropertyForm()
    return SavePropertyForm(request, form, 'Index.html')

def UpdateProduct(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=product)
    else:
        form = PropertyForm(instance=product)
    return SavePropertyForm(request, form, 'Index.html')
    
def DeleteProduct(request, pk):
    product = get_object_or_404(Products, pk=pk)
    data = dict()
    if request.method == 'POST':
        product.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        product = Products.objects.all()
        data['html_product_list'] = render_to_string('Index.html', {
            'product': product
        })
    else:
        context = {'product': product}
        data['html_form'] = render_to_string('Index.html',
            context,
            request=request,
        )
    return JsonResponse(data)