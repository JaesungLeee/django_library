# django_library
Hufs_IA Django project with local library
<br><br>
![libraryUML](./readmeImage/libraryUML.PNG) <br>
### UML 설명
#### BOOK Table
* title : 책의 제목
* author : 책의 저자 (1 ~ n명)
* summary : 책 내용 요약
* imprint : 책의 출판사
* ISBN : 13자의 책 Serial Number
* genre : 책의 장르 (1 ~ n개의 장르)
* language : 책의 언어
#### Author Table
* name : 저자 이름
* date_of_birth, date_of_death : 저자 정보
* books : 저자가 쓴 책들 (1 ~ n권)
#### Genre Table
* Book의 genre와 관련된 Table
* name : genre들
#### Language Table
* Book의 language와 관련된 Table
* name : Language들
#### BookInstance Table
* 도서관의 입장에서의 Table
* uniqueId : 책마다 구분할수 있는 ID가 필요
* due_back : 반납 기간
* status : 책을 대여했는지 책장에 꼽혀있는지의 상태 표시
* book : Book Table에 포함됨
