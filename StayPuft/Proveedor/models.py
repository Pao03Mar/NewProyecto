# Create your models here.
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class Proveedor(models.Model):
    regex_telefono = r'^(\d{3})-(\d{7})$'
    validar_telefono = RegexValidator(regex_telefono, message="El telefono debe contener 10 digitos en un formato de 'XXX-XXXXXXX'")

    regex_cuil = r'^(\d{2})-(\d{8})-(\d{1})$'
    validar_cuil = RegexValidator(regex_cuil, message="Debe tener un formato de XX-XXXXXXXX-X")

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name='Nombre', validators=[RegexValidator(r'^[a-zA-Z\s]+$', message="El nombre debe contener solo letras")])
    cuit = models.CharField(max_length=13, verbose_name='cuit', validators=[validar_cuil])
    telefono = models.CharField(max_length=11, verbose_name='Telefono', validators=[validar_telefono])
    direccion= models.CharField(max_length=100, verbose_name='direccion')
    correo = models.EmailField(verbose_name='correo')

    def __str__(self):
        fila = f"{self.id}: {self.nombre} {self.cuil} {self.tipo} {self.email}"
        return fila