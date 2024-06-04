#ifndef CAL_H_
#define CAL_H_
#include "main.h"
#include "stm32f0xx_ll_tim.h"

#define PWM_TIMER (TIM3)
#define PWM_TIMER_CHANNEL (LL_TIM_CHANNEL_CH4)




#define TIMER_CLK_SOURCE ((uint32_t)48000000)
#define TIMER_CLK   ((uint32_t)48000000)

#define OUTPUT_PWM_FREQ   ((uint32_t)(20000))
#define TIMER_ARR_VALUE ((uint16_t)(TIMER_CLK/OUTPUT_PWM_FREQ))//value to be written to ARR register, sets PWM freq to OUTPUT_PWM_FREQ


void run_calibration();
void setDutyCycle(int perc);


#endif