-- Yue Kuang
-- March 2021
-- This code initiate the schema of the course management database

-- Instructors Table
create table IF NOT EXISTS instructors(
    instructor_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    instructor_fname VARCHAR(20) NOT NULL,
    instructor_lname VARCHAR(20) NOT NULL,
    UNIQUE(instructor_id, instructor_fname, instructor_lname)
);

-- Student Table
create table IF NOT EXISTS students(
    student_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    student_fname VARCHAR(20) NOT NULL,
    student_lname VARCHAR(20) NOT NULL,
    UNIQUE(student_id,student_fname, student_lname)
);

-- Courses table
-- Its okay to have same course name, course code in different quarters different division. 
-- One course code can only corresponds with one course name
create table IF NOT EXISTS courses(
   course_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
   course_name VARCHAR(50) NOT NULL,
   code INT NOT NULL, 
   descript VARCHAR(200) NOT NULL,
   dept VARCHAR(20) NOT NULL,
   UNIQUE(course_name, code, dept)
);



-- Building
create table IF NOT EXISTS buildings(
    building_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    building_name VARCHAR(30) NOT NULL,
    CONSTRAINT building_info UNIQUE(building_id, building_name)
);

-- Room
create table IF NOT EXISTS rooms(
    room_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    room_name INT NOT NULL DEFAULT 0,
    building_id INT NOT NULL,
    FOREIGN KEY (building_id) REFERENCES buildings(building_id),
    capacity INT NOT NULL,
    whiteboard BOOLEAN NOT NULL,
    CONSTRAINT room_info UNIQUE(room_name,building_id)
);

-- day 
create table IF NOT EXISTS day_tb(
    day_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    day_data VARCHAR(4) NOT NULL,
    UNIQUE(day_id, day_data)
);

-- time
create table IF NOT EXISTS time_tb(
    time_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    UNIQUE(time_id, start_time, end_time)
);

-- Sections 
create table IF NOT EXISTS sections(
    section_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    course_id int not null,
    instructor_id INT, 
    ta_id INT,
    grader_id INT,
    room_id INT NOT NULL,
    day_id INT NOT NULL, 
    time_id INT NOT NULL,
    year SMALLINT NOT NULL,
    quarter ENUM('Spring', 'Winter', 'Summer', 'Fall') NOT NULL,
    max_enrollment INT NOT NULL,
    open_for_registration BOOLEAN NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (day_id) REFERENCES day_tb(day_id),
    FOREIGN KEY (time_id) REFERENCES time_tb(time_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    UNIQUE(room_id, time_id, day_id, quarter, year),
    UNIQUE(time_id, day_id, instructor_id, quarter, year)
);


create table IF NOT EXISTS labs(
    section_id INT NOT NULL,
    lab_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    lab_num INT NOT NULL,
    instructor_id INT,
    room_id INT,
    day_id INT, 
    time_id INT,
    FOREIGN KEY (room_id) REFERENCES rooms(room_id),
    FOREIGN KEY (day_id) REFERENCES day_tb(day_id),
    FOREIGN KEY (time_id) REFERENCES time_tb(time_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id),
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    UNIQUE(room_id, time_id, day_id),
    UNIQUE(time_id, day_id, instructor_id)
);

create table IF NOT EXISTS student_section(
    section_id INT NOT NULL,
    student_id INT NOT NULL,
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);