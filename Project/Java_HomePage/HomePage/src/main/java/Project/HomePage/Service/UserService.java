package Project.HomePage.Service;

import Project.HomePage.DTO.UserDTO;
import Project.HomePage.Entity.User;
import Project.HomePage.Repository.UserRepository;
import jakarta.persistence.EntityNotFoundException;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
@RequiredArgsConstructor
public class UserService {

    @Autowired
    private final UserRepository userRepository;

    public List<UserDTO> getAllUser(){
        List<User> users = userRepository.findAll();
        List<UserDTO> userDTOs = new ArrayList<>();

        for (User user : users) {
            UserDTO userDTO = new UserDTO();
            userDTO.setUserId(user.getUser_id());
            userDTO.setUserName(user.getUser_name());

            userDTOs.add(userDTO);
        }

        return userDTOs;
    }

    public UserDTO getUserInfo(String id) {

        User user = userRepository.findById(id).orElseThrow(EntityNotFoundException::new);
        UserDTO userDTO = new UserDTO();

        userDTO.setUserId(user.getUser_id());
        userDTO.setUserName(user.getUser_name());
        userDTO.setUserEmail(user.getUser_email());
        userDTO.setUserPhone(user.getUser_phone());

        return userDTO;
    }


}

