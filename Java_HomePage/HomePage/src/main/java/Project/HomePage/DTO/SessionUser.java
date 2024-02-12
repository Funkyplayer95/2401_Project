package Project.HomePage.DTO;

import Project.HomePage.Entity.User;
import lombok.Getter;

import java.io.Serializable;

@Getter
public class SessionUser implements Serializable {

    private String id;
    private String name;
    private String email;
    private int phone;

    public SessionUser(User user){
        this.id =user.getUserId();
        this.name = user.getUserName();
        this.email = user.getUserEmail();
        this.phone = user.getUserPhone();

    }
}
