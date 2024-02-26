package Project.HomePage.Controller;

import Project.HomePage.DTO.UserDTO;
import Project.HomePage.Service.UserService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequiredArgsConstructor
public class Usercontroller {

    @Autowired
    private final UserService userService;

    @RequestMapping("/mypage") // url주소에 /mypage로 이동시
    public String myPage(Model model, HttpSession session,
                         @RequestParam(value = "idvalue", required = false) String id) {
        if (id == null) { // id 값이 null이면
            id = session.getAttribute("idvalue").toString(); // id에 idvalue로 된 세션값을 넣는다.
        }
        session.setAttribute("idvalue", id); // id값을 idvalue라는 이름의 세션 값으로 설정.
        UserDTO userDTO = userService.getUserInfo(id); // id값을 받아와서 user정보를 userDTO에 저장.
        model.addAttribute("user", userDTO); // userDTO객체를 "user"이라는 모델 속성 으로 추가.

        return "mypage"; // mypage.html로 
    }


    @RequestMapping("/updatePw")
    public String updatePw(Model model, RedirectAttributes redirectAttributes,
                           @RequestParam("idvalue2") String idValue,
                           @RequestParam("newPw") String newPw,
                           @RequestParam("re_newPw") String reNewPw) {

        UserDTO userDTO = userService.getUserInfo(idValue); // RequestParam으로 받은 idValue를 이용. 사용자 조회
        model.addAttribute("user", userDTO); // user라는 모델에 정보를 주입.

        String passwordValidation = "^(?=.*[0-9])(?=.*[a-z])(?=.*[!@#$%^&*]).{8,}$"; // ^=문자열의 시작, $=문자열의 끝

        if (!newPw.matches(passwordValidation)) {
            redirectAttributes.addFlashAttribute("errorMessage", "비밀번호는 8자리 이상, 영어 소문자, 숫자, 특수문자를 각각 1개 이상 포함해야 합니다.");
            return "redirect:/mypage";
        } else if (!newPw.equals(reNewPw)) { // 새 비밀번호와 확인부분이 일치하지 않으면.
            // errorMessage를 FlashAttribute에 지정. redirectAttributes.addFlashAttribute는 작은 양의 정보를 전달하는데 사용한다함.
            redirectAttributes.addFlashAttribute("errorMessage", "새로운 비밀번호가 일치하지 않습니다.");
            return "redirect:/mypage"; // mypage로 redirect함.
        } else {
        userService.updatePassword(idValue, newPw); // 일치한다면  idValue값의 비밀번호를 newPw로 지정.
        redirectAttributes.addFlashAttribute("successMessage", "비밀번호가 변경되었습니다.");
        }

        return "redirect:/mypage";
    }


    @PostMapping("/uploadProfileImage")
    public String fileUpload(@RequestParam("imageFile") MultipartFile file,
                             HttpServletRequest req, RedirectAttributes redirectAttributes){
        try{
            String id = req.getSession().getAttribute("idvalue").toString(); // req를 통해 세션의 idvalue을 가져온다. 
            userService.imgSave(file, id); // imgSave 호출, 프로필 이미지 저장.
            redirectAttributes.addFlashAttribute("message", "이미지 업로드가 성공하였습니다!"); // 업로드 성공 메세지
        } catch (RuntimeException e){ //업로드 과정에서 예외 발생시 예외를 잡아 처리
            redirectAttributes.addFlashAttribute("error", e.getMessage()); // 리다이렉트된 페이지에 에러메세지가 나오도록
        }
        return "redirect:/mypage";
    }
}
