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
  scholar_LN VARCHAR(50),
  scholar_FN VARCHAR(50),
  scholar_MI VARCHAR(50),
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
  serv_hours_start_time TIME,
  serv_hours_end_time TIME,
  serv_hours_loc VARCHAR(255),
  serv_hours_slot_count INT,
  serv_hours_task VARCHAR(255),
  is_rendered BOOLEAN
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

-- Populate Tables

INSERT INTO user(user_id, email, user_password) VALUES
(200000, 'sch_uno@email.com', 'qwerty1213'),
(200001, 'sch_dos@email.com', 'qwerty1213'),
(200002, 'sch_tres@email.com', 'qwerty1213'),
(209997, 'adm_uno@email.com', 'qwerty1213'),
(209998, 'adm_dos@email.com', 'qwerty1213'),
(209999, 'adm_tres@email.com', 'qwerty1213');

INSERT INTO scholar(scholar_id, scholar_LN, scholar_FN, scholar_MI, hours_needed, hours_rendered, contact_no, room_code, room_name, scholar_year, course) VALUES
(200000, 'Blossom', 'Cherry', 'P', 10, 0, '09157423345', 'UDN315', 'ROOM 1', 3, 'BS CS'),
(200001, 'Berry', 'Blue', 'S', 23, 0, '09157443345', 'C201', 'ROOM 2', 3, 'BS CS'),
(200002, 'Sundae', 'Caramel', 'O', 10, 0, '09157223345', 'E113', 'ROOM 3', 3, 'BS CS');

INSERT INTO service_hour_listing(serv_hours_id, serv_hours_date, serv_hours_start_time, serv_hours_end_time, serv_hours_loc, serv_hours_slot_count, serv_hours_task, is_rendered) VALUES
(101, '2023-10-02', '13:00', '14:00', 'Location # 1', 2, 'Task # 1', 0),
(102, '2023-10-02', '08:00', '09:30', 'Location # 2', 2, 'Task # 2', 1),
(103, '2023-10-02', '15:30', '17:00', 'Location # 3', 2, 'Task # 3', 0);

INSERT INTO admins(admin_id) VALUES
(209997),
(209998),
(209999);

INSERT INTO registration (reg_id, scholar_id, serv_hours_id) VALUES
(451, 200001, 101),
(452, 200001, 102),
(453, 200000, 103);

INSERT INTO assignment (assignment_id, admin_id, serv_hours_id) VALUES
(551, 209997, 101),
(552, 209998, 102),
(553, 209999, 103);