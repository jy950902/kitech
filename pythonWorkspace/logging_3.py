
import logging
import time

logger = logging.getLogger('myApp')
hand = logging.FileHandler('myapp_.log')

#                              생성시간,   로그레벨 ,       프로세스ID,   메시지
formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')

# 파일핸들러에 문자열 포메터를 등록
hand.setFormatter(formatter)

logger.addHandler(hand)

logger.setLevel(logging.INFO)

logger.debug('틀렸음~!!')
logger.info('불켜짐')
logger.warning('사람 있음')
logger.error('사람 없음')
logger.critical('치명적~!!')