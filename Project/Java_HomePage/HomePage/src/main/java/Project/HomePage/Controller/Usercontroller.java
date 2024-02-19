package Project.HomePage.Controller;

import Project.HomePage.DTO.UserDTO;
import Project.HomePage.Service.UserService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequiredArgsConstructor
public class Usercontroller {

    @Autowired
    private final UserService userService;

    @RequestMapping("/mypage")
    public String myPage(Model model, HttpSession session,
                         @RequestParam(value = "idvalue", required = false) String id) {
        if (id == null) {
            id = session.getAttribute("idvalue").toString();
        }
        session.setAttribute("idvalue", id);
        UserDTO userDTO = userService.getUserInfo(id);
        model.addAttribute("user", userDTO);

        return "mypage";
    }


    @RequestMapping("/updatePw")
    public String updatePw(Model model, HttpServletRequest request, RedirectAttributes redirectAttributes, HttpSession session,
                           @RequestParam("idvalue2") String idValue,
                           @RequestParam("newPw") String newPw,
                           @RequestParam("re_newPw") String reNewPw) {

        String id = null;
        if (session.getAttribute("idvalue") != null) {
            id = session.getAttribute("idvalue").toString();
        }

        UserDTO userDTO = userService.getUserInfo(idValue);
        model.addAttribute("user", userDTO);

        BCryptPasswordEncoder passwordEncoder = new BCryptPasswordEncoder();

        // Perform password validation
        if (!newPw.equals(reNewPw)) {
            redirectAttributes.addFlashAttribute("errorMessage", "새로운 비밀번호가 일치하지 않습니다.");
            return "redirect:/mypage";
        } else {
        userService.updatePassword(idValue, newPw);
        redirectAttributes.addFlashAttribute("successMessage", "비밀번호가 변경되었습니다.");
        }

        return "redirect:/mypage";
    }


    @PostMapping("/uploadProfileImage")
    public String fileUpload(@RequestParam("imageFile") MultipartFile file,
                             HttpServletRequest req, RedirectAttributes redirectAttributes){
        try{
            String id = req.getSession().getAttribute("idvalue").toString();
            userService.imgSave(file, id);
            redirectAttributes.addFlashAttribute("message", "이미지 업로드가 성공하였습니다!");
        } catch (RuntimeException e){
            redirectAttributes.addFlashAttribute("error", e.getMessage());
        }
        return "redirect:/mypage";
    }
}
