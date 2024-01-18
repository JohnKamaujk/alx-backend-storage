-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;

    -- Initialize variables
    SET total_weighted_score = 0;
    SET total_weight = 0;

    -- Calculate weighted average for each user
    INSERT INTO users (average_score)
    SELECT
        u.id,
        IFNULL(SUM(c.score * p.weight), 0) / IFNULL(SUM(p.weight), 1) AS weighted_average
    FROM
        users u
    LEFT JOIN corrections c ON u.id = c.user_id
    LEFT JOIN projects p ON c.project_id = p.id
    GROUP BY
        u.id;

END //
DELIMITER ;
