-- 30일 대여, 11월(1~30일) 동안 대여 가능한 세단/SUV, 50만 이상 ~ 200만 미만
SELECT T.CAR_ID, T.CAR_TYPE, T.FEE
FROM (
    SELECT
        C.CAR_ID,
        C.CAR_TYPE,
        FLOOR(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) AS FEE
    FROM CAR_RENTAL_COMPANY_CAR C
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
      ON C.CAR_TYPE = P.CAR_TYPE
    WHERE C.CAR_TYPE IN ('세단', 'SUV') AND P.DURATION_TYPE = '30일 이상' 
      AND NOT EXISTS (                           -- 11월 기간과 겹치는 대여 이력이 없어야 "대여 가능"
          SELECT 1
          FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
          WHERE H.CAR_ID = C.CAR_ID
            AND H.START_DATE <= '2022-11-30'
            AND H.END_DATE   >= '2022-11-01'     
      )
) AS T
WHERE T.FEE >= 500000
  AND T.FEE < 2000000
ORDER BY T.FEE DESC, T.CAR_TYPE ASC, T.CAR_ID DESC;
