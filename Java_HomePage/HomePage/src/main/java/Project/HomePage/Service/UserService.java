package Project.HomePage.Service;

import Project.HomePage.DTO.UserDTO;
import Project.HomePage.Entity.User;
import Project.HomePage.Repository.UserRepository;
import jakarta.persistence.EntityNotFoundException;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    public UserDTO getUserInfo(String id) {

        User user = userRepository.findById(id).orElseThrow(EntityNotFoundException::new);
        UserDTO userDTO = new UserDTO();

        userDTO.setUserId(user.getUserId());
        userDTO.setUserName(user.getUserName());
        userDTO.setUserEmail(user.getUserEmail());
        userDTO.setUserPhone(user.getUserPhone());

        return userDTO;
    }

    public String getName(String Id) {
        User user = userRepository.findByUserName(Id).orElseThrow(EntityNotFoundException::new);
        return user.getUserName();
    }



}

