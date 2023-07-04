def find(start,end) :
    global k
    if start == end :return #시작과 끝이 같다면 진행x
    mid = (start+end)//2
    find(start,mid) ; find(mid+1,end) #배열을 둘로나눠 정렬진행
    if k <=end-start+1 : #정렬하려는 배열의 크기 >= K인지 확인
        j = sorted(i[start:end+1]) #원하는 배열만 정렬
        print(j[k-1]);exit() #A의 몇번째 배열에 들어갔는지 확인 후 정렬된 배열에서 그 수 출력
    k -= end-start+1 #정렬하려는 배열의 크기 < k 면 우리가 원하는 배열이 아니므로 A에 원소가 들어간 만큼 k를 빼줌

n,k = map(int,input().split()); i = list(map(int,input().split()))
find(0,n-1);print(-1) #만약 이 과정을 진행하였는데 프로그램을 종료되지 않았다면 저장횟수가 k보다 적은것이니 -1출력
