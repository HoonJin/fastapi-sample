INSERT INTO `voucher_sellers` (`name`, `url`, `tel`, `address`, `created_at`, `updated_at`)
VALUES
('우천사', 'http://www.wooticket.com', '02-7790-8589', '(우) 04535 서울시 중구 남대문로 64-1(서울시 중구 명동 2가 88-5번지) 프린스 빌딩 1층 101호', NOW(), NOW()),
('모두티켓', 'http://www.modooticket.co.kr', '02-773-8989', '서울특별시 중구 명동2길 16 진주빌딩 1층', NOW(), NOW()),
('상품권가게', 'https://www.ticketstore.co.kr', '031-385-8949', '경기도 안양시 동안구 동안로120 1층 109호(호계동,올림픽스포츠센터)', NOW(), NOW()),
('우현상품권', 'https://wooh.co.kr', '02-778-8504', '서울특별시 중구 남대문로 60, 1층(명동2가)', NOW(), NOW())
;


INSERT INTO `vouchers` (`name`, `par_value`, `category`, `created_at`, `updated_at`)
VALUES
('롯데백화점 50만원권', 500000.00, '백화점', NOW(), NOW()),
('롯데백화점 30만원권', 300000.00, '백화점', NOW(), NOW()),
('롯데백화점 10만원권', 100000.00, '백화점', NOW(), NOW()),
('롯데백화점 5만원권',  50000.00, '백화점', NOW(), NOW()),
('롯데백화점 3만원권',  30000.00, '백화점', NOW(), NOW()),
('롯데백화점 1만원권',  10000.00, '백화점', NOW(), NOW()),
('신세계백화점 50만원권', 500000.00, '백화점', NOW(), NOW()),
('신세계백화점 30만원권', 300000.00, '백화점', NOW(), NOW()),
('신세계백화점 10만원권', 100000.00, '백화점', NOW(), NOW()),
('신세계백화점 5만원권', 50000.00, '백화점', NOW(), NOW()),
('신세계백화점 1만원권', 10000.00, '백화점', NOW(), NOW()),
('신세계백화점 5천원권', 5000.00, '백화점', NOW(), NOW()),
('현대백화점 50만원권', 500000.00, '백화점', NOW(), NOW()),
('현대백화점 10만원권', 100000.00, '백화점', NOW(), NOW()),
('현대백화점 5만원권', 50000.00, '백화점', NOW(), NOW()),
('현대백화점 1만원권', 10000.00, '백화점', NOW(), NOW()),
('AK플라자 50만원권', 500000.00, '백화점', NOW(), NOW()),
('AK플라자 30만원권', 300000.00, '백화점', NOW(), NOW()),
('AK플라자 10만원권', 100000.00, '백화점', NOW(), NOW()),
('AK플라자 5만원권', 50000.00, '백화점', NOW(), NOW()),
('AK플라자 1만원권', 10000.00, '백화점', NOW(), NOW()),
('삼성상품권 10만원권', 100000.00, '백화점', NOW(), NOW()),
('삼성상품권 5만원권', 50000.00, '백화점', NOW(), NOW()),
('이랜드 10만원권', 100000.00, '백화점', NOW(), NOW()),
('갤러리아백화점 50만원권', 500000.00, '백화점', NOW(), NOW()),
('갤러리아백화점 10만원권', 100000.00, '백화점', NOW(), NOW()),
('갤러리아백화점 5만원권', 50000.00, '백화점', NOW(), NOW()),
('갤러리아백화점 1만원권', 10000.00, '백화점', NOW(), NOW()),
('그랜드백화점 10만원권', 100000.00, '백화점', NOW(), NOW()),
('메가마트 10만원권', 100000.00, '백화점', NOW(), NOW()),
('아이파크 10만원권', 100000.00, '백화점', NOW(), NOW()),
('아이파크 1만원권', 10000.00, '백화점', NOW(), NOW()),
('롯데 스페셜카드 50만원권', 500000.00, '기프트카드', NOW(), NOW()),
('롯데 스페셜카드 10만원권', 100000.00, '기프트카드', NOW(), NOW()),
('삼성 기프트카드 50만원권', 500000.00, '기프트카드', NOW(), NOW()),
('신한 기프트카드 50만원권', 500000.00, '기프트카드', NOW(), NOW()),
('현대 기프트카드 50만원권', 500000.00, '기프트카드', NOW(), NOW()),
('국민 기프트카드 50만원권', 500000.00, '기프트카드', NOW(), NOW()),
('KEB하나 기프트카드 50만원권', 500000.00, '기프트카드', NOW(), NOW()),
('BC 기프트카드 50만원권', 500000.00, '기프트카드', NOW(), NOW()),
('롯데 기프트카드 50만원권', 500000.00, '기프트카드', NOW(), NOW()),
('기프트카드 30만원권', 300000.00, '기프트카드', NOW(), NOW()),
('기프트카드 10만원권', 100000.00, '기프트카드', NOW(), NOW()),
('기프트카드 5만원권', 50000.00, '기프트카드', NOW(), NOW()),
('농협 기프트카드 50만원권', 500000.00, '기프트카드', NOW(), NOW()),
('농협 기프트카드 30만원권', 300000.00, '기프트카드', NOW(), NOW()),
('농협 기프트카드 10만원권', 100000.00, '기프트카드', NOW(), NOW()),
('홈플러스(디지털) 50만원권', 500000.00, '할인마트', NOW(), NOW()),
('홈플러스 30만원권', 300000.00, '할인마트', NOW(), NOW()),
('홈플러스 10만원권', 100000.00, '할인마트', NOW(), NOW()),
('홈플러스 5만원권', 50000.00, '할인마트', NOW(), NOW()),
('홈플러스 1만원권', 10000.00, '할인마트', NOW(), NOW()),
('농협 하나로상품권 10만원권', 100000.00, '할인마트', NOW(), NOW()),
('농협 하나로상품권 5만원권', 50000.00, '할인마트', NOW(), NOW()),
('농협 하나로상품권 1만원권', 10000.00, '할인마트', NOW(), NOW()),
('해피머니 문화상품권 1만원권', 10000.00, '도서/문화', NOW(), NOW()),
('해피머니 문화상품권 5천원권', 5000.00, '도서/문화', NOW(), NOW()),
('문화상품권 5만원권', 50000.00, '도서/문화', NOW(), NOW()),
('문화상품권 1만원권', 10000.00, '도서/문화', NOW(), NOW()),
('문화상품권 5천원권', 5000.00, '도서/문화', NOW(), NOW()),
('도서문화상품권 1만원권', 10000.00, '도서/문화', NOW(), NOW()),
('도서문화상품권 5천원권', 5000.00, '도서/문화', NOW(), NOW()),
('CJ 10만원권', 100000.00, '쇼핑', NOW(), NOW()),
('CJ 5만원권', 50000.00, '쇼핑', NOW(), NOW()),
('CJ 1만원권', 10000.00, '쇼핑', NOW(), NOW()),
('국민관광상품권 50만원권', 500000.00, '관광/여행', NOW(), NOW()),
('국민관광상품권 10만원권', 100000.00, '관광/여행', NOW(), NOW()),
('국민관광상품권 5만원권', 50000.00, '관광/여행', NOW(), NOW()),
('국민관광상품권 1만원권', 10000.00, '관광/여행', NOW(), NOW()),
('하나투어 여행상품권 10만원권', 100000.00, '관광/여행', NOW(), NOW()),
('모두투어 여행상품권 10만원권', 100000.00, '관광/여행', NOW(), NOW()),
('GS 주유상품권 10만원권', 100000.00, '주유', NOW(), NOW()),
('GS 주유상품권 5만원권', 50000.00, '주유', NOW(), NOW()),
('GS 주유상품권 1만원권', 10000.00, '주유', NOW(), NOW()),
('SK 주유상품권 1만원권', 10000.00, '주유', NOW(), NOW()),
('SK 주유상품권 5만원권', 50000.00, '주유', NOW(), NOW()),
('S-Oil 주유상품권 5만원권', 50000.00, '주유', NOW(), NOW()),
('S-Oil 주유상품권 1만원권', 10000.00, '주유', NOW(), NOW()),
('현대 주유상품권 5만원권', 50000.00, '주유', NOW(), NOW()),
('현대 주유상품권 1만원권', 10000.00, '주유', NOW(), NOW()),
('제일모직상품권 10만원권', 100000.00, '패션/의류', NOW(), NOW()),
('LG패션상품권 10만원권', 100000.00, '패션/의류', NOW(), NOW()),
('에스콰이어 10만원권', 100000.00, '패션/의류', NOW(), NOW()),
('두타몰 10만원권', 100000.00, '패션/의류', NOW(), NOW()),
('금강제화 10만원권', 100000.00, '패션/의류', NOW(), NOW()),
('금강제화 7만원권', 70000.00, '패션/의류', NOW(), NOW()),
('금강제화 5만원권', 500000.00, '패션/의류', NOW(), NOW()),
('롯데호텔 10만원권', 100000.00, '호텔/외식', NOW(), NOW()),
('워커힐호텔 10만원권', 100000.00, '호텔/외식', NOW(), NOW()),
('CJ 외식상품권 5만원권', 50000.00, '호텔/외식', NOW(), NOW()),
('토다이 10만원권', 100000.00, '호텔/외식', NOW(), NOW()),
('해피21 10만원권', 100000.00, '호텔/외식', NOW(), NOW())
;
