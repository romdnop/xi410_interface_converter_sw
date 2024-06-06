#ifndef CAL_H_
#define CAL_H_
#include "main.h"
#include "stm32f0xx_ll_tim.h"

#define PWM_TIMER (TIM3)
#define PWM_TIMER_CHANNEL (LL_TIM_CHANNEL_CH4)




#define TIMER_CLK_SOURCE ((uint32_t)48000000)
#define TIMER_CLK   ((uint32_t)48000000)

#define OUTPUT_PWM_FREQ   ((uint32_t)(10000))
#define TIMER_ARR_VALUE ((uint32_t)(TIMER_CLK/OUTPUT_PWM_FREQ))//value to be written to ARR register, sets PWM freq to OUTPUT_PWM_FREQ

void init_pwm();
void run_calibration();
void setDutyCycle(float perc);

#define PWM_TEMP_LOW ((uint32_t)(TIMER_ARR_VALUE*0.4))
#define PWM_TEMP_HIGH ((uint32_t)(TIMER_ARR_VALUE*0.65))


#endif