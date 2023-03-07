DROP DATABASE IF EXISTS dormtracker;
CREATE DATABASE dormtracker;
USE dormtracker;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS scholar;
DROP TABLE IF EXISTS admins;
DROP TABLE IF EXISTS service_hour_listing;
DROP TABLE IF EXISTS registration;
DROP TABLE IF EXISTS assignment;

CREATE TABLE user (
  user_id INT NOT NULL PRIMARY KEY,
  email VARCHAR(255),
  user_password VARCHAR(255)
);

CREATE TABLE scholar (
  scholar_id INT,
  hours_needed INT,
  hours_rendered INT,
  contact_no VARCHAR(20),
  room_code VARCHAR(50),
  room_name VARCHAR(100),
  scholar_year INT,
  course VARCHAR(100),
  FOREIGN KEY (scholar_id) REFERENCES user(user_id)
);

CREATE TABLE service_hour_listing (
  serv_hours_id INT NOT NULL PRIMARY KEY,
  serv_hours_date DATE,
  serv_hours_time TIME,
  serv_hours_loc VARCHAR(255),
  serv_hours_slot_count INT,
  serv_hours_task VARCHAR(255)
);

CREATE TABLE admins (
  admin_id INT,
  FOREIGN KEY (admin_id) REFERENCES user(user_id)
);

-- PUT ANY ASSOCIATIVE ENTITIES HERE 

CREATE TABLE registration (
  reg_id INT NOT NULL PRIMARY KEY,
  scholar_id INT,
  serv_hours_id INT,
  FOREIGN KEY (scholar_id) REFERENCES scholar(scholar_id),
  FOREIGN KEY (serv_hours_id) REFERENCES service_hour_listing(serv_hours_id)
);


CREATE TABLE assignment (
  assignment_id INT NOT NULL PRIMARY KEY,
  admin_id INT,
  serv_hours_id INT,
  FOREIGN KEY (admin_id) REFERENCES admins(admin_id),
  FOREIGN KEY (serv_hours_id) REFERENCES service_hour_listing(serv_hours_id)
);

--Populate Tables

INSERT INTO user(user_id, email, user_password) VALUES
(1001, 'sch_uno@email.com', 'qwerty1213'),
(1002, 'sch_dos@email.com', 'qwerty1213'),
(1003, 'sch_tres@email.com', 'qwerty1213'),
(1004, 'adm_uno@email.com', 'qwerty1213'),
(1005, 'adm_uno@email.com', 'qwerty1213'),
(1006, 'adm_uno@email.com', 'qwerty1213');

INSERT INTO scholar(scholar_id, hours_needed, hours_rendered, contact_no, room_code, room_name, scholar_year, course) VALUES
(1001, 10, 0, '09157423345', 'ABC-123', 'ROOM 1', 3, 'BS CS'),
(1002, 5, 5, '09157443345', 'CAB-123', 'ROOM 2', 3, 'BS CS'),
(1003, 0, 10, '09157223345', 'BCA-123', 'ROOM 3', 3, 'BS CS');

INSERT INTO service_hour_listing(serv_hours_id, serv_hours_date, serv_hours_time, serv_hours_loc, serv_hours_slot_count, serv_hours_task) VALUES
(101, '2023-10-02', '1:30', 'Location # 1', 5, 'Task # 1'),
(102, '2023-10-02', '2:30', 'Location # 2', 5, 'Task # 2'),
(103, '2023-10-02', '3:30', 'Location # 3', 5, 'Task # 3');

INSERT INTO admins(admin_id) VALUES
(1004),
(1005),
(1006);

INSERT INTO registration (reg_id, scholar_id, serv_hours_id) VALUES
(451, 1001, 101),
(452, 1002, 102),
(453, 1003, 103);

INSERT INTO assignment (assignment_id, admin_id, serv_hours_id) VALUES
(551, 1004, 101),
(552, 1005, 102),
(553, 1006, 103);