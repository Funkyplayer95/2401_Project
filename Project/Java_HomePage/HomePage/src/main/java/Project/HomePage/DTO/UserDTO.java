package Project.HomePage.DTO;

import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class UserDTO {

    private String userId;
    private String userPassword;
    private String userName;
    private String userEmail;
    private String userPhone;
    private int userImageId;
}
