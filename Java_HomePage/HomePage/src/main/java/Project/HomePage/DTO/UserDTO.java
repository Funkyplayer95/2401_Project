package Project.HomePage.DTO;

import lombok.*;

@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class UserDTO {

    private String userId;
    private String userName;
    private String userEmail;
    private int userPhone;
    private int userImageId;
}
