CREATE TABLE IF NOT EXISTS "clinic" (
    id INTEGER PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    location_id INT NOT NULL,
    FOREIGN KEY (location_id) REFERENCES location(id)
);
