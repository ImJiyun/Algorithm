-- 코드를 작성해주세요
SELECT
    he.EMP_NO,
    he.EMP_NAME,
    CASE 
        WHEN AVG(SCORE) >= 96 THEN 'S'
        WHEN AVG(SCORE) >= 90 THEN 'A'
        WHEN AVG(SCORE) >= 80 THEN 'B'
        ELSE 'C'
    END AS 'GRADE',
    
    CASE
        WHEN AVG(SCORE) >= 96 THEN SAL * 0.2
        WHEN AVG(SCORE) >= 90 THEN SAL * 0.15
        WHEN AVG(SCORE) >= 80 THEN SAL * 0.1
        ELSE SAL * 0
    END AS 'BONUS'
FROM
    HR_DEPARTMENT hd
JOIN
    HR_EMPLOYEES he
ON 
    hd.DEPT_ID = he.DEPT_ID
JOIN 
    HR_GRADE hg
ON 
    he.EMP_NO = hg.EMP_NO
GROUP BY
    he.EMP_NO, he.EMP_NAME
ORDER BY 
    he.EMP_NO