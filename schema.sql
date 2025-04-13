CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Venues (
    venue_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location TEXT NOT NULL,
    capacity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Concerts (
    concert_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    venue_id INT REFERENCES Venues(venue_id) ON DELETE CASCADE,
    event_date TIMESTAMP NOT NULL,
    ticket_price DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Tickets (
    ticket_id SERIAL PRIMARY KEY,
    concert_id INT REFERENCES Concerts(concert_id) ON DELETE CASCADE,
    seat_number VARCHAR(10) NOT NULL,
    status VARCHAR(20) CHECK (status IN ('available', 'booked')) DEFAULT 'available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- It is not required for now
-- CREATE TABLE Bookings (
--     booking_id SERIAL PRIMARY KEY,
--     user_id INT REFERENCES Users(user_id) ON DELETE CASCADE,
--     ticket_id INT REFERENCES Tickets(ticket_id) ON DELETE CASCADE,
--     booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     status VARCHAR(20) CHECK (status IN ('pending', 'confirmed', 'canceled')) DEFAULT 'pending'
-- );

CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY,
    booking_id INT REFERENCES Bookings(booking_id) ON DELETE CASCADE,
    amount DECIMAL(10,2) NOT NULL,
    payment_method VARCHAR(50) CHECK (payment_method IN ('credit_card', 'debit_card', 'paypal', 'upi')) NOT NULL,
    payment_status VARCHAR(20) CHECK (payment_status IN ('pending', 'completed', 'failed')) DEFAULT 'pending',
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
