WITH
    orders_last_month AS (
        SELECT
            menu_id,
            date (created_at) AS date,
            COUNT(*) AS orders_count
        FROM
            orders
        WHERE
            date (created_at) + INTERVAL '1 day' BETWEEN CURRENT_DATE - INTERVAL '1 month' AND CURRENT_DATE
        GROUP BY
            date (created_at),
            menu_id
    ),
    dishes_count AS (
        SELECT
            dish_id,
            SUM(orders_count) AS count
        FROM
            orders_last_month o
            JOIN dishes_menus dm ON o.menu_id = dm.menu_id
            AND o.date + INTERVAL '1 month 1 day' = dm.date
        GROUP BY
            dish_id
    ),
    dishes_ingredients_with_weights AS (
        SELECT
            dish_id,
            ingredient_id,
            weight::DECIMAL / COUNT(*) OVER (PARTITION BY dish_id)::DECIMAL AS ingredients_weight
        FROM
            dishes_ingredients AS di
            JOIN dishes AS d ON di.dish_id = d.id
    ),
    ingredients_total_weight AS (
        SELECT
            ingredient_id,
            SUM(ingredients_weight * count) AS total_weight
        FROM
            dishes_ingredients_with_weights AS weights
            JOIN dishes_count AS counts USING (dish_id)
        GROUP BY
            ingredient_id
    ),
    ingredients_productivity AS (
        SELECT
            ingredient_id,
            SUM(productivity) AS productivity
        FROM
            ingredients_suppliers AS ins
            JOIN suppliers s ON ins.supplier_id = s.id
        GROUP BY
            ingredient_id
    )

SELECT
    ingredient_id
FROM
    ingredients_total_weight AS itw
    JOIN ingredients_productivity AS ip USING (ingredient_id)
WHERE
    productivity * 1000 >= total_weight
ORDER BY
    ingredient_id