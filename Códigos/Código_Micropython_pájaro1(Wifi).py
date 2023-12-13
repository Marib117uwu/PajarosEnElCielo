import uasyncio as asyncio
import network
from machine import Pin, PWM
from time import sleep
from hcsr04 import HCSR04
from umqtt.simple import MQTTClient

#Declarar el sensor 
sensor = HCSR04(trigger_pin=5,echo_pin=18,echo_timeout_us=24000)

#Declaro Servo
servo = PWM(Pin(13), freq=50)

#Declaracion de varible para led
led1=Pin(12, Pin.OUT)
led2= Pin(4, Pin.OUT)
led3 = Pin(23, Pin.OUT)
led4 = Pin(14, Pin.OUT)
led5 = Pin(27, Pin.OUT)
led6 = Pin(26, Pin.OUT)
led7 = Pin(25, Pin.OUT)
led8 = Pin(33, Pin.OUT)

# Posición de grados que tiene el servo
pos = 0

# Iniciamos el servo en la posición inicial
servo.duty(pos)

#WIFI
#definir la propiedad de conexion
MQTT_BROKER= "192.168.1.100"
MQTT_CLIENT_ID = ""
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_TOPIC = "utng/mrt/pajaros_en_el_cielo"
MQTT_PORT = 1883
#Declaramos una funcion para wifi
def conectar_wifi():
    print("Conectando", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("linksys","")
    while not sta_if.isconnected():
        print(".",end="")
        sleep(0.3)
    print("Wifi conectada!")

#Funcion que realiza encender un led y apaga un led 
#De acuerdo al mensaje recibido  del servidor
def llegada_mensaje(topic, msg):
    print("Mensaje: ", msg)
    if msg == b'1':
        led2.value(1)
    elif msg== b'2':
        led3.value(1)
    elif msg== b'3':
        led4.value(1)
    elif msg== b'4':
        led6.value(1)
    elif msg== b'5':
        led7.value(1)
    elif msg== b'6':
        led8.value(1)
    elif msg == b'0':
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led6.value(0) 
        led7.value(0)
        led8.value(0)
    else:
        print("Mensaje no valido")

#Funcion que permite la suscripcion al servidor
#Devuelve un cliente
def suscribir():
    client = MQTTClient(MQTT_CLIENT_ID,MQTT_BROKER,port=MQTT_PORT,user=MQTT_USER,
    password=MQTT_PASSWORD,keepalive=0)
    client.set_callback(llegada_mensaje)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectando a: ", MQTT_BROKER,
    "en el topico: ", MQTT_TOPIC)
    return client
#Conectar wifi
conectar_wifi()
#crear objecto wifi
client = suscribir()

#Ciclo infinito
async def tarea_1():
    while True:
        #Declaramos una variable de distancia 
        distancia = sensor.distance_cm()
        #print("Distancia: ", distancia, "centímetros")

        if distancia < 30 :
            for pos in range(0, 90):
                servo.duty(pos * 10)
                sleep(0.01)
            # Mover el servo en el rango de 90 a 0 grados
            for pos in range(90, -1, -1):
                servo.duty(pos * 10)
                sleep(0.01)
            led1.value(1)
            led5.value(1)
            led2.value(1)
            led3.value(1)
            led4.value(1)
            led6.value(1)
            led7.value(1)
            led8.value(1)
            
        await asyncio.sleep(1)
        break
        
async def tarea_2():
    print("Esta es tarea dos")
    #client.wait_msg()
    client.check_msg()
    await asyncio.sleep(1)
    
# Ciclo principal adaptado para Node-RED
async def main():
    while True:
        await asyncio.gather(tarea_1(), tarea_2())
        await asyncio.sleep(0.1)  # Asegura que el bucle de eventos tenga tiempo para ejecutarse

# Ejecutar el bucle principal
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
