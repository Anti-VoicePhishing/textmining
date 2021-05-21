from konlpy.tag import Okt
import numpy as np
from numpy.linalg import norm
from numpy import dot 


#보이스피싱 데이터니까 변수에 저장해줘 
s1 = "저희 아들 이번주말 첫 돌 잔치에요 초대장 저희 보내드립니다. Vo.to/3₂C 축복해주세요"
s2 = "제 아들 이번주에 돌 잔치에요 초대장 보내드릴께요. Vo.to/3₂C 축복해주세요"
s3 = "저희 집 아들 이번주에 첫 돌 잔치입니다. 초대장 보내드리겠습니다. Vo.to/3₂C 축복해주세요"

#중요한 데이터들을 하나의 묶음으로 저장해줘 
voicepishing = [s1,s2,s3]
#print(pymk)

#오픈소스 한국어 분석기 가져와줘 
peachOkt = Okt()

# pymk에 명사만 저장하도록 해줘 
for i,s in enumerate(voicepishing):
    voicepishing[i] = ' '.join(peachOkt.nouns(s))
#print(voicepishing)

features = []
words = []
# 보이스피싱 전체 문장에 대해 반복 알고리즘 -> 단어 단위 다시 저장 
for i in range(len(voicepishing)):
    # 위에서 나눈 명사들을 각각 공백기준으로 단어로 따로 나눈 중요한 단어 데이터들을 모아 단어리스트로 만들어줘 
    word = voicepishing[i].split(" ")
    # 리스트를 자체를 더 큰 단어 리스트에 저장 (중첩리스트) -> [[],[],[]] 
    words.append(word)

    # 보이스피싱 한문장에 대해서 단어개수만큼 반복 알고리즘 -> 필터링
    for i in range(len(word)):
        # 필터 알고리즘 - 중복없는 단어만 저장하도록 
        if word[i] not in features:
            features.append(word[i])

print(features)

#특징 데이터에서 빈도수를 벡터화 (행렬로 )
def make_matrix(features, senctence):
    frequency_list = []
    for feature in features:
        #해당 feat에 대한 freq초기화 
        frequency = 0
        for word in senctence:
            if word == feature:
                frequency += 1
        # 한 feature가 끝났을 때 해당 feat에 대한 frequency저장 
        frequency_list.append(frequency)
    return frequency_list


def cos_sim(a,b):
    return dot(a,b) / (norm(a)* norm(b))


# 빈도수 기록 행렬 
frequency= []

# 전체 단어와 특징을 가지고 행렬을 만들어줘 
for i in range(len(voicepishing)):
    frequency.append(np.array(make_matrix(features,words[i])))
    print(frequency)

for i in range(len(voicepishing)):
    for j in range(i+1, len(voicepishing)):
        print(str(i)+ "과" + str(j)+ "사이의 유사도는 " + str(cos_sim(frequency[i], frequency[j])))



