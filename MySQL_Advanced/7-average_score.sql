-- Create the ComputeAverageScoreForUser stored procedure
delimiter $$
CREATE PROCEDURE ComputeAverageScoreForUser(input_id INT)
    BEGIN
        DECLARE average FLOAT;
        SELECT AVG(COALESCE(score)) INTO average
        FROM corrections
        WHERE user_id = input_id;

        UPDATE users
        SET average_score = average
        WHERE id = input_id;
    END;
$$
delimiter ;
