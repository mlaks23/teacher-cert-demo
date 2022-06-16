0. Why did you choose the board size for your finalized table?
	I used a board size of 100 x 100 for my finalized tables as I observed great fluctuations in the tick counts for much smaller board sizes (8 x 8). By choosing these larger board dimensions, I enabled the effects of the board size to become more predictable as I modify other factors. Sizes of 1000 x 1000 seemed to increase the time required for running significantly, so I settled with 100 x 100 as stable option.
1. Why did you choose the number of repetitions size for your finalized table?
	I used repetition sizes of 200 and 300 for my finalized tables as they are significantly larger than small sample sizes of 20 or 50 and more efficient to run (less straining on resources for little difference in return). After a benchmark of 150, there remains little discernible deviations in the tick count, assuming every other variable kept constant, so I used 200 repetitions just to ensure that the mean tick count is comprehensive and not terribly skewed by outliers in the data.
2. What did your testing show about changing the board size?
	From the results of my tests, there appears to be a direct positive relationship between the board size and the average tick count. When the board size is increased during testing by increments of 10, the corresponding tick counts also increased, often by a linear factor.
3. Knowing that there were differences based on boardsize, what was the relationship between the board size and the maximum burn time? How did you test this?
	Although the board size did not have a significant large-scale impact as the maximum burn time remained within the bounds of 0.60 and 0.70, as the board size increased, the maximum burn time began to manifest a trend of clustering around the early 0.60s (0.60 - 0.62). However, as the board size decreased, the maximum burn time routinely appeared near 0.65 and the higher decimals of the range. To test this, I generated tables with constant repetition counts and density intervals while adjusting the board size by increments of 10, starting from 10 and ending at 100. It is also interesting to note that these measures of maximum burn time fluctuated greatly with significantly lower board sizes (single digit dimensions), thereby demonstrating the law of large numbers.
4. What density of trees yields the maximum burn time?
	Depending on the board size, the maximum burn time required is approximately situated around densities of 0.61 and 0.62, which may vary with greater deviations if the board size is more drastically modified.

## Table 0 - General Overview of Tick Counts 
| Repetitions | Board Size | Density | Tick Count |
| ------------- |:-------------:| -----:| -----:|
| 200 | 100 | 0.05 | 1.26 |
| 200 | 100 | 0.1 | 1.97 |
| 200 | 100 | 0.15 | 2.64 |
| 200 | 100 | 0.2 | 3.76 |
| 200 | 100 | 0.25 | 4.89 |
| 200 | 100 | 0.3 | 6.4 |
| 200 | 100 | 0.35 | 9.05 |
| 200 | 100 | 0.4 | 12.53 |
| 200 | 100 | 0.45 | 18.61 |
| 200 | 100 | 0.5 | 29.76 |
| 200 | 100 | 0.55 | 64.35 |
| 200 | 100 | 0.6 | 210.3 |
| 200 | 100 | 0.65 | 175.6 |
| 200 | 100 | 0.7 | 146.1 |
| 200 | 100 | 0.75 | 131.38 |
| 200 | 100 | 0.8 | 122.16 |
| 200 | 100 | 0.85 | 115.82 |
| 200 | 100 | 0.9 | 110.59 |
| 200 | 100 | 0.95 | 106.19 |

## Table 1 - Examination of Maximized Tick Count Densities
| Repetitions | Board Size | Density | Tick Count |
| ------------- |:-------------:| -----:| -----:|
| 200 | 100 | 0.55 | 63.43 |
| 200 | 100 | 0.56 | 83.82 |
| 200 | 100 | 0.57 | 106.17 |
| 200 | 100 | 0.58 | 133.04 |
| 200 | 100 | 0.59 | 177.16 |
| 200 | 100 | 0.6 | 196.58 |
| 200 | 100 | 0.61 | 204.68 |
| 200 | 100 | 0.62 | 204.19 |
| 200 | 100 | 0.63 | 197.04 |
| 200 | 100 | 0.64 | 182.56 |
| 200 | 100 | 0.65 | 174.08 |
| 200 | 100 | 0.66 | 164.81 |
| 200 | 100 | 0.67 | 158.96 |
| 200 | 100 | 0.68 | 153.28 |
| 200 | 100 | 0.69 | 148.46 |
