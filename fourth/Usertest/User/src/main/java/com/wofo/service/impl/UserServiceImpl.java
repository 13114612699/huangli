package com.wofo.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.wofo.mapper.UserMapper;
import com.wofo.model.User;
import com.wofo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

/**
 * ClassName UserServiceImpl
 * Title
 * Description TODO
 * Author Wofo_
 * Date 2023/5/19 13:19
 * Version 1.0
 */
@Service
public class UserServiceImpl extends
        ServiceImpl<UserMapper, User> implements UserService {
    @Autowired
    private UserService userService;


    @Override
    public List<User> getAll() {
        QueryWrapper<User> wrapper = new QueryWrapper<>();
        List<User> userList = baseMapper.selectList(wrapper);

        return userList;
    }

    @Override
    public User getUser(String id) {
        User user = baseMapper.selectById(id);
        System.out.println("user = " + user);

        return user;
    }

    @Override
    public User update(User user) {
        User user1 = this.getUser(user.getId());
        user1.setUsername(user.getUsername());
        user1.setPassword(user.getPassword());
        baseMapper.updateById(user1);
        System.out.println("user1 = " + user1);
        return user1;
    }

    @Override
    public void delete(String id) {
        baseMapper.deleteById(id);


    }

    @Override
    public void insert(User user) {
        baseMapper.insert(user);


    }
}
