package com.wofo.Controller;

import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.wofo.model.User;
import com.wofo.service.UserService;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * ClassName UserController
 * Title
 * Description TODO
 * Author Wofo_
 * Date 2023/5/19 13:20
 * Version 1.0
 */
@Api(tags = "用户接口")
@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService userService;



}
