-- 코드를 입력하세요
# SELECT
#     *,
#     DATEDIFF(END_DATE, START_DATE) AS time_diff
# FROM
#     CAR_RENTAL_COMPANY_CAR AS t1
# LEFT JOIN
#     CAR_RENTAL_COMPANY_RENTAL_HISTORY AS t2
# ON 
#     t1.CAR_ID = t2.CAR_ID
# WHERE
#     t1.CAR_TYPE = '트럭'

# SELECT
#     *
# FROM
#     CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
# WHERE
#     car_type = '트럭'


WITH d AS (SELECT
    h.HISTORY_ID,
    h.CAR_ID,
    DATEDIFF(h.END_DATE, h.START_DATE) + 1 AS duration,
    # h.START_DATE,
    # h.END_DATE,
    c.CAR_TYPE,
    c.DAILY_FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS h
LEFT JOIN CAR_RENTAL_COMPANY_CAR AS c
ON h.CAR_ID = c.CAR_ID
WHERE
    c.CAR_TYPE = '트럭'
)

SELECT 
    d.HISTORY_ID,
    ROUND(IF(DISCOUNT_RATE IS NULL, (d.duration * d.DAILY_FEE), (d.duration * d.DAILY_FEE) * ((100 - p.DISCOUNT_RATE) / 100))) AS FEE
    # d.CAR_ID,
    # d.duration,
    # d.CAR_TYPE,
    # d.DAILY_FEE,
    # p.DISCOUNT_RATE
FROM d
LEFT JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS p
ON d.CAR_TYPE = p.CAR_TYPE
AND (
    (d.duration >= 90 AND p.DURATION_TYPE = '90일 이상') OR
    (d.duration >= 30 AND d.duration < 90 AND p.DURATION_TYPE = '30일 이상') OR
    (d.duration >= 7 AND d.duration < 30 AND p.DURATION_TYPE = '7일 이상')
)
ORDER BY
    FEE DESC,
    d.HISTORY_ID DESC