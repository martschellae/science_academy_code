int delayScritte = 200;



class Motor {
private:
  bool richtung;
  int schrittPin;
  int richtungsPin;
  int Koordinate;
  int gesamtLaenge;
public:

Motor::Motor(int pR, int pS) {
  this->richtungsPin = pR;
  this->schrittPin = pS;

  pinMode(richtungsPin, OUTPUT);
  pinMode(schrittPin, OUTPUT);
}

void Motor::schritt() {
  if(richtung) {
    digitalWrite(richtungsPin, HIGH);
    digitalWrite(schrittPin, HIGH);
    digitalWrite(schrittPin, LOW);

    
    delayMicroseconds(delayScritte);
  } else {   
    digitalWrite(richtungsPin, LOW);
    digitalWrite(schrittPin, HIGH);
    digitalWrite(schrittPin, LOW);

    
    delayMicroseconds(delayScritte);
  }

}

void Motor::bewegen(int anzahl) {
  for(int c = 0; c < anzahl; c++)
  {
    schritt();
    
  }
}
void Motor::hochfahren() {
  for (int c=0; c<(this->gesamtLaenge - this->Koordinate); c++){
    this->schritt();
  }
}

void Motor::richtungAendern() {
  this->richtung = !this->richtung;
}

void Motor::startpunkt(){
  this->richtungAendern();
  while(this->Koordinate != 0)
  {
    this->schritt();
  }
}

};




void setup() {
  // put your setup code here, to run once:

  Motor motorx(6, 4);
  Motor motory(6, 5);
  Motor motorz(6, 3);

  motorx.bewegen(1600);
  //motorx.richtungAendern();
  motorx.bewegen(1600);

  motory.bewegen(1600);
  //motory.richtungAendern();
  motory.bewegen(1600);

  delay(10000);

  motorz.bewegen(1600);
  //motorz.richtungAendern();
  motorz.bewegen(1600);
}

void loop() {
  // put your main code here, to run repeatedly:

}
