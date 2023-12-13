# CS 4315 - Assignment 3 - K-means clustering 
- Course: CS 4315 - Introduction to Data Mining and Information Retrieval | Instructor: Dr. Byron Gao, Associate Professor

# How to run
- unzip the file and move files from dataset folder to main folder
- run kmeans.py with your Python of choice
- enter name of the input text file and value of k cluster
- an output.txt file will be generated in the same folder as the datapath
- read data from output.txt onto gen.exe

# Note: 
- Unable to find a way to optimize and shorten the program in a way that can create new centroids based on the number of k-cluster requested by client. 
E.g. the program can only run up to k = 5 for task completion for the 4 input files. However, this can be resolved by adding new variable for centroid and creating an elif condition for when k = 6, 7, etc.
- The program might run into this error. Traceback (most recent call last):  a4, b4 = xSum / len(label4), ySum / len(label4) ZeroDivisionError: division by zero
This is because there is no data coordinate that fall under this randomly generated centroid. This can be resolved by re-running the program.

# Github Repository:
https://github.com/rnb90/cs4315-kmeans
