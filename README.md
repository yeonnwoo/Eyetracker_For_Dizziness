<p align="center" >
  :zap: 해당 자료들은 제6회 대한민국 sw융합 해커톤 대회에서 우수상을 수상한 프로젝트의 일부 자료입니다 :zap:
</p>


### :mag_right: Eyetracker_For_Dizziness

>**딥러닝을 이용한 이석증 분류기** 

* ### 프로젝트 소개
  <img src="https://user-images.githubusercontent.com/50096655/82443986-6fa8ba00-9add-11ea-9bd4-a7159d8a6093.gif">

  
  - Diagnosis of BPPV by eye movement tracker Algorithm
  

* ### 프로젝트 개요
  * 이석증
  
  * 프로젝트 목적<br>
    - 아래와 같이 기존의 안진검사의 한계점을 알아냄.<br>
      ∨ 환자는 병원에 방문하여 무거운 적외선 카메라가 부착된 특수한 안경을 착용하여 검사를 진행해야 한다는 불편함<br>
      ∨ 적외선 비디오 녹화 시스템을 이용하여 눈의 움직임을 다시 분석해야 하는 번거로움이 있음<br>
      ∨ 장비가 가벼운 재질이고 이동성이 좋은 관계로 파손의 위험이 높다는 것<br>
      ∨ 얼굴의 형태나 연령에 따라 여러 크기와 형태의 고글이 필요하다는 점<br>
        *출처 <대한평형의학회지 제 3 권 2호 2004; 245-253><br>
    
     - 간편하게 안진검사를 시행할 수 있는 서비스를 만들고자하였다.
    
   
  - Dataset<br>
    * 한계<br>
    의료 데이터의 특성 상, 병원과 협업하지 않고는 많은 데이터를 얻는데 한계가 있었다.<br>
    따라서 데이터는 유튜브에 공개적으로 업로드된 다수의 환자 영상으로 학습을 진행하였다.<br>
    부족한 데이터는 팀원들이 직접 동공의 움직임을 모방하여 data를 직접 구축했다.
  
  
  * 진단 방법
  
    * 머리가 움직이면 반고리관에서 내림프액 흐름이 생기고 흐름의 방향에 따라 특정 반고리관 전정신경이 흥분되는데 이렇게 흥분된 전정신경은 특정한 방      향으로 안구를 움직이게 만드는 신경들을 자극합니다. 그런데 이러한 정상적인 신호의 흐름이 깨지거나 항진되는 경우 머리의 움직임이 안구의 비정상적      인 운동을 만들어 내는데 이러한 안구의 움직임을 비정상 안진이라고 합니다. 비정상 안진이 나타나면 머리 움직임에 눈이 적절히 반응하지 못해 시야      가 흔들리거나 빙빙 도는 것같이 보이는데 이러한 안구의 움직임을 측정한다.

* ### 동공 추출 기법

  <img src="https://user-images.githubusercontent.com/50096655/82442944-96fe8780-9adb-11ea-9ede-89d3b77751cf.gif" width="400" height="300"></img>
  * open cv에서 미리 훈련된 데이터를 XML파일(haarcascade_eye.xml)을 제공하는데 이를 이용하여 먼저 눈을 검출
  * 검출 한 눈을 crop하여 그 안에서 gray 이미지의 Gaussian Noise를 제거
  * 이미지 thresholding을 통해 threshold보다 크면 0이고 아니면 value로 바꾸어 줌
  * 동공이 검정색인 점을 이용하여 Contour을 찾아줌
  




* ### reference
num| 사이트
--------- | ---------
1 | http://www.dizziness-and-balance.com/disorders/bppv/bppv-korean.htm
2 | http://www.ijircce.com/upload/2014/february/7J_A%20Survey.pdf
3 | http://www.ijsrp.org/research-paper-0513/ijsrp-p17106.pdf
4 | https://dgkim5360.tistory.com
5 | https://eehoeskrap.tistory.com/91


* ###  accuracy
<table>
  <th> </th>
  <th>0</th>
  <th>1</th>
  <th>accuracy</th>
  <tr>
    <td >normal</td>
    <td>130</td>
    <td>0</td>
    <td>100%</td>
  </tr>
    <tr>
    <td >abnormal(modified data)</td>
    <td>42</td>
    <td>88</td>
    <td>67.7%</td>
  </tr>
    <tr>
    <td >real_patient</td>
    <td>15</td>
    <td>115</td>
    <td>88.4%</td>
  </tr>
</table>
