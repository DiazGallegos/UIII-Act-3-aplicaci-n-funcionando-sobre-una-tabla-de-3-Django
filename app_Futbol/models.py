from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fundacion = models.DateField()
    estadio = models.CharField(max_length=100)
    entrenador = models.CharField(max_length=100)
    colores = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    POSICIONES = [
        ('POR', 'Portero'),
        ('DEF', 'Defensa'),
        ('MED', 'Mediocampista'),
        ('DEL', 'Delantero'),
    ]
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=100)
    posicion = models.CharField(max_length=3, choices=POSICIONES)
    numero_camiseta = models.PositiveIntegerField()
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="jugadores")
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Partido(models.Model):
    ESTADOS = [
        ('PEN', 'Pendiente'),
        ('JUG', 'Jugándose'),
        ('FIN', 'Finalizado'),
        ('SUS', 'Suspendido'),
    ]
    
    fecha = models.DateTimeField()
    estadio = models.CharField(max_length=100)
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_local")
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name="partidos_visitante")
    goles_local = models.PositiveIntegerField(default=0)
    goles_visitante = models.PositiveIntegerField(default=0)
    estado = models.CharField(max_length=3, choices=ESTADOS, default='PEN')
    
    def __str__(self):
        return f"{self.equipo_local} vs {self.equipo_visitante}"