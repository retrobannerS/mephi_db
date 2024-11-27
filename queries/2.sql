SELECT 
    ROUND(
        SUM(m.cost) FILTER (WHERE m.title = 'Похудение')::DECIMAL / 
        SUM(m.cost)::DECIMAL * 100, 2) AS losing_weight_revenue_ratio
FROM
    orders AS o
    INNER JOIN menus AS m on o.menu_id = m.id