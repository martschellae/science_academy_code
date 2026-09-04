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

int del = 200; 

int koordinate_x = 0;
int koordinate_y = 0;
int koordinate_z = 0;

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
  bool richtung;
  int schrittPin;
  int richtungsPin;
  int Koordinate;
  int gesamtLaenge;
public:

Motor::Motor(int pR, int pS, int K, int gL){
this->richtungsPin = pR;
this->schrittPin = pS;
this->Koordinate = K;
this->gesamtLaenge = gL;

pinMode(richtungsPin, OUTPUT);
pinMode(schrittPin, OUTPUT);
}

void Motor::schritt(){
  if(richtung)
  {
    digitalWrite(richtungsPin, HIGH);
    digitalWrite(schrittPin, HIGH);
    digitalWrite(schrittPin, LOW);

    this->Koordinate++;
    delayMicroseconds(del);
  }
    else
    {
      
      digitalWrite(richtungsPin, LOW);
      digitalWrite(schrittPin, HIGH);
      digitalWrite(schrittPin, LOW);

      this->Koordinate--;
      delayMicroseconds(del);
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
    infrarot = analogRead(A1);
    infrarot2 = analogRead(A2);
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
  while(this->Koordinate != 0)
  {
    this->schritt();
  }
}

};

void setup(){
  Motor motorx(6,5, 0, 200);
  Motor motory(6,4, 0, 200);
  Motor motorz(6,3, 200, 200);

  Serial.begin(9600);
  normalWert_x = analogRead (HallPin_x);
  normalWert_y = analogRead (HallPin_y);
  normalWert_z = analogRead (HallPin_z);

  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
}

void loop()
{
  prototyp();
}


void prototyp() 
{
  while(koordinate_x <= gesamtLaenge_x) 
  {
    motorx.schritt();
    koordinate_x++;
        if(koordinate_x % 2 == 0){
          while(koordinate_y <= gesamtLaenge_y){
            motory.schritt();
            koordinate_y++;
            motorz.bewegen(gesamtLaenge_z);

            motorz.richtungAendern();
            motorz.hochfahren();
          }
        }
        else{
          while(koordinate_y >= 0){
            motory.richtungAendern();
            motory.schritt();

            koordinate_y--;

            motorz.bewegen(gesamtLaenge_z);
            

            motorz.richtungAendern();
            motorz.hochfahren();
          }
        }
  }

  motory.startpunkt();
  motorx.startpunkt();
    
}

