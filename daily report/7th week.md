# 7th Week

### 2021.10.18.Mon
1. 제품 객체 정보 리뷰 데이터는 하나의 리뷰가 하나의 row에 들어가도록 reshape : [glowpick_review_dataframe.ipynb](https://github.com/eun61n00/Internship-2021F/blob/master/glowpick_scraping/glowpick_review_dataframe.ipynb)
2. DB 업로드 최종 완료
3. “naver beauty product info” 취급 브랜드 외 브랜드 기준 상품 url 취합 후 이미지 수집: [get_img_src.ipynb](https://github.com/eun61n00/Internship-2021F/blob/master/glowpick_scraping/get_img_src.ipynb), [get_img.ipynb](https://github.com/eun61n00/Internship-2021F/blob/master/glowpick_scraping/get_img.ipynb)

### 2021.10.19.Thu
1. 전날 수집된 이미지의 브랜드 idx, 제품 idx 파악 후, 아직 수집되지 않은 이미지 src와 이미지 수집 계속 진행
2. 네이버 뷰티윈도우와 글로우픽 제품 수기 매핑 진행

### 2021.10.20.Wed
1. 글로우픽 제품 이미지 형식 gif로 변경 -> 이미지 수집 코드 변경(gif 하나의 프레임을 png로 변경)([get_img.ipynb](https://github.com/eun61n00/Internship-2021F/blob/master/glowpick_scraping/get_img.ipynb))
2. 네이버 뷰티윈도우 제품과 글로우픽 제품 수기 매핑 진행 (700-950)

### 2021.10.21.Thu
1. 네이버 뷰티윈도우 제품과 글로우픽 제품 수기 매핑 진행 (951-1534)

### 2021.10.22.Fri
1. 네이버 뷰티윈도우와 글로우픽 제품 수기 매핑 담당 모두 완료 (1535-1678) + 미완료 담당 이관받아 진행 (3150-3335)
2. 신세계몰 먼데이문 브랜드 정보 수집 (브랜드 이름, 브랜드 id, 브랜드 내 제품 개수) (제품 개수를 선수집하여 추후 제품 객체 수집 시 유효한 개수 파악 가능)
    
    [ssg_monm_brand_crawling.ipynb](https://github.com/eun61n00/Internship-2021F/blob/master/sgg_monm/ssg_monm_brand_crawling.ipynb)
3. 신세계몰 먼데이문 브랜드 별 제품 id 수집 

    [ssg_monm_product_id_crawling.ipynb](https://github.com/eun61n00/Internship-2021F/blob/master/sgg_monm/ssg_monm_product_id_crawling.ipynb)
