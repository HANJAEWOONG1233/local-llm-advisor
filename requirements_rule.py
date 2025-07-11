# 파일명: requirements_rule.py (수정 완료)

GRADUATION_REQUIREMENTS = {
    '인공지능소프트웨어학과': {
        'total_credits': 130,
        
        'classification_credits': {
            '교필': 9,
            '교선': 21,
            '전선': 48,
            '심선': 12,
            '특필': 8,
            '일선': 0
        },
        
        'required_courses': [ 
            '공학설계입문', '진로설계1(자기이해와 대학생활)', '진로설계2(진로탐색과 자기계발)',
            '진로설계3(진로설정과 경력개발)', '진로설계4(취업전략과 실전취업)', '캡스톤디자인Ⅰ'
        ],
        
        'detailed_requirements': {
            # --- ★★★ 이 부분만 수정됩니다 ★★★ ---
            '교양 학점 합계': {
                'description': "교양(교필+교선+일선) 학점을 총 33학점 이상 이수", # 설명 변경
                'type': 'credit_sum',
                'classifications': ['교필', '교선', '일선'], # '일선' 추가
                'required_credits': 33
            },
            # --- ★★★ 수정 끝 ★★★ ---
            
            '기초교양 필수 과목': {
                'description': "'발표와 토론', '대학영어' 과목 필수 이수",
                'type': 'take_all',
                'courses': ['발표와 토론', '대학영어']
            },
            '기초교양 택1 (글쓰기)': {
                'description': "'창의글쓰기', '공학글쓰기' 중 1과목 이상 필수 이수",
                'type': 'take_one_or_more',
                'courses': ['창의글쓰기', '공학글쓰기']
            },
            '기초교양 택1 (코딩)': {
                'description': "코딩 5과목(C,Java,Python,Scratch,VB) 중 1과목 이상 필수 이수",
                'type': 'take_one_or_more',
                'courses': ['C 프로그래밍', 'Java 프로그래밍', 'Python 프로그래밍', 'Scratch 프로그래밍', '비주얼베이직']
            },
            '핵심교양 세부 영역': {
                'description': "핵심교양 3개 영역(소통과인성, 분석과판단, 도전과미래)에서 각각 1과목 이상 필수 이수",
                'type': 'area_based',
                'num_areas_required': 3,
                'areas': {
                    '소통과 인성': [
                        '문화콘텐츠스토리텔링', '인권과 사회', '종교와 문화', '인간과 환경',
                        '[계열교차 교과목] 과학기술의 탐색 (수학 과학 공학)',
                        '[계열교차 교과목] 인간의 탐색 (철학 역사 문학)'
                    ],
                    '분석과 판단': [
                        '합리적 문제해결과 논리', '인간과 윤리', '통계로 보는 세상',
                        '과학기술사', '심리분석'
                    ],
                    '도전과 미래': [
                        '한국사의 이해', '인간삶과 교육', '역사와 문화',
                        '세계시민과 국가', '경제와 사회'
                    ]
                }
            }
        }
    }
}