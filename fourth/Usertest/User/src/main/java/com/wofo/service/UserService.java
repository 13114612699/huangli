package com.wofo.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.wofo.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * ClassName UserService
 * Title
 * Description TODO
 * Author Wofo_
 * Date 2023/5/19 13:17
 * Version 1.0
 */

public interface UserService extends IService<User> {

    List<User> getAll();
    User getUser(String id);

    User update(User user);

    void delete(String id);

    void insert(User user);
}
