from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, AboutUs, ContactUs
from .forms import PostForm, EditForm, ServiceForm, AboutUsForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
#def home(request):
    #return render(request, 'home.html',{})
# from django.contrib.auth import logout
# from django.shortcuts import redirect

# def logout_view(request):
#     logout(request)
#     return redirect('home')

def LikeView(request, pk):
    post = get_object_or_404(Category, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else: 
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('service_detail', args=[str(pk)]))

def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html',{
        'cats':cats.title().replace('-',' '), 
        'category_post':category_post
    })
class ServiceView(ListView):
    model = Category
    template_name = 'our_services.html'
    ordering = ['-id']

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class AboutUsView(ListView):
    model = AboutUs
    template_name = 'about_us.html'
    ordering = ['-id']

class ContacttUsView(ListView):
    model = ContactUs
    template_name = 'contact_us.html'
    ordering = ['-id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'detailview.html'

class ServiceDetailView(DetailView):
    model = Category
    template_name = 'service_detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ServiceDetailView,self).get_context_data()
        stuff = get_object_or_404(Category, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id = self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        context['total_likes'] = total_likes
        return context


class AddServiceView(CreateView):
    model= Category
    form_class = ServiceForm
    template_name = 'add_service.html'
    # fields = '__all__'


class AddPostView(CreateView):
    model= Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class AddContactUsPostView(CreateView):
    model= ContactUs
    form_class = AboutUsForm
    template_name = 'add_contact_us_post.html'
    #fields = '__all__'

class AddAboutUsPostView(CreateView):
    model= AboutUs
    form_class = AboutUsForm
    template_name = 'add_about_us_post.html'
    #fields = '__all__'

class UpdateServicePostView(UpdateView):
    model = Category
    form_class = ServiceForm
    template_name = 'update_service_post.html'
    #fields = ['title','title_tag','body']

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title','title_tag','body']

class UpdateContactUsPostView(UpdateView):
    model = ContactUs
    form_class = AboutUsForm
    template_name = 'update_contact_us_post.html'
    #fields = ['title','title_tag','body']

class UpdateAboutUsPostView(UpdateView):
    model = AboutUs
    form_class = AboutUsForm
    template_name = 'update_about_us_post.html'
    #fields = ['title','title_tag','body']

class DeleteContactUsPostView(DeleteView):
    model = ContactUs
    template_name = 'delete_contact_us_post.html'
    success_url = reverse_lazy('home')
    
class DeleteAboutUsPostView(DeleteView):
    model = AboutUs
    template_name = 'delete_about_us_post.html'
    success_url = reverse_lazy('home')

class DeleteServicePostView(DeleteView):
    model = Category
    template_name = 'delete_service_post.html'
    success_url = reverse_lazy('our_services')

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')