drop table if exists Cities;
drop table if exists Airports;
drop table if exists Flights;
drop table if exists Airlines;

create table Cities (
	ID		int not null primary key,
	City		char(30),
	State       char(30)
	);

create table Airports (
	ID		int not null primary key,
	Code		char(3),
	CityID		int unsigned,
	Longitude   float,
	Latitude    float,
	x           float,
	y           float
	);

create table Airlines (
	ID		int not null primary key,
	Flight    char(30),
	Departure	time,
	Arrival		time,
	FlightID   int unsigned
	);

create table Flights (
	ID		int not null primary key,
	FromID  char(3),
	ToID    char(3)
	);

insert into Cities ( ID, City, State)  values ( 1, 'Seattle', 'WA');
insert into Cities ( ID, City, State)  values ( 2, 'San Francisco', 'CA');
insert into Cities ( ID, City, State)  values ( 3, 'New York', 'NY');
insert into Cities ( ID, City, State)  values ( 4, 'Miami', 'FL');
insert into Cities ( ID, City, State)  values ( 5, 'Denver', 'CO');
insert into Cities ( ID, City, State)  values ( 6, 'Oakland', 'CA');
insert into Cities ( ID, City, State)  values ( 7, 'Dallas', 'TX');
insert into Cities ( ID, City, State)  values ( 8, 'Salt Lake City', 'UT');
insert into Cities ( ID, City, State)  values ( 9, 'Chicago', 'IL');
insert into Cities ( ID, City, State)  values ( 10, 'Houston', 'TX');

insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y ) values ( 1, 'SEA', 1 ,122.3331, 47.6097, 2451.831, 4337.133);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y  ) values ( 2, 'SFO', 2, 122.4167, 7.7833, 2446.055, 3069.067);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y ) values ( 3, 'LGA', 3, 73.8726, 40.7772, 5800.335, 3414.569);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y  ) values ( 4, 'JFK', 3, 73.7789, 40.6397, 5806.809, 3398.035);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y  ) values ( 5, 'MIA', 4, 80.2089, 25.7753, 5362.512, 1911.75);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y  ) values ( 6, 'DIA', 5, 104.9903, 39.7392, 3650.177, 3291.403);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y  ) values ( 7, 'OAK', 6, 122.2708, 37.8044, 2456.136, 3071.402);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y  ) values ( 8, 'DFW', 7,96.797,32.7767,4216.314,2549.123);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y  ) values ( 9, 'SLC', 8,111.8833,40.75,3173.887,3411.293);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y  ) values ( 10, 'ORD', 9,87.9047,41.9786,4830.75,3562.023);
insert into Airports ( ID, Code, CityID, Longitude, Latitude, x, y  ) values ( 11, 'IAH', 10,95.3698,29.7604,4314.93,2263.708);

insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 1, 'CB1', '6:00', '7:00', 1);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 2, 'AK2155', '6:45', '8:55', 2);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 3, 'CBA', '7:00', '8:00', 3);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 4, 'AK1256', '7:15', '10:55', 4);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 5, 'CB2', '8:00', '9:00', 1);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 6, 'UA768', '8:05', '10:49', 5);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 7, 'AA1302', '8:10', '10:40', 5);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 8, 'DL34', '8:30', '11:45', 6);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 9, 'SWA10', '8:45', '11:15', 7);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 10, 'UA184', '8:50', '12:30', 8);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 11, 'CBB', '9:00', '10:00', 3);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 12, 'AK3392', '9:10', '11:25', 9);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 13, 'AK1234', '9:40', '12:05', 10);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 14, 'AA482', '9:45', '11:55', 11);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 15, 'SWA123', '9:45', '11:55', 2);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 16, 'CB3', '10:00', '11:00', 1);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 17, 'CBC', '11:00', '12:00', 3);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 18, 'UA123', '11:00', '17:20', 12);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 19, 'AA345', '11:25', '13:55', 13);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 20, 'UA345', '11:30', '14:05', 14);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 21, 'SWA11', '11:45', '14:15', 15);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 22, 'AA92', '11:55', '14:20', 16);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 23, 'DL882', '11:55', '15:10', 17);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 24, 'CB4', '12:00', '13:00', 1);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 25, 'AK3245', '12:15', '14:50', 18);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 26, 'DL382', '12:35', '14:55', 19);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 27, 'DL1214', '12:40', '14:05', 20);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 28, 'CBD', '13:00', '14:00', 3);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 29, 'AK2241', '13:05', '14:50', 21);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 30, 'SWA125', '13:25', '17:05', 22);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 31, 'DL1212', '13:40', '15:10', 23);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 32, 'CB5', '14:00', '15:00', 1);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 33, 'SWA76', '14:00', '16:38', 17);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 34, 'UA76', '14:10', '16:05', 24);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 35, 'AA562', '14:50', '17:40', 25);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 36, 'UA49', '14:50', '18:15', 26);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 37, 'DL885', '14:55', '17:05', 27);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 38, 'AA734', '14:55', '17:45', 28);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 39, 'CBE', '15:00', '16:00', 3);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 40, 'DL2222', '15:10', '18:05', 29);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 41, 'CB6', '16:00', '17:00', 1);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 42, 'AK246', '16:10', '18:40', 10);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 43, 'AA281', '16:15', '18:35', 30);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 44, 'AK3398', '16:40', '19:00', 9);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 45, 'CBF', '17:00', '18:00', 3);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 46, 'UA234', '17:25', '19:50', 31);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 47, 'DL421', '17:40', '21:20', 32);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 48, 'CB7', '18:00', '19:00', 1);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 49, 'AA0123', '18:35', '20:50', 33);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 50, 'CBG', '19:00', '20:00', 3);
insert into Airlines ( ID, Flight, Departure, Arrival, FlightID) values ( 51, 'AK3248', '19:45', '21:55', 18);

insert into Flights ( ID, FromID, ToID) values ( 1, 'LGA', 'JFK');
insert into Flights ( ID, FromID, ToID) values ( 2, 'SEA', 'DIA');
insert into Flights ( ID, FromID, ToID) values ( 3, 'JFK', 'LGA');
insert into Flights ( ID, FromID, ToID) values ( 4, 'SEA', 'ORD');
insert into Flights ( ID, FromID, ToID) values ( 5, 'MIA', 'DFW');
insert into Flights ( ID, FromID, ToID) values ( 6, 'SEA', 'SLC');
insert into Flights ( ID, FromID, ToID) values ( 7, 'SEA', 'OAK');
insert into Flights ( ID, FromID, ToID) values ( 8, 'MIA', 'ORD');
insert into Flights ( ID, FromID, ToID) values ( 9, 'SEA', 'SFO');
insert into Flights ( ID, FromID, ToID) values ( 10, 'DIA', 'SEA');
insert into Flights ( ID, FromID, ToID) values ( 11, 'MIA', 'LGA');
insert into Flights ( ID, FromID, ToID) values ( 12, 'SEA', 'JFK');
insert into Flights ( ID, FromID, ToID) values ( 13, 'ORD', 'JFK');
insert into Flights ( ID, FromID, ToID) values ( 14, 'LGA', 'ORD');
insert into Flights ( ID, FromID, ToID) values ( 15, 'OAK', 'SEA');
insert into Flights ( ID, FromID, ToID) values ( 16, 'DFW', 'LGA');
insert into Flights ( ID, FromID, ToID) values ( 17, 'OAK', 'DFW');
insert into Flights ( ID, FromID, ToID) values ( 18, 'SFO', 'SEA');
insert into Flights ( ID, FromID, ToID) values ( 19, 'SLC', 'ORD');
insert into Flights ( ID, FromID, ToID) values ( 20, 'DFW', 'SLC');
insert into Flights ( ID, FromID, ToID) values ( 21, 'DFW', 'DIA');
insert into Flights ( ID, FromID, ToID) values ( 22, 'DIA', 'MIA');
insert into Flights ( ID, FromID, ToID) values ( 23, 'SLC', 'DFW');
insert into Flights ( ID, FromID, ToID) values ( 24, 'JFK', 'MIA');
insert into Flights ( ID, FromID, ToID) values ( 25, 'ORD', 'DFW');
insert into Flights ( ID, FromID, ToID) values ( 26, 'ORD', 'SFO');
insert into Flights ( ID, FromID, ToID) values ( 27, 'ORD', 'SLC');
insert into Flights ( ID, FromID, ToID) values ( 28, 'LGA', 'DIA');
insert into Flights ( ID, FromID, ToID) values ( 29, 'SLC', 'SEA');
insert into Flights ( ID, FromID, ToID) values ( 30, 'LGA', 'MIA');
insert into Flights ( ID, FromID, ToID) values ( 31, 'SLC', 'SFO');
insert into Flights ( ID, FromID, ToID) values ( 32, 'MIA', 'DIA');
insert into Flights ( ID, FromID, ToID) values ( 33, 'DFW', 'MIA');

