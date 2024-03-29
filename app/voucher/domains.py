from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class VoucherBidAskDto(BaseModel):
    name: Optional[str]  # optional 이 아니어야 하나 구현 편의상 optional 로 처리함. 최종 메서드에서 필터링 해서 처리
    store: str
    bid: Decimal
    ask: Decimal


VOUCHER_NAME_DICT = {
    "롯데백화점 50만원권": '롯데백화점 50만원권',
    "롯데백화점상품권 50만원권": '롯데백화점 50만원권',
    "롯데상품권50만원권": '롯데백화점 50만원권',
    "롯데 상품권(50만원권)": '롯데백화점 50만원권',
    "롯데백화점상품권 30만원권": '롯데백화점 30만원권',
    "롯데백화점 10만원권": '롯데백화점 10만원권',
    "롯데백화점상품권 10만원권": '롯데백화점 10만원권',
    "롯데상품권10만원권": '롯데백화점 10만원권',
    "롯데 상품권(10만원권)": '롯데백화점 10만원권',
    "롯데백화점 5만원권": '롯데백화점 5만원권',
    "롯데백화점상품권 5만원권": '롯데백화점 5만원권',
    "롯데상품권5만원권": '롯데백화점 5만원권',
    "롯데 상품권(5만원권)": '롯데백화점 5만원권',
    "롯데백화점상품권 3만원권": '롯데백화점 3만원권',
    "롯데백화점 1만원권": '롯데백화점 1만원권',
    "롯데 상품권(1만원권)": '롯데백화점 1만원권',
    "롯데백화점상품권 1만원권": '롯데백화점 1만원권',
    "롯데상품권1만원권": '롯데백화점 1만원권',
    "롯데스폐셜카드(50만원권)": '롯데 스페셜카드 50만원권',
    "롯데스페셜(스페샬)기프트카드 50만원권": '롯데 스페셜카드 50만원권',
    "롯데 스페셜카드 상품권": '롯데 스페셜카드 10만원권',
    "롯데스페셜카드10만원권": '롯데 스페셜카드 10만원권',
    "롯데스폐셜카드10만원권": '롯데 스페셜카드 10만원권',
    "롯데스페셜(스페샬)기프트카드 10만원권": '롯데 스페셜카드 10만원권',
    "롯데호텔 10만원권(종이식)": '롯데호텔 10만원권',
    "롯데호텔10만원권(종이식)": '롯데호텔 10만원권',
    "롯데 백화점(면세점 및 호텔) 상품권": '롯데호텔 10만원권',
    "신세계백화점 50만원권": '신세계백화점 50만원권',
    "신세계백화점상품권 50만원권": '신세계백화점 50만원권',
    "신세계상품권50만원권": '신세계백화점 50만원권',
    "신세계 상품권(50만원권)": '신세계백화점 50만원권',
    "신세계백화점상품권 30만원권": '신세계백화점 30만원권',
    "신세계백화점 10만원권": '신세계백화점 10만원권',
    "신세계백화점상품권 10만원권": '신세계백화점 10만원권',
    "신세계상품권10만원권": '신세계백화점 10만원권',
    "신세계 상품권(10만원권)": '신세계백화점 10만원권',
    "신세계백화점 5만원권": '신세계백화점 5만원권',
    "신세계백화점상품권 5만원권": '신세계백화점 5만원권',
    "신세계상품권5만원권": '신세계백화점 5만원권',
    "신세계 상품권(5만원권)": '신세계백화점 5만원권',
    "신세계백화점 1만원권": '신세계백화점 1만원권',
    "신세계백화점상품권 1만원권": '신세계백화점 1만원권',
    "신세계상품권1만원권": '신세계백화점 1만원권',
    "신세계 상품권(1만원권)": '신세계백화점 1만원권',
    "신세계백화점상품권 5천원권": '신세계백화점 5천원권',
    "신세계 백화점 5000원권": '신세계백화점 5천원권',
    "현대백화점 50만원": '현대백화점 50만원권',
    "현대백화점상품권 50만원권": '현대백화점 50만원권',
    "현대상품권50만원권": '현대백화점 50만원권',
    "현대 상품권(50만원권)": '현대백화점 50만원권',
    "현대백화점 10만원권": '현대백화점 10만원권',
    "현대백화점상품권 10만원권": '현대백화점 10만원권',
    "현대상품권10만원권": '현대백화점 10만원권',
    "현대 상품권(10만원권)": '현대백화점 10만원권',
    "현대상품권5만원권": '현대백화점 5만원권',
    "현대백화점상품권 5만원권": '현대백화점 5만원권',
    "현대 상품권(5만원권)": '현대백화점 5만원권',
    "현대상품권1만원권": '현대백화점 1만원권',
    "현대백화점상품권 1만원권": '현대백화점 1만원권',
    "현대 상품권(1만원권)": '현대백화점 1만원권',
    "홈플러스50만원권디지탈": '홈플러스(디지털) 50만원권',
    "홈플러스 디지탈상품권(50만원권)": '홈플러스(디지털) 50만원권',
    "홈플러스 30만원권": '홈플러스 30만원권',
    "홈플러스상품권 30만원권": '홈플러스 30만원권',
    "홈플러스30만원권": '홈플러스 30만원권',
    "홈플러스 상품권(30만원권)": '홈플러스 30만원권',
    "홈플러스 10만원권": '홈플러스 10만원권',
    "홈플러스상품권 10만원": '홈플러스 10만원권',
    "홈플러스10만원권": '홈플러스 10만원권',
    "홈플러스 상품권(10만원권)": '홈플러스 10만원권',
    "홈플러스 5만원권": '홈플러스 5만원권',
    "홈플러스상품권 5만원권": '홈플러스 5만원권',
    "홈플러스5만원권": '홈플러스 5만원권',
    "홈플러스 상품권(5만원권)": '홈플러스 5만원권',
    "홈플러스 상품권(1만원권)": '홈플러스 1만원권',
    "AK플라자(프라자)상품권50만원": 'AK플라자 50만원권',
    "AK프라자상품권30만원": 'AK플라자 30만원권',
    "AK플라자 10만원권": 'AK플라자 10만원권',
    "AK플라자(프라자)상품권10만원": 'AK플라자 10만원권',
    "AK프라자10만원권": 'AK플라자 10만원권',
    "AK 상품권 (10만원권)": 'AK플라자 10만원권',
    "AK플라자(프라자)상품권5만원": 'AK플라자 5만원권',
    "AK플라자(프라자)상품권1만원": 'AK플라자 1만원권',
    "삼성상품권 10만원권 (종이식)": '삼성상품권 10만원권',
    "삼성상품권 10만원": '삼성상품권 10만원권',
    "삼성상품권10만원권": '삼성상품권 10만원권',
    "삼성 상품권(10만원권)": '삼성상품권 10만원권',
    "삼성상품권5만원권": '삼성상품권 5만원권',
    "삼성상품권 5만원": '삼성상품권 5만원권',
    "이랜드 상품권 10만원": '이랜드 10만원권',
    "이랜드상품권(뉴코아·NC백화점) 10만원권": '이랜드 10만원권',
    "이랜드상품권10만원권": '이랜드 10만원권',
    "이랜드 (10만원권)": '이랜드 10만원권',
    "갤러리아백화점상품권 50만원": '갤러리아백화점 50만원권',
    "갤러리아 상품권(50만원권)": '갤러리아백화점 50만원권',
    "갤러리아백화점10만원": '갤러리아백화점 10만원권',
    "갤러리아백화점상품권 10만원": '갤러리아백화점 10만원권',
    "갤러리아10만원권": '갤러리아백화점 10만원권',
    "갤러리아 상품권(10만원권)": '갤러리아백화점 10만원권',
    "갤러리아백화점상품권 5만원": '갤러리아백화점 5만원권',
    "갤러리아백화점상품권 1만원": '갤러리아백화점 1만원권',
    "갤러리아 지류상품권(1만원권)": '갤러리아백화점 1만원권',
    "메가마트 상품권": '메가마트 10만원권',
    "메가마트상품권 10만원": '메가마트 10만원권',
    "아이파크 상품권 10만원권": '아이파크 10만원권',
    "현대백화점아이파크상품권 10만원": '아이파크 10만원권',
    "아이파크10만원권": '아이파크 10만원권',
    "아이파크 (10만원권)": '아이파크 10만원권',
    "아이파크 1만원권": '아이파크 1만원권',
    "그랜드 백화점": '그랜드백화점 10만원권',
    "금강제화 상품권 10만원권": '금강제화 10만원권',
    "금강제화상품권 구두티켓 랜드로바 10만원권": '금강제화 10만원권',
    "금강제화10만원권": '금강제화 10만원권',
    "금강제화 (10만원권)": '금강제화 10만원권',
    "금강제화 상품권 7만원권": '금강제화 7만원권',
    "금강제화상품권 구두티켓 랜드로바 7만원권": '금강제화 7만원권',
    "금강제화7만원권": '금강제화 7만원권',
    "금강제화(7만원권)": '금강제화 7만원권',
    "금강제화 상품권 5만원권": '금강제화 5만원권',
    "금강제화상품권 구두티켓 랜드로바 5만원권": '금강제화 5만원권',
    "금강제화5만원권": '금강제화 5만원권',
    "금강제화(5만원권)": '금강제화 5만원권',
    "삼성 기프트카드": '삼성 기프트카드 50만원권',
    "삼성기프트카드 50만원": '삼성 기프트카드 50만원권',
    "삼성기프트50만원권": '삼성 기프트카드 50만원권',
    "삼성 기프트카드(50만원권)": '삼성 기프트카드 50만원권',
    "신한 기프트 카드": '신한 기프트카드 50만원권',
    "신한기프트카드 50만원": '신한 기프트카드 50만원권',
    "신한 기프트카드(50만원권)": '신한 기프트카드 50만원권',
    "현대 기프트 카드": '현대 기프트카드 50만원권',
    "현대기프트카드 50만원": '현대 기프트카드 50만원권',
    "현대 기프트카드(50만원권)": '현대 기프트카드 50만원권',
    "국민 기프트 카드": '국민 기프트카드 50만원권',
    "국민기프트카드 50만원": '국민 기프트카드 50만원권',
    "국민기프트50만원권": '국민 기프트카드 50만원권',
    "국민기프트카드 (50만원권)": '국민 기프트카드 50만원권',
    "KEB하나 기프트카드": 'KEB하나 기프트카드 50만원권',
    "KEB하나기프트카드 50만원": 'KEB하나 기프트카드 50만원권',
    "BC 기프트 카드": 'BC 기프트카드 50만원권',
    "BC기프트카드 50만원": 'BC 기프트카드 50만원권',
    "비씨기프트50만원권": 'BC 기프트카드 50만원권',
    "비씨 기프트카드(50만원권)": 'BC 기프트카드 50만원권',
    "롯데 기프트 카드": '롯데 기프트카드 50만원권',
    "롯데기프트카드 50만원": '롯데 기프트카드 50만원권',
    "롯데기프트카드(50만원권)": '롯데 기프트카드 50만원권',
    "각종 기프트카드 30만원권": '기프트카드 30만원권',
    "각종기프트카드 30만원": '기프트카드 30만원권',
    "기프트카드30만원권": '기프트카드 30만원권',
    "기프트카드(30만원권)": '기프트카드 30만원권',
    "각종 기프트카드 10만원권": '기프트카드 10만원권',
    "각종기프트카드 10만원": '기프트카드 10만원권',
    "기프트카드10만원권": '기프트카드 10만원권',
    "기프트카드(10만원권)": '기프트카드 10만원권',
    "각종 기프트카드 5만원권": '기프트카드 5만원권',
    "각종기프트카드 5만원": '기프트카드 5만원권',
    "기프트카드(5만원권)": '기프트카드 5만원권',
    "농협 기프트 카드 50만원권": '농협 기프트카드 50만원권',
    "농협기프트카드 50만원": '농협 기프트카드 50만원권',
    "농협기프트카드50만원권": '농협 기프트카드 50만원권',
    "농협 기프트 카드 30만원권": '농협 기프트카드 30만원권',
    "농협기프트카드 30만원": '농협 기프트카드 30만원권',
    "농협 기프트 카드 10만원권": '농협 기프트카드 10만원권',
    "농협기프트카드 10만원": '농협 기프트카드 10만원권',
    "농산물(농협)상품권 10만원": '농협 하나로상품권 10만원권',
    "농협하나로상품권10만원권": '농협 하나로상품권 10만원권',
    "농협하나로 상품권(10만원권)": '농협 하나로상품권 10만원권',
    "농협하나로상품권5만원권": '농협 하나로상품권 5만원권',
    "농협하나로 상품권(5만원권)": '농협 하나로상품권 5만원권',
    "농산물(농협) 상품권 1만원권": '농협 하나로상품권 1만원권',
    "농협하나로상품권1만원권": '농협 하나로상품권 1만원권',
    "농협하나로 상품권(1만원권)": '농협 하나로상품권 1만원권',
    "해피머니 문화상품권 1만원권": '해피머니 문화상품권 1만원권',
    "해피머니문화상품권(신권) 1만원": '해피머니 문화상품권 1만원권',
    "해피머니1만원권": '해피머니 문화상품권 1만원권',
    "해피머니(1만원권)": '해피머니 문화상품권 1만원권',
    "해피머니5천원권": '해피머니 문화상품권 5천원권',
    "해피머니 문화상품권 5천원권": '해피머니 문화상품권 5천원권',
    "해피머니상품권(5천원권)": '해피머니 문화상품권 5천원권',
    "해피머니문화상품권(신권) 5천원": '해피머니 문화상품권 5천원권',
    "컬쳐랜드문화상품권 5만원": '문화상품권 5만원권',
    "문화상품권 5만원권": '문화상품권 5만원권',
    "문화지류상품권(5만원)": '문화상품권 5만원권',
    "문화상품권 1만원권": '문화상품권 1만원권',
    "컬쳐랜드문화상품권(신권) 1만원": '문화상품권 1만원권',
    "문화상품1만원권": '문화상품권 1만원권',
    "컬처문화상품권(1만원권)": '문화상품권 1만원권',
    "문화상품권 5천원권": '문화상품권 5천원권',
    "컬쳐랜드문화상품권(신권)5천원": '문화상품권 5천원권',
    "문화상품5천원권": '문화상품권 5천원권',
    "컬처문화상품권(5천원권)": '문화상품권 5천원권',
    "도서문화상품권 1만원권": '도서문화상품권 1만원권',
    "도서문화상품권 1만원(신권)": '도서문화상품권 1만원권',
    "도서문화상품권1만원권": '도서문화상품권 1만원권',
    "도서문화상품권(1만원권)": '도서문화상품권 1만원권',
    "도서문화상품권 5천원권": '도서문화상품권 5천원권',
    "도서문화상품권 5천원(신권)": '도서문화상품권 5천원권',
    "도서문화상품권5천원권": '도서문화상품권 5천원권',
    "도서문화상품권(5천원)": '도서문화상품권 5천원권',
    "CJ 상품권 10만원": 'CJ 10만원권',
    "CJ통합상품권 10만원": 'CJ 10만원권',
    "CJ통합상품권(10만원권)": 'CJ 10만원권',
    "CJ 상품권 10만원권": 'CJ 10만원권',
    "CJ통합상품권 5만원": 'CJ 5만원권',
    "CJ통합상품권(5만원권)": 'CJ 5만원권',
    "CJ 상품권 1만원권": 'CJ 1만원권',
    "CJ통합상품권 1만원": 'CJ 1만원권',
    "CJ상품권 1만원권": 'CJ 1만원권',
    "CJ통합상품권(1만원권)": 'CJ 1만원권',
    "CJ 외식상품권 5만원권": 'CJ 외식상품권 5만원권',
    "CJ 빕스 외식상품권 5만원": 'CJ 외식상품권 5만원권',
    "CJ외식상품권5만원권": 'CJ 외식상품권 5만원권',
    "CJ외식 상품권(5만원권)": 'CJ 외식상품권 5만원권',
    "국민관광상품권 50만원권": '국민관광상품권 50만원권',
    "국민관광 상품권(50만원권)": '국민관광상품권 50만원권',
    "국민 관광상품권10만원권": '국민관광상품권 10만원권',
    "국민관광상품권10만원권": '국민관광상품권 10만원권',
    "국민관광상품권 10만원권": '국민관광상품권 10만원권',
    "국민관광 상품권(10만원권)": '국민관광상품권 10만원권',
    "국민관광 상품권(5만원권)": '국민관광상품권 5만원권',
    "국민관광상품권 5만원권": '국민관광상품권 5만원권',
    "국민관광상품권 1만원권": '국민관광상품권 1만원권',
    "국민관광 상품권(1만원권)": '국민관광상품권 1만원권',
    "GS주유상품권 10만원": 'GS 주유상품권 10만원권',
    "GS주유상품권(10만원권)": 'GS 주유상품권 10만원권',
    "GS 주유권 5만원권": 'GS 주유상품권 5만원권',
    "GS주유상품권 5만원": 'GS 주유상품권 5만원권',
    "GS주유5만원권": 'GS 주유상품권 5만원권',
    "GS주유상품권(5만원권)": 'GS 주유상품권 5만원권',
    "GS주유권 1만원권": 'GS 주유상품권 1만원권',
    "GS주유상품권 1만원": 'GS 주유상품권 1만원권',
    "GS주유1만원권": 'GS 주유상품권 1만원권',
    "GS주유상품권(1만원권)": 'GS 주유상품권 1만원권',
    "SK주유권 5만원": 'SK 주유상품권 5만원권',
    "SK주유상품권 5만원": 'SK 주유상품권 5만원권',
    "SK주유5만원권": 'SK 주유상품권 5만원권',
    "SK주유상품권(5만원권)": 'SK 주유상품권 5만원권',
    "SK주유권 1만원권": 'SK 주유상품권 1만원권',
    "SK주유상품권 1만원": 'SK 주유상품권 1만원권',
    "SK주유1만원권": 'SK 주유상품권 1만원권',
    "SK주유상품권(1만원권)": 'SK 주유상품권 1만원권',
    "S-oil주유권 5만원권": 'S-Oil 주유상품권 5만원권',
    "S-OIL 5만원권": 'S-Oil 주유상품권 5만원권',
    "S-OIL주유상품권 5만원": 'S-Oil 주유상품권 5만원권',
    "S오일 주유상품권(5만원권)": 'S-Oil 주유상품권 5만원권',
    "S-OIL 1만원권": 'S-Oil 주유상품권 1만원권',
    "S-OIL주유상품권 1만원": 'S-Oil 주유상품권 1만원권',
    "S오일 주유상품권(1만원권)": 'S-Oil 주유상품권 1만원권',
    "현대주유권 5만원": '현대 주유상품권 5만원권',
    "현대오일5만원권": '현대 주유상품권 5만원권',
    "현대오일주유상품권 5만원": '현대 주유상품권 5만원권',
    "현대오일 주유상품권(5만원권)": '현대 주유상품권 5만원권',
    "현대오일1만원권": '현대 주유상품권 1만원권',
    "현대오일주유상품권 1만원": '현대 주유상품권 1만원권',
    "현대오일 주유상품권(1만원권)": '현대 주유상품권 1만원권',
    "하나투어 여행상품권": '하나투어 여행상품권 10만원권',
    "하나투어 여행 상품권 10만원": '하나투어 여행상품권 10만원권',
    "하나투어10만원권": '하나투어 여행상품권 10만원권',
    "하나투어 상품권": '하나투어 여행상품권 10만원권',
    "모두투어 여행상품권": '모두투어 여행상품권 10만원권',
    "모두투어 여행 상품권": '모두투어 여행상품권 10만원권',
    "모두투어10만원권": '모두투어 여행상품권 10만원권',
    "모두투어 상품권": '모두투어 여행상품권 10만원권',
    "제일모직상품권10만원권(면세점가능)": '제일모직상품권 10만원권',
    "제일모직상품권10만원권": '제일모직상품권 10만원권',
    "제일모직상품권10만": '제일모직상품권 10만원권',
    "제일모직 상품권(10만원권)": '제일모직상품권 10만원권',
    "LG패션 상품권 10만원권": 'LG패션상품권 10만원권',
    "LG패션상품권10만원권": 'LG패션상품권 10만원권',
    "LF LG 패션상품권": 'LG패션상품권 10만원권',
    "에스콰이어10만원권": '에스콰이어 10만원권',
    "워커힐호텔상품권10만원권": '워커힐호텔 10만원권',
    "워커힐 상품권(10만원권)": '워커힐호텔 10만원권',
    "토다이 10만원권": '토다이 10만원권',
    "토다이상품권 10만원": '토다이 10만원권',
    "토다이 상품권(10만원권)": '토다이 10만원권',
    "해피21_10만원권": '해피21 10만원권',
    "두타 상품권": '두타몰 10만원권',
}
