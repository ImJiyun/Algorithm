-- 코드를 입력하세요
WITH food_rank_table AS (
    SELECT 
        CATEGORY,
        PRODUCT_NAME,
        PRICE,
        DENSE_RANK() OVER (PARTITION BY CATEGORY ORDER BY PRICE DESC) AS food_rank
    FROM 
        FOOD_PRODUCT
)

SELECT 
    CATEGORY,
    PRICE AS MAX_PRICE,
    PRODUCT_NAME
FROM
    food_rank_table
WHERE
    food_rank = 1
    AND
    CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY
    MAX_PRICE DESC