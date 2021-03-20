#Design Underground System
'''
Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
    A customer with a card id equal to id, gets in the station stationName at time t.
    A customer can only be checked into one place at a time.
    
void checkOut(int id, string stationName, int t)
    A customer with a card id equal to id, gets out from the station stationName at time t.
    
double getAverageTime(string startStation, string endStation)
    Returns the average time to travel between the startStation and the endStation.
    The average time is computed from all the previous traveling from startStation to endStation that happened directly.
    Call to getAverageTime is always valid.
    
You can assume all calls to checkIn and checkOut methods are consistent. If a customer gets in at time t1 at some station,
they get out at time t2 with t2 > t1. All events happen in chronological order.

Example:
Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn",
"getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],
["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

Explanation
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);
undergroundSystem.checkOut(27, "Waterloo", 20);
undergroundSystem.checkOut(32, "Cambridge", 22);
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. There were two travels from "Leyton" to "Waterloo",The average time is((15-3)+(20-10))/2=11.00000
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000


Solution:
To solve this, we use 3 dictionaries.
card_ids is used to store the ids, the in station and the in time for every check-in.
times is used to store the total time taken for trips between a pair of stations.
count is used to store the number of trips between each pair of stations.

During the check-in, we add the station and the time and assign it to card_ids using the id.
At the checkout, we take the information from card_ids, and use it to calculate the total time taken between both stations, and add it to times.
We also increment the count for that pair of stations.

Finally, when getAverageTime is called, we simply divide the total time taken for those stations(from times dictionary) by the number of
trips (from count dictionary).
'''

class UndergroundSystem:

    def __init__(self):
        self.card_ids={}
        self.times={}
        self.count={}

    def checkIn(self,id,stationName,t):
        self.card_ids[id]=(stationName,t)

    def checkOut(self,id,stationName,t):
        station,time_in=self.card_ids.pop(id)
        if (station,stationName) in self.times:
            self.times[(station,stationName)]+=t-time_in
        else:
            self.times[(station,stationName)]=t-time_in
        if (station,stationName) in self.count:
            self.count[(station,stationName)]+=1
        else:
            self.count[(station,stationName)]=1
        
        
    def getAverageTime(self,startStation,endStation):
        return self.times[(startStation,endStation)]/self.count[(startStation,endStation)]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)