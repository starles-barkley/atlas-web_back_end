-- Create the ComputeAverageScoreForUser stored procedure
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average_score DECIMAL(10, 2);

    -- Compute the average score for the given user
    SELECT AVG(score)
    INTO average_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the average_score field in the users table
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END$$
