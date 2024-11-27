WITH
    orders_last_month AS (
        SELECT
            *
        FROM
            orders
        WHERE
            created_at >= CURRENT_DATE - INTERVAL '1 month'
    )

SELECT
    SUM(m.cost) AS Выручка
FROM
    orders_last_month AS o
    INNER JOIN menus AS m on o.menu_id = m.id