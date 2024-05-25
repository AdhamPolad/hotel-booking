CREATE TABLE IF NOT EXISTS hotel_booking.credit_cards (
    id INT AUTO_INCREMENT PRIMARY KEY,
    number VARCHAR(16),
    expiration VARCHAR(5),
    cvc VARCHAR(3),
    holder VARCHAR(255),
    balance DECIMAL(10, 2)
);


INSERT INTO hotel_booking.credit_cards (number, expiration, cvc, holder, balance) VALUES
('123456789012345', '12/26', '123', 'JOHN SMITH', 1900.00),
('5678', '12/28', '456', 'JANE SMITH', 1888.00);