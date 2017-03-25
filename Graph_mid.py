
import os
from datetime import datetime, timedelta
from collections import defaultdict
import sqlite3

class Graph(object):
    '''
    Develop a Graph class in which the database can be connected. 
    Method findPath   find all the possible path between two destinations
    Method findShortestPath   find the shortest path among all the pathes found in the method findPath
    Method findLongestPath   find the longest path among all the pathes found in the method findPath
    '''

    def __init__(self, folder_name):
        '''
        open the database file from the directory and connect with it
        '''
        os.chdir( folder_name )
        self.db = sqlite3.connect('Graph.db')
        self.db.text_factory = str
    
    def getPosition(self,ID):
        cu = self.db.cursor()   
        cu.execute('SELECT x,y FROM Airports WHERE Code=?', (ID,))
        pos1 = cu.fetchall()
        cu.close()
        return pos1[0]

    def findPath(self, startID, endID, path={'airports':[],'flights':[],'time':[]}):
        cu = self.db.cursor()   
        cu.execute('SELECT a.Flight, f.ToID, a.Departure, a.Arrival FROM Airlines as a, FLights as f WHERE a.FlightID = f.ID AND f.FromID = ?',(startID,))
        # select all the possible destinations which departs from the startID 
        # meanwhile the airline number and the time of departure and arrival are selected as well in order to calculate the travel time
        attached = cu.fetchall()
        # Using the recursive algorithm to find all existing pathes without any duplication and false
        path['airports'] = path['airports'] + [startID]       
        if startID == endID:
            return [path]
        way = [] 
        for item in attached:       
            if item[0] not in path['flights'] and item[1] not in path['airports']:                
                path['flights'] = path['flights']+[item[0]]
                path['time'] = path['time']+[item[2:]]
                nextID = item[1] 
                new_path = self.findPath(nextID, endID, path={'airports':path['airports'][:],'flights':path['flights'][:],'time':path['time'][:]})
                path['flights'].remove(item[0])
                path['time'].remove(item[2:])                             
                for i in new_path:
                    way.append(i)
        path['airports'].remove(startID)
        cu.close()         
        return way # return the airport track as well as the airlines and times
    
    def findPathTotalTime(self,startID,endID):
        a=self.findPath(startID,endID)
        for item in a:
            # extract the time information in the dictionary
            time = [j for i in item['time'] for j in i]
            totaltime = 0  # add each time period into the totaltime
            for i,k in enumerate(time):
                if i+1<len(time):
                    t1 = datetime.strptime(time[i],'%H:%M')
                    t2 = datetime.strptime(time[i+1],'%H:%M')
                    # consider the layover between two airports, if the layover is less than 30 minutes, the next filght has to take off at tomorrow
                    if t1 <= t2 and t1 < t2 - timedelta(minutes=30):
                        totaltime += t2.minute - t1.minute + 60*t2.hour - 60*t1.hour
                    else:
                        totaltime += (24-t1.hour+t2.hour)*60 + (t2.minute-t1.minute)
            # add the total time into the dictionary as the return option
            item['totaltime'] = '%s day(s) %s hour(s) %s minutes' % (totaltime/60/24, totaltime/60%24, totaltime%60)
        return a
    
    def findShortestPath(self, startID, endID):
        # obtain all the tracks found in the findPath method
        a=self.findPathTotalTime(startID,endID)
        total = []
        for item in a :
            total.append(item['totaltime'])
        # find the minimum totaltime and pair with the airport track
        for i in range(0,len(total)):
            if total[i]==min(total):
                shortest = a[i] 
        return shortest


    def findLongestPath(self, startID, endID):
        # similar to the findShortestPath, but to find the longest travel time
        a=self.findPathTotalTime(startID,endID)
        total = []
        for item in a :
            total.append(item['totaltime'])
        for i in range(0,len(total)):
            if total[i]==max(total):
                longest = a[i] 
        return longest

    def getAirportCodes(self):
        cu = self.db.cursor()   
        cu.execute('SELECT Code FROM Airports')
        code = cu.fetchall()
        airport = []
        for item in code:
            airport.append(item[0])
        airport.sort()
        return airport
    
    def getAttached(self,startID):
        cu = self.db.cursor()   
        cu.execute('SELECT a.Flight, f.ToID, p.x, p.y FROM Airlines as a, FLights as f, Airports as p WHERE a.FlightID = f.ID AND p.Code = f.ToID AND f.FromID = ?',(startID,))
        # select all the possible destinations which departs from the startID 
        # meanwhile the airline number and the time of departure and arrival are selected as well in order to calculate the travel time
        attached = cu.fetchall()
        return attached
    
    def getMax(self):
        cu = self.db.cursor()   
        cu.execute('SELECT MAX(x) FROM Airports')
        Xmax = cu.fetchone()
        cu.execute('SELECT MAX(y) FROM Airports')
        Ymax = cu.fetchone()
        return [Xmax[0],Ymax[0]]
        
    def getMin(self):
        cu = self.db.cursor()
        cu.execute('SELECT Min(x) FROM Airports')
        Xmin = cu.fetchone()
        cu.execute('SELECT Min(y) FROM Airports')
        Ymin = cu.fetchone()
        return [Xmin[0],Ymin[0]]


