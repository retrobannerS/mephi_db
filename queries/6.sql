WITH
    most_popular_category AS (
        SELECT
            preference_category_id,
            COUNT(pu.id) AS count
        FROM
            preferences_users pu
            JOIN preferences p ON pu.preference_id = p.id
        GROUP BY
            preference_category_id
        ORDER BY
            count DESC
        LIMIT
            1
    ),
    preferences_from_most_popular_category AS (
        SELECT
            id,
            title
        FROM
            preferences
        WHERE
            preference_category_id = (
                SELECT
                    preference_category_id
                FROM
                    most_popular_category
            )
    ),
    ingredients_from_most_popular_category AS (
        SELECT
            ip.ingredient_id
        FROM
            ingredients_preferences ip
        JOIN preferences_from_most_popular_category p ON ip.preference_id = p.id
    )

SELECT
    DISTINCT d.title
FROM
    dishes_ingredients
    JOIN ingredients_from_most_popular_category i ON dishes_ingredients.ingredient_id = i.ingredient_id
    JOIN dishes d ON dishes_ingredients.dish_id = d.id
ORDER BY
    d.title;