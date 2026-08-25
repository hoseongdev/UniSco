"""2026-08-25: parent_occupation_condition(확인 불가 랭킹 전용 태그) 21건을 전수 재검토해서
3그룹으로 승격 — parent_university_staff/alumni, parent_clergy_or_missionary 승격과 동일한
패턴("본인/부모가 이 직업군인가요"에 예/아니오로 답할 수 있는 명확한 사실). 8~9개 개별 직업군
으로 잘게 쪼개는 대신 3그룹으로 크게 묶기로 사용자가 확정(2026-08-25, "분류기준 구체화" 논의).

- parent_civil_servant: 교사·경찰·소방·군인 등 공무원
- parent_small_business_or_worker: 중소기업·산업체 근로자 또는 소상공인(본인/부모 혼재).
  환경미화원(지자체 소속 근로자, 정식 공무원과는 다름)도 이 그룹.
- parent_local_service_leader: 이장·통장·새마을지도자 등 지역 봉사·자치직

21건 전부 required_special_status가 [parent_occupation_condition] 단일값임을 사전 확인
완료(배열 전체 교체 안전) — backend/app/models/enums.py의 3개 신규 값 참고, 상세는
audit_reports/fix_promote_parent_occupation_2026-08-25_diff.md 참고.

사용법:
    python fix_promote_parent_occupation_2026-08-25.py           # dry-run만
    python fix_promote_parent_occupation_2026-08-25.py --apply    # 실제 반영
"""
from __future__ import annotations

import sys
from pathlib import Path

import psycopg2

OLD_TAG = "parent_occupation_condition"

TARGET_TAGS: dict[int, str] = {
    # 공무원(교사·경찰·소방·군인 등)
    171: "parent_civil_servant",  # 교육직계장학금 — 교사
    249: "parent_civil_servant",  # 교육자직계자녀장학금(한남대) — 교사
    927: "parent_civil_servant",  # 황경자 장학금 — 소방공무원
    1031: "parent_civil_servant",  # 지정기탁장학금(백운장학회) — 경찰서·소방서 재직자
    640: "parent_civil_servant",  # 아산MIU자녀장학생 — 군인·소방·경찰 공무원
    # 중소기업·산업체 근로자 또는 소상공인(본인/부모)
    926: "parent_small_business_or_worker",  # 중소기업근로자자녀장학금(전남)
    1124: "parent_small_business_or_worker",  # 산업체노동자장학생(안산) — 학생 본인
    982: "parent_small_business_or_worker",  # 지역상생장학생(시흥) — 소상공인/산단재직자
    1069: "parent_small_business_or_worker",  # 기업체근로자자녀장학금(김해)
    1130: "parent_small_business_or_worker",  # 산단노동자자녀장학금(안산)
    74: "parent_small_business_or_worker",  # 화성시인재육성재단 소상공인 장학금
    1132: "parent_small_business_or_worker",  # 소상공인자녀장학금(안산)
    1131: "parent_small_business_or_worker",  # 특별장학생(안산상공회의소) — 회원사 재직 근로자
    238: "parent_small_business_or_worker",  # 환경미화원자녀장학금
    # 이장·통장·새마을지도자 등 지역 봉사·자치직
    1005: "parent_local_service_leader",  # 향토인재육성장학금(이장자녀, 횡성)
    1011: "parent_local_service_leader",  # 애향장학생(이통반장자녀, 춘천)
    1078: "parent_local_service_leader",  # 이통장자녀장학생(공주시)
    1063: "parent_local_service_leader",  # 청소년육성기금(새마을지도자자녀, 제주)
    1060: "parent_local_service_leader",  # 청소년육성기금(의용소방자녀, 제주)
    1061: "parent_local_service_leader",  # 청소년육성기금(방재단원자녀, 제주)
    1062: "parent_local_service_leader",  # 청소년육성기금(지도위원자녀, 제주)
}


def load_database_url() -> str:
    env_path = Path(__file__).resolve().parents[2] / "backend" / ".env"
    for line in env_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("DATABASE_URL="):
            return line.split("=", 1)[1].strip()
    raise RuntimeError(f"DATABASE_URL not found in {env_path}")


def main() -> None:
    apply = "--apply" in sys.argv
    conn = psycopg2.connect(load_database_url())
    cur = conn.cursor()

    target_ids = list(TARGET_TAGS)
    cur.execute(
        "SELECT id, name, required_special_status FROM scholarship "
        "WHERE id = ANY(%s) ORDER BY id",
        (target_ids,),
    )
    before_rows = {r[0]: r for r in cur.fetchall()}

    missing = [i for i in target_ids if i not in before_rows]
    if missing:
        print(f"경고: DB에 없는 id {missing} — 스킵")

    unexpected = [sid for sid, row in before_rows.items() if row[2] != [OLD_TAG]]
    if unexpected:
        print(f"경고: 예상과 다른 태그 조합 발견, 안전을 위해 스킵함: {unexpected}")
        for sid in unexpected:
            print(f"  id={sid}: {before_rows[sid][2]}")

    changed = 0
    for sid, new_tag in TARGET_TAGS.items():
        if sid not in before_rows or sid in unexpected:
            continue
        cur.execute(
            "UPDATE scholarship SET required_special_status = %s WHERE id = %s",
            ([new_tag], sid),
        )
        changed += 1

    cur.execute(
        "SELECT id, name, required_special_status FROM scholarship "
        "WHERE id = ANY(%s) ORDER BY id",
        (target_ids,),
    )
    after_rows = {r[0]: r for r in cur.fetchall()}

    for sid in target_ids:
        if sid not in before_rows:
            continue
        before, after = before_rows[sid], after_rows[sid]
        if before == after:
            continue
        print(f"id={sid} {before[1]}: {before[2]} -> {after[2]}")

    print(f"\n총 {len(target_ids)}건 대상, {changed}건 변경.")

    if apply:
        conn.commit()
        print("반영 완료(commit).")
    else:
        conn.rollback()
        print("dry-run만 수행(rollback, 실제 반영 안 됨).")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
