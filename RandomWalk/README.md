# Case Study - Hacker Math
Throw the dice in the air to decide if you go up or down one step in the empire state building.

If it comes 1 or 2: one step down\
If it comes 3,4 or 5: one step up\
If it comes 6: roll the dice again

To see if we should take a bet that we can go up to 60 steps:
First we should simulate a random walk.

### What is a random walk?
It is a process of determining the probable location of a point subject to random motions
given the probabilities (the same for each step) of moving some distance in the same
direction.\
**For example**: a path traced by a molecule as it travels in a liquid or a gas; or 
a financial status of a gambler.

### Back to the case study...
A random walk will be a set of numbers of the position where we are at that repetition
of the dice throwing. 
To see its distribution we should repeat it multiple times.
As many times we repeat it, it will tend to the theoretical distribution.

### Why do we transpose the matrix _all walks_?
Because that way, each row will correspond to the various positions after throwing
the dice one time!

## What are the odds that you'll reach 60 steps high on the Empire State Building?

Basically, you want to know about the end points of all the random walks you've
simulated. These end points have a certain distribution that you can visualize with a histogram.