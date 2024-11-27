WITH
    yandex_split_payments AS (
        SELECT
            i.*
        FROM
            payment_infos i
            JOIN payment_methods m ON i.payment_method_id = m.id
        WHERE
            m.title = 'Яндекс.Сплит'
    )

SELECT
    o.id AS order_id,
    DATE(o.created_at) AS order_created_at,
    p.requisites AS requisites
FROM
    orders o
    JOIN yandex_split_payments p ON o.payment_info_id = p.id
WHERE
    o.status = 'returned'