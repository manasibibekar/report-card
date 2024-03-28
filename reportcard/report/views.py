from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q, Sum


def homepage(request):

    if request.GET.get('search_html'):
        to_search = request.GET.get('search_html')   
        queryset = Student.objects.all()
        queryset = queryset.filter(
            Q(student_name__icontains = to_search) |
            Q(department__department__icontains = to_search) |
            Q(student_id__student_id__icontains = to_search) | 
            Q(student_email__icontains = to_search)
        )
    
    else:
        queryset = Student.objects.all()

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {"students": page_obj}
    return render(request, 'home.html', context)


def see_marks(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id = student_id)
    total_marks_dict = queryset.aggregate(total_marks = Sum('marks'))
    total_marks = total_marks_dict.get('total_marks')
    return render(request, 'see_marks.html', {'queryset': queryset, 'total_marks': total_marks})
