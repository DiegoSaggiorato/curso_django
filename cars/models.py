from django.db import models

# Create your models here.

class Car (models.Model): # herda da classe model do django
	# agora a partir daqui vamos escrever os nossos campos
	id = models.AutoField(primary_key=True) # ele se autopreenche com chave primária
	model = models.CharField(max_length = 200, blank = True, null=True) # o modelo dos carros Charfilds é um camop do tipo string
	# max_length = máximo do tamanho da string
	# blank= True permite deixar o campo em branco
	# null - True permite deixar nulo se quiser
	brand = models.CharField(max_length = 200) # marca
	factory_year = models.IntegerField() # ano de fabricação
	model_year = models.IntegerField() # ano do modelo
	value = models.FloatField(blank = True, null= True) # valor
	
	