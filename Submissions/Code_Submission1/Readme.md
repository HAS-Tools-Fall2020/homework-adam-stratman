# Assignment 8 (code_submission1)
## Adam Stratman
### 10/18/2020


#### Written Assignment

#### 1. A brief summary of the AR model you built and why. Use whatever graphs you find helpful.

For my final version of the AR model I reduced it two time lag series. In week 6 I had incorporated a third week step. I ultimately found this to be redundant and did not add anything to my model. I kept the original flow_weekly data as my input and used a time frame from 1996- mid 2000 to train the data and 2000-present as the test data. This yielded a .68 COD value which is what made me continue on with this model for my final script. This time series includes the first 1.5 years of a historic drought that Arizona experienced in 1999-2004.

#### 2. An explanation of how you generated your forecasts and why (i.e. did you  use  your AR model or not?)

For my forecast I created a function that took each of the two models utilized in my script and multiplied them by a correction factor. The correction factors were chosen based on looking at the most current 7 day average and comparing it to the AR model produced in the script (past 7 day average)/(AR model). This gives a value that is more realistic to what we can expect to see for next weeks average flow. I did this because although my AR models both had relatively high coefficients of determination they produced values that are off by 30+ CFS in comparison to observed data.  

#### 3. A brief summary of what you got out of the peer evaluation. How did you make your script better?

My peer evaluation was super helpful. Alcely illustrated how I could turn my 2 functions I had created and make them into one. Additionally she pointed a major typo that was in my model with incorrect index values. Overall it was a good experience and I think as we continue to learn as a class the more effective our feedback will become for our peers.

#### 4. Describe the part of your script that you are most proud of and why.

In this script, I am the most proud of the 16 week forecast that it produces at the very end. This is because it was the first thing I was able to do in this class where I had an idea of how I wanted to do something and was able to accomplish it without having to struggle through it. It also helped me understand how we can redefine data and look at parts of it that we may find useful (minimum, maximum). I used the average minimum weekly flow values from 2019 to predict the 16 week forecast. For the forecast, I coupled 2019 weekly average minimums (week1, and following week). Although this may not be the most accurate forecast, I think it was a valuable learning experience for me.
