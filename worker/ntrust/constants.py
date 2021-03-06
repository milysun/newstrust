# this coverts
# * well formatted email
# * bad formatted email like, `aaa@aaa`
SRE_EMAIL = '[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+'

SENTENCE_ENDING_CHARS = (
    '.',
    '?',
    '!',
    '”',
    '“',
)

STOPWORDS_ENGLISH = (
    'i',
    'me',
    'my',
    'myself',
    'we',
    'our',
    'ours',
    'ourselves',
    'you',
    'your',
    'yours',
    'yourself',
    'yourselves',
    'he',
    'him',
    'his',
    'himself',
    'she',
    'her',
    'hers',
    'herself',
    'it',
    'its',
    'itself',
    'they',
    'them',
    'their',
    'theirs',
    'themselves',
    'what',
    'which',
    'who',
    'whom',
    'this',
    'that',
    'these',
    'those',
    'am',
    'is',
    'are',
    'was',
    'were',
    'be',
    'been',
    'being',
    'have',
    'has',
    'had',
    'having',
    'do',
    'does',
    'did',
    'doing',
    'a',
    'an',
    'the',
    'and',
    'but',
    'if',
    'or',
    'because',
    'as',
    'until',
    'while',
    'of',
    'at',
    'by',
    'for',
    'with',
    'about',
    'against',
    'between',
    'into',
    'through',
    'during',
    'before',
    'after',
    'above',
    'below',
    'to',
    'from',
    'up',
    'down',
    'in',
    'out',
    'on',
    'off',
    'over',
    'under',
    'again',
    'further',
    'then',
    'once',
    'here',
    'there',
    'when',
    'where',
    'why',
    'how',
    'all',
    'any',
    'both',
    'each',
    'few',
    'more',
    'most',
    'other',
    'some',
    'such',
    'no',
    'nor',
    'not',
    'only',
    'own',
    'same',
    'so',
    'than',
    'too',
    'very',
    's',
    't',
    'can',
    'will',
    'just',
    'don',
    'should',
    'now',
)

PROVIDER_CODE = {
    '01100101': '경향신문',
    '01100201': '국민일보',
    '01100301': '내일신문',
    '01100501': '문화일보',
    '01100611': '서울신문',
    '01100701': '세계일보',
    '01101001': '한겨레',
    '01101101': '한국일보',
    '01200101': '경기일보',
    '01200201': '경인일보',
    '01300101': '강원도민일보',
    '01400201': '대전일보',
    '01400351': '중도일보',
    '01400401': '중부매일',
    '01400551': '충북일보',
    '01400701': '충청투데이',
    '01500051': '경남신문',
    '01500151': '경남도민일보',
    '01500301': '경상일보',
    '01500401': '국제신문',
    '01500501': '대구일보',
    '01500601': '매일신문',
    '01500701': '부산일보',
    '01500801': '영남일보',
    '01500901': '울산매일',
    '01600301': '광주일보',
    '01600501': '무등일보',
    '01600801': '전남일보',
    '01601001': '경북도민일보',
    '01601101': '전북일보',
    '01700201': '한라일보',
    '02100101': '매일경제',
    '02100311': '서울경제',
    '02100501': '파이낸셜뉴스',
    '02100601': '한국경제',
    '02100701': '헤럴드경제',
    '01300201': '강원일보',

    # newly added at Thu Mar 16 05:21:09 KST 2017; from `newsdb`
    '01200401': '인천일보',
    '07100502': '환경일보',
    '04101208': '조세일보',
    '04101258': '투데이코리아',
    '01500201': '경북일보',
    '05420702': '홍성신문·내포타임즈',
    '01100751': '아시아투데이',
    '04101008': '이데일리',
    '05520352': '당진시대',
    '08200101': 'OBS',
    '03100201': 'THE KOREA TIMES',
    '08100411': 'YTN',
    '01700401': '제주신보',
    '01100601': '서울신문',
    '01400501': '중부일보',
    '02100321': '서울경제',
    '05410052': '옥천신문',
    '02100351': '이투데이',
    '01400601': '충청일보',
    '01401608': '이투데이',
    '08100301': 'SBS',
    '04400108': '헬로우디디(대덕넷)',
    '01400301': '동양일보',
    '02100801': '아시아경제',
    '08100401': 'YTN',
    '08100201': 'MBC',
    '07100602': '피티저널',
    '01400211': '대전일보',
    '07100702': '한국기자협회',
    '06100252': '시사IN',
    '08520101': 'KNN',
    '04100608': 'Break News',
    '07100902': '어린이강원일보',
    '01600601': '새전북신문',
    '04100078': '뉴스핌',
    '03100101': '환경일보',

    # add 2017-08-08
    '07200502': '소년한국일보',
    '01700101': '제민일보',
    '07100952': 'KPOP HERALD',
    '10100301': '스포츠한국',
    '02100201': '머니투데이',
    '04100058': 'CBS노컷뉴스',
    '07100501': '전자신문',
    '01100401': '동아일보',
    '10100101': '스포츠서울',
    '02100851': '아주경제',
    '04100158': '데일리안',
}
