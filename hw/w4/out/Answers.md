Homework-4 Answers

**1. Does SMO do better than the random baselines (see prints 1,2,4)?**

Answer: Yes, based on the outputs we got.We observed SMO does better than random baselines.This can be proved from the results.For example in the print 2.Top6 we got values like ['4341', '10', '20'] for weight,acceleration and mpg respectively [['4341', '10', '20']](https://github.com/RatishkumarS/NCSU-CSC-591-021-Group-21/blob/main/hw/w4/out/w4.out#L189) whereas for print 4 [['3085.25','12.925','20']](https://github.com/RatishkumarS/NCSU-CSC-591-021-Group-21/blob/main/hw/w4/out/w4.out#L192) and print 6[['3211','17','20']](https://github.com/RatishkumarS/NCSU-CSC-591-021-Group-21/blob/main/hw/w4/out/w4.out#L212) . The print results in 4 and 6 produced better results in terms of weight, acceleration and mpg which makes it clear that SMO does a better job than random baselines.


**2.  How many y row evaluations are required for print 3?**

Answer: We calculate absolute best (print 3) by using  y row evaluations as it is calculated like this rows[0].cells[len(rows[0].cells) which means it takes (#yColumns * #Data) evaluations to find the absolute best. Number of Columns= 3 and records we have is 398. So the number of evaluation it takes is 398*3=1194.

**3.    How does SMO do compared to absolute best (print 3)**

Answer: Sequential Model Optimizer does tend to perform quite well in comparison to absolute best. However, we cannot say it perfectly matches the performance of absolute best but it does provide good results. Lets see this o/p [['2135', '16.6', '30']](https://github.com/RatishkumarS/NCSU-CSC-591-021-Group-21/blob/main/hw/w4/out/w4.out#L286) and compare it with the o/p we got from absolute best [['2130', '24.6', '40']](https://github.com/RatishkumarS/NCSU-CSC-591-021-Group-21/blob/main/hw/w4/out/w4.out#L265). We can obeserve how close the SMO can get to the absolute best and also we noticed it was also fast in providing the results which can compromise the small accuracy variations.
