/* Create a WiFi access point and provide an UDP server on it. */

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <WiFiUdp.h>

extern "C" {
#include "user_interface.h"
}


/* Access Point credentials. */
const char *ssid = "ESPap";
const char *password = "thereisnospoon";

/* Local port to listen on */
unsigned int localPort = 8888;

/* buffers for receiving and sending data */
char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; //buffer to hold incoming packet,

/* An WiFiUDP instance to let us send and receive packets over UDP */
WiFiUDP Udp;
IPAddress remoteIP;
unsigned int remotePort;


/* Timer Interrupt configuration */
os_timer_t myTimer;

bool sendPacket;

unsigned int counter = 0;
String message;

/* Callback function that will be called when the timer interrupt is triggered */
void timerCallback(void *pArg) {

  /* Send data from the sensors to the remote computer */
  if (sendPacket == true)
  {
    counter++;
    message = "";
    for (int i = 0; i <= 9; i++)
    {
      message.concat(counter+i);
      if (i != 9)
        message.concat(",");
    }
    Udp.beginPacket(remoteIP, remotePort);
    Udp.write(message.c_str());
    Udp.endPacket();
  }
}

void user_init(void) {  
  /*
    os_timer_setfn - Define a function to be called when the timer fires
    
    void os_timer_setfn(
        os_timer_t *pTimer,
        os_timer_func_t *pFunction,
        void *pArg)
    
    Define the callback function that will be called when the timer reaches zero. 
      The pTimer parameters is a pointer to the timer control structure.
      The pFunction parameters is a pointer to the callback function.
      The pArg parameter is a value that will be passed into the called back function. The callback function should have the signature:
        
        void (*functionName)(void *pArg)
    
      The pArg parameter is the value registered with the callback function.
  */

  os_timer_setfn(&myTimer, timerCallback, NULL);

  /*
    os_timer_arm -  Enable a millisecond granularity timer.

    void os_timer_arm(
        os_timer_t *pTimer,
        uint32_t milliseconds,
        bool repeat)

    Arm a timer such that is starts ticking and fires when the clock reaches zero.
      The pTimer parameter is a pointed to a timer control structure.
      The milliseconds parameter is the duration of the timer measured in milliseconds. 
      The repeat parameter is whether or not the timer will restart once it has reached zero.
  */

  os_timer_arm(&myTimer, 100, true);  
}


void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  
  delay(1000);
  Serial.begin(115200);
  Serial.println();
  Serial.print("Configuring access point...");

  /* Starting access point */
  /* You can remove the password parameter if you want the AP to be open. */
  WiFi.softAP(ssid, password);

  IPAddress myIP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(myIP);

  /* Start the UDP server */
  Serial.print("Starting UDP server...");  
  Udp.begin(localPort);

  /* Configure timer interrupt */
  user_init();
}

void loop() {
  /* If there's data available, read a packet */
  int packetSize = Udp.parsePacket();
  if (packetSize)
  {
    /* Read the IP and port of whoever sent the package */
    remoteIP = Udp.remoteIP();
    remotePort = Udp.remotePort();

    /* Read the packet into packetBufffer */
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);

    /* If the packet contains the start message, start sending back data */
    if (packetBuffer)
    {
      Serial.print("Received packet of size ");
      Serial.println(packetSize);
      Serial.print("From ");
      IPAddress remoteIp = Udp.remoteIP();
      Serial.print(remoteIp);
      Serial.print(", port ");
      Serial.println(Udp.remotePort());
      
      // read the packet into packetBufffer
      int len = Udp.read(packetBuffer, 255);
      if (len > 0) {
        packetBuffer[len] = 0;
      }
      Serial.println("Contents:");
      Serial.println(packetBuffer);
    
      sendPacket = true;
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
   
  yield();

}
