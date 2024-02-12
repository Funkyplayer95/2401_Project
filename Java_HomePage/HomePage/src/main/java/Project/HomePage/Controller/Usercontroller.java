package Project.HomePage.Controller;

import Project.HomePage.DTO.SessionUser;
import Project.HomePage.DTO.UserDTO;
import Project.HomePage.Service.UserService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
@RequiredArgsConstructor
public class Usercontroller {

    private final UserService userService;

    @GetMapping("/mypage")
    public String myPage(Model model, HttpSession session) {
        SessionUser sessionUser = (SessionUser) session.getAttribute("user_id");
        String userId = sessionUser.getId();

        UserDTO userDTO = userService.getUserInfo(userId);
        model.addAttribute("user", userDTO);

        return "mypage";
    }

}