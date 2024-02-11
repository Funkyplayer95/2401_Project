package Project.HomePage.Entity;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.*;

@Entity
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
@ToString
public class User {

    @Id
    private int userCode;
    private String userId;
    private String userPassword;
    private String userName;
    private char userGender;
    private int userRrn1;
    private int userRrn2;
    private String userEmail;
    private int userAddressNum;
    private String userAddressDoro;
    private String userAddressJibun;
    private String userAddressDetail;
    private int userImageId;
}
