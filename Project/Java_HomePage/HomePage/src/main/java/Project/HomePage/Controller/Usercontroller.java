package Project.HomePage.Controller;

import Project.HomePage.DTO.UserDTO;
import Project.HomePage.Service.UserService;
import jakarta.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.CrossOrigin;
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


    @RequestMapping("/mypage")
    public String myPage(Model model, HttpServletRequest request) {
        String idvalue = request.getParameter("idvalue");

        UserDTO userDTO = userService.getUserInfo(idvalue);
        model.addAttribute("user", userDTO);

        return "mypage";
    }

    @PostMapping("/uploadProfileImage")
    public String fileUpload(@RequestParam("imageFile") MultipartFile file, @RequestParam("idvalue") String id,
                             RedirectAttributes redirectAttributes){
        try{
            userService.imgSave(file, id);
            redirectAttributes.addFlashAttribute("message", "이미지 업로드가 성공하였습니다!");
            return "redirect:/mypage?idvalue=" + id;
        } catch (RuntimeException e){
            redirectAttributes.addFlashAttribute("error", e.getMessage());
            return "redirect:/mypage?idvalue=" + id;
        }
    }



//    @GetMapping("/")
//    public String list(Model model) {
//        List<UserDTO> users = userService.getAllUser();
//        model.addAttribute("userList", users);
//        return "databasetest";
//    }
}
