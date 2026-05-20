#include <LiquidCrystal_I2C.h>
#include <Wire.h>
LiquidCrystal_I2C lcd(0x20, 16, 2); 

// Variáveis
int votos[4] = {0, 0, 0, 0};
bool reset = false;

// Constantes
const int button[5] = {5,4,3,2,6};
const int posCursor[4] = {0,4,8,12};
const int led = 7;
const char candidato[4] = {'A','B','C','D'};

// Protótipo das funçõs
void ligarLed();
void contarVoto(int pos);

// ========================
// Função inicio
// ========================
void setup() {
  lcd.init(); 
  lcd.clear();   
  lcd.backlight();
  // Exibição dos Candidatos
  for (int i=0;i<4;i++){
  	lcd.setCursor(posCursor[i], 0);  lcd.print(candidato[i]);
    lcd.setCursor(posCursor[i], 1);  lcd.print(0);
  }
  
  // Definindo pin
  for(int i=0;i<5;i++){
    pinMode(button[i],INPUT_PULLUP);
  }
  pinMode(led, OUTPUT);
}

// ========================
// Função de processo
// ========================
void loop() {
  
  // Reset da votação
  if (digitalRead(button[4]) == LOW){
    ligarLed();
    int maior=votos[0],vencedor=0,empatado=0;
    reset = true;
    lcd.clear();
    
    // Verifica o vencedor
    for(int i=0;i<4;i++){
      if(votos[i] > maior){
        maior = votos[i];
        vencedor = i;
      }
    }
    for(int i=0;i<4;i++){
      if(votos[i] == maior){
      	empatado++;
      }
    }
    lcd.setCursor(0,0);
    if(empatado==1){ 
    	// Vencedor único
    	lcd.print("VENCEDOR: ");
    	lcd.setCursor(10,0);
    	lcd.print(candidato[vencedor]);
    }
    else{ 
    	// Candidatos com votos iguais
    	lcd.print("EMPATE");
    }
    delay(1000);
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("VOTOS ZERADOS");
    for(int i=0;i<4;i++){
      votos[i] = 0;
    }
    delay(1000);
    lcd.clear();
    // Exibição dos Candidatos
  	for (int i=0;i<4;i++){
  		lcd.setCursor(posCursor[i], 0);  lcd.print(candidato[i]);
    	lcd.setCursor(posCursor[i], 1);  lcd.print(0);
  	}         
    reset = false;
  } 
  
  // Loop votação
  if(reset == false){
  	if (digitalRead(button[0]) == LOW){
    	contarVoto(0);
  	}
  	if (digitalRead(button[1]) == LOW){
    	contarVoto(1);
  	}
  	if (digitalRead(button[2]) == LOW){
    	contarVoto(2);
  	}                           
  	if (digitalRead(button[3]) == LOW){
    	contarVoto(3);
  	}    
  }
}

// Definição das Funções

// ========================
// Função ligar entrada 7
// ========================
void ligarLed() { 
    //Debounce imbutido
	delay(100);
	digitalWrite(led, HIGH);  
	delay(100);
	digitalWrite(led,LOW);
}

// ========================
// Função contar votos
// ========================
void contarVoto(int pos){
	votos[pos]++;
	lcd.setCursor(posCursor[pos], 1);  
	lcd.print(votos[pos]);
	ligarLed();
}
