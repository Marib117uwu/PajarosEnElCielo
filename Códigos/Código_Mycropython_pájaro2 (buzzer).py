
from machine import Pin, PWM
from time import sleep

# Crear objeto buzzer
buzzer = PWM(Pin(2), freq=440, duty=512)

# Definir una función para emitir sonido
def sonido(freq, duracion):
    buzzer.freq(freq)
    buzzer.duty(512)
    sleep(duracion)
    buzzer.duty(0)  # Apagar el sonido después de la duración

# Función para la melodía de "Entre campanas"
def entre_campanas():
    sonido(659, 0.5)  # Frecuencia para el primer tono (Mi)
    sleep(0.5)  # Pausa de 0.5 segundos
    sonido(587, 0.5)  # Frecuencia para el segundo tono (Re)
    sleep(0.5)  # Pausa de 0.5 segundos
    sonido(659, 0.5)  # Frecuencia para el tercer tono (Mi)
    sleep(0.5)  # Pausa de 0.5 segundos
    sonido(587, 0.5)  # Frecuencia para el cuarto tono (Re)
    sleep(0.5)  # Pausa de 0.5 segundos

# Función para la melodía de "Los peces en el río"
def peces_en_el_rio():
    sonido(659, 0.5)  # Frecuencia para el primer tono (Mi)
    sleep(0.5)  # Pausa de 0.5 segundos
    sonido(587, 0.5)  # Frecuencia para el segundo tono (Re)
    sleep(0.5)  # Pausa de 0.5 segundos
    sonido(523, 1)  # Frecuencia para el tercer tono (Do)
    sleep(1)  # Pausa de 1 segundo

# Iniciar el ciclo infinito
try:
    while True:
        entre_campanas()  # Reproduce la melodía de "Entre campanas"
        sleep(600)  # Pausa de 10 minutos (600 segundos) entre cada melodía
        peces_en_el_rio()  # Reproduce la melodía de "Los peces en el río"
        sleep(600)  # Pausa de 10 minutos (600 segundos) entre cada melodía
except KeyboardInterrupt:
    # Si se presiona Ctrl+C, se detiene el bucle y se apaga el buzzer
    buzzer.duty(0)





















