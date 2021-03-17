LOAD DATA LOCAL INFILE '/Users/ykuang/Desktop/2020-2021Winter/oop/final_project/react-flask-app/database_schema/buildings.csv'
INTO TABLE buildings
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ykuang/Desktop/2020-2021Winter/oop/final_project/react-flask-app/database_schema/rooms'
INTO TABLE rooms
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ykuang/Desktop/2020-2021Winter/oop/final_project/react-flask-app/database_schema/days.csv'
INTO TABLE day_tb
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;


LOAD DATA INFILE '/Users/ykuang/Desktop/2020-2021Winter/oop/final_project/react-flask-app/database_schema/time.csv'
INTO TABLE time_tb
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ykuang/Desktop/2020-2021Winter/oop/final_project/react-flask-app/database_schema/courses.csv'
INTO TABLE courses
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;

LOAD DATA INFILE '/Users/ykuang/Desktop/2020-2021Winter/oop/final_project/react-flask-app/database_schema/sections.csv'
INTO TABLE sections
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '/n'
IGNORE 1 ROWS;