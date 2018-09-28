# author: Thomas Benjamin
# email: trbenjamin@gmail.com
# date: Thu, 27 Sep 2018

import numpy as np
import sys

def shuffle(arr):
    idx = np.arange(len(arr))
    for v in idx:
        i = np.random.choice(idx)
        # Cycle: last element to tmp location
        # random location to last location
        # tmp location to above random location
        arr_tmp  = arr[-1]
        arr[-1]  = arr[i]
        arr[i] = arr_tmp

    return arr
    

def draw_remove_element(arr, n):
    """
    Remove and save x = arr[n]. Shift arr[n+1:] to the left.
    Return x and the shifted arr
    """
    if n < 0 or n >= len(arr):
        print ("Index of arr is out of range.")
        sys.exit("Index of arr is out of range.")
    else:
        x = arr[n]
        #print (x)
        left_side  = arr[:n]
        right_side = arr[n+1:]
    return x, np.concatenate([left_side, right_side])

def urn_setup():
    """
    Setup the urn array with 11115 balls: 59 green and 11056 red.
    """
    grn_balls = np.array(['G' for v in range(59)])
    red_balls = np.array(['R' for v in range(11056)])
    urn = np.concatenate([grn_balls, red_balls])
    # Shuffle (mix) the urn array N times, then sample
    for v in range(32):
        urn  = shuffle(urn)
    return urn

def draw_250():
    """
    Setup the urn, then perform 250 drawings, recording the number of Red and Green Balls
    """
    red = 0
    grn = 0
    arr = urn_setup()
    for v in range(250):
        n = np.random.randint(0,len(arr))
        x, arr = draw_remove_element(arr, np.random.randint(0,len(arr)))
        if x == 'R':
            red += 1
        elif x == 'G':
            grn += 1
    print("Red: %d  ::  Grn: %d" % (red, grn))
    return red, grn

##### Begin Script execution #####
win = 0
lose = 0
runs = 32
for n in range(runs):
    sys.stdout.write ("run " + str(n) + ": ")
    red, grn = draw_250()
    if grn == 0:
        lose += 1
    else:
        win += 1
print ("\nIn %d runs: Wins = %d, Losses = %d, Pct Wins = %.2f %%" % (runs, win, lose, 100.0*win/(win + lose)))