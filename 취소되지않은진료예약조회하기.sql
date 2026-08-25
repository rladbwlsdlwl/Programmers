-- 코드를 입력하세요
SELECT a.apnt_no, b.pt_name, a.pt_no, a.mcdp_cd, c.dr_name, a.apnt_ymd
FROM appointment a JOIN patient b on a.pt_no = b.pt_no 
    JOIN doctor c on a.mddr_id = c.dr_id
WHERE apnt_ymd >= "2022-04-13" and apnt_ymd < "2022-04-14" # timestamp 비교
    and apnt_cncl_yn = "n"
ORDER BY a.apnt_ymd asc;
