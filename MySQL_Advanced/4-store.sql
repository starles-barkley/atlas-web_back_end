-- Create a trigger that decreases the item quantity after a new order is inserted
DELIMITER $$

CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity of the item after a new order is placed
    UPDATE items
    SET quantity = quantity - NEW.order_quantity
    WHERE id = NEW.item_id;
END$$

DELIMITER ;
