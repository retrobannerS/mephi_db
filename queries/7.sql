WITH
    ingredients_costs_in_rubles AS (
        SELECT
            id,
            cost * 7.55 AS cost_rubles
        FROM
            ingredients
    ),
    dishes_costs AS (
        SELECT
            d.dish_id AS id,
            SUM(i.cost_rubles) AS cost
        FROM
            dishes_ingredients d
            JOIN ingredients_costs_in_rubles i ON d.ingredient_id = i.id
        GROUP BY
            d.dish_id
    ),
    menus_costs_and_dishes AS (
        SELECT
            menu_id,
            m.date,
            SUM(cost) AS our_cost,
            ARRAY_AGG(dish_id) AS dishes
        FROM
            dishes_menus m
            JOIN dishes_costs c ON m.dish_id = c.id
        GROUP BY
            menu_id,
            m.date
        ORDER BY
            m.date,
            menu_id
    ),
    menus_profits AS (
        SELECT
            mc.*,
            m.cost,
            ROUND((m.cost - mc.our_cost)::DECIMAL, 2) AS profit,
            ROUND((m.cost - mc.our_cost)::DECIMAL / mc.our_cost::DECIMAL * 100, 2) AS profit_percent
        FROM
            menus_costs_and_dishes mc
            JOIN menus m ON mc.menu_id = m.id
    ),
    max_profit AS (
        SELECT
            menu_id,
            date,
            dishes,
            profit,
            profit_percent
        FROM
            menus_profits
        ORDER BY
            profit_percent DESC
        LIMIT 1
    ),
    max_profit_percent AS (
        SELECT
            menu_id,
            date,
            dishes,
            profit,
            profit_percent
        FROM
            menus_profits
        ORDER BY
            profit DESC
        LIMIT 1
    )

SELECT * FROM max_profit UNION ALL SELECT * FROM max_profit_percent;