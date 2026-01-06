-- 코드를 작성해주세요
# 첫 시도 
# WITH longer_than_33 AS (
#     SELECT
#         FISH_TYPE
#     FROM
#         FISH_INFO
#     GROUP BY
#         FISH_TYPE
#     HAVING  
#         AVG(LENGTH) >= 33
# )

# SELECT
#     COUNT(FISH_TYPE) AS FISH_COUNT,
#     MAX(LENGTH) AS MAX_LENGTH,
#     FISH_TYPE
# FROM
#     FISH_INFO
# WHERE
#     FISH_TYPE IN (
#         SELECT
#             *
#         FROM
#             longer_than_33
#     )
# GROUP BY
#     FISH_TYPE

WITH not_null_table AS(
    SELECT
        FISH_TYPE,
        IF(LENGTH IS NULL, 10, LENGTH) AS LENGTH
    FROM
        FISH_INFO
)

SELECT
    COUNT(FISH_TYPE) AS FISH_COUNT,
    MAX(LENGTH) AS MAX_LENGTH,
    FISH_TYPE
FROM
    not_null_table
GROUP BY
    FISH_TYPE
HAVING
    AVG(LENGTH) >= 33
ORDER BY
    FISH_TYPE
