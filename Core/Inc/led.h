#include "main.h"


#ifndef LED_H_
#define LED_H_

#define LED_PORT   LED_STAT_GPIO_Port
#define LED_PIN     LED_STAT_Pin


void led_on();
void led_off();
void led_blink(uint32_t);
void led_blink_number(uint32_t number);


#endif
