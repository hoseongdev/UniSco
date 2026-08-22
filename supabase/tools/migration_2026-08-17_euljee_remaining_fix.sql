-- 2026-08-17 을지대 재검증 나머지 정정 (일현육성장학금 4종 마감일/카테고리, 을지가족/한마음봉사 설명 채움, 외국인장학금 조건 보완)
-- id=310의 "세종학당 중급2→토픽4급 인정" 매핑 문구는 원문 재확인이 더 필요해서 이번엔 손 안 댐

BEGIN;

UPDATE scholarship
SET application_deadline = '2026-05-20',
    category_l1 = 'school_internal',
    category_l2 = 'academic_merit'
WHERE id IN (1216,1217,1218,1219);

UPDATE scholarship
SET description = '교직원 직계자녀·협력병원 및 학교법인 재직자 자녀, 본교 졸업생 자녀, 또는 형제자매 2인 이상 재학 중인 학생 대상.'
WHERE id = 305;

UPDATE scholarship
SET description = '학생봉사단 "빛길" 활동자 또는 재학 중 누적 봉사시간 300시간 이상인 학생 대상.'
WHERE id = 314;

-- id=310은 위 주석대로 진짜 손 안 댐 — 이 파일에 있던 UPDATE가 바로 위
-- migration_2026-08-17_euljee_310_final.sql이 "원문에 없는 지어낸 내용"이라며 제거한
-- 토픽 등급 매핑을 그대로 되살리고 있었음(파일명이 알파벳순으로 뒤라 두 파일을 순서대로
-- 실행하면 방금 고친 걸 다시 덮어씀) — 자기모순이라 이 블록 삭제, 310_final.sql의 값이 최종.

COMMIT;
