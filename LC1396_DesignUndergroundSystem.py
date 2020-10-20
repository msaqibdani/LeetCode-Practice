from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        
        self.station_average = {}
        self.customers_checked_in = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers_checked_in[id] = (stationName, t)
    

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        fromStation, fromTime = self.customers_checked_in[id]
        del self.customers_checked_in[id]
        prev_total_time, n = self.station_average.get((fromStation, stationName), [0, 0])
        self.station_average[(fromStation, stationName)] = [prev_total_time + t - fromTime, n + 1]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        total_time, n = self.station_average.get((startStation, endStation), [0, 1])
        return total_time/n
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)