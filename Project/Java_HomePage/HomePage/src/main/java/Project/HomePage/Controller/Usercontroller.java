package Project.HomePage.Controller;

import Project.HomePage.DTO.UserDTO;
import Project.HomePage.Entity.User;
import Project.HomePage.Service.UserService;
import jakarta.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;

@Controller
@RequiredArgsConstructor
public class Usercontroller {

    @Autowired
    private final UserService userService;

    @RequestMapping("/mypage")
    public String myPage(Model model, HttpServletRequest request) {
        String idvalue = request.getParameter("idvalue");

        UserDTO userDTO = userService.getUserInfo(idvalue);
        model.addAttribute("user", userDTO);

        return "mypage";
    }

    @GetMapping("/")
    public String list(Model model) {
        List<UserDTO> users = userService.getAllUser();
        model.addAttribute("userList", users);
        return "databasetest";
    }
}
