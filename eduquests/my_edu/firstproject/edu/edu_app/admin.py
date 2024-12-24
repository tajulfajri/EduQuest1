from django.contrib import admin
from .models import QuizResult, UserClass, Class, UserProfile, Progress
# Impor model Anda

# Mendaftarkan model ke admin site
@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'quiz_name', 'score', 'submit_date')  # Kolom yang ditampilkan

# Menambahkan Class model ke admin
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Menampilkan nama dan deskripsi kelas di admin
    search_fields = ('name',)  # Menambahkan pencarian berdasarkan nama kelas

admin.site.register(Class, ClassAdmin)

# Menambahkan UserClass model ke admin
class UserClassAdmin(admin.ModelAdmin):
    list_display = ('user', 'class_name', 'is_paid')  # Menampilkan pengguna, kelas, dan status pembayaran
    list_filter = ('is_paid',)  # Menambahkan filter berdasarkan status pembayaran
    search_fields = ('user__username', 'class_name__name')  # Pencarian berdasarkan username dan nama kelas

admin.site.register(UserClass, UserClassAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','full_name', 'age', 'kelas', 'gender', 'parent_phone')
    search_fields = ['user__username', 'full_name', 'kelas']
    list_filter = ('gender', 'kelas')

admin.site.register(Progress)
    




