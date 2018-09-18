from django.shortcuts import render,redirect
from app01 import models

def get_students(request):
    stu_list = models.Student.objects.all()
    return render(request,'get_students.html',{'stu_list':stu_list})

def add_students(request):
    if request.method == 'GET':
        cs_list = models.Classes.objects.all()
        #[(id=1,title='aaa')]
        # for row in cs_list:
        #     print(row.id,row.title)
        return render(request,'add_students.html',{'cs_list':cs_list})
    elif request.method == 'POST':
        u = request.POST.get('username')
        a = request.POST.get('age')
        g = request.POST.get('gender')
        c = request.POST.get('cs')
        models.Student.objects.create(
            username = u,
            age = a,
            gender = g,
            cs_id = c
        )
        return redirect('/students.html')

def del_students(request):
    nid = request.GET.get('nid')
    models.Student.objects.filter(id=nid).delete()
    return redirect('/students.html')


def edit_students(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj = models.Student.objects.filter(id=nid).first()
        #obj中有当前学生的班级ID
        print(obj)
        print(obj.id)
        print(obj.username)
        print(obj.age)
        print(obj.gender)
        cls_list = models.Classes.objects.values('id','title')
        #cls_list中有所有班级的ID和班级名称
        # for row in cls_list:
        #     print(row['id'])
        return render(request,'edit_students.html',{'obj' : obj , 'cls_list': cls_list})
    elif request.method == "POST":
        nid = request.GET.get('nid')
        user = request.POST.get('username')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        class_id = request.POST.get('class_id')
        models.Student.objects.filter(id=nid).update(username=user,age=age,gender=gender,cs_id=class_id)
        return redirect('/students.html')

