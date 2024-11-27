WITH
    main_table AS (
        SELECT
            u.id,
            COUNT(o.id) AS orders_count
        FROM
            users u
            JOIN orders o ON u.id = o.user_id
        GROUP BY
            u.id
        ORDER BY
            orders_count ASC
    ),
    series AS (
        SELECT
            orders_count,
            ROW_NUMBER() OVER (
                ORDER BY
                    orders_count
            ) AS row_number,
            COUNT(*) OVER () AS total_rows
        FROM
            main_table
    )

SELECT
    AVG(orders_count) AS median_count
FROM
    series
WHERE
    row_number BETWEEN total_rows / 2.0 AND total_rows  / 2.0 + 1