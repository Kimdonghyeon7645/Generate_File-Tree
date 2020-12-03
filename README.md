# 🖨📃 원하는 폴더의 트리구조 생성기

## 개요
```markdown
###### 트리구조 출력 결과
📦 test_folder
 ┣ 📁 outter_folder
 ┃ ┣ 📁 inner_folder
 ┃ ┃ ┗ 📜 tests_in_inner.txt
 ┃ ┗ 📜 tests_in_outter.txt
 ┣ 📁 outter_folder_2
 ┃ ┗ 📁 inner_folder_2
 ┃   ┗ 📜 encapsulated.txt
 ┗ 📜 tests.txt
```
원하는 폴더 위치를 트리 구조로 출력하는 파이썬 스크립트!

## 동기

폴더 구조가 한눈에 들어오지 않는 깃허브에서,  
트리구조로 한눈에 모든 파일을 표시하고 싶을때, 아래와 같은 플러그인을 이용해왔다.   
![image](https://user-images.githubusercontent.com/48408417/100516136-107edd00-31c5-11eb-831c-ada190cf6daa.png)

여기서 ```generator tree text```로 해당 폴더의 트리를 텍스트로 전달받아서, 이걸 readme.md 파일에 올리는 용으로 자주 사용하였는데,  
자주 쓰다보니까 보이는 아쉬운 점이 있었다. 

1. (가장중요) vscode 플러그인이라서 트리 텍스트를 얻기위해 vscode를 열어야 한다... 
2. 아이콘이 항상 고정되어, 내가 원하는 걸로 사용하지 못한다.
3. 파일없이 폴더만 중첩된 경우에 예쁘지 않게 출력된다?

근데, 생각해보니 파이썬의 ```os``` 라이브러리를 이용한다면, 나도 이런 기능을 파이썬 스크립트로 만들 수 있지 않나 싶어,  
목마른 사람이 우물파듯이, 직접 원하는 기능을 보완한 스크립트를 만들었다.
