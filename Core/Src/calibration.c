#include "main.h"
#include "calibration.h"

/// @brief Device calibration function
/*
Consequtively changes PWM output to the following values:

-20degC = 10% PWM
15degC = 55% PWM
50degC = 100% PWM

The idea is to hold the value for 5-10seconds to allow adjustment of the OpAmp output

TIM3_CH4 in PWM mode
*/
void run_calibration()
{
    //TIM2 clock is 25MHz
    //PWM freq is 5kHz
    //MX_TIM2_Init();
    //LL_TIM_SetPrescaler(TIM2, 5000);
    //LL_TIM_SetAutoReload(TIM2,65536);
    //LL_TIM_EnableCounter(TIM2);
    
    //TIM2->CCR3 |= 0x1FFF;
    //TIM2->CCER |= TIM_CCER_CC3E;
    //TIM2->PSC = 5000;
    //TIM2->ARR = 0xFFFF;
    //TIM2->CR1 |= TIM_CR1_CEN;
    

    //LL_TIM_SetPrescaler(TIM2, OUTPUT_PWM_FREQ-1);
    LL_TIM_CC_EnableChannel(PWM_TIMER,LL_TIM_CHANNEL_CH4);


    //PRESCALER SETUP
    //Set timer freq to 1MHz
    /*
    OutputFreq = CLK_FREQ/(PSC+1)

    PCS -> Output freq
    0 - 48MHz
    1 - 24MHz
    2 - 16MHz
    47 - 1MHz
    47999 - 1kHz
    */
    LL_TIM_SetPrescaler(PWM_TIMER, TIMER_CLK_SOURCE/TIMER_CLK-1); //OutputFreq = CLK_FREQ/(PSC+1)
    //LL_TIM_CC_EnableChannel

    LL_TIM_SetAutoReload(PWM_TIMER,TIMER_ARR_VALUE);
    //LL_TIM_CC_SetUpdate(TIM2,LL_T)
    LL_TIM_OC_SetCompareCH4(PWM_TIMER,100);
    LL_TIM_EnableCounter(PWM_TIMER);

    //uint32_t pwm_outputs[4] = {1, (uint32_t)(OUTPUT_PWM_FREQ*0.2),(uint32_t)(OUTPUT_PWM_FREQ*0.55),(uint32_t)(OUTPUT_PWM_FREQ)};
    uint32_t pwm_cycle[4] = {1,20,55,100};
    //setDutyCycle(99);
    int i = 0;
    while(1)
    {
        for(i=0;i<4;i++)
        {
            //blink
            LL_GPIO_ResetOutputPin(LED_STAT_GPIO_Port,LED_STAT_Pin);
            LL_mDelay(100);
            LL_GPIO_SetOutputPin(LED_STAT_GPIO_Port,LED_STAT_Pin);
            LL_mDelay(100);
            //LL_TIM_OC_SetCompareCH4(PWM_TIMER,pwm_outputs[i]);
            setDutyCycle(pwm_cycle[i]);
            LL_mDelay(3000);
            //TIM2->ARR = pwm_outputs[i];
            //LL_TIM_SetAutoReload(TIM2,pwm_outputs[i]);
        }
        i=0;
        
    }
}


//sets duty cycle in %
void setDutyCycle(int perc)
{
    uint32_t timerDutyCylceUnits;
    timerDutyCylceUnits = (uint32_t)(TIMER_ARR_VALUE*perc/100);
    LL_TIM_OC_SetCompareCH4(PWM_TIMER,timerDutyCylceUnits);
}
