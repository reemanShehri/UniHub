from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, Course, Board, Post, Reply, Notification, Announcement
from .forms import *
from django.db.models import Q


def home(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)  # تأخير الحفظ
            user.gender = form.cleaned_data['gender']  # تخصيص الحقول
            user.date_of_birth = form.cleaned_data['date_of_birth']
            user.save()  # الحفظ بعد التخصيص
            login(request, user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request, 'pages/signup.html', {'form': form})




@login_required
def profile(request):
    return render(request, 'pages/completeProfile.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        data =loginForm(username=username,password=password)
        data.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'pages/login.html')

@login_required
def logout(request):
    logout(request)
    return redirect('home')

# @login_required
# def dashboard(request):
#     student = Student.objects.get(user=request.user)
#     courses = student.courses.all()
#     boards = Board.objects.filter(course__in=courses)
#     posts = Post.objects.filter(board__in=boards)
#     return render(request, 'pages/Dashboard.html', {'student': student, 'courses': courses, 'boards': boards, 'posts': posts})



@login_required
def dashboard(request):
    # جلب الطالب المرتبط بالمستخدم الحالي مباشرة
    student = Student.objects.get(user=request.user)
    # جلب الدورة المرتبطة بالطالب (إذا كانت واحدة)
    course = student.courses.first()  # يمكن استخدام .first() للحصول على أول دورة فقط
    # جلب المجموعات المرتبطة بالدورة
    boards = Board.objects.filter(course=course)
    # جلب المشاركات المرتبطة بالمجموعات
    posts = Post.objects.filter(board__in=boards)

    return render(request, 'pages/Dashboard.html', {
        'student': student,
        'course': course,
        'boards': boards,
        'posts': posts,
    })

    try:
        # الحصول على الطالب المرتبط بالمستخدم الحالي
        student = get_object_or_404(Student, user=request.user)
        # جلب جميع الدورات المرتبطة بالطالب
        courses = student.courses
        # جلب جميع المجموعات المرتبطة بالدورات
        boards = Board.objects.filter(course__in=courses)
        # جلب جميع المشاركات المرتبطة بالمجموعات
        posts = Post.objects.filter(board__in=boards)

        # عرض البيانات في الصفحة
        return render(request, 'pages/Dashboard.html', {
            'student': student,
            'courses': courses,
            'boards': boards,
            'posts': posts
        })
    except Exception as e:
        # معالجة الأخطاء غير المتوقعة
        return render(request, 'pages/Error.html', {'error': str(e)})

@login_required
def create_post(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = Student.objects.get(user=request.user)
            post.board = board
            post.save()
            return redirect('board_detail', board_id=board.id)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form, 'board': board})

@login_required
def board_detail(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    posts = Post.objects.filter(board=board)
    return render(request, 'board_detail.html', {'board': board, 'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    replies = Reply.objects.filter(post=post)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = Student.objects.get(user=request.user)
            reply.post = post
            reply.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = ReplyForm()
    return render(request, 'Board.html', {'post': post, 'replies': replies, 'form': form})

@login_required
def create_announcement(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.board = board
            announcement.save()
            return redirect('board_detail', board_id=board.id)
    else:
        form = AnnouncementForm()
    return render(request, 'create_announcement.html', {'form': form, 'board': board})





def search(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        courses = Course.objects.filter(name__icontains=query)
    else:
        posts = Post.objects.all()
        courses = Course.objects.all()
    return render(request, 'search_results.html', {'posts': posts, 'courses': courses, 'query': query})



@login_required
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user.student)
    notification.is_read = True
    notification.save()
    return redirect('dashboard')




def student_detail(request, id):
     student = Student.objects.get(pk=id)  # Fetch the student using the ID
     return render(request, 'pages/student_detail.html', {'student': student})
