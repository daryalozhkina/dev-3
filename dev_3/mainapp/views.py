from django.shortcuts import render

from mainapp.models import CollegeGroup, Student


def index(request):
    return render(request, 'mainapp/index.html')


def students(request):
    categories = CollegeGroup.objects.all()
    context = {
        'categories': categories,
        'page_title': 'каталог'
    }
    return render(request, 'mainapp/students.html', context)


def student_page(request, pk):
   items = Student.objects.filter(category_id=pk)
   context = {
       'items': items,
       'page_title': 'cтраница студентов'
   }
   return render(request, 'mainapp/students_pade.html', context)

# Create your views here.
