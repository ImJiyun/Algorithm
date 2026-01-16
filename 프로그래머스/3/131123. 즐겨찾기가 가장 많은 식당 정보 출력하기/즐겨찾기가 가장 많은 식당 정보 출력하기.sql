-- 코드를 입력하세요
# SELECT
#     FOOD_TYPE,
#     REST_ID,
#     REST_NAME,
#     FAVORITES
# FROM (
#     SELECT
#         FOOD_TYPE,
#         REST_ID,
#         REST_NAME,
#         FAVORITES,
#         ROW_NUMBER() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS RN
#     FROM REST_INFO
# ) AS Ranked
# WHERE RN = 1
# ORDER BY FOOD_TYPE DESC;

WITH fav_rank_table AS (
    SELECT
        *,
        RANK() OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS fav_rank
    FROM
        REST_INFO 
)

SELECT
    FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES
FROM
    fav_rank_table
WHERE
    fav_rank = 1
ORDER BY
    FOOD_TYPE DESC