-- Creates a function SafeDiv that divides (and returns) the first by
-- the second number returns 0 if the second number is equal to 0.
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER //

CREATE FUNCTION SafeDiv(
    IN p_a INT,
    IN p_b INT
)
RETURNS INT
BEGIN
    DECLARE result INT;

    -- Compute the result
    IF p_b == 0 THEN
        SET result = 0;
    ELSE
        SET result = p_a / p_b;
    END IF;

    RETURN result;
END;
//

DELIMITER ;
