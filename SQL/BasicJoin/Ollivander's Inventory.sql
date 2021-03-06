SELECT W.ID,WP.AGE,W.COINS_NEEDED,W.POWER
FROM WANDS W INNER JOIN WANDS_PROPERTY WP ON W.CODE = WP.CODE
WHERE WP.IS_EVIL =0 AND 
W.COINS_NEEDED = (SELECT MIN(W1.COINS_NEEDED)FROM WANDS W1 INNER JOIN WANDS_PROPERTY WP1 ON W1.CODE = WP1.CODE WHERE W.POWER = W1.POWER AND WP.AGE = WP1.AGE)
ORDER BY W.POWER DESC, WP.AGE DESC
