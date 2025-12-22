-- 코드를 입력하세요
# WITH CARS AS (
#     SELECT
#         CAR_ID
#     FROM
#         CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE
#         START_DATE >= '2022-08-01' 
#         AND START_DATE <='2022-10-31'
#     GROUP BY 
#         CAR_ID
#     HAVING
#         COUNT(CAR_ID) >= 5
# )  

# SELECT
#     MONTH(START_DATE) AS MONTH,
#     t1.CAR_ID,
#     COUNT(*) AS RECORDS
# FROM
#     CAR_RENTAL_COMPANY_RENTAL_HISTORY AS t1
# JOIN
#     CARS AS t2
#     ON t1.CAR_ID = t2.CAR_ID
# WHERE
#     t1.START_DATE >= '2022-08-01'
#     AND t1.START_DATE <='2022-10-31'
# GROUP BY
#     MONTH,
#     t1.CAR_ID
# HAVING
#     RECORDS != 0
# ORDER BY
#     MONTH,
#     t1.CAR_ID DESC

WITH base AS (
    SELECT
        MONTH(START_DATE) AS MONTH,
        CAR_ID,
        COUNT(*) AS RECORDS
    FROM
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE
        START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY
        MONTH,
        CAR_ID
), rent_total AS (
    SELECT
        *,
        SUM(RECORDS) OVER (PARTITION BY CAR_ID) AS total
    FROM
        base
)

SELECT
    MONTH,
    CAR_ID,
    RECORDS
FROM
    rent_total
WHERE
    total >= 5
ORDER BY
    MONTH,
    CAR_ID DESC