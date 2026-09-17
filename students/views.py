from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages


def student_list(request):
    search = request.GET.get('search', '')

    if search:
        students = Student.objects.filter(
            name__icontains=search
        ) | Student.objects.filter(
            email__icontains=search
        ) | Student.objects.filter(
            department__icontains=search
        )
    else:
        students = Student.objects.all()

    total_students = Student.objects.count()

    return render(request, 'students/student_list.html', {
        'students': students,
        'search': search,
        'total_students': total_students
    })


def add_student(request):
    if request.method == 'POST':

        email = request.POST['email']

        if Student.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return render(request, 'students/add_student.html')

        Student.objects.create(
            name=request.POST['name'],
            email=email,
            phone=request.POST['phone'],
            address=request.POST['address'],
            department=request.POST['department']
        )

        messages.success(request, 'Student added successfully!')
        return redirect('student_list')

    return render(request, 'students/add_student.html')


def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == 'POST':

        email = request.POST['email']

        if Student.objects.filter(email=email).exclude(id=id).exists():
            messages.error(request, 'Email already exists!')
            return render(request, 'students/edit_student.html', {
                'student': student
            })

        student.name = request.POST['name']
        student.email = email
        student.phone = request.POST['phone']
        student.address = request.POST['address']
        student.department = request.POST['department']

        student.save()

        messages.success(request, 'Student updated successfully!')
        return redirect('student_list')

    return render(request, 'students/edit_student.html', {
        'student': student
    })


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()

    messages.success(request, 'Student deleted successfully!')
    return redirect('student_list')