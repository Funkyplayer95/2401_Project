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

    public UserDTO getUserInfo(String id) {

        User user = userRepository.findById(id).orElseThrow(EntityNotFoundException::new);
        // 아이디가 있으면 반환. 아이디에 해당하는 사용자가 없으면 예외를 발생시킨다.

        UserDTO userDTO = new UserDTO(); // 새로운 DTO객체 생성

        userDTO.setUserId(user.getUser_id()); // DTO에 user_id를 set한다
        userDTO.setUserName(user.getUser_name()); // DTO에 user_name를 set한다
        userDTO.setUserEmail(user.getUser_email()); // DTO에 user_email를 set한다
        userDTO.setUserPhone(user.getUser_phone()); // DTO에 user_phone를 set한다
        userDTO.setProfileImage(user.getProfile_image()); // DTO에 user_profile_image를 set한다
        userDTO.setImageExtension(getExtension(user.getProfile_image())); // DTO에 user_id를 set한다
        // getExtension 메소드는 파일의 확장자를 추출해서 반환하는 메서드이다.

        return userDTO; // set된 userDTO를 반환
    }
    
    @Transactional //선언적 트랜잭션. 적용된 범위에서는 트랜잭션 기능이 포함된 프록시 객체가 생성되어 자동 commit/rollback 시켜준다.
    //비즈니스 로직에서 쪼갤 수 없는 하나의 작업 단위. 데이터베이스 상태변경하며 한 번에 수행되어야 한다.
    public void updatePassword(String id, String newPw) {

        User user = userRepository.findById(id).orElseThrow(EntityNotFoundException::new); // 아이디를 통해 사용자를 찾는다
        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder(); // BCrypt 암호화 할때 사용하는 객체

        //더티체킹(Dirty Checking) = JPA 핵심 기능. 전체 데이터베이스 안불러와도 됨.
        user.setUser_password(passwordEncoder.encode(newPw)); // 비밀번호를 저장할때 newPw를 암호화로 인코딩한 후 저장.
        userRepository.save(user); // save문을 통해 update 시킨다.
    }

    //이미지 저장하는 메서드
    public void imgSave(MultipartFile file, String id){
        try{
            User user = userRepository.findById(id).orElseThrow(); // 아이디를 통해 사용자 찾기.
            String filename = file.getOriginalFilename(); //업로드된 파일의 이름을 가져온다.
            List<String> allowedExtensions = Arrays.asList("img", "jpg", "png"); // 업로드 허용할 확장자를 리스트로 정의.

            //파일 이름에서 확장자 부분을 추출. requireNonNull는 obj가 null이면 nullpointerror를 발생해주는 메서드.
            String extension = Objects.requireNonNull(filename).substring(filename.lastIndexOf(".") + 1);
            if (!allowedExtensions.contains(extension)) { // 업로드된 파일의 확장자가 allowedExtensions 값이 아니라면
                throw new RuntimeException("img, jpg, png 파일만 업로드가능합니다."); // runtimeexception을 던진다.
            }

            // 이미지 데이터를 Base64로 인코딩
            String encodedImage = Base64.getEncoder().encodeToString(file.getBytes());
            // 업로드된 이미지 파일을 byte배열로 읽고, base64로 인코딩한다. 이미지 데이터를 문자열로 저장하도록 하는 방법.

            user.setProfile_image(encodedImage); // 파일의 인코딩된 이미지 데이터를 저장
            user.setImageExtension(extension); // 파일의 확장자를 저장
            userRepository.save(user); // save문을 사용하여 update를 진행.
        } catch (IOException e) { // 파일을 읽기/쓰기에서 발생하는 예외를 처리하는 부분
            throw new RuntimeException("파일을 저장할 수 없습니다. 오류 : " + e.getMessage()); // errorMessage와 함께 이유를 출력
        }
    }

    //확장자를 저장하는 함수
    public String getExtension(String filename) {
        String extension = ""; // 확장자를 저장할 문자열을 선언. 초기화.
        if (filename != null) { // filename이 null이 아니면
            Path path = Paths.get(filename); // Paths.get 메서드를 이용해 파일이름을 경로로 변환.
            if (path.getFileName().toString().contains(".")) { // 파일 이름에 "."이 포함돼 있는지 확인. "."이 있다면 확장자가 존재한다 판단
                extension = path.getFileName().toString().substring(path.getFileName().toString().lastIndexOf(".") + 1);
                // path.getFileName().toString().lastIndexOf(".") + 1를 통해 마지막"."의 위치를 찾고, 그 뒤의 문자열을 substring을 통해 추출한다.
                // 추출한것을 extension에 저장한다.
            }
        }
        return extension; //저장한 extension을 반환한다.
    }

}

