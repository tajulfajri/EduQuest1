from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from edu_app.models import QuizResult
from django.utils import timezone
from .forms import signupform, UserForm
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import UserClass, Class, UserProfile, Progress
from .forms import UserProfileForm
from django.db.models import Sum
import re


# Fungsi untuk Signup
def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('edu_app:login')
    else:
        form = signupform()
    return render(request, 'edu_app/signup.html', {'form': form})

# Fungsi untuk Login
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('edu_app:dashboard')
        else:
            return render(request, 'edu_app/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'edu_app/login.html')

# Fungsi untuk Logout
def logout_view(request):
    logout(request)
    return redirect('edu_app:home')

# Fungsi untuk Home
def home(request):
    return render(request, 'edu_app/home.html')

# Fungsi untuk Our Team
def ourteam(request):
    return render(request, 'edu_app/ourteam.html')

# Fungsi untuk Course
def course(request):
    return render(request, 'edu_app/course.html')

# Fungsi untuk Dashboard
def dashboard(request):
    return render(request, 'edu_app/dashboard.html')

# Fungsi untuk Class 1
def class1(request):
    return render(request, 'edu_app/class1.html')

def class2(request):
    return render(request, 'edu_app/class2.html')

def class3(request):
    return render(request, 'edu_app/class3.html')

def class4(request):
    return render(request, 'edu_app/class4.html')

def class5(request):
    return render(request, 'edu_app/class5.html')

def class6(request):
    return render(request, 'edu_app/class6.html')

# Fungsi untuk Belajar Menyenangkan
def belajarmenyenangkan(request):
    return render(request, 'edu_app/belajarmenyenangkan.html')

# Fungsi untuk Minat Bakat
def minatbakat(request):
    return render(request, 'edu_app/minatbakat.html')

# Fungsi untuk Manajemen Waktu
def manajemenwaktu(request):
    return render(request, 'edu_app/manajemenwaktu.html')

# Fungsi untuk Materi Modul 1
def materimodul1(request):
    return render(request, 'edu_app/materimodul1.html')


def materimodul1class3(request):
    return render(request, 'edu_app/materimodul1class3.html')

# Fungsi untuk Quiz Modul 1
def Quizmodul1_view(request):
    return render(request, 'edu_app/Quizmodul1.html')

def quizresult(request):
    return render(request, 'edu_app/quizresult.html')

def profil(request):
    return render(request, 'edu_app/profil.html')

def detail(request):
    return render(request, 'edu_app/detail.html')

def materimodul2(request):
    return render(request, 'edu_app/materimodul2.html')

def materimodul3(request):
    return render(request, 'edu_app/materimodul3.html')

def Quizclass3(request):
    return render(request, 'edu_app/Quizclass3.html')

def courses(request):
    return render(request, 'edu_app/courses.html')

def kosakata(request):
    return render(request, 'edu_app/kosakata.html')

def leaderboard(request):
    return render(request, 'edu_app/leaderboard.html')

def hasilquiz(request):
    return render(request, 'edu_app/hasilquiz.html')

def progressbelajar(request):
    return render(request, 'edu_app/progressbelajar.html')

def Inggrismudah(request):
    return render(request, 'edu_app/Inggrismudah.html')

def materimodul1class4(request):
    return render(request, 'edu_app/materimodul1class4.html')

def quizmodul1class4(request):
    return render(request, 'edu_app/quizmodul1class4.html')

def modul1class6(request):
    return render(request, 'edu_app/modul1class6.html')

def quizmodul1class6(request):
    return render(request, 'edu_app/quizmodul1class6.html')

def pembayaran(request):
    return render(request, 'edu_app/pembayaran.html')

def materimodul1(request):
    youtube_url = "https://youtu.be/GpZQ8iMPzS4?si=9BXQ-Td7IqAhy7ce"  # URL YouTube
    video_id = get_youtube_id(youtube_url)  # Ambil ID video
    return render(request, 'edu_app/materimodul1.html', {'video_id': video_id})

def materimodul1class3(request):
    youtube_url = "https://youtu.be/74FA1dyVVKs?si=gUlFOWdOSrpUilNf"  # URL YouTube
    video_id = get_youtube_id(youtube_url)  # Ambil ID video
    return render(request, 'edu_app/materimodul1class3.html', {'video_id': video_id})

def materimodul1class4(request):
    youtube_url = "https://youtu.be/ll7X981C4c8?si=0W18v0WAYudDv6VU"  # URL YouTube
    video_id = get_youtube_id(youtube_url)  # Ambil ID video
    return render(request, 'edu_app/materimodul1class4.html', {'video_id': video_id})

def modul1class6(request):
    youtube_url = "https://youtu.be/hjFaqDNUVFo?si=72eiEpK3uZX0-ZPN"  # URL YouTube
    video_id = get_youtube_id(youtube_url)  # Ambil ID video
    return render(request, 'edu_app/modul1class6.html', {'video_id': video_id})

def get_youtube_id(url):
    """
    Fungsi untuk mengambil ID video dari URL YouTube
    """
    match = re.search(r'(youtu\.be/|youtube\.com/watch\?v=|youtube\.com/embed/)([a-zA-Z0-9_-]+)', url)
    if match:
        return match.group(2)  # ID video ada di grup kedua
    return None


# Fungsi untuk Kuiz

def Quizmodul1(request):
    user = request.user
    if request.method == 'POST':
        quiz_name = request.POST.get('quiz_name')
        correct_answers = {
            'question1': 'Good Morning',
            'question2': 'Good Night',
            'question3': 'Sore/Malam',
            'question4': 'Good Afternoon',
            'question5': 'How are you?',
            'question6': 'Im Happy',
            'question7': 'Im Tired',
            'question8': 'Pagi',
            'question9': 'Good Afternoon',
            'question10': 'Good Evening',
            'question11': 'Good Night',
            'question12': 'Apa Kabar?',
            'question13': 'Im Fine, Thank You',
            'question14': 'Siang Hari',
            'question15': 'Good Night',
            'question16': 'Good Afternoon',
            'question17': 'Akan Tidur',
            'question18': 'Im Fine, Thank You',
            'question19': 'Berkenalan',
            'question20': 'See You Later'
        }

        total_score = 0
        for question, correct_answer in correct_answers.items():
            user_answer = request.POST.get(question)
            if user_answer and user_answer.strip().lower() == correct_answer.strip().lower():
                total_score += 5  # Tambah skor 5 untuk jawaban yang benar

        # Tentukan class_number dan module_number sesuai dengan logika atau kebutuhan
        class_number = 1  # Misalnya, Kelas 1
        module_number = 1  # Misalnya, Modul 1

        # Update atau buat objek Progress untuk melacak progres kuis
        progress, created = Progress.objects.get_or_create(user=user, class_number=class_number, module_number=module_number)
        progress.completed = True  # Menandakan kuis sudah selesai
        progress.score = total_score  # Menyimpan total skor
        progress.save()

        # Simpan total skor di session
        request.session['total_score'] = total_score
        request.session['quiz_name'] = quiz_name  # Simpan nama kuis di session

        return redirect('edu_app:quizresult')  # Redirect ke halaman hasil kuis

    return render(request, 'edu_app/Quizmodul1.html')  # Render halaman kuis

# Fungsi untuk Kuiz
@login_required
def quizresult(request):
    score = request.session.get('total_score', 0)  # Mengambil skor dari session
    quiz_name = request.session.get('quiz_name', 'Unknown Quiz')  # Mengambil nama kuis dari session

    # Log data untuk debugging (opsional)
    print(f"Score: {score}, Quiz Name: {quiz_name}")

    if score:  # Jika ada skor, buat objek QuizResult
        user = request.user
        quizresult = QuizResult.objects.create(
            user=user,
            quiz_name=quiz_name,
            score=score
        )
        
        # Ambil waktu submit dan sesuaikan dengan timezone lokal
        submit_time = timezone.localtime(quizresult.submit_date)
        print(f"Submit Date: {submit_time}")

        return render(request, 'edu_app/quizresult.html', {
            'score': score,
            'quiz_name': quiz_name,
            'submit_date': submit_time
        })

    # Jika tidak ada skor, arahkan kembali ke halaman kuis
    return redirect('edu_app:Quizmodul1')


@login_required
def payment_view(request, class_id):
    user_class = UserClass.objects.get(user=request.user, id=class_id)
    
    # Misalnya ini adalah pengecekan apakah pembayaran berhasil (ganti sesuai dengan logika pembayaranmu)
    payment_successful = check_payment_gateway_status()  # type: ignore # Implementasikan ini sesuai dengan gateway yang kamu pakai
    
    if payment_successful:
        # Pembayaran berhasil, update status di database
        user_class.is_paid = True
        user_class.save()

        # Simpan status pembayaran di session jika ingin mempermudah pengecekan status
        request.session['is_paid'] = True

        return redirect('class_detail', class_id=class_id)
    else:
        return render(request, 'payment_failed.html', {'user_class': user_class})


@login_required
def class_detail(request, class_id):
    # Ambil data kelas dan cek apakah pengguna sudah membayar
    user_class = UserClass.objects.get(user=request.user, id=class_id)

    if user_class.is_paid:
        # Jika sudah bayar, tampilkan kelas langsung tanpa modal
        return render(request, 'class_content.html', {'class': user_class})

    # Jika belum bayar, tampilkan modal untuk memilih bayar atau uji gratis
    return render(request, 'class_detail.html', {'class': user_class})

def check_payment_status(request):
    try:
        # Mendapatkan status pembayaran dari model UserClass
        user_class = UserClass.objects.get(user=request.user)
        return JsonResponse({
            "isPaid": user_class.is_paid,  # Menyediakan status pembayaran
            "trialUrl": reverse('edu_app:class6'),  # URL untuk uji coba
            "payUrl": reverse('edu_app:pembayaran'),  # URL untuk pembayaran
        })
    except UserClass.DoesNotExist:
        return JsonResponse({
            "isPaid": False,
            "trialUrl": reverse('edu_app:class6'),
            "payUrl": reverse('edu_app:pembayaran')
        })
    
@login_required
def profil(request):
    # Ambil atau buat profil pengguna jika belum ada
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('edu_app:detail')  # Redirect setelah berhasil simpan
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'edu_app/profil.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'user_profile': user_profile,  # Kirim user_profile ke template
    })


def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()  # Menyimpan foto profil
            return redirect('edu_app:profil')  # Redirect ke halaman profil setelah penyimpanan
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'edu_app/profil.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def detail(request):
    # Ambil profil pengguna yang sedang login
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    return render(request, 'edu_app/detail.html', {'profile': user_profile})

def dashboard(request):
     # Ambil profil pengguna yang sedang login, atau buat baru jika belum ada
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    # Kirim objek profile ke template
    return render(request, 'edu_app/dashboard.html', {'profile': user_profile, 'user': request.user})

@login_required
def hasilquiz(request):
    # Ambil hasil quiz terbaru
    latest_result = QuizResult.objects.filter(user=request.user).order_by('-submit_date').first()

    # Ambil semua hasil quiz untuk tabel
    all_results = QuizResult.objects.filter(user=request.user).order_by('-submit_date')

    return render(request, 'edu_app/hasilquiz.html', {
        'latest_result': latest_result,
        'results': all_results
    })

#fungsi untuk leaderboard
@login_required
def leaderboard(request):
    # mengelompokkan score berdasarkan pengguna, menghitung total score, dan mengurutkan secara global
    leaderboard_data = QuizResult.objects.values('user__username')\
        .annotate(total_score=Sum('score'))\
        .order_by('-total_score')[:5] #batasi hanya 10 teratas
    
    return render(request, 'edu_app/leaderboard.html',{
        'leaderboard_data': leaderboard_data,
    })
    
def set_payment_session(request):
    if request.method == 'POST':
        # Perbarui sesi dengan status pembayaran
        print("POST request received")  # Verifikasi permintaan diterima
        print(request.body)  # Cek apakah ada data yang dikirim
        request.session['payment_status'] = 'success'
        print("Session set:", request.session.get('payment_status'))  # Cek sesi
        return JsonResponse({'message': 'Payment session updated successfully.'})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def check_session(request):
    # Mengambil data dari sesi
    payment_status = request.session.get('payment_status', 'Not set')
    return JsonResponse({'payment_status': payment_status})

def progressbelajar(request):
    user = request.user
    progress_data = {}

    for class_number in range(1, 7):  # Kelas 1 hingga Kelas 6
        completed_modules = Progress.objects.filter(user=user, class_number=class_number, completed=True).count()
        total_modules = 6  # Total modul per kelas
        percentage = (completed_modules / total_modules * 100) if total_modules > 0 else 0
        progress_data[class_number] = {
            'completed': completed_modules,
            'total': total_modules,
            'percentage': percentage,  # Hitung persentase di sini
        }

    return render(request, 'edu_app/progressbelajar.html', {'progress_data': progress_data})


def progress_view(request):
    progress_data = {
        1: {"completed": 5, "total": 10, "percentage": 50},
        2: {"completed": 3, "total": 10, "percentage": 30},
    }
    return render(request, 'progressbelajar.html', {'progress_data': progress_data})


