package Project.HomePage.Entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.*;

@Entity // entity 설정
@Getter // lombok getter 설정
@Setter // lombok setter 설정
@AllArgsConstructor // 모든 인자를 가진 객체 생성
@NoArgsConstructor // 아무 인자도 없는 객체 생성
@Table(name = "userinfo") // DB테이블명 연동
@ToString // ToString 생성
public class User {

    @Id // 기본키 지정 (이 키를 이용하여 테이블 찾음)
    private String user_id; //사용자 아이디
    private String user_password; //사용자 비밀번호
    private String user_name; // 사용자 이름
    private char user_gender; // 사용자 성별
    private int user_rrn1; // 주민등록번호 앞자리
    private int user_rrn2; // 주민등록번호 뒷자리
    private String user_email; // 사용자 이메일
    private int user_address_num; // 사용자 주소 번호
    private String user_address_doro; // 사용자 도로명 주소
    private String user_address_jibun; // 사용자 지번 주소
    private String user_address_detail; // 사용자 상세 주소
    private String user_phone; // 사용자 전화번호
    private String profile_image; // 사용자 대표 이미지
    private String imageExtension; // 사용자 대표 이미지 확장자
}
