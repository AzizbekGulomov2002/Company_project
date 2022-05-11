from django.contrib import admin


from .models import Exercises, Worker, Work_table



class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name','position','birth_date']
    list_per_page=4
    search_fields = ['name','position','birth_date']
    
    

admin.site.register(Worker, WorkerAdmin)
    

class ExercisesAdmin(admin.ModelAdmin):
    list_display = ['title','start_date','dedline','status']
    list_per_page=4
    search_fields = ['title','start_date','dedline','status',]

admin.site.register(Exercises, ExercisesAdmin)

class Work_tableAdmin(admin.ModelAdmin):
    list_display = ['worker_id','name_id','title']
    list_per_page=4
    search_fields = ['worker_id','name_id','title']
    
    
admin.site.register(Work_table, Work_tableAdmin)






