WITH RECURSIVE
    users_tree AS (
        SELECT
            id,
            CONCAT (first_name, ' ', middle_name, ' ', last_name) AS full_name,
            invited_by_id AS parent_id,
            1 AS level
        FROM
            users
        WHERE
            invited_by_id IS NULL
        UNION ALL
        SELECT
            u.id,
            CONCAT (first_name, ' ', middle_name, ' ', last_name) AS full_name,
            invited_by_id AS parent_id,
            ut.level + 1
        FROM
            users u
            JOIN users_tree ut ON u.invited_by_id = ut.id
    )

SELECT
    *
FROM
    users_tree

