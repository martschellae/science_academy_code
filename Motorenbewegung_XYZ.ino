int HallPin_x = A0;
int HallPin_y = A1;
int HallPin_z = A2;


int HallSignal_x = 0;
int HallSignal_y = 0;
int HallSignal_z = 0;

long normalWert_x = 0;
long normalWert_y = 0;
long normalWert_z = 0;

int millimeterX = 3;
int millimeterY = 5;
int millimeterZ = 1;

int messabstand = 800;
long schrittzaehler = 0;



void messen() {
  HallSignal_x = analogRead(HallPin_x);
  HallSignal_x = HallSignal_x - normalWert_x;

  HallSignal_y = analogRead(HallPin_y);
  HallSignal_y = HallSignal_y - normalWert_x;

  HallSignal_z = analogRead(HallPin_z);
  HallSignal_z = HallSignal_z - normalWert_x;
}

class Motor {
private:
  
  int schrittPin;
  int richtungsPin;
  
public:
long gesamtLaenge;
bool richtung;
long Koordinate;
int delaySchritte;
long schritte;
long distanz;
float faktor;
long gsamtlaenge;

Motor::Motor(int pR, int pS, long K, long gL, int ds, long steps, float fkt){
this->richtungsPin = pR;
this->schrittPin = pS;
this->Koordinate = K;
this->gesamtLaenge = gL;
this->delaySchritte = ds;
this->schritte = steps;
this->faktor = fkt;

pinMode(richtungsPin, OUTPUT);
pinMode(schrittPin, OUTPUT);
}

void Motor::schritt(){
  if(richtung)
  {
    digitalWrite(richtungsPin, HIGH);
    digitalWrite(schrittPin, HIGH);
    digitalWrite(schrittPin, LOW);

    this->Koordinate--;
    schrittzaehler++;
    delayMicroseconds(this->delaySchritte);
  }else{
    digitalWrite(richtungsPin, LOW);
    digitalWrite(schrittPin, HIGH);
    digitalWrite(schrittPin, LOW);

    schrittzaehler++;
    this->Koordinate++;
    delayMicroseconds(this->delaySchritte);
  }

}

void Motor::bewegen(long millimeter, bool ausgeben) 
{
  distanz = millimeter * schritte / faktor;
  for(int c = 0; c < distanz; c++)
  {
    if(ausgeben){
      messen();
      printen();
    }
    this->schritt();
  }
}

void Motor::hochfahren()
{
  for (int c=0; c<(this->gesamtLaenge - this->Koordinate); c++){
    this->schritt();
  }
}

void Motor::richtungHoch() {
  this->richtung = false;
}

void Motor::richtungRunter() {
  this->richtung = true;
}
void Motor::nullpunkt(int zeit) {
  for(int c = 0; c <= zeit; c++) {
    this->richtungHoch();
    schritt();
  }
  this->Koordinate = 0;
}

void Motor::durchschnitt() {
  normalWert_x = normalWert_x + analogRead(HallPin_x);
  normalWert_y = normalWert_y + analogRead(HallPin_y);
  normalWert_z = normalWert_z + analogRead(HallPin_z);
}

void Motor::umrechnen(){
  this->gsamtlaenge = this->gesamtLaenge * this->schritte / this->faktor;
}
};

void setup(){
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  Serial.begin(250000);
 
  scannenXY();
}

void loop()
{
  
}
Motor motorx(6,5, 0, 9, 10, 3200, 2);
Motor motory(6,3, 0, 10, 10, 3200, 2);
Motor motorz(6, 4, 0, 5, 1000, 6400, 51.7);


void scannenXY(){

  motorx.umrechnen();
  motory.umrechnen();
  motorz.umrechnen();
 
  motorz.Koordinate=0;
  motory.Koordinate = motory.gsamtlaenge;
  motorz.richtungHoch();
  motorz.bewegen(70, false);
  
  for(int c = 0; c < 500; c++)
  {
    motorx.durchschnitt();
  }
  normalWert_x = normalWert_x / 500;
  normalWert_y = normalWert_y / 500;
  normalWert_z = normalWert_z / 500;
  motorz.richtungRunter();
  motorz.bewegen(70, false);
  
  while(motorz.Koordinate < motorz.gsamtlaenge) {

      while(motorx.Koordinate < motorx.gsamtlaenge) {
        motory.richtungRunter();
        motory.bewegen(millimeterY, true);
        motorx.richtungHoch();
        motorx.bewegen(millimeterX, true);
        motory.richtungHoch();
        motory.bewegen(millimeterY, true);
        motorx.richtungHoch();
        motorx.bewegen(millimeterX, true);
      }
      motory.richtungRunter();
      motory.bewegen(millimeterY, true);
      motorz.richtungHoch();
      motorz.bewegen(millimeterZ, true);
      while(motorx.Koordinate >= 0) {
        motory.richtungHoch();
        motory.bewegen(millimeterY, true);
        motorx.richtungRunter();
        motorx.bewegen(millimeterX, true);
        motory.richtungRunter();
        motory.bewegen(millimeterY, true);
        motorx.richtungRunter();
        motorx.bewegen(millimeterX, true);
      }
      motory.richtungHoch();
      motory.bewegen(millimeterY, true);
      motorz.richtungHoch();
      motorz.bewegen(millimeterZ, true);
  }

}
void printen()
{  if(schrittzaehler % messabstand == 0){

      Serial.print(motorx.Koordinate);
      Serial.print(", ");
      Serial.print(motory.Koordinate);
      Serial.print(", ");
      Serial.print(motorz.Koordinate);
      Serial.print(", ");

      Serial.print(HallSignal_x);
      Serial.print(", ");
      Serial.print(HallSignal_y);
      Serial.print(", ");
      Serial.print(HallSignal_z);
      Serial.println("");
    }
}