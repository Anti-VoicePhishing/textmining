
E_s = 0
simga_s=0


'''
패턴 분석에 활용되고 있는 이산 푸리에 변환을
텍스트 패턴 분석에 적용하고자 ! 
>  텍스트를 수치화 (신호화) 

이와 같이 이산 푸리에 변환을 텍스트 마이닝에 적용한 경우 

1. 유사한 패턴을 가지는 텍스트 탐색 
2. 동일 위치에 동일용어를 가지는 텍스트 탐색 

'''

def vectorizing(string):
    summation = 0 #sigmaCA (character ascii코드 값의 합을 구해줘)
    wordcount = len(string) # 문자의 길이 

    # 각 문자를 ascii코드 값을 바꾼 값들의 집합 
    vectorized = []

    ## CA를 구하는 부분 
    for word in string:
        summation += ord(word)
        vectorized.append(ord(word))

    ## E(S)를 구하는 부분 
    global E_s
    if E_s == 0:
        E_s = summation / wordcount

    normalized_string = []
    
    ## sigma구하는 부분 

    global simga_s
    if simga_s == 0:
        simga_s = (summation / wordcount)

    normalized_string = []

    #Di 구하는 부분 
    for word in string:
        Di = (ord(word) -E_s) / simga_s
        # 반올림 
        normalized_string.append(round(Di,2))

    return vectorized, normalized_string


original = "고객님 예약하신 물품 보냈습니다. 클릭 조회부탁합니다. http://tinyurl.com/y9bjdgtl"
transform = "고객님 먼저 얘기하셨던 물품 보냈습니다. 클릭 조회부탁합니다. http://tinyurl.com/y9bjdgtl"
'''
문자열에서 문자 하나씩 접근 가능 
for o in original:
    print(o)
'''
# 여기서는 특수문자를 제외한 모든 문자를 ascii코드 값으로 변환하도록 텍스트 신호로 만드는 방법 
original = original.replace(".","").replace(" ","")
#print(original)

transfrom = transform.replace(".","").replace(" ","")

unicode_original, vectorized_original = vectorizing(original)
print(unicode_original, vectorized_original)





