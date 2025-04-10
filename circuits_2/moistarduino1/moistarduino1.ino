// C++ code
//
int sensor;

void setup()
{
pinMode(4, OUTPUT);
pinMode(3, OUTPUT);
Serial.begin(9600);
}

void loop()
{
  delay(100);
  sensor = analogRead(A0);
  sensor = sensor/8.76;
  Serial.println(sensor);
  if (sensor >= 40){
    digitalWrite(3,HIGH);}
 if(sensor < 60){
    digitalWrite(4,HIGH);}
   if (sensor < 40){
    digitalWrite(3, LOW);}
  if (sensor >=60);{
    digitalWrite(4, LOW); }
  
  










}
