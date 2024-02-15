package Project.HomePage.DTO;

import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class UserDTO {
    //내가 필요한 정보만 진행.
    private String userId; // 유저 아이디(findById 사용을 위해)
    private String userPassword; // 유저 비밀번호(변경시 필요)
    private String userName; // 유저 이름 (마이페이지)
    private String userEmail; // 유저 이메일 (마이페이지)
    private String userPhone; // 유저 전화번호(변경시 필요)
    private String profileImage; // 유저 대표이미지 (변경시 필요)
    private String imageExtension; // 유저 확장자 (변경시 필요)
}
