from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,User
from .models import Post
from django.views.generic import ListView,DetailView,CreateView
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST.get('first_name',False)
        last_name=request.POST.get('last_name',False)
        email=request.POST.get('email',False)
        username=request.POST.get('username',False)
        password1=request.POST.get('password1',False)
        password2=request.POST.get('password2',False)
        remember_me=request.POST.get('remember-me',False)

        # user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
        if remember_me:   
            if password1==password2:
                if User.objects.filter(username=username).exists():
                    # print('user already exist...')
                    messages.info(request,'check for username, email and password')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    # print('email already taken...')
                    messages.info(request,'check for username, email and password')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password1,username=username)
                    user.save();
                    # print('user created')
                    # return redirect('/')
                    return redirect('login')
            else:
                # print('please check password...')
                messages.info(request,'check for username, email and password')
                return redirect('register')

    else:
        return render(request,"register.html")


# def login(request):
#     if request.method=='POST':
#         email=request.POST.get('email',False)
#         password=request.POST.get('password',False)

#         user=auth.authenticate(email=email,password=password)

#         if user is not None:
#             auth.login(request,user)
#             return redirect("/")
#         else:
#             messages.info(request,'invalid credentials')
#             return redirect("login")
#     else:
#         return render(request,"login.html")

def login(request):
    if request.method=='POST':
        username=request.POST.get('username',False)
        password=request.POST.get('password',False)

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def blogs(request):
    # context={'posts':Post.objects.all()}
    posts = Post.objects.all()
    return render(request,'blogs.html',{"posts":posts})

class PostListView(ListView):
    model = Post
    template_name = 'blogs.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog_details.html'  # <app>/<model>_<viewtype>.html
class PostDetailView(View):
    def get(self,request,*args,**kwargs):
        post=Post.objects.get(pk=kwargs['pk'])
        show=False
        show1=True
        if post.author==request.user:
            show=True
            show1=False
        return render(request,'blog_details.html',{'post':post,'show':show,'show1':show1})
    def post(self,request):
        pass
class PostCreateView(View):
    @method_decorator(login_required(login_url='login'))
    def get(self,request):
        #obj=['Aisi','sdnskn']
        return render(request,'submit.html')
    def post(self,request):
        x=Post(title=request.POST['title'],content=request.POST['content'],author=request.user,genre=request.POST["genre"])
        x.save()
        return redirect('post',x.pk)



def about(request):
    return render(request,'about.html')

class update(View):
    def get(self,request,*args,**kwargs):
        post=Post.objects.get(pk=kwargs['id'])
        return render(request,'update.html',{"post":post})
    def post(self,request,*args,**kwargs):
        post=Post.objects.get(pk=kwargs['id'])
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.save()
        return redirect('post',post.pk)
        


class delete(View):
    def get(self,request,*args,**kwargs):
        post=Post.objects.get(pk=kwargs['id'])

        post.delete()
        return redirect('blogs')

class like(View):
    def get(self,request,*args,**kwargs):
        post=Post.objects.get(pk=kwargs['id'])
        if post.Likes.filter(id=request.user.id).exists():
            post.Likes.remove(request.user)
        else:
            post.Likes.add(request.user)

        return redirect('post',post.pk)

class report(View):
    def get(self,request,*args,**kwargs):
        post=Post.objects.get(pk=kwargs['id'])

        if post.report.filter(id=request.user.id).exists():
            post.report.remove(request.user)
        else:
            post.report.add(request.user)
        if post.report.count()==2:
            post.delete()
            return redirect('blogs')

        return redirect('post',post.pk)