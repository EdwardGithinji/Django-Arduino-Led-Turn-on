void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("Hi!, I am Arduino");

}

void loop() {
  // put your main code here, to run repeatedly:
  char data;
  while(Serial.available()){    
    data = Serial.read();
    if(data == '1'){
      digitalWrite(LED_BUILTIN, HIGH); 
    }
  
    else if(data == '0'){      
      digitalWrite(LED_BUILTIN, LOW);
    
    }
  
  }


}
