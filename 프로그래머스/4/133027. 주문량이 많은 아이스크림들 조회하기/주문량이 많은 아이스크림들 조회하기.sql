-- 코드를 입력하세요
WITH first_total AS (
    SELECT
        FLAVOR,
        SUM(TOTAL_ORDER) AS total_one
    FROM
        FIRST_HALF 
    GROUP BY
        FLAVOR
), second_total AS (
    SELECT
        FLAVOR,
        SUM(TOTAL_ORDER) AS total_two
    FROM
        JULY 
    GROUP BY
        FLAVOR
)

SELECT
    f.FLAVOR
FROM
    first_total AS f
JOIN
    second_total AS s
ON
    f.FLAVOR = s.FLAVOR
ORDER BY
    total_one + total_two DESC
LIMIT 
    3
    