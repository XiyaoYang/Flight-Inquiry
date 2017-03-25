# Flight-Inquiry-App

Problem Statement:

Develop a graphic representation of the graph problem using Python wx.DC (in a frame).



The simple application provides the following functionality:

1. Create a air traffic problem SQL database

2. Read a graph (air traffic problem) from the SQL database using sqlite3.

3. Design and implement a graphical user interface (GUI) that allows users to
   
   a. Plot the entire graph (2D drawing using black or blue lines and points)
   
   b. Select start and end points from pull-down menus
   
   c. Display a list of shortest path or found paths, depending on user selection
   
   d. If the user selects “shortest path”, plot that path using a red line
   
   e. Make sure the window is scalable and does not mess up the plot

4. All output goes through the GUI

5. The provided map requires an alternative mapping of longitude and latitude as follows:

x = R * (longitude0 – longitude)

y = R * (tan(latitude) – tan(latitude0))

with R the radius of Earth and longitude0 the longitude of the left edge of the map, and latitude0 the latitude of the bottom of the map.


