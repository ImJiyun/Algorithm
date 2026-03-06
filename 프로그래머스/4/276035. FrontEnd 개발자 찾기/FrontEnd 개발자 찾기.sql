-- 코드를 작성해주세요
SELECT
    d.ID,
    d.EMAIL,
    d.FIRST_NAME,
    d.LAST_NAME
FROM
    DEVELOPERS AS d
JOIN
    SKILLCODES AS s
ON
    d.SKILL_CODE & s.CODE = s.CODE
    AND
    CATEGORY = 'Front End'
ORDER BY
    ID