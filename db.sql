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

/** PUT ANY ASSOCIATIVE ENTITIES HERE **/

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

