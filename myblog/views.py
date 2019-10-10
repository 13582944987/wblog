from django.shortcuts import render,redirect

from myblog.models import Blog
import os

# import markdown

def index(request):
    # 主界面
    blog = Blog.objects.all().filter()
    blog_data = {
        'blog': blog
    }
    return render(request,'index.html',blog_data)

def blog_content(request,id):
    #博客内容
    blod_conet = Blog.objects.get(id = id)
    blog = Blog.objects.all().filter()

    blog_data = {
        'blog': blog,
        'blod_conet': blod_conet
    }
    return render(request,'index2.html',blog_data)





def user_infor(request):
    if request.method == "POST":
        blog_title = request.POST.get("blog_title")
        blog_text = request.POST.get("blog_text")
        blog_types = request.POST.get("blog_types")
        Blog.objects.create(
            title=blog_title,
            content=blog_text,
            categorie = blog_types
        )
        #重定向到首页
        return redirect('/myblog/')
        # blog = Blog.objects.all().filter()
        # blog_data = {
        #     'blog':blog
        # }
        # return render(request,'index2.html',blog_data)
    else:
        return render(request,'index2.html')\

#文件上传
def user_file(request):
    file = request.FILES.get('img')
    file_path = os.path.join('static/media',file.name)
    f = open(file_path, mode='wb')
    for i in file.chunks():
        f.write(i)
    f.close()
    return redirect('/myblog')