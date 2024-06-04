#include "led.h"

void led_on()
{
    HAL_GPIO_WritePin(LED_PORT, LED_PIN, GPIO_PIN_SET);
}


void led_off()
{
    HAL_GPIO_WritePin(LED_PORT, LED_PIN, GPIO_PIN_RESET);
}


void led_blink(uint32_t blink_delay)
{
    led_on();
    HAL_Delay(blink_delay);
    led_off();
    HAL_Delay(blink_delay);
}


void led_blink_number(uint32_t number)
{
    uint32_t i = 0;
    for(i=0;i<number;i++)
    {
        led_blink(500);
    }
}