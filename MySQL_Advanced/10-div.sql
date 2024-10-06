-- Create the SafeDiv function
DELIMITER $$

CREATE FUNCTION SafeDiv(
    a INT,
    b INT
) RETURNS DECIMAL(10, 2)
BEGIN
    RETURN CASE
        WHEN b = 0 THEN 0
        ELSE a / b
    END;
END$$

DELIMITER ;
