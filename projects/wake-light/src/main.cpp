#include <WiFi.h>
#include <time.h>

const char* ssid = "Y";
const char* password = "pdkh2002";

const int WAKE_HOUR = 6;
const int WAKE_MINUTE = 30;

void setup() {
    //connect to wifi
WiFi.begin(ssid, password);
while (WiFi.status() != WL_CONNECTED) {
    delay(500);
}
    //sync to time
configTime(3 * 3600, 0, "pool.ntp.org");
}

void loop() {
    //check if it is wake time

    //turn light on or off

}