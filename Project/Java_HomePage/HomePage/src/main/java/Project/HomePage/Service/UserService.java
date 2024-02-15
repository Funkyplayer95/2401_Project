package Project.HomePage.Service;

import Project.HomePage.DTO.UserDTO;
import Project.HomePage.Entity.User;
import Project.HomePage.Repository.UserRepository;
import jakarta.persistence.EntityNotFoundException;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

@Service
@RequiredArgsConstructor
public class UserService {

    @Autowired
    private final UserRepository userRepository;
    private final Path root = Paths.get("uploads");

    public UserDTO getUserInfo(String id) {

        User user = userRepository.findById(id).orElseThrow(EntityNotFoundException::new);
        UserDTO userDTO = new UserDTO();

        userDTO.setUserId(user.getUser_id());
        userDTO.setUserName(user.getUser_name());
        userDTO.setUserEmail(user.getUser_email());
        userDTO.setUserPhone(user.getUser_phone());
        userDTO.setProfileImage(user.getProfile_image());
        userDTO.setImageExtension(getExtension(user.getProfile_image()));

        return userDTO;
    }

    @Transactional //선언적 트랜잭션. 적용된 범위에서는 트랜잭션 기능이 포함된 프록시 객체가 생성되어 자동 commit/rollback 시켜준다.
    //비즈니스 로직에서 쪼갤 수 없는 하나의 작업 단위. 데이터베이스 상태변경하며 한 번에 수행되어야 한다.
    public void updatePassword(String id, String newPw) {

        User user = userRepository.findById(id).orElseThrow(() -> new NoSuchElementException("유저를 찾을 수 없습니다." + id));
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

        //더티체킹(Dirty Checking) = JPA 핵심 기능. 전체 데이터베이스 안불러와도 됨.
        user.setUser_password(passwordEncoder.encode(newPw));
        userRepository.save(user);
    }
    @Transactional
    public void updatePhone(String id, String newPhone) {

        User user = userRepository.findById(id).orElseThrow(() -> new NoSuchElementException("유저를 찾을 수 없습니다." + id));
        user.setUser_phone(newPhone);
        userRepository.save(user);
    }
    public void imgSave(MultipartFile file, String id){
        try{
            User user = userRepository.findById(id).orElseThrow();
            String filename = file.getOriginalFilename();
            List<String> allowedExtensions = Arrays.asList("img", "jpg", "png");

            String extension = Objects.requireNonNull(filename).substring(filename.lastIndexOf(".") + 1);
            if (!allowedExtensions.contains(extension)) {
                throw new RuntimeException("img, jpg, png 파일만 업로드가능합니다.");
            }

            // 이미지 데이터를 Base64로 인코딩
            String encodedImage = Base64.getEncoder().encodeToString(file.getBytes());

            user.setProfile_image(encodedImage);
            user.setImageExtension(extension); // 파일의 확장자를 저장
            userRepository.save(user);
        } catch (IOException e) {
            throw new RuntimeException("파일을 저장할 수 없습니다. 오류 : " + e.getMessage());
        }
    }

    //확장자 명칭을 저장하는 함수
    public String getExtension(String filename) {
        String extension = "";
        if (filename != null) {
            Path path = Paths.get(filename);
            if (path.getFileName().toString().contains(".")) {
                extension = path.getFileName().toString().substring(path.getFileName().toString().lastIndexOf(".") + 1);
            }
        }
        return extension;
    }





//    public List<UserDTO> getAllUser(){
//        List<User> users = userRepository.findAll();
//        List<UserDTO> userDTOs = new ArrayList<>();
//
//        for (User user : users) {
//            UserDTO userDTO = new UserDTO();
//            userDTO.setUserId(user.getUser_id());
//            userDTO.setUserName(user.getUser_name());
//
//            userDTOs.add(userDTO);
//        }
//
//        return userDTOs;
//    }


}

