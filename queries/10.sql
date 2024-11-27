WITH
    main_table AS (
        SELECT
            DATE (o.created_at) AS date,
            SUM(m.cost) AS revenue
        FROM
            orders o
            JOIN menus m ON o.menu_id = m.id
        GROUP BY
            DATE (o.created_at)
        ORDER BY
            date
    )

SELECT
    date,
    revenue,
    (revenue - LAG (revenue, 1) OVER ()) AS revenue_growth_abs,
    ROUND(100 * (revenue - LAG (revenue, 1) OVER ())::DECIMAL / LAG (revenue, 1) OVER ()::DECIMAL, 2) AS revenue_growth_rate
FROM
    main_table