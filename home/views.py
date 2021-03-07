from django.shortcuts import render
from .forms import StudentForm
from .models import Student
from django.http import JsonResponse

# Create your views here.
def home_view(request):
    form = StudentForm()
    students = Student.objects.all()
    context = {
        'form':form,
        'students':students,
    }
    return render(request,"home.html",context)


def save_data(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            data = Student.objects.values().order_by('-id')
            st_data =list(data)
            return JsonResponse({'status':'success','st_data':st_data[0],})
        return JsonResponse({'status':'fail'})


def delete_data(request):
    if request.method == "GET":
        id = request.GET['sid']
        print(id)
        data = Student.objects.get(id=id)
        data.delete()
        return JsonResponse({'status':'success'})

def edit_data(request):
    if request.method == "POST":
        id = request.POST['id']
        data = Student.objects.get(id=id)
        print(data)
        data.name=request.POST['name']
        print(request.POST['name'])
        data.age=request.POST['age']
        data.address=request.POST['address']
        data.save()
        return JsonResponse({'id':data.id,'name':data.name,'age':data.age,'address':data.address,})
        # form = StudentForm(request.POST,instance=data)
        # print(form.errors)
        # if form.is_valid():
        #     print('yoo')
        #     form.save()
        #     return JsonResponse({'data-sid':data.id})
    else:
        id = request.GET['sid']
        data = Student.objects.get(id=id)
        st_data = {'id':data.id,'name':data.name, 'age':data.age, 'address':data.address }
        return JsonResponse(st_data)
