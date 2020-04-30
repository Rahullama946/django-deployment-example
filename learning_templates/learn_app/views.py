from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict ={'text':'hello world','number':100 }
    return render(request,'learn_app/index.html',context_dict)

def others(request):
    return render(request,'learn_app/others.html')

def relative_url_templates(request):
    return render(request,'learn_app/relative_url_templates.html')