CREATE DATABASE IF NOT EXISTS hotel_booking;

CREATE TABLE IF NOT EXISTS hotel_booking.hotels (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    city VARCHAR(255),
    capacity INT,
    available BOOLEAN
);

INSERT INTO hotel_booking.hotels (name, city, capacity, available) VALUES
('Tourist Sunny Apartment', 'Anchorage', 4, 1),
('Snow Palace', 'New Delhi', 5, 1),
('City Break Inn', 'Porto-Novo', 3, 1);

INSERT INTO hotel_booking.hotels (name, city, capacity, available)
VALUES
('Grand Hotel', 'New York', 200, 1),
('Marina Bay Sands', 'Singapore', 500, 1),
('The Ritz-Carlton', 'London', 300, 1),
('Four Seasons Hotel', 'Paris', 400, 1),
('Hilton Garden Inn', 'Tokyo', 250, 1);

ALTER TABLE hotel_booking.hotels ADD COLUMN price DECIMAL(10, 2);

INSERT INTO hotel_booking.hotels (name, city, available, price) VALUES
('Hilton', 'New York', TRUE, 250.00),
('Marriott', 'Los Angeles', TRUE, 200.00),
('Hilton', 'San Francisco', FALSE, 300.00),
('Holiday Inn', 'Chicago', TRUE, 150.00);

UPDATE hotel_booking.hotels SET price = 100.00 WHERE price IS NULL;