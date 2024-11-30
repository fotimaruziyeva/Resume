from django.shortcuts import render
from .models import Blog
from django.contrib import messages
from django.views.generic.list import ListView
from .forms import ContactForm
from django.views.generic.edit import FormView
def home_view(request):
    return render(request, 'index.html')

def about_view(request):
    blog_lists = Blog.objects.order_by('-created_at')[:4]
    return render(request, 'about.html',{'blog_list': blog_lists})

class BlogListView(ListView):
    model = Blog
    template_name = "blog.html"
    context_object_name = 'blog_list'  
    paginate_by = 2

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm  
    success_url = '/'  

    def form_valid(self, form):
       
        contact = form.save(commit=False)  
        print(contact)
        contact.save()  

      
        messages.success(self.request, "Your message has been sent successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

def portfolio_view(request):
    return render(request, 'portfolio.html')
