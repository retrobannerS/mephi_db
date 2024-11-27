SELECT 
    title, 
    cost,
    ROUND(cost::DECIMAL / 1.2 * 0.2, 2) AS tax,
    ROUND(cost::DECIMAL / 1.2, 2) AS cost_before_tax
FROM
    menus
