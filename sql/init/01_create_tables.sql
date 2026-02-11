-- Create Sales Analytics Database Schema

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(50),
    region VARCHAR(100),
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    segment VARCHAR(50),
    INDEX idx_region (region),
    INDEX idx_segment (segment)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    cost DECIMAL(10, 2) NOT NULL,
    stock INT DEFAULT 0,
    INDEX idx_category (category)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATETIME NOT NULL,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    total_amount DECIMAL(10, 2) NOT NULL,
    region VARCHAR(100),
    category VARCHAR(100),
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
    INDEX idx_date (date),
    INDEX idx_region (region),
    INDEX idx_category (category)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert sample data
INSERT INTO customers (name, email, phone, region, segment) VALUES
('Juan Pérez', 'juan.perez@email.com', '555-0001', 'Norte', 'VIP'),
('María García', 'maria.garcia@email.com', '555-0002', 'Sur', 'Regular'),
('Carlos López', 'carlos.lopez@email.com', '555-0003', 'Centro', 'Regular');

INSERT INTO products (name, category, price, cost, stock) VALUES
('Laptop Dell', 'Electrónica', 1200.00, 800.00, 50),
('Mouse Logitech', 'Accesorios', 25.00, 15.00, 200),
('Teclado Mecánico', 'Accesorios', 80.00, 50.00, 100);

INSERT INTO sales (date, product_id, customer_id, quantity, unit_price, total_amount, region, category) VALUES
('2024-01-15 10:30:00', 1, 1, 2, 1200.00, 2400.00, 'Norte', 'Electrónica'),
('2024-01-16 14:20:00', 2, 2, 5, 25.00, 125.00, 'Sur', 'Accesorios'),
('2024-01-17 09:15:00', 3, 3, 3, 80.00, 240.00, 'Centro', 'Accesorios');