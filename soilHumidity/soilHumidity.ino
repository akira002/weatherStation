void setup()
{
  Serial.begin(9600);
  pinMode(A0, INPUT);
}

void loop()
{
  int s0 = analogRead(A0); //take a sample
  Serial.println(s0);
  delay(500);
}

