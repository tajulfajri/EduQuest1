from django.db import models
from django.contrib.auth.models import User

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Menghubungkan ke pengguna
    quiz_name = models.CharField(max_length=255)  # Nama kuis
    score = models.IntegerField()  # Skor kuis
    submit_date = models.DateTimeField(auto_now_add=True)  # Tanggal submit otomatis

    def __str__(self):
        return f"{self.user.username} - {self.quiz_name} - {self.score}"

    def save(self, *args, **kwargs):
        if QuizResult.objects.filter(user=self.user, quiz_name=self.quiz_name).exists():
            raise ValueError("User sudah mengikuti kuis ini.")
        super().save(*args, **kwargs)
    
class UserClass(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=False)
    
# Model untuk menyimpan informasi kelas
class Class(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    # Menghubungkan ke model User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)  # Gambar 
    # Data tambahan
    full_name = models.CharField(max_length=100, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    kelas = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], blank=True, null=True)
    parent_phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
   
    def __str__(self):
        return self.user.username
    
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_number = models.IntegerField(default=1)  # Menetapkan nilai default untuk class_number
    module_number = models.IntegerField()  # Modul 1, Modul 2, ...
    score = models.IntegerField(default=0)  # Skor yang didapatkan
    completed = models.BooleanField(default=False)  # Apakah modul ini sudah selesai

    def __str__(self):
        return f"Progress {self.user.username} - Modul {self.module_number} - Kelas {self.class_number}"

