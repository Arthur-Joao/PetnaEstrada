from django.db import models

from django.db import models


class UF(models.Model):
    sigla = models.CharField(max_length=2, verbose_name="Sigla da Unidade da Federação")


    def __str__(self):
        return self.sigla
   
    class Meta:
        verbose_name = "Unidade da Federação"
        verbose_name_plural = "Unidades da Federação"
   
class Cidade(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da cidade")
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, verbose_name="UF")


    def __str__(self):
        return f"{self.nome}, {self.uf}"
   
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Bairro(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do bairro")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do bairro")


    def __str__(self):
        return f"{self.nome}, {self.cidade}"
   
    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

class Tipo(models.Model):
    especie = models.CharField(max_length=50, verbose_name="Nome da espécie")
    raca = models.CharField(max_length=50, verbose_name="Nome da raça")


    def __str__(self):
        return f"{self.especie}, {self.raca}"
   
    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipos"

class Usuario(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do usuário")
    email = models.CharField(max_length=50, verbose_name="e-mail")
    senha = models.CharField(max_length=50, verbose_name="senha")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    numero = models.CharField(max_length=11, verbose_name="Número de telefone")
    data = models.DateField( verbose_name="data de nascimento")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade do usuário")


    def __str__(self):
        return self.nome
   
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

class Feedback(models.Model):
    estrelas = models.IntegerField(verbose_name="Quantidade de estrelas")
    comentario = models.TextField(verbose_name="comentário")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Nome de usuário")


    def __str__(self):
        return self.comentario
   
    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"

class Status(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Status do animal")


    def __str__(self):
        return self.nome
   
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"

class Animal(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do animal")
    tamanho = models.CharField(max_length=4, verbose_name="Altura(cm) do animal")
    idade = models.IntegerField( verbose_name="Idade do animal")
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name="Tipo do animal")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name="Status do animal")
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, verbose_name="Bairro frequentemente visto")


    def __str__(self):
        return self.nome
   
    class Meta:
        verbose_name="Animal"
        verbose_name_plural="Animais"

class Vacina(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome da vacina")


    def __str__(self):
        return self.nome
   
    class Meta:
        verbose_name = "Vacina"
        verbose_name_plural = "Vacinas"

class FotoAnimal(models.Model):
    id_foto = models.CharField(max_length=100, verbose_name="ID")
    url = models.CharField(max_length=100, verbose_name="URL")
    descricao = models.TextField(verbose_name="Descrição da foto")
    data_upload = models.DateField(verbose_name="data de upload")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal da foto")


    def __str__(self):
        return self.id_foto
   
    class Meta:
        verbose_name = "Foto do animal"
        verbose_name_plural = "Fotos dos animais"

class AnimalporVacina(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    vacina = models.ForeignKey(Vacina, on_delete=models.CASCADE, verbose_name="Vacina")


    def __str__(self):
        return f"{self.animal}, {self.vacina}"
   
    class Meta:
        verbose_name = "Animal por vacina"
        verbose_name_plural = "Animais por vacinas"
