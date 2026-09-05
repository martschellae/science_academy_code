int HallPin_x = A0;
int HallPin_y = A1;
int HallPin_z = A2;


int HallSignal_x = 0;
int HallSignal_y = 0;
int HallSignal_z = 0;

int normalWert_x = 0;
int normalWert_y = 0;
int normalWert_z = 0;


int gesamtLaenge_x = 200;
int gesamtLaenge_y = 200;
int gesamtLaenge_z = 200;

int infrarot = 100;
int infrarot2 = 100;

int koordinate_x = 0;
int koordinate_y = 0;
int koordinate_z = 0;

long millimeterz=91;
long schrittez=6400;
long distanz = millimeterz * schrittez / 51.7;


void messen() {
  HallSignal_x = analogRead(HallPin_x);
  HallSignal_x = HallSignal_x - normalWert_x;

  HallSignal_y = analogRead(HallPin_y);
  HallSignal_y = HallSignal_y - normalWert_y;

  HallSignal_z = analogRead(HallPin_z);
  HallSignal_z = HallSignal_z - normalWert_z;
}

class Motor {
private:
  
  int schrittPin;
  int richtungsPin;
  int gesamtLaenge;
public:
bool richtung;
int Koordinate;
int delaySchritte;
Motor::Motor(int pR, int pS, int K, int gL, int ds){
this->richtungsPin = pR;
this->schrittPin = pS;
this->Koordinate = K;
this->gesamtLaenge = gL;
this->delaySchritte = ds;

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
    delayMicroseconds(this->delaySchritte);
  }else{
    digitalWrite(richtungsPin, LOW);
    digitalWrite(schrittPin, HIGH);
    digitalWrite(schrittPin, LOW);

    this->Koordinate++;
    delayMicroseconds(this->delaySchritte);
  }

}

void Motor::printen()
{
  Serial.println(HallSignal_x);
  Serial.println(HallSignal_y);
  Serial.println(HallSignal_z);

  Serial.println(koordinate_x );
  Serial.println(koordinate_y);
  Serial.println(this->Koordinate);
}

void Motor::bewegen(int anzahl) 
{
  for(int c = 0; c < anzahl; c++)
  {
    //infrarot = analogRead(A1);
    //infrarot2 = analogRead(A2);
    /*if(infrarot > 2 && infrarot2 > 2) {
    }
    */
    messen();
    printen();
    this->schritt();
  }
}

void Motor::hochfahren()
{
  for (int c=0; c<(this->gesamtLaenge - this->Koordinate); c++){
    this->schritt();
  }
}

void Motor::richtungAendern()
{
  this->richtung = !this->richtung;

}

void Motor::startpunkt(){
  this->richtungAendern();
  while(this->Koordinate != 0){
    this->schritt();
  }
}

void Motor::bewegeZu(int ziel) {
  if(this->Koordinate < ziel) {
    richtung=true;
    while(this->Koordinate != ziel) {
      this->schritt();
    }
  }else{
    if(this->Koordinate > ziel) {
      richtung=false;
      while(this->Koordinate != ziel) {
        this->schritt();
      }
    }
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
};

void setup(){
  Serial.begin(9600);
  normalWert_x = analogRead (HallPin_x);
  normalWert_y = analogRead (HallPin_y);
  normalWert_z = analogRead (HallPin_z);

  pinMode(A1, INPUT);
  pinMode(A2, INPUT);

  scannenXY();
}

void loop()
{
  
}



void scannenXY() {
  Motor motorx(6,5, 0, 2000, 200);
  Motor motory(6,3, 0, 20000, 200);
  Motor motorz(6, 4, 0, 2000, 1000);

  motorz.nullpunkt(20500);
  motorz.richtungRunter();
  motorz.bewegen(distanz);
  
  while(motorz.Koordinate < 0) {
      while(motory.Koordinate <= gesamtLaenge_y) {
        motorx.richtungRunter();
        motorx.bewegen(1000);
        motory.richtungHoch();
        motory.bewegen(100);
        motorx.richtungHoch();
        motorx.bewegen(1000);
        motory.richtungHoch();
        motory.bewegen(100);
        
      }
      motorz.richtungHoch();
      motorz.bewegen(100);
  }
  motorx.startpunkt();
  motory.startpunkt();
}
