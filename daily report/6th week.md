#6th Week

### 2021.10.12.Tue

1. 오전까지 수집된 제품 객체 정보 19134개 공유
   - df_glowpick_prd_info_v3.csv
2. 이번주에 수집된 제품 객체 수집 진행 상황 보고
   - 현재까지 수집 완료된 제품 46126개이고, 1798개 상품 수집 더 필요. 내일 오전까지 수집 완료 예상.
3. df_v4_review update
4. naver price comparison(네이버 가격 비교) page 브랜드 검색 크롤링 코드



### 2021.10.13.Wed
1. 글로우픽 내 등록상품_ 전체 데이터 수집 완료
2. 수집 완료된 제품 객체 정보 dataframe 전처리 진행
  - 가격 미정, 용량 미정, 프로필 미등록 회원 등 nan값 처리
  - 리뷰가 중복된 제품 카테고라이징 [check_duplicates_review.ipynb](https://github.com/eun61n00/Internship-2021F/blob/master/glowpick_scraping/check_dulicates_review.ipynb)


### 2021.10.14.Thu
1. 전체 제품 객체 정보 수집 데이터 전처리 진행
  - 리뷰 유실된 제품들 리뷰만 재수집
  - bridge table의 제품 정렬 순서로 sorting
  - nan값인 브랜드 id와 브랜드 link값 채우기


### 2021.10.15.Fri
1. 전체 제품 객체 정보 데이터 최종 퀄리티 체크
2. DB 업로드 [DB_upload_glowpick_prd_info.ipynb](https://github.com/eun61n00/Internship-2021F/edit/master/README.md)
  - column size 문제로 두개의 table로 분리하여 업로드 (제품 정보 / 리뷰)
3. 네이버 뷰티윈도우 제품과 글로우픽 제품 수기 매핑 진행
