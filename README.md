# DEVTOWN
# JPMC Task 1
Starter repo for task 1 of the JPMC software engineering program
# Stock Correlation Monitoring Dashboard

This repository is created to implement a chart in a trader's dashboard, allowing them to identify under/over-valued stocks. The trader aims to monitor two historically correlated stocks and visualize when the correlation weakens, indicating potential trade opportunities.

## Overview

The main goal is to implement a dashboard using JPMorgan Chase's Perspective data visualization software. The dashboard will display historical correlations between two selected stocks and highlight instances when one stock deviates significantly from the historical correlation.

## Implementation Steps

1. **Data Interface:**
   - Interface with a relevant financial data feed to fetch historical stock prices for the selected stocks.

2. **Data Processing:**
   - Calculate historical correlation between the two stocks.

3. **Dashboard Integration:**
   - Utilize JPMorgan Chase's Perspective data visualization software to create a chart displaying the historical correlation.

4. **Correlation Monitoring:**
   - Implement a mechanism to continuously monitor the correlation between the two stocks.

5. **Trade Strategy:**
   - Develop a trade strategy to buy the relatively underperforming stock and sell the relatively outperforming stock when the correlation weakens.

6. **Profitability Check:**
   - Track the performance of the trade to ensure profitability, especially when the two stock prices subsequently converge.


