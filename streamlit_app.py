<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>한국 뮤지컬 대백과</title>
    <style>
        /* 기본 스타일 및 폰트 설정 */
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');

        body {
            font-family: 'Noto Sans KR', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
            color: #343a40;
        }

        /* 전체 레이아웃을 감싸는 컨테이너 */
        .container {
            max-width: 900px;
            margin: 20px auto;
            padding: 20px;
        }

        /* 헤더 스타일 */
        header {
            text-align: center;
            margin-bottom: 40px;
        }

        header h1 {
            font-size: 2.8em;
            color: #1a3a64;
            margin-bottom: 10px;
        }

        /* 검색창 스타일 */
        #search-box {
            width: 100%;
            padding: 12px 20px;
            margin-bottom: 40px;
            box-sizing: border-box;
            border: 2px solid #ced4da;
            border-radius: 25px;
            font-size: 1em;
            transition: border-color 0.3s;
        }

        #search-box:focus {
            border-color: #495057;
            outline: none;
        }

        /* 각 뮤지컬 정보를 담는 카드 스타일 */
        .musical-card {
            background: #ffffff;
            margin-bottom: 30px;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
            overflow: hidden;
        }

        .musical-card h2 {
            font-size: 1.8em;
            color: #0056b3;
            margin-top: 0;
            border-bottom: 2px solid #e9ecef;
            padding-bottom: 10px;
        }

        .musical-card h3 {
            font-size: 1.2em;
            color: #343a40;
            margin-top: 25px;
            margin-bottom: 15px;
            position: relative;
            padding-left: 15px;
        }
        
        .musical-card h3::before {
            content: '';
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 5px;
            height: 20px;
            background-color: #0056b3;
            border-radius: 3px;
        }

        /* 줄거리 및 캐스팅 정보 스타일 */
        .musical-card p {
            margin-bottom: 15px;
        }
        
        .cast-history {
            background-color: #f1f3f5;
            padding: 20px;
            border-radius: 8px;
            margin-top: 10px;
        }

        .role-cast {
            margin-bottom: 10px;
        }

        .role-cast strong {
            display: block;
            color: #495057;
            margin-bottom: 5px;
        }

        .role-cast span {
            font-size: 0.95em;
            color: #6c757d;
        }
        
    </style>
</head>
<body>

    <div class="container">
        <header>
            <h1>한국 뮤지컬 대백과</h1>
            <p>대한민국을 빛낸 뮤지컬과 배우들의 역사를 한눈에 확인하세요.</p>
        </header>

        <input type="text" id="search-box" placeholder="뮤지컬 제목을 검색하세요...">

        <div id="musical-list">

            <!-- 뮤지컬 목록 시작 -->
            <div class="musical-card"><h2>광화문 연가</h2><h3>줄거리</h3><p>죽음을 앞둔 주인공 '명우'가 마지막 1분을 앞두고 '월하'와 함께 떠나는 시간 여행을 통해 자신의 젊은 날의 사랑과 우정을 되돌아보는 이야기입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>중년 명우:</strong><span>안재욱, 이건명, 강필석, 윤도현, 차지연</span></div><div class="role-cast"><strong>월하:</strong><span>구원영, 김호영, 이석훈, 정성화, 차지연</span></div><div class="role-cast"><strong>젊은 명우:</strong><span>허도영, 김성규, 박강현, 이찬동</span></div></div></div>
            <div class="musical-card"><h2>그날들</h2><h3>줄거리</h3><p>故 김광석의 노래들로 이루어진 주크박스 뮤지컬. 청와대 경호실을 배경으로 20년 전 사라진 '그녀'와 경호원의 미스터리한 사건을 그립니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>정학:</strong><span>유준상, 이건명, 최재웅, 오만석, 엄기준, 지창욱</span></div><div class="role-cast"><strong>무영:</strong><span>지창욱, 오종혁, 온주완, 양요섭, 규현, 남우현, 윤두준</span></div><div class="role-cast"><strong>그녀:</strong><span>김지현, 신다은, 루나, 방민아, 효정</span></div></div></div>
            <div class="musical-card"><h2>노트르담 드 파리</h2><h3>줄거리</h3><p>15세기 파리, 추악한 외모의 꼽추 종지기 '콰지모도'와 아름다운 집시 여인 '에스메랄다', 그리고 그녀를 둘러싼 세 남자의 비극적인 사랑과 숙명을 그린 작품입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>콰지모도:</strong><span>윤형렬, 홍광호, 케이윌, 정성화, 마이클리</span></div><div class="role-cast"><strong>에스메랄다:</strong><span>바다, 윤공주, 차지연, 전나영, 유리아</span></div><div class="role-cast"><strong>그랭구와르:</strong><span>박은태, 마이클리, 정동하, 이충주, 조휘</span></div><div class="role-cast"><strong>프롤로:</strong><span>서범석, 민영기, 최민철, 이정열</span></div></div></div>
            <div class="musical-card"><h2>데스노트</h2><h3>줄거리</h3><p>이름이 적히면 죽는 '데스노트'를 손에 넣은 천재 고등학생 라이토와 명탐정 엘(L)의 치열한 두뇌 싸움을 그린, 동명 만화 원작의 뮤지컬입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>야가미 라이토:</strong><span>홍광호, 고은성, 박혜나, 김성철</span></div><div class="role-cast"><strong>엘(L):</strong><span>김준수, 김성철, 박혜나, 서경수</span></div><div class="role-cast"><strong>렘:</strong><span>박혜나, 김선영, 장은아</span></div><div class="role-cast"><strong>류크:</strong><span>강홍석, 서경수, 장지후</span></div><div class="role-cast"><strong>아마네 미사:</strong><span>정선아, 벤, 케이, 류인아</span></div></div></div>
            <div class="musical-card"><h2>드라큘라</h2><h3>줄거리</h3><p>수백 년 동안 한 여인만을 사랑해 온 드라큘라 백작의 이야기를 다룹니다. 거부할 수 없는 매력의 뱀파이어와 그를 둘러싼 인물들의 운명적인 사랑과 갈등을 그립니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>드라큘라:</strong><span>김준수, 전동석, 신성록, 류정한, 박은석</span></div><div class="role-cast"><strong>미나:</strong><span>조정은, 임혜영, 린아, 아이비, 박지연</span></div><div class="role-cast"><strong>반 헬싱:</strong><span>강태을, 손준호, 유준상, 박은석</span></div></div></div>
            <div class="musical-card"><h2>라흐마니노프</h2><h3>줄거리</h3><p>신경쇠약으로 절망에 빠진 천재 작곡가 '라흐마니노프'가 정신의학자 '니콜라이 달' 박사를 만나 상처를 치유하고 재기하는 과정을 그린 2인극 뮤지컬입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>라흐마니노프:</strong><span>박유덕, 이해준, 정동화, 박규원</span></div><div class="role-cast"><strong>니콜라이 달:</strong><span>유성재, 정민, 임병근</span></div></div></div>
            <div class="musical-card"><h2>레드북</h2><h3>줄거리</h3><p>19세기 영국, 보수적인 시대에 맞서 자신의 욕망과 삶을 솔직하게 표현하는 여성 작가 '안나'의 유쾌하고 감동적인 성장 드라마입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>안나:</strong><span>옥주현, 아이비, 차지연, 유리아, 박진주</span></div><div class="role-cast"><strong>브라운:</strong><span>박은석, 이상이, 송원근, 신성민</span></div></div></div>
            <div class="musical-card"><h2>레미제라블</h2><h3>줄거리</h3><p>빵 한 조각을 훔친 죄로 19년간 감옥살이를 한 장발장의 기구한 인생을 통해 인간의 존엄성과 사랑, 용서를 다룬 빅토르 위고 원작의 대서사시입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>장발장:</strong><span>정성화, 양준모, 민우혁, 최재림</span></div><div class="role-cast"><strong>자베르:</strong><span>문종원, 김우형, 카이, 김준현</span></div><div class="role-cast"><strong>판틴:</strong><span>조정은, 차지연, 린아</span></div><div class="role-cast"><strong>코제트:</strong><span>이지수, 이하경, 최현주</span></div><div class="role-cast"><strong>마리우스:</strong><span>조상웅, 박지연, 윤소호</span></div></div></div>
            <div class="musical-card"><h2>레베카</h2><h3>줄거리</h3><p>죽은 전 부인 '레베카'의 그림자가 드리운 맨덜리 저택에 새로 들어온 '나(I)'가 집사 '댄버스 부인'과 맞서며 사랑과 자아를 찾아가는 미스터리 스릴러입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>막심 드 윈터:</strong><span>류정한, 민영기, 엄기준, 송창의, 카이, 신성록</span></div><div class="role-cast"><strong>댄버스 부인:</strong><span>옥주현, 신영숙, 차지연, 장은아, 리사</span></div><div class="role-cast"><strong>나(I):</strong><span>임혜영, 김보경, 송상은, 루나, 이지혜, 박지연</span></div></div></div>
            <div class="musical-card"><h2>렌트</h2><h3>줄거리</h3><p>1990년대 뉴욕 이스트 빌리지에 모여 사는 가난한 예술가들의 꿈과 열정, 사랑과 우정, 그리고 삶의 희망에 대한 이야기입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>로저:</strong><span>장지후, 정원영, 조형균</span></div><div class="role-cast"><strong>마크:</strong><span>배두훈, 정원영, 이충주</span></div><div class="role-cast"><strong>미미:</strong><span>아이비, 김수하, 전나영</span></div><div class="role-cast"><strong>엔젤:</strong><span>김호영, 조권, 렌</span></div></div></div>
            <div class="musical-card"><h2>마리 퀴리</h2><h3>줄거리</h3><p>최초로 노벨상을 두 번 수상한 위대한 과학자 '마리 퀴리'의 삶을 다룹니다. 자신의 연구가 초래한 비극에 맞서며 진실을 찾아가는 그녀의 고뇌와 신념을 그립니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>마리 퀴리:</strong><span>김소향, 옥주현, 리사</span></div><div class="role-cast"><strong>안느:</strong><span>김히어라, 이봄소리, 효정</span></div><div class="role-cast"><strong>피에르 퀴리:</strong><span>김찬호, 박영수, 임별</span></div></div></div>
            <div class="musical-card"><h2>마타하리</h2><h3>줄거리</h3><p>제1차 세계대전 당시 이중 스파이 혐의로 총살당한 무희 '마타하리'의 실화를 바탕으로, 화려한 삶 뒤에 숨겨진 그녀의 비극적인 사랑과 운명을 그립니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>마타하리:</strong><span>옥주현, 차지연, 김소향</span></div><div class="role-cast"><strong>아르망:</strong><span>엄기준, 송창의, 정택운(레오), 임슬옹</span></div><div class="role-cast"><strong>라두 대령:</strong><span>류정한, 김준현, 신성록</span></div></div></div>
            <div class="musical-card"><h2>맘마미아!</h2><h3>줄거리</h3><p>그리스의 작은 섬에서 엄마 '도나'와 사는 딸 '소피'가 자신의 결혼식을 앞두고 아빠일 가능성이 있는 세 남자를 초대하며 벌어지는 유쾌한 소동을 그립니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>도나:</strong><span>최정원, 신영숙, 김선영</span></div><div class="role-cast"><strong>소피:</strong><span>박지연, 서현, 루나, 김금나</span></div><div class="role-cast"><strong>타냐:</strong><span>전수경, 김영주, 홍지민</span></div><div class="role-cast"><strong>로지:</strong><span>이경미, 박준면, 오기쁨</span></div></div></div>
            <div class="musical-card"><h2>모차르트!</h2><h3>줄거리</h3><p>천재 음악가 모차르트의 삶을 그리고 있지만, 그의 천재성을 상징하는 아이 '아마데'와의 갈등을 통해 자유를 갈망했던 인간 '볼프강'의 고뇌를 조명합니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>볼프강 모차르트:</strong><span>박효신, 김준수, 박은태, 전동석, 규현, 수호, 김희재</span></div><div class="role-cast"><strong>콜로레도 대주교:</strong><span>민영기, 김준현, 손준호</span></div><div class="role-cast"><strong>콘스탄체 베버:</strong><span>정선아, 차지연, 김소향, 린아</span></div></div></div>
            <div class="musical-card"><h2>몬테크리스토</h2><h3>줄거리</h3><p>촉망받는 젊은 선원 '에드몬드 단테스'가 친구와 주변 사람들의 음모로 억울한 누명을 쓰고 악명 높은 감옥에 갇힙니다. 극적으로 탈출한 그는 '몬테크리스토 백작'이라는 이름으로 돌아와 자신을 배신한 이들에게 통쾌한 복수를 시작합니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>에드몬드 단테스/몬테크리스토 백작:</strong><span>류정한, 엄기준, 신성록, 카이, 서인국, 고은성, 김성철, 이규형</span></div><div class="role-cast"><strong>메르세데스:</strong><span>옥주현, 차지연, 린아, 조정은, 선민, 이지혜</span></div><div class="role-cast"><strong>몬데고:</strong><span>최민철, 김승대, 강태을, 이상현</span></div></div></div>
            <div class="musical-card"><h2>명성황후</h2><h3>줄거리</h3><p>조선의 마지막 국모, 명성황후의 비극적인 삶과 일본의 만행에 맞서 나라를 지키려 했던 그녀의 강인한 모습을 그린 대한민국 대표 창작 뮤지컬입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>명성황후:</strong><span>이태원, 김소현, 신영숙, 차지연, 김선영</span></div><div class="role-cast"><strong>고종:</strong><span>박완, 강필석, 손준호</span></div><div class="role-cast"><strong>홍계훈:</strong><span>박송권, 최우혁, 윤형렬</span></div></div></div>
            <div class="musical-card"><h2>베르테르</h2><h3>줄거리</h3><p>괴테의 소설 '젊은 베르테르의 슬픔'을 원작으로, '롯데'를 향한 '베르테르'의 순수하고도 열정적인 사랑과 그로 인한 깊은 고뇌를 서정적인 음악으로 풀어냅니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>베르테르:</strong><span>조승우, 엄기준, 규현, 카이, 유연석, 나현우</span></div><div class="role-cast"><strong>롯데:</strong><span>이지혜, 김예원, 이지수</span></div><div class="role-cast"><strong>알베르트:</strong><span>이상현, 박은석, 김성철</span></div></div></div>
            <div class="musical-card"><h2>벤허</h2><h3>줄거리</h3><p>귀족 가문의 자제였던 '유다 벤허'가 친구의 배신으로 노예로 전락한 후, 역경을 딛고 복수에 나서는 과정을 그린 장대한 스케일의 창작 뮤지컬입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>유다 벤허:</strong><span>유준상, 박은태, 카이, 신성록, 규현</span></div><div class="role-cast"><strong>메셀라:</strong><span>박민성, 이지훈, 서경수</span></div><div class="role-cast"><strong>에스더:</strong><span>윤공주, 아이비, 선민</span></div></div></div>
            <div class="musical-card"><h2>빌리 엘리어트</h2><h3>줄거리</h3><p>1980년대 영국, 파업 중인 탄광촌을 배경으로, 권투보다 발레를 사랑한 소년 '빌리'가 꿈을 향해 나아가는 감동적인 성장 이야기입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>빌리:</strong><span>김현준, 성지환, 심현서, 천우진, 이우진, 주현준</span></div><div class="role-cast"><strong>아빠:</strong><span>김갑수, 최명경, 조정근</span></div></div></div>
            <div class="musical-card"><h2>빨래</h2><h3>줄거리</h3><p>서울의 한 달동네를 배경으로, 서점에서 일하는 '나영'과 몽골 출신 이주노동자 '솔롱고'를 비롯한 서민들의 팍팍하지만 따뜻한 삶의 이야기를 그립니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>서나영:</strong><span>홍지희, 강연정, 김주연</span></div><div class="role-cast"><strong>솔롱고:</strong><span>홍광호, 임창정, 이정은</span></div></div></div>
            <div class="musical-card"><h2>서편제</h2><h3>줄거리</h3><p>이청준의 동명 소설을 원작으로, 소리꾼 아버지 '유봉'과 그의 딸 '송화', 아들 '동호'의 한과 예술혼이 담긴 삶을 한국적인 정서와 음악으로 풀어낸 작품입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>송화:</strong><span>차지연, 이자람, 장은아, 이소연</span></div><div class="role-cast"><strong>동호:</strong><span>박영수, 김재범, 서범석</span></div><div class="role-cast"><strong>유봉:</strong><span>이정열, 서범석, 양준모</span></div></div></div>
            <div class="musical-card"><h2>스위니토드</h2><h3>줄거리</h3><p>19세기 런던, 억울한 옥살이를 하고 돌아온 이발사 '벤자민 바커'가 '스위니 토드'로 이름을 바꾸고, 자신을 불행에 빠뜨린 자들에게 잔혹한 복수를 하는 이야기입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>스위니 토드:</strong><span>조승우, 류정한, 홍광호, 박은태, 강필석, 신성록</span></div><div class="role-cast"><strong>러빗 부인:</strong><span>옥주현, 전미도, 김지현, 린아, 이지혜</span></div><div class="role-cast"><strong>터핀 판사:</strong><span>김도형, 서영주, 박인배</span></div></div></div>
            <div class="musical-card"><h2>스토리 오브 마이 라이프</h2><h3>줄거리</h3><p>베스트셀러 작가 '토마스'가 어린 시절 가장 친한 친구였던 '앨빈'의 갑작스러운 죽음을 계기로, 그와 함께했던 추억을 되짚으며 잊고 있던 영감을 되찾는 2인극입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>토마스 위버:</strong><span>이석준, 고영빈, 강필석, 김종구, 조성윤</span></div><div class="role-cast"><strong>앨빈 켈비:</strong><span>이창용, 정동화, 김재범, 정원영</span></div></div></div>
            <div class="musical-card"><h2>시카고</h2><h3>줄거리</h3><p>1920년대 재즈 시대의 시카고, 살인을 저지르고도 스타가 되길 꿈꾸는 '록시 하트'와 '벨마 켈리'의 이야기를 통해 당시 사회의 부조리와 허영을 풍자합니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>벨마 켈리:</strong><span>최정원, 윤공주, 박칼린</span></div><div class="role-cast"><strong>록시 하트:</strong><span>아이비, 티파니 영, 민경아, 옥주현</span></div><div class="role-cast"><strong>빌리 플린:</strong><span>박건형, 최재림, 남경주</span></div></div></div>
            <div class="musical-card"><h2>아이다</h2><h3>줄거리</h3><p>고대 이집트를 배경으로, 적국인 누비아의 공주 '아이다'와 이집트 장군 '라다메스', 그리고 이집트 공주 '암네리스'의 엇갈린 사랑과 운명을 다룹니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>아이다:</strong><span>옥주현, 차지연, 윤공주, 전나영</span></div><div class="role-cast"><strong>라다메스:</strong><span>김우형, 민우혁, 최재림</span></div><div class="role-cast"><strong>암네리스:</strong><span>정선아, 아이비, 김수하</span></div></div></div>
            <div class="musical-card"><h2>아몬드</h2><h3>줄거리</h3><p>감정을 느끼지 못하는 소년 '윤재'가 타인과 관계를 맺으며 세상을 배워나가는 과정을 그린 동명의 베스트셀러 소설 원작 뮤지컬입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><p>2025년 9월 초연 예정으로 캐스팅 정보는 추후 공개됩니다.</p></div></div>
            <div class="musical-card"><h2>어쩌면 해피엔딩</h2><h3>줄거리</h3><p>가까운 미래, 인간을 돕기 위해 만들어졌지만 구형이 되어 버려진 로봇 '올리버'와 '클레어'가 만나 사랑과 삶의 의미를 배워가는 따뜻하고 서정적인 이야기입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>올리버:</strong><span>정문성, 전성우, 신성민, 임준혁</span></div><div class="role-cast"><strong>클레어:</strong><span>전미도, 박지연, 강혜인, 한재아</span></div></div></div>
            <div class="musical-card"><h2>엑스칼리버</h2><h3>줄거리</h3><p>왕의 운명을 타고난 청년 '아더'가 성검 엑스칼리버를 뽑고 혼란스러운 고대 영국을 지켜내는 영웅으로 성장해가는 과정을 그린 대작입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>아더:</strong><span>카이, 김준수, 서은광, 도겸, 김성규</span></div><div class="role-cast"><strong>랜슬럿:</strong><span>이지훈, 에녹, 강태을</span></div><div class="role-cast"><strong>모르가나:</strong><span>신영숙, 장은아, 옥주현</span></div><div class="role-cast"><strong>기네비어:</strong><span>김소향, 케이, 민경아</span></div></div></div>
            <div class="musical-card"><h2>엘리자벳</h2><h3>줄거리</h3><p>오스트리아 황후 '엘리자벳'의 일대기에 '죽음(Der Tod)'이라는 판타지적 요소를 더해, 자유를 갈망했던 그녀의 삶을 드라마틱하게 그린 작품입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>엘리자벳:</strong><span>옥주현, 김소현, 신영숙, 이지혜, 김선영</span></div><div class="role-cast"><strong>죽음(토드):</strong><span>김준수, 박효신, 전동석, 박형식, 정택운(레오), 신성록</span></div><div class="role-cast"><strong>루케니:</strong><span>박은태, 이지훈, 강태을, 김수용</span></div></div></div>
            <div class="musical-card"><h2>영웅</h2><h3>줄거리</h3><p>1909년, 하얼빈역에서 이토 히로부미를 저격한 안중근 의사의 마지막 1년을 그린 대한민국 대표 창작 뮤지컬입니다. 조국 독립을 위해 목숨을 바친 안중근의 인간적인 고뇌와 숭고한 정신을 장엄하고 감동적인 음악으로 담아냈습니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>안중근:</strong><span>정성화, 양준모, 민우혁, 류정한, 신성록</span></div><div class="role-cast"><strong>이토 히로부미:</strong><span>김도형, 서영주, 이정열</span></div><div class="role-cast"><strong>설희:</strong><span>정재은, 린지, 리사</span></div></div></div>
            <div class="musical-card"><h2>오페라의 유령</h2><h3>줄거리</h3><p>파리 오페라 하우스 지하에 숨어 사는 천재 음악가 '유령'과 프리마돈나 '크리스틴', 그리고 귀족 '라울'의 비극적이고 아름다운 사랑 이야기입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>유령(팬텀):</strong><span>윤영석, 홍광호, 박효신, 조승우, 최재림, 전동석</span></div><div class="role-cast"><strong>크리스틴:</strong><span>김소현, 이혜경, 임혜영, 손지수, 송은혜</span></div><div class="role-cast"><strong>라울:</strong><span>류정한, 정상윤, 송원근, 황건하</span></div></div></div>
            <div class="musical-card"><h2>웃는 남자</h2><h3>줄거리</h3><p>17세기 영국, 찢어진 입을 가진 기형적인 외모의 '그윈플렌'이 유랑극단에서 광대로 살아가며 겪는 사랑과 사회 부조리에 대한 이야기입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>그윈플렌:</strong><span>박효신, 박강현, 수호, 박은태, 규현</span></div><div class="role-cast"><strong>우르수스:</strong><span>정성화, 양준모, 민영기</span></div><div class="role-cast"><strong>데아:</strong><span>민경아, 이수빈, 양서윤</span></div><div class="role-cast"><strong>조시아나 여공작:</strong><span>신영숙, 옥주현, 김소향</span></div></div></div>
            <div class="musical-card"><h2>위키드</h2><h3>줄거리</h3><p>도로시가 오즈에 오기 전, 초록 마녀 엘파바와 금발 마녀 글린다의 숨겨진 우정과 성장을 통해 선과 악의 편견을 깨는 감동적인 이야기입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>엘파바:</strong><span>옥주현, 박혜나, 차지연, 손승연</span></div><div class="role-cast"><strong>글린다:</strong><span>정선아, 김보경, 아이비, 나하나</span></div><div class="role-cast"><strong>피에로:</strong><span>민우혁, 고은성, 서경수, 진태화</span></div></div></div>
            <div class="musical-card"><h2>지저스 크라이스트 수퍼스타</h2><h3>줄거리</h3><p>예수의 마지막 7일간의 행적을 제자 유다의 시선에서 재해석한 록 오페라. 예수의 인간적인 고뇌와 갈등을 강렬한 음악으로 표현합니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>지저스:</strong><span>박은태, 마이클리, 임태경</span></div><div class="role-cast"><strong>유다:</strong><span>윤형렬, 한지상, 최재림, 서은광</span></div><div class="role-cast"><strong>마리아:</strong><span>정선아, 장은아, 이영미</span></div></div></div>
            <div class="musical-card"><h2>지킬앤하이드</h2><h3>줄거리</h3><p>인간의 내면에 공존하는 선과 악을 분리하려는 의사 '지킬'이 실험을 통해 자신의 또 다른 인격인 '하이드'를 만들어내면서 벌어지는 비극적 스릴러입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>지킬/하이드:</strong><span>조승우, 류정한, 홍광호, 박은태, 전동석, 신성록, 박건형, 민우혁</span></div><div class="role-cast"><strong>루시:</strong><span>김선영, 옥주현, 아이비, 윤공주, 린아, 해나, 선민</span></div><div class="role-cast"><strong>엠마:</strong><span>조정은, 김소현, 임혜영, 이지혜, 최수진, 민경아</span></div></div></div>
            <div class="musical-card"><h2>캣츠</h2><h3>줄거리</h3><p>1년에 한 번 열리는 '젤리클 축제'에 모인 고양이들이 새로운 삶을 얻을 단 한 마리의 고양이로 선택받기 위해 각자의 이야기를 노래하는 내용입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>그리자벨라:</strong><span>옥주현, 박혜나, 인순이, 차지연</span></div><div class="role-cast"><strong>럼 텀 터거:</strong><span>빅스 켄, 이장우, 김준현</span></div><div class="role-cast"><strong>멍커스트랩:</strong><span>이시언, 이창희, 유회웅</span></div></div></div>
            <div class="musical-card"><h2>킹키부츠</h2><h3>줄거리</h3><p>폐업 위기에 처한 구두 공장을 물려받은 '찰리'가 드랙퀸 '롤라'를 만나 여장 남자를 위한 부츠 '킹키부츠'를 만들면서 벌어지는 신나는 이야기입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>롤라:</strong><span>정성화, 강홍석, 최재림, 박은태</span></div><div class="role-cast"><strong>찰리:</strong><span>이석훈, 김호영, 성규, 신재범</span></div><div class="role-cast"><strong>로렌:</strong><span>김지우, 김환희, 나하나</span></div></div></div>
            <div class="musical-card"><h2>팬레터</h2><h3>줄거리</h3><p>1930년대 경성을 배경으로, 천재 소설가 '김해진'과 그를 동경하는 작가 지망생 '정세훈', 그리고 비밀에 싸인 천재 여류작가 '히카루'의 이야기를 다룬 미스터리 드라마입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>정세훈:</strong><span>문성일, 김성철, 려욱, 윤소호</span></div><div class="role-cast"><strong>김해진:</strong><span>김종구, 이규형, 김경수</span></div><div class="role-cast"><strong>히카루:</strong><span>소정화, 김히어라, 조지승</span></div></div></div>
            <div class="musical-card"><h2>팬텀</h2><h3>줄거리</h3><p>'오페라의 유령' 에릭의 인간적인 면모에 초점을 맞춰, 그의 비극적인 과거와 천재성, 그리고 크리스틴을 향한 순수한 사랑을 깊이 있게 다룬 작품입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>팬텀(에릭):</strong><span>박효신, 박은태, 전동석, 카이, 규현, 류정한</span></div><div class="role-cast"><strong>크리스틴 다에:</strong><span>임선혜, 김소현, 이지혜, 김수</span></div><div class="role-cast"><strong>필립 드 샹동 백작:</strong><span>손준호, 박송권, 이해준</span></div></div></div>
            <div class="musical-card"><h2>프랑켄슈타인</h2><h3>줄거리</h3><p>19세기 유럽, 천재 과학자 빅터 프랑켄슈타인이 생명 창조에 성공하지만, 그가 만든 피조물에게 '괴물'이라는 이름으로 버림받으며 비극이 시작됩니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>빅터 프랑켄슈타인:</strong><span>류정한, 유준상, 전동석, 민우혁, 규현</span></div><div class="role-cast"><strong>앙리 뒤프레/괴물:</strong><span>박은태, 한지상, 카이, 박민성, 정택운(레오)</span></div><div class="role-cast"><strong>엘렌:</strong><span>서지영, 박혜나, 안시하</span></div><div class="role-cast"><strong>줄리아:</strong><span>안시하, 이지혜, 박혜나</span></div></div></div>
            <div class="musical-card"><h2>헤드윅</h2><h3>줄거리</h3><p>동독 출신의 트랜스젠더 록 가수 '헤드윅'이 자신의 실패한 사랑과 음악 인생에 대한 이야기를 콘서트 형식으로 풀어내는 모노드라마 뮤지컬입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>헤드윅:</strong><span>조승우, 오만석, 조정석, 유연석, 전동석, 마이클리, 정문성, 이규형, 렌</span></div><div class="role-cast"><strong>이츠학:</strong><span>전혜선, 이영미, 제이민, 유리아, 홍서영</span></div></div></div>
            <div class="musical-card"><h2>호프: 읽히지 않은 책과 읽히지 않은 인생</h2><h3>줄거리</h3><p>현대 문학의 거장 요제프 클라인의 미발표 원고를 평생 지켜온 78세 노인 '에바 호프'의 삶을 통해, 원고가 곧 자신이었던 한 인간의 인생을 그립니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><div class="role-cast"><strong>호프:</strong><span>김선영, 차지연, 김지현</span></div><div class="role-cast"><strong>K:</strong><span>고훈정, 조형균, 김경수</span></div></div></div>
            <div class="musical-card"><h2>훅 (HOOK)</h2><h3>줄거리</h3><p>피터팬 이야기의 악당 '후크 선장'의 숨겨진 과거와 그가 왜 그렇게 될 수밖에 없었는지를 새로운 시각으로 풀어낸 창작 뮤지컬입니다.</p><h3>역대 주요 출연진</h3><div class="cast-history"><p>2025년 9월 초연 예정으로 캐스팅 정보는 추후 공개됩니다.</p></div></div>
            <!-- 추가 뮤지컬 카드들... -->
        </div>
    </div>

    <script>
        // 검색 기능을 위한 JavaScript 코드
        document.getElementById('search-box').addEventListener('keyup', function() {
            let searchTerm = this.value.toLowerCase(); // 입력된 검색어를 소문자로 변환
            let musicalCards = document.querySelectorAll('.musical-card');

            musicalCards.forEach(function(card) {
                let title = card.querySelector('h2').textContent.toLowerCase(); // 각 카드의 제목을 소문자로 가져옴
                
                // 제목에 검색어가 포함되어 있으면 카드를 보여주고, 그렇지 않으면 숨김
                if (title.includes(searchTerm)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        });
    </script>

</body>
</html>
