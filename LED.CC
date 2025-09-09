
const int LED_WHITE = 12;
const int LED_BLUE = 13;

void setup()
{
  pinMode(LED_WHITE, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
}

void loop()
{
  digitalWrite(LED_WHITE, HIGH);
  delay(1000); // Wait for 100 millisecond(s)
  digitalWrite(LED_BLUE, LOW);
  delay(1000); // Wait for 100 millisecond(s)
  
  digitalWrite(LED_WHITE, LOW);
  delay(1000); // Wait for 100 millisecond(s)
  digitalWrite(LED_BLUE, HIGH);
  delay(1000); // Wait for 100 millisecond(s)
}