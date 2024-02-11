CREATE TABLE IF NOT EXISTS "clinician" (
    id INTEGER PRIMARY KEY NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    location_id INT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES location(id)
);
