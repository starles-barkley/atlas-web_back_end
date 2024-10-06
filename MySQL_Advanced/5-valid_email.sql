-- Create a trigger that resets valid_email when the email is updated

delimiter $$
CREATE TRIGGER validator BEFORE UPDATE ON users
    FOR EACH ROW
    BEGIN
        IF NEW.email != OLD.email THEN
            SET NEW.valid_email = 0;
        END IF;
    END;
$$
delimiter ;