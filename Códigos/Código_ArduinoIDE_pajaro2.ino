int pinPulsador = 8; // Declaramos el número del pin donde está conectado el pulsador
int pinMotor = 9;  // Pin del motor
int pinLED = 13; // Pin para el LED

int estadoPulsador = 0; // Variable para guardar el estado actual del pulsador
int estadoPulsadorAnterior = 0; // Variable para guardar el estado anterior del pulsador
int estadoMotor = LOW; // Variable para guardar el estado del motor

void setup() {
   pinMode(pinMotor, OUTPUT); // Inicializa el pin del motor como salida
   pinMode(pinPulsador, INPUT); // Inicializa el pin del pulsador como entrada
   pinMode(pinLED, OUTPUT); // Inicializa el pin del LED como salida
   digitalWrite(pinMotor, LOW); // Establece el motor en estado de reposo
   digitalWrite(pinLED, LOW); // Apaga el LED inicialmente
}

void loop() {
   estadoPulsador = digitalRead(pinPulsador); // Lee el valor actual del pulsador
   delay(50); // Pequeña pausa para estabilidad

   // Verifica si el pulsador cambió de estado
   if (estadoPulsador != estadoPulsadorAnterior) {
     if (estadoPulsador == HIGH) { // Si el pulsador se ha presionado
       estadoMotor = !estadoMotor; // Invierte el estado del motor (enciende/apaga)
       digitalWrite(pinMotor, estadoMotor); // Actualiza el estado del motor

       if (estadoMotor == HIGH) {
         digitalWrite(pinLED, HIGH); // Enciende el LED si el motor está encendido
       } else {
         digitalWrite(pinLED, LOW); // Apaga el LED si el motor está apagado
       }
     }
   }
   
   estadoPulsadorAnterior = estadoPulsador; // Actualiza el estado anterior del pulsador
}