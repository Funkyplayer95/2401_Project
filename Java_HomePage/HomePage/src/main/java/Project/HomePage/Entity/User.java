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
    private int user_code;
    private String user_id;
    private String user_password;
    private String user_name;
    private char user_gender;
    private int user_rrn1;
    private int user_rrn2;
    private String user_email;
    private int user_address_num;
    private String user_address_doro;
    private String user_address_jibun;
    private String user_address_detail;
    private int user_image_id;

}
