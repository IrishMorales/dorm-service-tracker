CREATE TABLE scholar (
  scholar_id INT NOT NULL PRIMARY KEY,
  passwrd VARCHAR(50) NOT NULL,
  obfmail VARCHAR(255) NOT NULL,
  hours_needed INT,
  hours_rendered INT,
  contact_no VARCHAR(20),
  room_code VARCHAR(50),
  room_name VARCHAR(100),
  schlr_year INT,
  course VARCHAR(100)
);

CREATE TABLE service_hour_details (
  sh_id INT NOT NULL PRIMARY KEY,
  sh_date DATE,
  sh_time TIME,
  sh_loc VARCHAR(255),
  sh_slots INT,
  sh_task VARCHAR(255)
);

CREATE TABLE admin (
  admin_id INT NOT NULL PRIMARY KEY,
  passwrd VARCHAR(50) NOT NULL,
  obfmail VARCHAR(255) NOT NULL
);

/** PUT ANY ASSOCIATIVE ENTITIES HERE **/

CREATE TABLE registration (
  reg_id INT NOT NULL PRIMARY KEY,
  scholar_id INT,
  sh_id INT,
  FOREIGN KEY (scholar_id) REFERENCES scholar(scholar_id),
  FOREIGN KEY (sh_id) REFERENCES service_hour_details(sh_id)
);


CREATE TABLE assigment (
  assigment_id INT NOT NULL PRIMARY KEY,
  admin_id INT,
  sh_id INT,
  FOREIGN KEY (admin_id) REFERENCES admin(admin_id),
  FOREIGN KEY (sh_id) REFERENCES service_hour_details(sh_id)
);

