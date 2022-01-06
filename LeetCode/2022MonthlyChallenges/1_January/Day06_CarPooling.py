#Car Pooling
'''
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that
the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively.
The locations are given as the number of kilometers due east from the car's initial location.
Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example:
    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false

    Input: trips = [[2,1,5],[3,3,7]], capacity = 5
    Output: true
'''

class Solution:
    def carPooling(self,trips,capacity):
        last=0
        for n,f,t in trips:
            last=max(last,t)
        station=[0]*(last+2)
        for n,f,t in trips:
            station[f+1]+=n
            station[t+1]-=n
        for i in range(1,len(station)):
            station[i]+=station[i-1]
        return max(station)<=capacity