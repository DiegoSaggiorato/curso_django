from django.contrib import admin

# precisamos importar a nossa classe para indicar ao admin
from cars.models import Car

class CarAdmin(admin.ModelAdmin):# herdando da classe ModelAdmin
	# teremos que usar estes mesmo nomes para subscrever as classes herdada
	list_display = ('model','brand','factory_year','model_year','value')
	# indica quais campos quer deixar a disposição do admin
	search_fields = ('model',)
	# é o campo de busca que o usuário poderá fazer
	
admin.site.register(Car,CarAdmin)
# este comando aponta para o django qual classe quero registrar e a classe de permissão do admin