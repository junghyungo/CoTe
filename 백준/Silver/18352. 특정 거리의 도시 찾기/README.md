# [Silver II] 특정 거리의 도시 찾기 - 18352 

[문제 링크](https://www.acmicpc.net/problem/18352) 

### 성능 요약

메모리: 173372 KB, 시간: 2728 ms

### 분류

너비 우선 탐색, 데이크스트라, 그래프 이론, 그래프 탐색, 최단 경로

### 제출 일자

2025년 5월 10일 01:37:55

### 문제 설명

<p style="user-select: auto !important;">어떤 나라에는 1번부터 <em style="user-select: auto !important;">N</em>번까지의 도시와 <em style="user-select: auto !important;">M</em>개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.</p>

<p style="user-select: auto !important;">이 때 특정한 도시 <em style="user-select: auto !important;">X</em>로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 <em style="user-select: auto !important;">K</em>인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 <em style="user-select: auto !important;">X</em>에서 출발 도시 <em style="user-select: auto !important;">X</em>로 가는 최단 거리는 항상 0이라고 가정한다.</p>

<p style="user-select: auto !important;">예를 들어 <em style="user-select: auto !important;">N</em>=4, <em style="user-select: auto !important;">K</em>=2, <em style="user-select: auto !important;">X</em>=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.</p>

<p style="text-align: center; user-select: auto !important;"><img alt="" src="https://upload.acmicpc.net/a5e311d7-7ce4-4638-88a5-3665fb4459e5/-/preview/" style="height: 249px; width: 250px; user-select: auto !important;"></p>

<p style="text-align: justify; user-select: auto !important;">이 때 1번 도시에서 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 2인 도시는 4번 도시 뿐이다.  2번과 3번 도시의 경우, 최단 거리가 1이기 때문에 출력하지 않는다.</p>

### 입력 

 <p style="user-select: auto !important;">첫째 줄에 도시의 개수 <em style="user-select: auto !important;">N</em>, 도로의 개수 <em style="user-select: auto !important;">M</em>, 거리 정보 <em style="user-select: auto !important;">K</em>, 출발 도시의 번호 <em style="user-select: auto !important;">X</em>가 주어진다. (2 ≤ <em style="user-select: auto !important;">N </em>≤ 300,000, 1 ≤ <em style="user-select: auto !important;">M </em>≤ 1,000,000, 1 ≤ <em style="user-select: auto !important;">K </em>≤ 300,000, 1 ≤ <em style="user-select: auto !important;">X </em>≤ <em style="user-select: auto !important;">N</em>) 둘째 줄부터 <em style="user-select: auto !important;">M</em>개의 줄에 걸쳐서 두 개의 자연수 <em style="user-select: auto !important;">A</em>, <em style="user-select: auto !important;">B</em>가 공백을 기준으로 구분되어 주어진다. 이는 <em style="user-select: auto !important;">A</em>번 도시에서 <em style="user-select: auto !important;">B</em>번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ <em style="user-select: auto !important;">A</em>, <em style="user-select: auto !important;">B </em>≤ <em style="user-select: auto !important;">N</em>) 단, <em style="user-select: auto !important;">A</em>와 <em style="user-select: auto !important;">B</em>는 서로 다른 자연수이다.</p>

### 출력 

 <p style="user-select: auto !important;"><em style="user-select: auto !important;">X</em>로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 <em style="user-select: auto !important;">K</em>인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.</p>

<p style="user-select: auto !important;">이 때 도달할 수 있는 도시 중에서, 최단 거리가 <em style="user-select: auto !important;">K</em>인 도시가 하나도 존재하지 않으면 -1을 출력한다.</p>

