# 개요
- '파이썬 날코딩으로 알고 짜는 딥러닝(윤덕호 저)'을 Ipython Notebook이 아닌 PyCharm에서 작동 가능한 형식으로 리팩토링 해 보는 토이프로젝트(?)
- 책에 나와있는 ```bash %run *.ipynb``` 형식의 작동방식은 Google Colaboratory에서 수정 후 바로 반영되지 않는 불편함이 있어서 시작하게 됨
- 좋은 책을 작성해주신 교수님께 감사드립니다.

# 목적
- Deep Learning 알고리즘(특히, RNN 계열) 내부 원리 학습
- 이후 추가적으로 학습(e.g Attention-Mechanism)한 내용을 프레임워크 없이 코딩 후 반영
- 학습한 내용 중 실무에서 직접 적용해 본 내용 반영

# 리팩토링 포인트
- mathutil ipynb 내부에 정의된 순수함수들을 클래스 내부에서 staticmethod로 변경
