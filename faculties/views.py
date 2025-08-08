from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Faculty

def faculty_overview(request):
    """Display overview of all faculties"""
    faculties = Faculty.objects.all()
    return render(request, 'faculties/faculty_overview.html', {'faculties': faculties})

def faculty_detail(request, faculty_id):
    """Display detailed view of a specific faculty"""
    faculty = get_object_or_404(Faculty, id=faculty_id)
    return render(request, 'faculties/faculty_detail.html', {
        'faculty': faculty,
        'faculty_id': faculty_id
    })

@login_required
def apply_to_faculty(request, faculty_id):
    """Handle faculty application"""
    faculty = get_object_or_404(Faculty, id=faculty_id)
    return render(request, 'faculties/apply_to_faculty.html', {'faculty': faculty})

