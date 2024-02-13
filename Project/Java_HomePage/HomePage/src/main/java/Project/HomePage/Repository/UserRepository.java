package Project.HomePage.Repository;

import Project.HomePage.Entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface UserRepository extends JpaRepository<User,String>{

    List<User> findAll();
}
