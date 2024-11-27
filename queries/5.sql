WITH
    payment_infos_and_methods AS (
        SELECT
            i.id AS payment_info_id,
            m.title AS payment_method
        FROM
            payment_infos i
            JOIN payment_methods m ON i.payment_method_id = m.id
    ),
    user_method_counts AS (
        SELECT
            o.user_id,
            p.payment_method,
            COUNT(o.id) AS orders_count
        FROM
            orders o
            JOIN payment_infos_and_methods p USING (payment_info_id)
        GROUP BY
            o.user_id,
            p.payment_method
    ),
    user_method_counts_with_total AS (
        SELECT
            *,
            SUM(orders_count) OVER (
                PARTITION BY
                    user_id
            ) AS total_orders_count
        FROM
            user_method_counts
    ),
    users_with_almost_cash_orders AS (
        SELECT
            user_id AS id
        FROM
            user_method_counts_with_total
        WHERE
            payment_method = 'Наличные курьеру'
            AND orders_count > total_orders_count / 2
    )

SELECT
    u.id,
    CONCAT(u.first_name, ' ', u.middle_name, ' ', u.last_name) AS name,
    u.bonuses
FROM
    users u
    JOIN users_with_almost_cash_orders u_cash USING (id)
ORDER BY
    u.bonuses DESC
LIMIT
    5;