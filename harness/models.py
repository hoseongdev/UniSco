"""파이프라인 각 단계를 오가는 데이터 구조.

여기 정의된 dataclass들이 harness/의 모든 모듈이 공유하는 "계약"임 — collect_links.py가
Listing을 만들고, extract.py가 ExtractedScholarship을 만들고, verify.py가 그걸
VerifiedScholarship으로 바꾸고, build_pr.py가 그걸 읽어서 SQL/마크다운을 만듦.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

# backend/app/models/scholarship.py의 Scholarship 컬럼과 정확히 일치해야 함(id 제외).
# 새 필드를 여기 추가하고 싶으면 먼저 backend 쪽 모델/DB 컬럼부터 추가할 것 — 하네스가
# 스키마를 앞서가면 안 됨(설계안 "새 필드 추가 금지" 원칙).
SCHOLARSHIP_FIELD_NAMES: tuple[str, ...] = (
    "name",
    "provider",
    "description",
    "amount",
    "application_url",
    "min_age",
    "max_age",
    "required_gender",
    "eligible_region",
    "required_military_status",
    # 2026-08-15 백엔드에 추가된 필드인데 하네스 스키마 미러링이 그때 같이 안 됨(2026-08-22
    # 재검증 PR 리뷰 중 발견 — 그 사이 수집된 데이터는 이 조건을 아예 못 잡았을 가능성).
    "required_discharge_type",
    "max_income_bracket",
    "min_gpa",
    "min_gpa_basis",
    "requires_disability",
    "required_disability_type",
    "foreigner_eligibility",
    "language_test_type",
    "language_test_min_score",
    "required_special_status",
    "required_special_status_all",
    "excluded_special_status",
    "application_deadline",
    "grade_level",
    "major",
    "excluded_major",
    "admission_track",
    "affiliated_institution",
    "min_credits",
    "min_credits_last_semester",
    "admission_score_condition",
    "headcount",
    "application_period",
    "eligible_university",
    "eligible_college",
    "required_enrollment_status",
    "min_grade",
    "max_grade",
    "required_degree_level",
    "category_l1",
    "category_l2",
)

# 값을 안 채워도(=원문 근거 없음) 정상인 필드 — 리스트 필드들은 "빈 리스트=조건 없음"이
# 정상값이라 not_applicable 판정 시 빈 문자열이 아니라 빈 리스트가 "값 없음"의 기준이 됨.
LIST_VALUED_FIELDS: frozenset[str] = frozenset(
    {"required_special_status", "required_special_status_all", "excluded_special_status"}
)

# 비어있으면 안 되는 필드 — 2026-08-22 추가. id=46류 사고 재검증 중, name이 NULL인 채로
# "플래그된 필드 없음(정상)"으로 통과한 레코드가 목원대 3건/한남대 6건/KAIST 28건(39%!)
# 발견됨 — scholarship.name이 DB NOT NULL이라 이 상태로 SQL을 실행하면 배치 전체가
# 실패함(하나의 멀티로우 INSERT문이라 한 행만 잘못돼도 전부 롤백). verify.py가 이 집합에
# 있는 필드는 비어있으면 무조건 needs_review로 걸러냄(원래 있던 "원문에 근거 없어서
# 정상적으로 비움" 취급을 안 함 — name이 없는 건 애초에 정상 상태가 아니므로).
REQUIRED_SCHOLARSHIP_FIELDS: frozenset[str] = frozenset({"name"})


@dataclass
class Listing:
    """collect_links.py가 게시판에서 모은 공고 하나."""

    url: str
    title: str
    university: str
    department: str | None = None  # None이면 대학 공통 게시판
    board_name: str = ""


@dataclass
class CollectionResult:
    """게시판 하나를 순회한 결과 — "다 봤는지"를 코드가 판단한 증거를 담음."""

    university: str
    board_name: str
    listings: list[Listing]
    expected_count: int | None  # 게시판이 표시한 총 게시물 수 (파싱 실패 시 None)
    actual_count: int
    ok: bool  # expected_count == actual_count (파싱 자체가 안 됐으면 False)
    note: str = ""


@dataclass
class ExtractedField:
    """LLM이 반환한 필드 하나 — 값과 그 근거가 된 원문 인용을 항상 같이 들고 있음."""

    value: Any
    source_quote: str


@dataclass
class ExtractedScholarship:
    """extract.py의 단일 호출 결과 (문서 1건 = 이 객체 1개, 상태 없음).

    is_scholarship — 2026-08-22 추가. 하네스가 크롤링하는 게시판엔 "장학공지 게시판이
    카페로 옮겨갔다는 안내", "계좌정보 등록 안내" 같은 진짜 장학금 공고가 아닌 글도 섞여
    들어옴 — 기존엔 이런 걸 걸러낼 방법이 없어서 LLM이 억지로 장학금 스키마에 끼워
    맞추려다 name조차 못 채우는 레코드가 나왔음(2026-08-22 목원/한남/KAIST 재검증 중
    발견). 기본값 True — 판단 자체가 실패해도(예: 이 필드가 파싱 안 됨) 진짜 장학금을
    실수로 누락시키는 쪽보다 사람이 검토할 항목이 하나 더 느는 쪽이 안전함("과다매칭이
    과소매칭보다 낫다" 원칙과 동일한 방향)."""

    source_url: str
    fields: dict[str, ExtractedField]
    is_scholarship: bool = True
    is_scholarship_reason: str = ""

    def get(self, name: str) -> ExtractedField:
        return self.fields[name]


@dataclass
class VerifiedField:
    """verify.py가 ExtractedField를 기계적으로 검증한 결과."""

    name: str
    value: Any
    source_quote: str
    status: str  # "confirmed" | "needs_review" | "not_applicable"
    reason: str = ""
    # not_applicable: 값이 없고 인용도 없음(원문에 근거 없어서 정상적으로 비운 케이스) — 플래그 아님.
    # confirmed: 인용문이 원문에 실제로 존재함(정확 일치 또는 퍼지 매치).
    # needs_review: 값은 있는데 인용이 없거나(no_quote), 인용이 원문에 없거나(quote_not_found),
    #               2중 추출 결과가 서로 다름(dual_extract_mismatch).


@dataclass
class VerifiedScholarship:
    """build_pr.py가 SQL/리뷰 마크다운을 만드는 데 쓰는 최종 산출물."""

    source_url: str
    listing_title: str
    fields: dict[str, VerifiedField]
    is_scholarship: bool = True
    is_scholarship_reason: str = ""

    @property
    def flagged_fields(self) -> list[VerifiedField]:
        return [f for f in self.fields.values() if f.status == "needs_review"]

    @property
    def has_flags(self) -> bool:
        return len(self.flagged_fields) > 0

    def value(self, name: str) -> Any:
        return self.fields[name].value
