int x;
char controlCodes[4];
char startChar = '<';
char endChar = '>';



void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void loop() {
  bool newData = false;
  int ndx = 0;
  char quadrant;
  char coil;
  char phase;
  bool started;
  while (Serial.available() && newData == false){
    char recievedChar = Serial.read();
    if (recievedChar == startChar){
      started = true;
    }
    if (started){
      if (ndx == 1){
      quadrant = recievedChar;
      Serial.print("quad: ");
      Serial.println(quadrant);
      }
      if (ndx == 2){
        coil = recievedChar;
        Serial.print("coil: ");
        Serial.println(coil);
      }
      if (ndx ==3){
        phase = recievedChar;
        Serial.print("phase: ");
        Serial.println(phase);
      }
      if (ndx ==4){
        newData == true;
        started == false;
        ndx = 0;
      }
      ndx ++;
    }
    
  }
  if (newData == true){
    Serial.print("Quadrant: ");
    Serial.println(quadrant);
    newData == false;
  }

}
